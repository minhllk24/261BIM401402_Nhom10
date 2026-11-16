DIAGRAMS = {}

# ==============================================================================
# 01. TỔNG QUAN CÁC THÀNH PHẦN DỰ ÁN (Hình 3.2)
# ==============================================================================
DIAGRAMS["01_project_overview"] = {
    "page_w": 1040, "page_h": 290,
    "vertices": [
        {"id": "t", "val": "Hình: Tổng quan các thành phần của dự án", "x": 0, "y": 5, "w": 1040, "h": 30, "style": "text;html=1;align=center;verticalAlign=middle;fontStyle=1;fontSize=15;fontColor=#1F3864;", "is_title": True},
        {"id": "o1", "val": "Dữ liệu & Pipeline ML<br>(src/, run_pipeline.py)", "x": 30, "y": 65, "w": 210, "h": 75, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;"},
        {"id": "o2", "val": "Artifacts & Registry<br>(models, tables, manifests)", "x": 280, "y": 65, "w": 210, "h": 75, "style": "shape=cylinder3;boundedLbl=1;whiteSpace=wrap;html=1;fillColor=#E1D5E7;strokeColor=#7E5A9B;"},
        {"id": "o3", "val": "Backend FastAPI<br>(29 thao tác API trong mã)", "x": 530, "y": 65, "w": 210, "h": 75, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;"},
        {"id": "o4", "val": "Frontend React<br>(10 trang)", "x": 780, "y": 65, "w": 210, "h": 75, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#D5E8D4;strokeColor=#82B366;"},
        {"id": "o5", "val": "Tests (30+ tệp)<br>+ tài liệu 16 giai đoạn", "x": 280, "y": 185, "w": 210, "h": 65, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#F8CECC;strokeColor=#B85450;"},
        {"id": "o6", "val": "Inventory Planning<br>(mô phỏng bổ sung)", "x": 530, "y": 185, "w": 210, "h": 65, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#D5E8D4;strokeColor=#82B366;"}
    ],
    "edges": [
        {"id": "e0", "src": "o1", "tgt": "o2", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=1;exitY=0.5;entryX=0;entryY=0.5;"},
        {"id": "e1", "src": "o2", "tgt": "o3", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=1;exitY=0.5;entryX=0;entryY=0.5;"},
        {"id": "e2", "src": "o3", "tgt": "o4", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=1;exitY=0.5;entryX=0;entryY=0.5;"},
        {"id": "e3", "src": "o5", "tgt": "o2", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=0.5;exitY=0;entryX=0.5;entryY=1;dashed=1;"},
        {"id": "e4", "src": "o3", "tgt": "o6", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=0.5;exitY=1;entryX=0.5;entryY=0;"}
    ]
}

# ==============================================================================
# 02. VÒNG ĐỜI MACHINE LEARNING END-TO-END (Hình 3.1)
# ==============================================================================
DIAGRAMS["02_ml_lifecycle"] = {
    "page_w": 1040, "page_h": 700,
    "vertices": [
        {"id": "t", "val": "Hình: Vòng đời Machine Learning end-to-end của dự án", "x": 0, "y": 5, "w": 1040, "h": 30, "style": "text;html=1;align=center;verticalAlign=middle;fontStyle=1;fontSize=15;fontColor=#1F3864;", "is_title": True},
        # Top group: VÒNG ĐỜI HUẤN LUYỆN
        {"id": "g1", "val": "VÒNG ĐỜI HUẤN LUYỆN (Training Lifecycle, offline)", "x": 10, "y": 40, "w": 1020, "h": 430, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=none;strokeColor=#1F3864;fontStyle=1;verticalAlign=top;spacingTop=10;", "is_group": True},
        # Row 1 (y=80, h=70, y_mid=115.0)
        {"id": "a0", "val": "0. Nhu cầu nghiệp vụ<br>(dự báo SKU–tuần, hoạch<br>định bổ sung)", "x": 30, "y": 80, "w": 175, "h": 70, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;"},
        {"id": "a1", "val": "1. Giao dịch bán lẻ<br>UCI Online Retail II<br>(1.067.371 dòng)", "x": 235, "y": 80, "w": 175, "h": 70, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;"},
        {"id": "a2", "val": "2. Lưu trữ dữ liệu<br>raw_transactions.parquet /<br>Excel", "x": 440, "y": 80, "w": 175, "h": 70, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#E1D5E7;strokeColor=#7E5A9B;"},
        {"id": "a3", "val": "3. Làm sạch & tiền xử lý<br>(6 bước, còn 1.003.466<br>dòng)", "x": 645, "y": 80, "w": 175, "h": 70, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;"},
        {"id": "a4", "val": "4. Mô hình hóa dữ liệu<br>Panel SKU–tuần (2.785<br>SKU)", "x": 845, "y": 80, "w": 165, "h": 70, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;"},
        # Row 2 (y=200, h=70, y_mid=235.0) - right to left
        {"id": "b1", "val": "5. Kỹ thuật đặc trưng<br>71 features, Shift-before<br>-roll", "x": 845, "y": 200, "w": 165, "h": 70, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;"},
        {"id": "b2", "val": "6. Chia tập dữ liệu<br>5-fold Expanding window<br>+ Holdout", "x": 645, "y": 200, "w": 175, "h": 70, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;"},
        {"id": "b3", "val": "7. Huấn luyện đa mô hình<br>Baselines, CatBoost,<br>LightGBM, TiDE, TFT", "x": 440, "y": 200, "w": 175, "h": 70, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;"},
        {"id": "b4", "val": "8. Đánh giá & so sánh<br>MAE, RMSE, WAPE,<br>Pinball", "x": 235, "y": 200, "w": 175, "h": 70, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;"},
        {"id": "b5", "val": "Đạt ngưỡng<br>chấp nhận?<br>(WAPE, MAE tối ưu)", "x": 25, "y": 195, "w": 185, "h": 80, "style": "rhombus;whiteSpace=wrap;html=1;fillColor=#FFF2CC;strokeColor=#D6B656;"},
        # Row 3 (y=330, h=70, y_mid=365.0) - left to right
        {"id": "b6", "val": "9. Đóng băng mô hình<br>(Model Freeze & SHA-256)", "x": 235, "y": 330, "w": 175, "h": 70, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#D5E8D4;strokeColor=#82B366;"},
        {"id": "b7", "val": "10. Model Registry<br>(models/, metadata.json,<br>artifacts)", "x": 440, "y": 327.5, "w": 175, "h": 75, "style": "shape=cylinder3;boundedLbl=1;whiteSpace=wrap;html=1;fillColor=#E1D5E7;strokeColor=#7E5A9B;"},
        # Bottom group: VÒNG ĐỜI PHỤC VỤ & VẬN HÀNH
        {"id": "g2", "val": "VÒNG ĐỜI PHỤC VỤ & VẬN HÀNH (Serving & Operation Lifecycle, online)", "x": 10, "y": 490, "w": 1020, "h": 195, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=none;strokeColor=#82B366;fontStyle=1;verticalAlign=top;spacingTop=10;", "is_group": True},
        # Row 4 (y=545, h=75, y_mid=582.5) - left to right
        {"id": "c1", "val": "11. Serving Ready<br>(Model Registry API)", "x": 30, "y": 545, "w": 200, "h": 75, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#D5E8D4;strokeColor=#82B366;"},
        {"id": "c2", "val": "12. Backend FastAPI<br>(29 endpoints, RBAC,<br>POST /forecasts/run)", "x": 255, "y": 545, "w": 200, "h": 75, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;"},
        {"id": "c3", "val": "13. Suy luận & Hoạch định<br>(Rollout đệ quy H=4,<br>mô phỏng tồn kho)", "x": 480, "y": 545, "w": 200, "h": 75, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;"},
        {"id": "c4", "val": "14. Giao diện người dùng<br>(Desktop PyQt6 /<br>Web React 18 SPA)", "x": 705, "y": 545, "w": 165, "h": 75, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;"},
        {"id": "c5", "val": "Người dùng<br>(Analyst, Planner)", "x": 895, "y": 545, "w": 130, "h": 75, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;"}
    ],
    "edges": [
        # Row 1: 100% straight horizontal at Y=115.0
        {"id": "e0", "src": "a0", "tgt": "a1", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=1;exitY=0.5;entryX=0;entryY=0.5;"},
        {"id": "e1", "src": "a1", "tgt": "a2", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=1;exitY=0.5;entryX=0;entryY=0.5;"},
        {"id": "e2", "src": "a2", "tgt": "a3", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=1;exitY=0.5;entryX=0;entryY=0.5;"},
        {"id": "e3", "src": "a3", "tgt": "a4", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=1;exitY=0.5;entryX=0;entryY=0.5;"},
        # Straight vertical drop at X=927.5
        {"id": "e4", "src": "a4", "tgt": "b1", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=0.5;exitY=1;entryX=0.5;entryY=0;"},
        # Row 2: 100% straight horizontal at Y=235.0
        {"id": "e5", "src": "b1", "tgt": "b2", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=0;exitY=0.5;entryX=1;entryY=0.5;"},
        {"id": "e6", "src": "b2", "tgt": "b3", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=0;exitY=0.5;entryX=1;entryY=0.5;"},
        {"id": "e7", "src": "b3", "tgt": "b4", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=0;exitY=0.5;entryX=1;entryY=0.5;"},
        {"id": "e8", "src": "b4", "tgt": "b5", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=0;exitY=0.5;entryX=1;entryY=0.5;"},
        # Straight vertical drop at X=322.5
        {"id": "e9", "src": "b4", "tgt": "b6", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=0.5;exitY=1;entryX=0.5;entryY=0;"},
        # Straight horizontal at Y=365.0
        {"id": "e10", "src": "b6", "tgt": "b7", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=1;exitY=0.5;entryX=0;entryY=0.5;"},
        # Clean L-turn from b6 (left X=222.5) to c1 (top center X=130, Y=545)
        {"id": "e11", "src": "b6", "tgt": "c1", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=0;exitY=0.5;entryX=0.5;entryY=0;", "pts": [(222.5, 365.0), (130.0, 365.0), (130.0, 545.0)], "drawio_pts": [(130.0, 365.0)]},
        # Row 4: 100% straight horizontal at Y=582.5
        {"id": "e12", "src": "c1", "tgt": "c2", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=1;exitY=0.5;entryX=0;entryY=0.5;"},
        {"id": "e13", "src": "c2", "tgt": "c3", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=1;exitY=0.5;entryX=0;entryY=0.5;"},
        {"id": "e14", "src": "c3", "tgt": "c4", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=1;exitY=0.5;entryX=0;entryY=0.5;"},
        {"id": "e15", "src": "c4", "tgt": "c5", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=1;exitY=0.5;entryX=0;entryY=0.5;"}
    ]
}

# ==============================================================================
# 03. QUY TRÌNH TIỀN XỬ LÝ VÀ LÀM SẠCH DỮ LIỆU (Hình 3.4)
# ==============================================================================
DIAGRAMS["03_data_processing"] = {
    "page_w": 1040, "page_h": 460,
    "vertices": [
        {"id": "t", "val": "Hình: Quy trình làm sạch dữ liệu (waterfall 6 bước)", "x": 0, "y": 5, "w": 1040, "h": 30, "style": "text;html=1;align=center;verticalAlign=middle;fontStyle=1;fontSize=15;fontColor=#1F3864;", "is_title": True},
        # Row 1 (y=55, h=65, y_mid=87.5): Left to Right
        {"id": "r", "val": "Raw: 1.067.371 dòng<br>(8 cột, 2009-12-01 → 2011-12-09)", "x": 20, "y": 55, "w": 225, "h": 65, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#E1D5E7;strokeColor=#7E5A9B;"},
        {"id": "s1", "val": "B1. Loại trùng lặp chính xác<br>−34.335", "x": 275, "y": 55, "w": 210, "h": 65, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;"},
        {"id": "s2", "val": "B2. Loại hóa đơn hủy (prefix C)<br>−19.104", "x": 525, "y": 55, "w": 210, "h": 65, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;"},
        # Row 2 (y=165, h=65, y_mid=197.5): Right to Left
        {"id": "s3", "val": "B3. Quantity ≤ 0<br>−3.393", "x": 525, "y": 165, "w": 210, "h": 65, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;"},
        {"id": "s4", "val": "B4. Price ≤ 0<br>−2.626", "x": 275, "y": 165, "w": 210, "h": 65, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;"},
        # Row 3 (y=275, h=70, y_mid=310.0): Left to Right
        {"id": "s5", "val": "B5. Dòng phi hàng hóa<br>(bưu phí, phí NH, thủ công)<br>−4.447", "x": 275, "y": 275, "w": 210, "h": 70, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;"},
        {"id": "s6", "val": "B6. Giữ CustomerID<br>thiếu 226.842 dòng<br>(không loại)", "x": 515, "y": 262.5, "w": 230, "h": 95, "style": "rhombus;whiteSpace=wrap;html=1;fillColor=#FFF2CC;strokeColor=#D6B656;"},
        {"id": "o", "val": "Dữ liệu sạch: 1.003.466 dòng<br>(94,01% raw)", "x": 775, "y": 275, "w": 235, "h": 70, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#D5E8D4;strokeColor=#82B366;"},
        # Final aggregation box (y=375, h=70)
        {"id": "w", "val": "Gộp theo tuần ISO<br>(Thứ Hai → Chủ nhật)<br>nhãn week_start", "x": 775, "y": 375, "w": 235, "h": 70, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;"}
    ],
    "edges": [
        # Row 1 straight horizontal
        {"id": "e0", "src": "r", "tgt": "s1", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=1;exitY=0.5;entryX=0;entryY=0.5;"},
        {"id": "e1", "src": "s1", "tgt": "s2", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=1;exitY=0.5;entryX=0;entryY=0.5;"},
        # Straight vertical drop s2 -> s3 at X=630.0
        {"id": "e2", "src": "s2", "tgt": "s3", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=0.5;exitY=1;entryX=0.5;entryY=0;"},
        # Row 2 straight horizontal right-to-left
        {"id": "e3", "src": "s3", "tgt": "s4", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=0;exitY=0.5;entryX=1;entryY=0.5;"},
        # Straight vertical drop s4 -> s5 at X=380.0
        {"id": "e4", "src": "s4", "tgt": "s5", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=0.5;exitY=1;entryX=0.5;entryY=0;"},
        # Row 3 straight horizontal
        {"id": "e5", "src": "s5", "tgt": "s6", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=1;exitY=0.5;entryX=0;entryY=0.5;"},
        {"id": "e6", "src": "s6", "tgt": "o", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=1;exitY=0.5;entryX=0;entryY=0.5;"},
        # Straight vertical drop o -> w at X=892.5
        {"id": "e7", "src": "o", "tgt": "w", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=0.5;exitY=1;entryX=0.5;entryY=0;"}
    ]
}

# ==============================================================================
# 04. XÂY DỰNG PANEL NHU CẦU SKU–TUẦN (Hình 3.5)
# ==============================================================================
DIAGRAMS["04_sku_week_panel"] = {
    "page_w": 1040, "page_h": 380,
    "page_w": 1040, "page_h": 390,
    "vertices": [
        {"id": "t", "val": "Hình: Xây dựng panel nhu cầu SKU–tuần", "x": 0, "y": 5, "w": 1040, "h": 30, "style": "text;html=1;align=center;verticalAlign=middle;fontStyle=1;fontSize=15;fontColor=#1F3864;", "is_title": True},
        # Row 1 (y_mid=87.5): Pipeline flow
        {"id": "p1", "val": "Dữ liệu giao dịch sạch<br>(1.003.466 dòng)", "x": 20, "y": 55, "w": 200, "h": 65, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;"},
        {"id": "p2", "val": "Lưới Descartes<br>2.785 SKU × 106 tuần", "x": 250, "y": 55, "w": 210, "h": 65, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;"},
        {"id": "p3", "val": "Zero-filling nhu cầu<br>không phát sinh = 0", "x": 490, "y": 55, "w": 215, "h": 65, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;"},
        {"id": "p4", "val": "Phân loại trưởng thành<br>(tuần phát sinh đầu ≤ w)", "x": 745, "y": 40, "w": 230, "h": 95, "style": "rhombus;whiteSpace=wrap;html=1;fillColor=#FFF2CC;strokeColor=#D6B656;"},
        {"id": "p1", "val": "Giao dịch sạch<br>(1.003.466 dòng)", "x": 20, "y": 55, "w": 170, "h": 65, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;"},
        {"id": "p2", "val": "Tổng hợp SKU × tuần<br>(demand = Σ quantity)", "x": 220, "y": 55, "w": 180, "h": 65, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;"},
        {"id": "p3", "val": "Điền 0 từ tuần bán đầu tiên<br>đến cuối chuỗi", "x": 430, "y": 55, "w": 190, "h": 65, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;"},
        # 40px clear whitespace corridor between p3 (right X=620) and p4 (left X=660)!
        {"id": "p4", "val": "Lọc SKU đủ điều kiện<br>(≥10 tuần hoạt động, ≥50 đơn vị<br>trước mốc 2010-04-27)", "x": 660, "y": 40, "w": 240, "h": 95, "style": "rhombus;whiteSpace=wrap;html=1;fillColor=#FFF2CC;strokeColor=#D6B656;"},
        # Row 2 (y_mid=210.0): 2 Subsets side by side
        {"id": "m1", "val": "CAUSAL_MATURE: 1.717 SKU<br>(đủ lịch sử cho lag 26 tuần)", "x": 490, "y": 175, "w": 220, "h": 70, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#D5E8D4;strokeColor=#82B366;"},
        {"id": "m2", "val": "LATE_MATURING: 1.068 SKU<br>(xuất hiện muộn, xử lý riêng)", "x": 750, "y": 175, "w": 220, "h": 70, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;"},
        # Row 3 (y_mid=317.5): Unified panel v1.1
        {"id": "p7", "val": "Panel v1.1: 2.785 SKU<br>(sku_id, week_start duy nhất, 263.149 dòng)", "x": 585, "y": 285, "w": 300, "h": 65, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#E1D5E7;strokeColor=#7E5A9B;"}
        {"id": "m1", "val": "CAUSAL_MATURE<br>1.717 SKU (nhóm chính)", "x": 420, "y": 175, "w": 200, "h": 70, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#D5E8D4;strokeColor=#82B366;"},
        {"id": "m2", "val": "LATE_MATURING<br>1.068 SKU (phân tích phụ)", "x": 660, "y": 175, "w": 240, "h": 70, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;"},
        # Row 3 (y_mid=320.0): Unified panel v1.1
        {"id": "p7", "val": "Panel v1.1: 2.785 SKU<br>(sku_id, week_start) duy nhất", "x": 520, "y": 285, "w": 260, "h": 70, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#E1D5E7;strokeColor=#7E5A9B;"}
    ],
    "edges": [
        # Row 1 straight horizontal
        {"id": "e0", "src": "p1", "tgt": "p2", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=1;exitY=0.5;entryX=0;entryY=0.5;"},
        {"id": "e1", "src": "p2", "tgt": "p3", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=1;exitY=0.5;entryX=0;entryY=0.5;"},
        {"id": "e2", "src": "p3", "tgt": "p4", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=1;exitY=0.5;entryX=0;entryY=0.5;"},
        # Branch 1: p4 left apex (745, 87.5) -> m1 top (600, 175)
        {"id": "e3", "src": "p4", "tgt": "m1", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=0;exitY=0.5;entryX=0.5;entryY=0;", "pts": [(745.0, 87.5), (600.0, 87.5), (600.0, 175.0)], "drawio_pts": [(600.0, 87.5)]},
        # Branch 2: p4 bottom apex (860, 135) -> m2 top (860, 175) - 100% straight vertical
        # Branch 1: p4 bottom apex (780, 135) drops to Y=155, branches left to X=520 and drops into m1 top (520, 175)
        {"id": "e3", "src": "p4", "tgt": "m1", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=0.5;exitY=1;entryX=0.5;entryY=0;", "pts": [(780.0, 135.0), (780.0, 155.0), (520.0, 155.0), (520.0, 175.0)], "drawio_pts": [(780.0, 155.0), (520.0, 155.0)]},
        # Branch 2: p4 bottom apex (780, 135) -> m2 top (780, 175) - 100% straight vertical drop
        {"id": "e4", "src": "p4", "tgt": "m2", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=0.5;exitY=1;entryX=0.5;entryY=0;"},
        # Symmetric convergence into p7: m1 -> p7
        {"id": "e5", "src": "m1", "tgt": "p7", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=0.5;exitY=1;entryX=0.25;entryY=0;", "pts": [(600.0, 245.0), (600.0, 265.0), (660.0, 265.0), (660.0, 285.0)], "drawio_pts": [(600.0, 265.0), (660.0, 265.0)]},
        # Symmetric convergence into p7: m2 -> p7
        {"id": "e6", "src": "m2", "tgt": "p7", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=0.5;exitY=1;entryX=0.75;entryY=0;", "pts": [(860.0, 245.0), (860.0, 265.0), (810.0, 265.0), (810.0, 285.0)], "drawio_pts": [(860.0, 265.0), (810.0, 265.0)]}
        # Symmetrical convergence into p7: m1 -> p7
        {"id": "e5", "src": "m1", "tgt": "p7", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=0.5;exitY=1;entryX=0.5;entryY=0;", "pts": [(520.0, 245.0), (520.0, 265.0), (650.0, 265.0), (650.0, 285.0)], "drawio_pts": [(520.0, 265.0), (650.0, 265.0)]},
        # Symmetrical convergence into p7: m2 -> p7
        {"id": "e6", "src": "m2", "tgt": "p7", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=0.5;exitY=1;entryX=0.5;entryY=0;", "pts": [(780.0, 245.0), (780.0, 265.0), (650.0, 265.0), (650.0, 285.0)], "drawio_pts": [(780.0, 265.0), (650.0, 265.0)]}
    ]
}

# ==============================================================================
# 05. KỸ THUẬT ĐẶC TRƯNG VÀ KIỂM SOÁT RÒ RỈ DỮ LIỆU (Hình 3.6)
# ==============================================================================
DIAGRAMS["05_feature_engineering"] = {
    "page_w": 1040, "page_h": 480,
    "vertices": [
        {"id": "t", "val": "Hình: Quy trình Feature Engineering và kiểm soát rò rỉ dữ liệu", "x": 0, "y": 5, "w": 1040, "h": 30, "style": "text;html=1;align=center;verticalAlign=middle;fontStyle=1;fontSize=15;fontColor=#1F3864;", "is_title": True},
        # Left input (y_mid=215.0)
        {"id": "p_sku", "val": "Panel SKU–tuần<br>(đến tuần w−1)", "x": 20, "y": 185, "w": 190, "h": 60, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#E1D5E7;strokeColor=#7E5A9B;"},
        {"id": "f_shift", "val": "Shift trước, Roll sau<br>y_past = y[w−7d]", "x": 240, "y": 185, "w": 185, "h": 60, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;"},
        # 5 Feature groups in middle column (X=475, W=235)
        {"id": "f1", "val": "Lag: 1, 2, 3, 4, 8, 12, 13, 26 tuần", "x": 475, "y": 45, "w": 235, "h": 55, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;"},
        {"id": "f2", "val": "Rolling<br>mean/std/min/max/zero-ratio + EWMA", "x": 475, "y": 115, "w": 235, "h": 55, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;"},
        # f3 is perfectly aligned at Y_mid=215.0 with Allowlist 71!
        {"id": "f3", "val": "Động lượng & tăng trưởng<br>(diff, growth ratio ∈ [−5, 5])", "x": 475, "y": 185, "w": 235, "h": 60, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;"},
        {"id": "f4", "val": "Hoạt động & giá<br>(txn_count, khách, last price)", "x": 475, "y": 260, "w": 235, "h": 55, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;"},
        {"id": "f5", "val": "Lịch xác định trước<br>tuần, tháng, sin/cos, Q4, Noel", "x": 475, "y": 330, "w": 235, "h": 55, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;"},
        # Right column: Allowlist 71 (y_mid=215.0)
        {"id": "f_allow", "val": "Allowlist 71 predictor<br>loại 11 cột (nhãn, khóa,<br>ABC/XYZ/SBC)", "x": 765, "y": 165, "w": 230, "h": 100, "style": "rhombus;whiteSpace=wrap;html=1;fillColor=#FFF2CC;strokeColor=#D6B656;"},
        # Shifted down boxes for spacious clean vertical drops
        {"id": "f_leak", "val": "Kiểm toán rò rỉ<br>(test_feature_leakage_v1_2.py)", "x": 765, "y": 305, "w": 230, "h": 60, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#F8CECC;strokeColor=#B85450;"},
        {"id": "f8", "val": "Ma trận đặc trưng<br>263.149 dòng (dev)", "x": 765, "y": 395, "w": 230, "h": 60, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#D5E8D4;strokeColor=#82B366;"}
    ],
    "edges": [
        # Input connection
        {"id": "e0", "src": "p_sku", "tgt": "f_shift", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=1;exitY=0.5;entryX=0;entryY=0.5;"},
        # Distributor bus: f_shift (425, 215) branches via bus at X=450
        {"id": "e1", "src": "f_shift", "tgt": "f1", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=1;exitY=0.5;entryX=0;entryY=0.5;", "pts": [(425.0, 215.0), (450.0, 215.0), (450.0, 72.5), (475.0, 72.5)], "drawio_pts": [(450.0, 215.0), (450.0, 72.5)]},
        {"id": "e2", "src": "f_shift", "tgt": "f2", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=1;exitY=0.5;entryX=0;entryY=0.5;", "pts": [(425.0, 215.0), (450.0, 215.0), (450.0, 142.5), (475.0, 142.5)], "drawio_pts": [(450.0, 215.0), (450.0, 142.5)]},
        # Straight horizontal into f3
        {"id": "e3", "src": "f_shift", "tgt": "f3", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=1;exitY=0.5;entryX=0;entryY=0.5;"},
        {"id": "e4", "src": "f_shift", "tgt": "f4", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=1;exitY=0.5;entryX=0;entryY=0.5;", "pts": [(425.0, 215.0), (450.0, 215.0), (450.0, 287.5), (475.0, 287.5)], "drawio_pts": [(450.0, 215.0), (450.0, 287.5)]},
        {"id": "e5", "src": "f_shift", "tgt": "f5", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=1;exitY=0.5;entryX=0;entryY=0.5;", "pts": [(425.0, 215.0), (450.0, 215.0), (450.0, 357.5), (475.0, 357.5)], "drawio_pts": [(450.0, 215.0), (450.0, 357.5)]},
        # Collector bus: f3 goes 100% straight into f_allow at Y=215.0!
        {"id": "e8", "src": "f3", "tgt": "f_allow", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=1;exitY=0.5;entryX=0;entryY=0.5;"},
        # Other 4 groups merge into the trunk at X=735
        {"id": "e6", "src": "f1", "tgt": "f_allow", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=1;exitY=0.5;entryX=0;entryY=0.5;", "pts": [(710.0, 72.5), (735.0, 72.5), (735.0, 215.0), (765.0, 215.0)], "drawio_pts": [(735.0, 72.5), (735.0, 215.0)]},
        {"id": "e7", "src": "f2", "tgt": "f_allow", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=1;exitY=0.5;entryX=0;entryY=0.5;", "pts": [(710.0, 142.5), (735.0, 142.5), (735.0, 215.0), (765.0, 215.0)], "drawio_pts": [(735.0, 142.5), (735.0, 215.0)]},
        {"id": "e9", "src": "f4", "tgt": "f_allow", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=1;exitY=0.5;entryX=0;entryY=0.5;", "pts": [(710.0, 287.5), (735.0, 287.5), (735.0, 215.0), (765.0, 215.0)], "drawio_pts": [(735.0, 287.5), (735.0, 215.0)]},
        {"id": "e10", "src": "f5", "tgt": "f_allow", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=1;exitY=0.5;entryX=0;entryY=0.5;", "pts": [(710.0, 357.5), (735.0, 357.5), (735.0, 215.0), (765.0, 215.0)], "drawio_pts": [(735.0, 357.5), (735.0, 215.0)]},
        # Collector bus: 4 branch lines merge into the trunk at X=735 with endArrow=none
        {"id": "e6", "src": "f1", "tgt": "f_allow", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=none;strokeColor=#1F3864;exitX=1;exitY=0.5;entryX=0;entryY=0.5;", "pts": [(710.0, 72.5), (735.0, 72.5), (735.0, 215.0)], "drawio_pts": [(735.0, 72.5), (735.0, 215.0)]},
        {"id": "e7", "src": "f2", "tgt": "f_allow", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=none;strokeColor=#1F3864;exitX=1;exitY=0.5;entryX=0;entryY=0.5;", "pts": [(710.0, 142.5), (735.0, 142.5), (735.0, 215.0)], "drawio_pts": [(735.0, 142.5), (735.0, 215.0)]},
        {"id": "e9", "src": "f4", "tgt": "f_allow", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=none;strokeColor=#1F3864;exitX=1;exitY=0.5;entryX=0;entryY=0.5;", "pts": [(710.0, 287.5), (735.0, 287.5), (735.0, 215.0)], "drawio_pts": [(735.0, 287.5), (735.0, 215.0)]},
        {"id": "e10", "src": "f5", "tgt": "f_allow", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=none;strokeColor=#1F3864;exitX=1;exitY=0.5;entryX=0;entryY=0.5;", "pts": [(710.0, 357.5), (735.0, 357.5), (735.0, 215.0)], "drawio_pts": [(735.0, 357.5), (735.0, 215.0)]},
        # Single central trunk from f3 (710, 215) straight through X=735 into f_allow (765, 215) with the single crisp arrowhead!
        {"id": "e8", "src": "f3", "tgt": "f_allow", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=1;exitY=0.5;entryX=0;entryY=0.5;", "pts": [(710.0, 215.0), (765.0, 215.0)]},
        # Right column straight vertical drops: f_allow -> f_leak at X=880.0
        {"id": "e11", "src": "f_allow", "tgt": "f_leak", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=0.5;exitY=1;entryX=0.5;entryY=0;"},
        # f_leak -> f8 at X=880.0
        {"id": "e12", "src": "f_leak", "tgt": "f8", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=0.5;exitY=1;entryX=0.5;entryY=0;"}
    ]
}

# ==============================================================================
# 06. PHÂN CHIA THỜI GIAN VÀ KIỂM ĐỊNH (Hình 3.7)
# 06. PHÂN CHIA THỜI GIAN VÀ KIỂM ĐỊNH (Hình 3.7 - SỐ LIỆU CHUẨN THỰC TẾ)
# ==============================================================================
DIAGRAMS["06_temporal_split"] = {
    "page_w": 1040, "page_h": 360,
    "page_w": 1040, "page_h": 380,
    "vertices": [
        {"id": "t", "val": "Hình: Phân chia thời gian (Development 5-fold OOF và Holdout)", "x": 0, "y": 5, "w": 1040, "h": 30, "style": "text;html=1;align=center;verticalAlign=middle;fontStyle=1;fontSize=15;fontColor=#1F3864;", "is_title": True},
        # Row 1 (y_mid=97.5)
        {"id": "t0", "val": "Panel đầy đủ: 96 tuần ISO<br>(2.785 SKU, bỏ 2 tuần biên)", "x": 20, "y": 65, "w": 200, "h": 65, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;"},
        {"id": "t2", "val": "Tập phát triển (Dev): 84 tuần<br>(dùng cho 5-fold CV & OOF)", "x": 260, "y": 65, "w": 220, "h": 65, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;"},
        # 5 Folds stacked vertically (center X=645.0)
        {"id": "t4", "val": "Fold 1: Train 64 tuần → Val 4 tuần", "x": 525, "y": 45, "w": 240, "h": 50, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;"},
        {"id": "t5", "val": "Fold 2: Train 68 tuần → Val 4 tuần", "x": 525, "y": 105, "w": 240, "h": 50, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;"},
        {"id": "t6", "val": "Fold 3: Train 72 tuần → Val 4 tuần", "x": 525, "y": 165, "w": 240, "h": 50, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;"},
        {"id": "t7", "val": "Fold 4: Train 76 tuần → Val 4 tuần<br>Fold 5: Train 80 tuần → Val 4 tuần", "x": 525, "y": 225, "w": 240, "h": 55, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;"},
        # Holdout box (y_mid=130.0)
        {"id": "t8", "val": "Tập kiểm định cuối (Holdout)<br>12 tuần độc lập hoàn toàn", "x": 800, "y": 95, "w": 215, "h": 70, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#D5E8D4;strokeColor=#82B366;"},
        # Row 2 (y_mid=217.5)
        {"id": "t1", "val": "Bỏ 2 tuần biên<br>(tuần đầu & cuối bị cắt lát)", "x": 20, "y": 185, "w": 200, "h": 65, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#F8CECC;strokeColor=#B85450;"},
        {"id": "t3", "val": "Nguyên tắc: Shift-before-roll<br>chống rò rỉ target trong tuần", "x": 260, "y": 185, "w": 220, "h": 65, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFF2CC;strokeColor=#D6B656;"},
        # Warning box
        {"id": "t9", "val": "Cảnh báo: Không xáo trộn ngẫu nhiên<br>(No random K-Fold)", "x": 240, "y": 295, "w": 260, "h": 50, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#F8CECC;strokeColor=#B85450;"}
        {"id": "t", "val": "Hình: Chia dữ liệu theo thời gian — Development, 5 fold OOF và Holdout", "x": 0, "y": 5, "w": 1040, "h": 30, "style": "text;html=1;align=center;verticalAlign=middle;fontStyle=1;fontSize=15;fontColor=#1F3864;", "is_title": True},
        # Box 1: 106 tuần ISO (Purple, top-left)
        {"id": "t0", "val": "106 tuần ISO<br>(2009-11-30 → 2011-12-05)", "x": 20, "y": 55, "w": 200, "h": 65, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#E1D5E7;strokeColor=#7E5A9B;"},
        # Box 2: Tuần biên không đầy đủ (Light Red, bottom-left)
        {"id": "t1", "val": "Tuần biên không đầy đủ (2)<br>2009-11-30 và 2011-12-05", "x": 20, "y": 175, "w": 200, "h": 65, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#F8CECC;strokeColor=#B85450;"},
        # Box 3: Development pool: 96 tuần mục tiêu (Blue/White, top-middle)
        {"id": "t2", "val": "Development pool: 96 tuần mục tiêu<br>2009-12-07 → 2011-10-03", "x": 260, "y": 55, "w": 225, "h": 65, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;"},
        # Box 4: Final Holdout (niêm phong): 8 tuần (Light Green, bottom-middle)
        {"id": "t3", "val": "Final Holdout (niêm phong): 8 tuần<br>2011-10-10 → 2011-11-28", "x": 260, "y": 175, "w": 225, "h": 65, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#D5E8D4;strokeColor=#82B366;"},
        # Box 5: Chấm Holdout đúng 1 lần (Yellow Diamond, bottom-middle)
        {"id": "t4", "val": "Chấm Holdout đúng 1 lần<br>(22.280 lượt dự báo)", "x": 267.5, "y": 280, "w": 210, "h": 80, "style": "rhombus;whiteSpace=wrap;html=1;fillColor=#FFF2CC;strokeColor=#D6B656;"},
        # Right column: 5 Folds stacked vertically (center X=665.0)
        {"id": "f1", "val": "Fold 1: train 56 tuần → val 8 tuần<br>(2011-01-03 → 2011-02-21)", "x": 535, "y": 40, "w": 255, "h": 55, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;"},
        {"id": "f2", "val": "Fold 2: train 64 → val 8<br>(2011-02-28 → 2011-04-18)", "x": 535, "y": 105, "w": 255, "h": 55, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;"},
        {"id": "f3", "val": "Fold 3, 4: mở rộng 8 tuần/lần", "x": 535, "y": 170, "w": 255, "h": 50, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;"},
        {"id": "f5", "val": "Fold 5: val 2011-08-15 → 2011-10-03", "x": 535, "y": 230, "w": 255, "h": 50, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;"},
        # Far Right: Pooled OOF 5 fold (Green box, widened to 200px for zero overflow)
        {"id": "oof", "val": "Pooled OOF 5 fold<br>(68.680 quan sát nhóm chính)", "x": 820, "y": 115, "w": 200, "h": 70, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#D5E8D4;strokeColor=#82B366;"}
    ],
    "edges": [
        # Straight horizontal t0 -> t2 at Y=97.5
        # Straight horizontal t0 -> t2 at Y=87.5
        {"id": "e0", "src": "t0", "tgt": "t2", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=1;exitY=0.5;entryX=0;entryY=0.5;"},
        # Straight vertical drop t0 -> t1 at X=120.0
        {"id": "e1", "src": "t0", "tgt": "t1", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=0.5;exitY=1;entryX=0.5;entryY=0;"},
        # t2 -> t4 via corridor
        {"id": "e2", "src": "t2", "tgt": "t4", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=1;exitY=0.5;entryX=0;entryY=0.5;", "pts": [(480.0, 97.5), (502.5, 97.5), (502.5, 70.0), (525.0, 70.0)], "drawio_pts": [(502.5, 97.5), (502.5, 70.0)]},
        # Straight vertical drops down the folds at X=645.0
        {"id": "e3", "src": "t4", "tgt": "t5", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=0.5;exitY=1;entryX=0.5;entryY=0;"},
        {"id": "e4", "src": "t5", "tgt": "t6", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=0.5;exitY=1;entryX=0.5;entryY=0;"},
        {"id": "e5", "src": "t6", "tgt": "t7", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=0.5;exitY=1;entryX=0.5;entryY=0;"},
        # Straight horizontal t5 -> t8 at Y=130.0
        {"id": "e6", "src": "t5", "tgt": "t8", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=1;exitY=0.5;entryX=0;entryY=0.5;"},
        # Row 2 straight horizontal t1 -> t3 at Y=217.5
        {"id": "e7", "src": "t1", "tgt": "t3", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=1;exitY=0.5;entryX=0;entryY=0.5;dashed=1;"},
        # Straight vertical drop t3 -> t9 at X=370.0
        {"id": "e8", "src": "t3", "tgt": "t9", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=0.5;exitY=1;entryX=0.5;entryY=0;"}
        # Dashed horizontal arrow t1 -> t3 at Y=207.5
        {"id": "e2", "src": "t1", "tgt": "t3", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=1;exitY=0.5;entryX=0;entryY=0.5;dashed=1;"},
        # Straight vertical drop t3 -> t4 at X=372.5
        {"id": "e3", "src": "t3", "tgt": "t4", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=0.5;exitY=1;entryX=0.5;entryY=0;"},
        # Corridor connection t2 -> f1
        {"id": "e4", "src": "t2", "tgt": "f1", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=1;exitY=0.5;entryX=0;entryY=0.5;", "pts": [(485.0, 87.5), (510.0, 87.5), (510.0, 67.5), (535.0, 67.5)], "drawio_pts": [(510.0, 87.5), (510.0, 67.5)]},
        # Straight vertical drops down the folds at X=662.5
        {"id": "e5", "src": "f1", "tgt": "f2", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=0.5;exitY=1;entryX=0.5;entryY=0;"},
        {"id": "e6", "src": "f2", "tgt": "f3", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=0.5;exitY=1;entryX=0.5;entryY=0;"},
        {"id": "e7", "src": "f3", "tgt": "f5", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=0.5;exitY=1;entryX=0.5;entryY=0;"},
        # Corridor connection from fold block to oof (68.680 quan sát)
        {"id": "e8", "src": "f5", "tgt": "oof", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=1;exitY=0.5;entryX=0;entryY=0.5;", "pts": [(790.0, 255.0), (805.0, 255.0), (805.0, 150.0), (820.0, 150.0)], "drawio_pts": [(805.0, 255.0), (805.0, 150.0)]}
    ]
}

print("Batch 1 compiled.")
