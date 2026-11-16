import os
import re
import xml.etree.ElementTree as ET
import fitz # PyMuPDF
from PIL import Image

DRAWIO_DIR = r"FINAL_ML_PROJECT_REPORT_V5\03_DIAGRAMS\source_drawio"
SVG_DIR = r"FINAL_ML_PROJECT_REPORT_V5\03_DIAGRAMS\exports_svg"
PNG_DIR = r"FINAL_ML_PROJECT_REPORT_V5\03_DIAGRAMS\exports_png"

os.makedirs(DRAWIO_DIR, exist_ok=True)
os.makedirs(SVG_DIR, exist_ok=True)
os.makedirs(PNG_DIR, exist_ok=True)

def escape_xml_text(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")

def create_drawio_file(fpath, name, page_w, page_h, vertices, edges):
    root = ET.Element("mxfile", host="app.diagrams.net")
    diagram = ET.SubElement(root, "diagram", name=name, id=name)
    model = ET.SubElement(diagram, "mxGraphModel", dx="1000", dy="700", grid="1", gridSize="10",
                          page="1", pageScale="1", pageWidth=str(page_w), pageHeight=str(page_h))
    mxroot = ET.SubElement(model, "root")
    ET.SubElement(mxroot, "mxCell", id="0")
    ET.SubElement(mxroot, "mxCell", id="1", parent="0")

    for v in vertices:
        st = v.get("style", "")
        if "fontFamily=" not in st:
            st = "fontFamily=Arial;" + st
        val = v.get("val", "")
        vlines = val.split("<br>")
        if len(vlines) > 1 and not vlines[0].startswith("<b>") and not v.get("is_title"):
            drawio_val = f"<b>{vlines[0]}</b><br>" + "<br>".join(vlines[1:])
        else:
            drawio_val = val
        c = ET.SubElement(mxroot, "mxCell", id=v["id"], value=drawio_val,
                         style=st, vertex="1", parent="1")
        ET.SubElement(c, "mxGeometry", x=str(v["x"]), y=str(v["y"]),
                      width=str(v["w"]), height=str(v["h"]), **{"as": "geometry"})

    for e in edges:
        st = e.get("style", "")
        if "fontFamily=" not in st:
            st = "fontFamily=Arial;" + st
        c = ET.SubElement(mxroot, "mxCell", id=e["id"], source=e["src"], target=e["tgt"],
                         style=st, edge="1", parent="1")
        if e.get("val"):
            c.set("value", e["val"])
        geom = ET.SubElement(c, "mxGeometry", relative="1", **{"as": "geometry"})
        d_pts = e.get("drawio_pts", e.get("pts"))
        if d_pts:
            arr = ET.SubElement(geom, "Array", **{"as": "points"})
            for px, py in d_pts:
                ET.SubElement(arr, "mxPoint", x=str(px), y=str(py))

    xml_str = ET.tostring(root, encoding="utf-8").decode("utf-8")
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(xml_str)

def create_svg_file(fpath, page_w, page_h, vertices, edges):
    vert_map = {v["id"]: v for v in vertices}
    svg_parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{page_w}" height="{page_h}" viewBox="0 0 {page_w} {page_h}" font-family="Arial, \'Segoe UI\', Tahoma, sans-serif">',
        f'<rect width="{page_w}" height="{page_h}" fill="#ffffff"/>',
        '<defs>',
        '  <style>',
        '    text { font-family: Arial, "Segoe UI", Tahoma, sans-serif; }',
        '  </style>',
        '  <marker id="ar" markerWidth="7" markerHeight="7" refX="6" refY="3.5" orient="auto"><path d="M0,0.5 L6,3.5 L0,6.5 z" fill="#1F3864"/></marker>',
        '</defs>'
    ]

    # 1. Containers / Groups first
    for v in vertices:
        if "dashed=1" in v.get("style", "") or v.get("is_group"):
            x, y, w, h = v["x"], v["y"], v["w"], v["h"]
            fill = "#F8FAFC"
            stroke = "#8497B0"
            svg_parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{fill}" stroke="{stroke}" stroke-width="1.5" stroke-dasharray="6 4"/>')
            val = v.get("val", "")
            if val:
                glines = [line.strip() for line in val.split("<br>") if line.strip()]
                if len(glines) == 1:
                    esc_line = escape_xml_text(glines[0])
                    svg_parts.append(f'<text x="{x + w/2}" y="{y + 20}" text-anchor="middle" dominant-baseline="middle" font-size="12" font-weight="bold" fill="#1F3864">{esc_line}</text>')
                else:
                    g_line_height = 15.0
                    g_start_y = y + h/2 - ((len(glines)-1)*g_line_height)/2
                    for gi, gline in enumerate(glines):
                        esc_line = escape_xml_text(gline)
                        gly = g_start_y + gi * g_line_height
                        weight = 'font-weight="bold"' if gi == 0 else 'font-weight="normal"'
                        svg_parts.append(f'<text x="{x + w/2}" y="{gly:.2f}" text-anchor="middle" dominant-baseline="middle" font-size="10.5" {weight} fill="#1F3864">{esc_line}</text>')

    # 2. Main vertices
    for v in vertices:
        if "dashed=1" in v.get("style", "") or v.get("is_group"):
            continue
        x, y, w, h = v["x"], v["y"], v["w"], v["h"]
        style = v.get("style", "")
        val = v.get("val", "")

        # Title
        if "text;" in style or v.get("is_title"):
            esc_val = escape_xml_text(val)
            svg_parts.append(f'<text x="{x + w/2}" y="{y + h/2}" text-anchor="middle" dominant-baseline="middle" font-size="15" font-weight="bold" fill="#1F3864">{esc_val}</text>')
            continue

        fill = "#FFFFFF"
        stroke = "#1F3864"
        font_color = "#000000"

        if "fillColor=" in style:
            m = re.search(r'fillColor=([^;]+)', style)
            if m: fill = m.group(1)
        if "strokeColor=" in style:
            m = re.search(r'strokeColor=([^;]+)', style)
            if m: stroke = m.group(1)
        if "fontColor=" in style:
            m = re.search(r'fontColor=([^;]+)', style)
            if m: font_color = m.group(1)

        is_cylinder = "cylinder" in style
        is_rhombus = "rhombus" in style

        # Cylinder geometry
        if is_cylinder:
            ch = 8.0 # sleek 8px cap
            svg_parts.append(f'<path d="M {x} {y+ch} A {w/2} {ch} 0 0 1 {x+w} {y+ch} L {x+w} {y+h-ch} A {w/2} {ch} 0 0 1 {x} {y+h-ch} Z" fill="{fill}" stroke="{stroke}" stroke-width="1.5"/>')
            svg_parts.append(f'<ellipse cx="{x+w/2}" cy="{y+ch}" rx="{w/2}" ry="{ch}" fill="{fill}" stroke="{stroke}" stroke-width="1.5"/>')
            svg_parts.append(f'<path d="M {x} {y+h-ch} A {w/2} {ch} 0 0 0 {x+w} {y+h-ch}" fill="none" stroke="{stroke}" stroke-width="1.5"/>')
        # Rhombus geometry
        elif is_rhombus:
            svg_parts.append(f'<polygon points="{x+w/2},{y} {x+w},{y+h/2} {x+w/2},{y+h} {x},{y+h/2}" fill="{fill}" stroke="{stroke}" stroke-width="1.5"/>')
        # Rounded rectangle
        else:
            svg_parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="{fill}" stroke="{stroke}" stroke-width="1.5"/>')

        # Text rendering with strict margin protection and unified typography
        lines = [line.strip() for line in val.split("<br>") if line.strip()]
        if lines:
            line_count = len(lines)
            font_size = 9.5 if line_count >= 4 else (10.0 if line_count == 3 else 10.5)
            line_height = 13.5 if line_count >= 4 else (14.5 if line_count == 3 else 15.5)

            if is_cylinder:
                body_avail_h = h - (2 * ch + 12.0)
                text_total_h = (line_count - 1) * line_height
                start_y = (y + 2 * ch + 6.0) + (body_avail_h - text_total_h) / 2
            else:
                start_y = y + h / 2 - ((line_count - 1) * line_height) / 2

            for i, line in enumerate(lines):
                esc_line = escape_xml_text(line)
                ly = start_y + i * line_height
                # Standardized typography: Line 1 bold, Lines 2+ regular
                if i == 0:
                    weight = 'font-weight="bold"'
                    fsz = font_size
                else:
                    weight = 'font-weight="normal"'
                    fsz = max(9.0, font_size - 0.5)
                svg_parts.append(f'<text x="{x + w/2}" y="{ly:.2f}" text-anchor="middle" dominant-baseline="middle" font-size="{fsz}" {weight} fill="{font_color}">{esc_line}</text>')

    # 3. Edges
    for e in edges:
        style = e.get("style", "")
        pts = e.get("pts", [])
        src = vert_map.get(e["src"])
        tgt = vert_map.get(e["tgt"])
        if not src or not tgt:
            continue

        stroke = "#1F3864"
        if "strokeColor=" in style:
            m = re.search(r'strokeColor=([^;]+)', style)
            if m: stroke = m.group(1)
        dashed = 'stroke-dasharray="5 4"' if "dashed=1" in style else ""
        has_arrow = "endArrow=block" in style or "endArrow=classic" in style
        if "endArrow=none" in style:
            has_arrow = False
        marker = 'marker-end="url(#ar)"' if has_arrow else ""

        # Parse exact anchor ratios if present
        m_exX = re.search(r'exitX=([0-9.]+)', style)
        m_exY = re.search(r'exitY=([0-9.]+)', style)
        m_enX = re.search(r'entryX=([0-9.]+)', style)
        m_enY = re.search(r'entryY=([0-9.]+)', style)

        if m_exX and m_exY:
            p1 = (src["x"] + src["w"] * float(m_exX.group(1)), src["y"] + src["h"] * float(m_exY.group(1)))
        elif "exitX=1" in style:
            p1 = (src["x"] + src["w"], src["y"] + src["h"]/2)
        elif "exitX=0" in style:
            p1 = (src["x"], src["y"] + src["h"]/2)
        elif "exitY=1" in style:
            p1 = (src["x"] + src["w"]/2, src["y"] + src["h"])
        elif "exitY=0" in style:
            p1 = (src["x"] + src["w"]/2, src["y"])
        else:
            p1 = (src["x"] + src["w"], src["y"] + src["h"]/2)

        if m_enX and m_enY:
            p2 = (tgt["x"] + tgt["w"] * float(m_enX.group(1)), tgt["y"] + tgt["h"] * float(m_enY.group(1)))
        elif "entryX=0" in style:
            p2 = (tgt["x"], tgt["y"] + tgt["h"]/2)
        elif "entryX=1" in style:
            p2 = (tgt["x"] + tgt["w"], tgt["y"] + tgt["h"]/2)
        elif "entryY=0" in style:
            p2 = (tgt["x"] + tgt["w"]/2, tgt["y"])
        elif "entryY=1" in style:
            p2 = (tgt["x"] + tgt["w"]/2, tgt["y"] + tgt["h"])
        else:
            p2 = (tgt["x"], tgt["y"] + tgt["h"]/2)

        mid_x, mid_y = (p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2

        if pts:
            points_str = " ".join([f"{px:.1f},{py:.1f}" for px, py in pts])
            svg_parts.append(f'<polyline points="{points_str}" fill="none" stroke="{stroke}" stroke-width="1.5" {dashed} {marker}/>')
            if len(pts) >= 2:
                mid_idx = len(pts) // 2
                if len(pts) % 2 == 0:
                    mid_x = (pts[mid_idx-1][0] + pts[mid_idx][0]) / 2
                    mid_y = (pts[mid_idx-1][1] + pts[mid_idx][1]) / 2
                else:
                    mid_x, mid_y = pts[mid_idx][0], pts[mid_idx][1]
        else:
            if abs(p1[1] - p2[1]) < 0.5 or abs(p1[0] - p2[0]) < 0.5:
                svg_parts.append(f'<line x1="{p1[0]:.1f}" y1="{p1[1]:.1f}" x2="{p2[0]:.1f}" y2="{p2[1]:.1f}" stroke="{stroke}" stroke-width="1.5" {dashed} {marker}/>')
            elif ("exitY=1" in style or "exitY=0") and ("entryY=0" in style or "entryY=1" in style):
                my = (p1[1] + p2[1]) / 2
                svg_parts.append(f'<polyline points="{p1[0]:.1f},{p1[1]:.1f} {p1[0]:.1f},{my:.1f} {p2[0]:.1f},{my:.1f} {p2[0]:.1f},{p2[1]:.1f}" fill="none" stroke="{stroke}" stroke-width="1.5" {dashed} {marker}/>')
            else:
                mx = (p1[0] + p2[0]) / 2
                svg_parts.append(f'<polyline points="{p1[0]:.1f},{p1[1]:.1f} {mx:.1f},{p1[1]:.1f} {mx:.1f},{p2[1]:.1f} {p2[0]:.1f},{p2[1]:.1f}" fill="none" stroke="{stroke}" stroke-width="1.5" {dashed} {marker}/>')

        # Edge label rendering
        edge_val = e.get("val", "")
        if edge_val:
            lbl_w = max(40, len(edge_val) * 7.5 + 12)
            svg_parts.append(f'<rect x="{mid_x - lbl_w/2:.1f}" y="{mid_y - 14:.1f}" width="{lbl_w:.1f}" height="16" fill="#ffffff" stroke="#DAE8FC" stroke-width="1" rx="3"/>')
            svg_parts.append(f'<text x="{mid_x:.1f}" y="{mid_y - 6:.1f}" text-anchor="middle" dominant-baseline="middle" font-size="9.0" font-weight="bold" fill="#1F3864">{escape_xml_text(edge_val)}</text>')

    svg_parts.append('</svg>')
    svg_str = "\n".join(svg_parts)
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(svg_str)
    return svg_str

def render_png_from_svg(svg_path, png_path, dpi=144):
    doc = fitz.open(svg_path)
    page = doc[0]
    pix = page.get_pixmap(dpi=dpi)
    pix.save(png_path)
    doc.close()
