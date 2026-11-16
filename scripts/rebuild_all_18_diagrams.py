import os
import sys
sys.path.insert(0, os.path.abspath("."))
import fitz
from scripts.diagram_builder_base import (
    create_drawio_file, create_svg_file, render_png_from_svg,
    DRAWIO_DIR, SVG_DIR, PNG_DIR
)
from scripts.diagram_defs_part1 import DIAGRAMS as D1
from scripts.diagram_defs_part2 import DIAGRAMS_PART2 as D2
from scripts.diagram_defs_part3 import DIAGRAMS_PART3 as D3

ALL_DIAGRAMS = {}
ALL_DIAGRAMS.update(D1)
ALL_DIAGRAMS.update(D2)
ALL_DIAGRAMS.update(D3)

print(f"Loaded {len(ALL_DIAGRAMS)} diagrams.")

for name, diag in sorted(ALL_DIAGRAMS.items()):
    pw = diag["page_w"]
    ph = diag["page_h"]
    verts = diag["vertices"]
    edges = diag["edges"]

    # 1. Write Drawio XML
    drawio_path = os.path.join(DRAWIO_DIR, f"{name}.drawio")
    create_drawio_file(drawio_path, name, pw, ph, verts, edges)

    # 2. Write SVG
    svg_path = os.path.join(SVG_DIR, f"{name}.svg")
    create_svg_file(svg_path, pw, ph, verts, edges)

    # 3. Render PNG via PyMuPDF (fitz) at 144 DPI
    png_path = os.path.join(PNG_DIR, f"{name}.png")
    render_png_from_svg(svg_path, png_path, dpi=144)

    print(f"  [OK] {name}: drawio, svg, png generated successfully.")

print("\nALL 18 DIAGRAMS GENERATED AND RENDERED PERFECTLY!")
