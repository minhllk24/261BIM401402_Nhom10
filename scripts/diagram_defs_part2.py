DIAGRAMS_PART2 = {}

# ==============================================================================
# 07. QUY TRÌNH HUẤN LUYỆN VÀ LỰA CHỌN THUẬT TOÁN (Hình 3.8)
# ==============================================================================
DIAGRAMS_PART2["07_model_training"] = {
    "page_w": 1040, "page_h": 400,
    "vertices": [
        {"id": "t", "val": "Hình: Quy trình huấn luyện và lựa chọn thuật toán", "x": 0, "y": 5, "w": 1040, "h": 30, "style": "text;html=1;align=center;verticalAlign=middle;fontStyle=1;fontSize=15;fontColor=#1F3864;", "is_title": True},
        {"id": "m0", "val": "Feature matrix + allowlist", "x": 20, "y": 140, "w": 200, "h": 70, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;"},
        # 3 candidate models: m1 (y_mid=90), m2 (y_mid=175), m3 (y_mid=265)
        {"id": "m1", "val": "Baseline thống kê<br>Naive_1, MA_4/8/13, Croston, SBA", "x": 255, "y": 55, "w": 235, "h": 70, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;"},
        {"id": "m2", "val": "Cây boosting<br>CatBoost (MAE, Poisson, Tweedie)<br>LightGBM (L1, Poisson, Tweedie)", "x": 255, "y": 140, "w": 235, "h": 70, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;"},
        {"id": "m3", "val": "Deep learning<br>TiDE, TFT (chuỗi, đa horizon)", "x": 255, "y": 230, "w": 235, "h": 70, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;"},
        # Early stopping diamond (y_mid=175, center X=627.5)
        {"id": "m4", "val": "Early stopping nội bộ<br>(cửa sổ thời gian cuối<br>fold)", "x": 525, "y": 130, "w": 205, "h": 90, "style": "rhombus;whiteSpace=wrap;html=1;fillColor=#FFF2CC;strokeColor=#D6B656;"},
        # Output column: all center X=870.0
        {"id": "m5", "val": "Dự báo OOF 5 fold", "x": 765, "y": 60, "w": 210, "h": 60, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;"},
        {"id": "m6", "val": "Bảng metric pooled OOF", "x": 765, "y": 145, "w": 210, "h": 60, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#D5E8D4;strokeColor=#82B366;"},
        {"id": "m7", "val": "Chọn ứng viên theo ma<br>trận đa tiêu chí", "x": 765, "y": 230, "w": 210, "h": 70, "style": "rhombus;whiteSpace=wrap;html=1;fillColor=#FFF2CC;strokeColor=#D6B656;"}
    ],
    "edges": [
        # Fork from m0 to m1 (top) via distributor bus at X=237.5
        {"id": "e0", "src": "m0", "tgt": "m1", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=1;exitY=0.5;entryX=0;entryY=0.5;", "pts": [(220.0, 175.0), (237.5, 175.0), (237.5, 90.0), (255.0, 90.0)], "drawio_pts": [(237.5, 175.0), (237.5, 90.0)]},
        # Straight horizontal m0 -> m2 at Y=175.0
        {"id": "e1", "src": "m0", "tgt": "m2", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=1;exitY=0.5;entryX=0;entryY=0.5;"},
        # Fork from m0 to m3 (bottom) via distributor bus at X=237.5
        {"id": "e2", "src": "m0", "tgt": "m3", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=1;exitY=0.5;entryX=0;entryY=0.5;", "pts": [(220.0, 175.0), (237.5, 175.0), (237.5, 265.0), (255.0, 265.0)], "drawio_pts": [(237.5, 175.0), (237.5, 265.0)]},
        # Straight horizontal m1 -> m5 at Y=90.0
        {"id": "e3", "src": "m1", "tgt": "m5", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=1;exitY=0.5;entryX=0;entryY=0.5;"},
        # Straight horizontal m2 -> m4 at Y=175.0
        {"id": "e4", "src": "m2", "tgt": "m4", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=1;exitY=0.5;entryX=0;entryY=0.5;"},
        # m3 -> m4: clean 90-deg turn into bottom apex of m4
        {"id": "e5", "src": "m3", "tgt": "m4", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=1;exitY=0.5;entryX=0.5;entryY=1;", "pts": [(490.0, 265.0), (627.5, 265.0), (627.5, 220.0)], "drawio_pts": [(627.5, 265.0)]},
        # Straight horizontal m4 -> m6 at Y=175.0
        {"id": "e6", "src": "m4", "tgt": "m6", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=1;exitY=0.5;entryX=0;entryY=0.5;"},
        # Straight vertical drop m5 -> m6 at X=870.0
        {"id": "e7", "src": "m5", "tgt": "m6", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=0.5;exitY=1;entryX=0.5;entryY=0;"},
        # Straight vertical drop m6 -> m7 at X=870.0
        {"id": "e8", "src": "m6", "tgt": "m7", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=0.5;exitY=1;entryX=0.5;entryY=0;"}
    ]
}

# ==============================================================================
# 08. HUẤN LUYỆN CATBOOST VÀ ROLLOUT ĐỆ QUY (Hình 3.9)
# ==============================================================================
DIAGRAMS_PART2["08_catboost_rollout"] = {
    "page_w": 1040, "page_h": 360,
    "vertices": [
        {"id": "t", "val": "Hình: Huấn luyện CatBoost MAE và suy luận đa bước theo rollout đệ quy", "x": 0, "y": 5, "w": 1040, "h": 30, "style": "text;html=1;align=center;verticalAlign=middle;fontStyle=1;fontSize=15;fontColor=#1F3864;", "is_title": True},
        # Row 1 (y_mid=95.0)
        {"id": "c0", "val": "Đặc trưng tại gốc dự báo T", "x": 20, "y": 62.5, "w": 190, "h": 65, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;"},
        {"id": "c1", "val": "CatBoost MAE<br>depth=6, lr=0.05, seed=42<br>340 vòng (nhóm chính)", "x": 250, "y": 52.5, "w": 235, "h": 85, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;"},
        {"id": "c2", "val": "ŷ(h) → cắt ≥ 0", "x": 525, "y": 62.5, "w": 190, "h": 65, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;"},
        {"id": "c7", "val": "Chuỗi dự báo H=1..4", "x": 785, "y": 62.5, "w": 195, "h": 65, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#D5E8D4;strokeColor=#82B366;"},
        # Row 2 (y_mid=225.0)
        {"id": "c3", "val": "Đặc trưng chưa biết:<br>carry-forward từ gốc", "x": 20, "y": 190, "w": 190, "h": 70, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#F8CECC;strokeColor=#B85450;"},
        {"id": "c4", "val": "Lịch tuần kế tiếp<br>(xác định)", "x": 250, "y": 190, "w": 200, "h": 70, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;"},
        {"id": "c5", "val": "Cập nhật buffer lag đệ quy<br>(dự báo thay cho thực tế)", "x": 505, "y": 190, "w": 230, "h": 70, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;"},
        {"id": "c4", "val": "Lịch tuần kế tiếp<br>(xác định)", "x": 250, "y": 190, "w": 235, "h": 70, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;"},
        {"id": "c5", "val": "Cập nhật buffer lag đệ quy<br>(dự báo thay cho thực tế)", "x": 515, "y": 190, "w": 210, "h": 70, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;"},
        {"id": "c6", "val": "h = h + 1 (lặp đến H=4)<br>h ≤ H? (Có → bước tiếp;<br>Không → kết thúc)", "x": 780, "y": 175, "w": 200, "h": 100, "style": "rhombus;whiteSpace=wrap;html=1;fillColor=#FFF2CC;strokeColor=#D6B656;"}
    ],
    "edges": [
        # Row 1 straight horizontal at Y=95.0
        {"id": "e0", "src": "c0", "tgt": "c1", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=1;exitY=0.5;entryX=0;entryY=0.5;"},
        {"id": "e1", "src": "c1", "tgt": "c2", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=1;exitY=0.5;entryX=0;entryY=0.5;"},
        {"id": "e2", "src": "c2", "tgt": "c7", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=1;exitY=0.5;entryX=0;entryY=0.5;"},
        # Straight vertical drop c2 -> c5 at X=620.0
        {"id": "e3", "src": "c2", "tgt": "c5", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=0.5;exitY=1;entryX=0.5;entryY=0;"},
        # Row 2 straight horizontal at Y=225.0
        # Row 2 straight horizontal: c3 -> c4, c4 -> c5, c5 -> c6
        {"id": "e4", "src": "c3", "tgt": "c4", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=1;exitY=0.5;entryX=0;entryY=0.5;"},
        {"id": "e5", "src": "c4", "tgt": "c5", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=1;exitY=0.5;entryX=0;entryY=0.5;"},
        {"id": "e6", "src": "c5", "tgt": "c6", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=1;exitY=0.5;entryX=0;entryY=0.5;"},
        # Clean perimeter feedback loop: from c6 bottom (880, 275) around bottom (Y=315) and left margin (X=10) into c0
        {"id": "e7", "src": "c6", "tgt": "c0", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=0.5;exitY=1;entryX=0;entryY=0.5;dashed=1;", "pts": [(880.0, 275.0), (880.0, 315.0), (10.0, 315.0), (10.0, 95.0), (20.0, 95.0)], "drawio_pts": [(880.0, 315.0), (10.0, 315.0), (10.0, 95.0)]}
        # Feedback loop: from c6 bottom (880, 275) down to Y=315, left along clear bottom corridor to X=115, up into c3 bottom (115, 260)
        {"id": "e7", "src": "c6", "tgt": "c3", "val": "Có (h ≤ H)", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=0.5;exitY=1;entryX=0.5;entryY=1;dashed=1;", "pts": [(880.0, 275.0), (880.0, 315.0), (115.0, 315.0), (115.0, 260.0)], "drawio_pts": [(880.0, 315.0), (115.0, 315.0)]},
        # Feature input from c4 up into CatBoost MAE c1 at X=350.0
        {"id": "e8", "src": "c4", "tgt": "c1", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=0.5;exitY=0;entryX=0.5;entryY=1;"}
    ]
}

# ==============================================================================
# 09. KIẾN TRÚC MÔ HÌNH DEEP LEARNING TiDE (Hình 3.10)
# ==============================================================================
DIAGRAMS_PART2["09_deep_learning_flow"] = {
    "page_w": 1040, "page_h": 320,
    "vertices": [
        {"id": "t", "val": "Hình: Kiến trúc luồng suy luận Deep Learning (TiDE)", "x": 0, "y": 5, "w": 1040, "h": 30, "style": "text;html=1;align=center;verticalAlign=middle;fontStyle=1;fontSize=15;fontColor=#1F3864;", "is_title": True},
        # Row 1 (y_mid=102.5)
        {"id": "d1", "val": "Chuỗi quá khứ L=13 tuần<br>+ tương lai H=4 tuần<br>+ static attributes", "x": 20, "y": 65, "w": 210, "h": 75, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;"},
        {"id": "d2", "val": "Feature Projection<br>& Dense Encoder (MLP)<br>áp dụng ReLU + Dropout", "x": 265, "y": 65, "w": 225, "h": 75, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;"},
        {"id": "d3", "val": "Dense Decoder<br>giải mã đặc trưng ẩn<br>cho H=4 bước tương lai", "x": 525, "y": 65, "w": 235, "h": 75, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;"},
        # Green box spans Y=65..260 so both inputs enter 100% straight horizontally!
        {"id": "d5", "val": "Dự báo đa bước H=1..4<br>(tương đương CatBoost<br>rollout, độc lập từng bước)", "x": 795, "y": 65, "w": 225, "h": 195, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#D5E8D4;strokeColor=#82B366;"},
        # Row 2: Skip connection (y_mid=212.5)
        {"id": "d_hid", "val": "Biểu diễn đặc trưng ẩn<br>(kích thước d_model = 64/128)", "x": 265, "y": 180, "w": 225, "h": 65, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#E1D5E7;strokeColor=#7E5A9B;"},
        {"id": "d_skip", "val": "Linear Skip Connection<br>Ánh xạ trực tiếp từ đầu vào<br>sang không gian đầu ra", "x": 525, "y": 180, "w": 235, "h": 65, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFF2CC;strokeColor=#D6B656;"}
    ],
    "edges": [
        # Row 1 straight horizontal
        {"id": "e0", "src": "d1", "tgt": "d2", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=1;exitY=0.5;entryX=0;entryY=0.5;"},
        {"id": "e1", "src": "d2", "tgt": "d3", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=1;exitY=0.5;entryX=0;entryY=0.5;"},
        # d3 -> d5: 100% DEAD STRAIGHT HORIZONTAL LINE (NO KINKS!)
        {"id": "e2", "src": "d3", "tgt": "d5", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=1;exitY=0.5;entryX=0;entryY=0.192;"},
        {"id": "e2", "src": "d3", "tgt": "d5", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=1;exitY=0.5;entryX=0;entryY=0.1923;", "pts": [(760.0, 102.5), (795.0, 102.5)]},
        # Straight vertical drop d2 -> d_hid at X=377.5
        {"id": "e3", "src": "d2", "tgt": "d_hid", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=0.5;exitY=1;entryX=0.5;entryY=0;"},
        # Row 2 straight horizontal
        {"id": "e4", "src": "d_hid", "tgt": "d_skip", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=1;exitY=0.5;entryX=0;entryY=0.5;dashed=1;"},
        # d_skip -> d5: 100% DEAD STRAIGHT HORIZONTAL LINE (NO KINKS!)
        {"id": "e5", "src": "d_skip", "tgt": "d5", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=1;exitY=0.5;entryX=0;entryY=0.756;"}
        {"id": "e5", "src": "d_skip", "tgt": "d5", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=1;exitY=0.5;entryX=0;entryY=0.7564;", "pts": [(760.0, 212.5), (795.0, 212.5)]}
    ]
}

# ==============================================================================
# 10. QUY TRÌNH ĐÁNH GIÁ MÔ HÌNH VÀ BẢO VỆ CHỐNG LEAKAGE (Hình 3.11)
# ==============================================================================
DIAGRAMS_PART2["10_model_evaluation"] = {
    "page_w": 1040, "page_h": 340,
    "vertices": [
        {"id": "t", "val": "Hình: Quy trình đánh giá mô hình và cơ chế bảo vệ chống rò rỉ", "x": 0, "y": 5, "w": 1040, "h": 30, "style": "text;html=1;align=center;verticalAlign=middle;fontStyle=1;fontSize=15;fontColor=#1F3864;", "is_title": True},
        # Row 1 (y_mid=97.5)
        {"id": "e1", "val": "5 folds Expanding<br>Window (Walk-Forward)", "x": 20, "y": 65, "w": 190, "h": 65, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;"},
        {"id": "e2", "val": "Tính metric từng fold<br>(MAE, RMSE, WAPE,<br>SMAPE, Pinball 0.1/0.5/0.9)", "x": 245, "y": 65, "w": 225, "h": 65, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;"},
        {"id": "e3", "val": "Gộp dự báo (Pooled OOF)<br>trên toàn bộ 5 fold", "x": 505, "y": 55, "w": 210, "h": 85, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;"},
        {"id": "e4", "val": "Phân rã hiệu năng theo<br>nhóm ABC / XYZ", "x": 755, "y": 65, "w": 235, "h": 65, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;"},
        # Row 2 (y_mid=240.0)
        {"id": "e5", "val": "Kiểm định thống kê:<br>Wilcoxon signed-rank + DM-test", "x": 497.5, "y": 205, "w": 225, "h": 70, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#D5E8D4;strokeColor=#82B366;"},
        {"id": "e6", "val": "Bảo vệ chống rò rỉ (Leakage Guard)<br>Đánh giá strictly trên tập test<br>(không can thiệp tương lai)", "x": 760, "y": 205, "w": 225, "h": 70, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#F8CECC;strokeColor=#B85450;"}
    ],
    "edges": [
        # Row 1 straight horizontal
        {"id": "e0", "src": "e1", "tgt": "e2", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=1;exitY=0.5;entryX=0;entryY=0.5;"},
        {"id": "e1", "src": "e2", "tgt": "e3", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=1;exitY=0.5;entryX=0;entryY=0.5;"},
        {"id": "e2", "src": "e3", "tgt": "e4", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=1;exitY=0.5;entryX=0;entryY=0.5;"},
        # Straight vertical drop e3 -> e5 at X=610.0
        {"id": "e3", "src": "e3", "tgt": "e5", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=0.5;exitY=1;entryX=0.5;entryY=0;"},
        # Straight vertical drop e4 -> e6 at X=872.5
        {"id": "e4", "src": "e4", "tgt": "e6", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=0.5;exitY=1;entryX=0.5;entryY=0;"},
        # Straight horizontal e5 -> e6 at Y=240.0
        {"id": "e5", "src": "e5", "tgt": "e6", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=1;exitY=0.5;entryX=0;entryY=0.5;dashed=1;"}
    ]
}

# ==============================================================================
# 11. MODEL REGISTRY VÀ ĐÓNG BĂNG MÔ HÌNH (Hình 3.12)
# ==============================================================================
DIAGRAMS_PART2["11_model_registry"] = {
    "page_w": 1040, "page_h": 360,
    "vertices": [
        {"id": "t", "val": "Hình: Model Registry, đóng băng mô hình và trạng thái phục vụ", "x": 0, "y": 5, "w": 1040, "h": 30, "style": "text;html=1;align=center;verticalAlign=middle;fontStyle=1;fontSize=15;fontColor=#1F3864;", "is_title": True},
        # Row 1 (y_mid=107.5)
        {"id": "s0", "val": "Artifact huấn luyện<br>(.cbm/.joblib/.pt)", "x": 20, "y": 75, "w": 185, "h": 65, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;"},
        {"id": "s1", "val": "Tính SHA-256 + manifest<br>(allowlist, cấu hình, horizon)", "x": 240, "y": 75, "w": 215, "h": 65, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;"},
        {"id": "s2", "val": "ArtifactRole:<br>CV_ARTIFACT → CANDIDATE<br>→<br>FROZEN_MODEL →<br>INFERENCE_TESTED", "x": 495, "y": 50, "w": 250, "h": 115, "style": "rhombus;whiteSpace=wrap;html=1;fillColor=#FFF2CC;strokeColor=#D6B656;"},
        # Output branches: s3 at Y=85.0, s4 at Y=180.0
        {"id": "s3", "val": "SERVING_READY<br>(được phép dự báo)", "x": 800, "y": 55, "w": 195, "h": 60, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#D5E8D4;strokeColor=#82B366;"},
        {"id": "s4", "val": "NOT_READY<br>(HTTP 409 khi gọi dự báo)", "x": 800, "y": 150, "w": 195, "h": 60, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#F8CECC;strokeColor=#B85450;"},
        # Verification service (center X=620.0 matching s2)
        {"id": "s5", "val": "Model Registry Service<br>kiểm tra đường dẫn trong thư mục<br>quản lý", "x": 495, "y": 235, "w": 250, "h": 70, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#E1D5E7;strokeColor=#7E5A9B;"}
    ],
    "edges": [
        # Straight horizontal s0 -> s1 at Y=107.5
        {"id": "e0", "src": "s0", "tgt": "s1", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=1;exitY=0.5;entryX=0;entryY=0.5;"},
        # Straight horizontal s1 -> s2 at Y=107.5
        {"id": "e1", "src": "s1", "tgt": "s2", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=1;exitY=0.5;entryX=0;entryY=0.5;"},
        # Fork to s3 (SERVING_READY) via distributor bus at X=770.0
        {"id": "e2", "src": "s2", "tgt": "s3", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=1;exitY=0.5;entryX=0;entryY=0.5;", "pts": [(745.0, 107.5), (770.0, 107.5), (770.0, 85.0), (800.0, 85.0)], "drawio_pts": [(770.0, 107.5), (770.0, 85.0)]},
        # Fork to s4 (NOT_READY) via distributor bus at X=770.0
        {"id": "e3", "src": "s2", "tgt": "s4", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=1;exitY=0.5;entryX=0;entryY=0.5;", "pts": [(745.0, 107.5), (770.0, 107.5), (770.0, 180.0), (800.0, 180.0)], "drawio_pts": [(770.0, 107.5), (770.0, 180.0)]},
        # Straight vertical drop from s5 up into s2 at X=620.0
        {"id": "e4", "src": "s5", "tgt": "s2", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=0.5;exitY=0;entryX=0.5;entryY=1;"}
    ]
}

# ==============================================================================
# 12. LUỒNG SUY LUẬN DỰ BÁO VÀ PHÒNG THỦ DỮ LIỆU (Hình 3.13)
# 12. LUỒNG SUY LUẬN DỰ BÁO KHI CÓ YÊU CẦU TỪ NGƯỜI DÙNG (Hình 3.13 - SỐ LIỆU CHUẨN THỰC TẾ)
# ==============================================================================
DIAGRAMS_PART2["12_forecast_inference"] = {
    "page_w": 1040, "page_h": 400,
    "page_w": 1040, "page_h": 380,
    "vertices": [
        {"id": "t", "val": "Hình: Luồng suy luận dự báo và cơ chế phòng thủ dữ liệu", "x": 0, "y": 5, "w": 1040, "h": 30, "style": "text;html=1;align=center;verticalAlign=middle;fontStyle=1;fontSize=15;fontColor=#1F3864;", "is_title": True},
        # Tier 1 (Top, y_mid=87.5): Happy path request validation & load
        {"id": "i0", "val": "Yêu cầu dự báo<br>POST /forecasts/run<br>(SKU, Horizon = 4)", "x": 20, "y": 55, "w": 195, "h": 65, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;"},
        {"id": "i1", "val": "Schema Validation<br>(FastAPI Pydantic,<br>kiểu & ràng buộc)", "x": 250, "y": 40, "w": 210, "h": 95, "style": "rhombus;whiteSpace=wrap;html=1;fillColor=#FFF2CC;strokeColor=#D6B656;"},
        {"id": "i2", "val": "Defense in depth<br>(SKU tồn tại, đủ dữ liệu<br>lịch sử, manifest hợp lệ)", "x": 495, "y": 40, "w": 210, "h": 95, "style": "rhombus;whiteSpace=wrap;html=1;fillColor=#FFF2CC;strokeColor=#D6B656;"},
        {"id": "i3", "val": "Nạp mô hình FROZEN<br>(kiểm tra SHA-256)", "x": 740, "y": 55, "w": 220, "h": 65, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;"},
        # Tier 2 (Middle, y_mid=207.5): Rejection (under i1 & i2) and Execution (under i3)
        {"id": "i7", "val": "Từ chối sớm: HTTP 400 / 404 / 422<br>(thất bại schema, SKU lạ, thiếu dữ liệu)", "x": 250, "y": 175, "w": 455, "h": 65, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#F8CECC;strokeColor=#B85450;"},
        {"id": "i4", "val": "Suy luận đa bước<br>(CatBoost rollout / TiDE)", "x": 740, "y": 175, "w": 220, "h": 65, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;"},
        # Tier 3 (Bottom, y_mid=315.0): Persistence & Success Response
        {"id": "i5", "val": "Ghi nhận SQLite & MySQL<br>forecast_runs &amp;<br>forecast_records", "x": 740, "y": 277.5, "w": 220, "h": 75, "style": "shape=cylinder3;boundedLbl=1;whiteSpace=wrap;html=1;fillColor=#E1D5E7;strokeColor=#7E5A9B;"},
        {"id": "i6", "val": "Trả về 200 OK<br>+ mảng dự báo H bước", "x": 465, "y": 277.5, "w": 240, "h": 75, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#D5E8D4;strokeColor=#82B366;"}
        {"id": "t", "val": "Hình: Luồng suy luận dự báo khi có yêu cầu từ người dùng", "x": 0, "y": 5, "w": 1040, "h": 30, "style": "text;html=1;align=center;verticalAlign=middle;fontStyle=1;fontSize=15;fontColor=#1F3864;", "is_title": True},
        # Row 1 (y_mid=90.0): Left to right
        {"id": "i0", "val": "POST /api/v1/forecasts<br>(JWT, vai trò ≥ Analyst)", "x": 20, "y": 55, "w": 200, "h": 70, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;"},
        {"id": "i1", "val": "Xác thực + RBAC + kiểm<br>tra schema<br>horizon ≤ 4", "x": 255, "y": 42.5, "w": 215, "h": 95, "style": "rhombus;whiteSpace=wrap;html=1;fillColor=#FFF2CC;strokeColor=#D6B656;"},
        {"id": "i2", "val": "Registry: model_id<br>SERVING_READY?", "x": 510, "y": 42.5, "w": 215, "h": 95, "style": "rhombus;whiteSpace=wrap;html=1;fillColor=#FFF2CC;strokeColor=#D6B656;"},
        {"id": "i3", "val": "Nạp mô hình + panel dữ liệu", "x": 765, "y": 55, "w": 215, "h": 70, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;"},
        # Row 2 (y_mid=210.0): Right to left
        {"id": "i4", "val": "Rollout H=1..4<br>cho các SKU yêu cầu", "x": 765, "y": 175, "w": 215, "h": 70, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#6C8EBF;"},
        {"id": "i5", "val": "Lưu run + records<br>(SQLite, UNIQUE run×sku×tuần)", "x": 505, "y": 175, "w": 225, "h": 70, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#E1D5E7;strokeColor=#7E5A9B;"},
        {"id": "i6", "val": "Phản hồi JSON /<br>xuất CSV, XLSX", "x": 255, "y": 175, "w": 215, "h": 70, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#D5E8D4;strokeColor=#82B366;"},
        # Row 3 (y_mid=315.0): Error branch reference box across bottom
        {"id": "i7", "val": "Nhánh lỗi: sai/thiếu token → 401; thiếu quyền → 403;<br>sai schema hoặc H > 4 → 422; mô hình NOT_READY → 409", "x": 255, "y": 285, "w": 475, "h": 60, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#F8CECC;strokeColor=#B85450;"}
    ],
    "edges": [
        # Tier 1 straight horizontal at Y=87.5
        # Row 1 straight horizontal at Y=90.0
        {"id": "e0", "src": "i0", "tgt": "i1", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=1;exitY=0.5;entryX=0;entryY=0.5;"},
        {"id": "e1", "src": "i1", "tgt": "i2", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=1;exitY=0.5;entryX=0;entryY=0.5;"},
        {"id": "e2", "src": "i2", "tgt": "i3", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=1;exitY=0.5;entryX=0;entryY=0.5;"},
        # Straight vertical drops from diamonds into Rejection box i7 (ZERO COLLISIONS!)
        {"id": "e6", "src": "i1", "tgt": "i7", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=0.5;exitY=1;entryX=0.23;entryY=0;dashed=1;"},
        {"id": "e7", "src": "i2", "tgt": "i7", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=0.5;exitY=1;entryX=0.77;entryY=0;dashed=1;"},
        # Straight vertical drop i3 -> i4 at X=850.0
        {"id": "e1", "src": "i1", "tgt": "i2", "val": "hợp lệ", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=1;exitY=0.5;entryX=0;entryY=0.5;"},
        {"id": "e2", "src": "i2", "tgt": "i3", "val": "có", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=1;exitY=0.5;entryX=0;entryY=0.5;"},
        # Straight vertical drop i3 -> i4 at X=872.5
        {"id": "e3", "src": "i3", "tgt": "i4", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=0.5;exitY=1;entryX=0.5;entryY=0;"},
        # Straight vertical drop i4 -> i5 at X=850.0
        {"id": "e4", "src": "i4", "tgt": "i5", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=0.5;exitY=1;entryX=0.5;entryY=0;"},
        # Straight horizontal line left from i5 into i6 at Y=315.0
        # Row 2 straight horizontal pointing left at Y=210.0
        {"id": "e4", "src": "i4", "tgt": "i5", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=0;exitY=0.5;entryX=1;entryY=0.5;"},
        {"id": "e5", "src": "i5", "tgt": "i6", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=0;exitY=0.5;entryX=1;entryY=0.5;"}
    ]
}

# ==============================================================================
# 13. QUY TRÌNH MÔ PHỎNG BỔ SUNG TỒN KHO (Hình 3.14)
# ==============================================================================
DIAGRAMS_PART2["13_inventory_planning"] = {
    "page_w": 1040, "page_h": 400,
    "vertices": [
        {"id": "t", "val": "Hình: Quy trình mô phỏng bổ sung tồn kho", "x": 0, "y": 5, "w": 1040, "h": 30, "style": "text;html=1;align=center;verticalAlign=middle;fontStyle=1;fontSize=15;fontColor=#1F3864;", "is_title": True},
        # Row 1 (y_mid=97.5)
        {"id": "v0", "val": "Dự báo H=1..4 (forecast_run)<br>hoặc nhu cầu nhập tay", "x": 20, "y": 65, "w": 210, "h": 65, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;"},
        {"id": "v1", "val": "Protection period = L + R<br>(lead time + chu kỳ rà soát)", "x": 255, "y": 65, "w": 215, "h": 65, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;"},
        {"id": "v2", "val": "∑ dự báo bước ≤ L+R", "x": 500, "y": 65, "w": 215, "h": 65, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;"},
        {"id": "v_ref", "val": "Tham khảo: phân loại ABC / XYZ /<br>SBC<br>(hiển thị ở SKU Explorer)", "x": 745, "y": 65, "w": 240, "h": 65, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#E1D5E7;strokeColor=#7E5A9B;"},
        # Row 2 (y_mid=212.5) -> all h=75
        {"id": "v3", "val": "Gross = ∑ dự báo + tồn an toàn<br>(người dùng nhập)", "x": 500, "y": 175, "w": 215, "h": 75, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;"},
        {"id": "v4", "val": "Net = Gross − tồn kho − hàng<br>đang về", "x": 255, "y": 175, "w": 215, "h": 75, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;"},
        {"id": "v5", "val": "Đơn bổ sung = max(0, Net)<br>SIMULATION_BASED_ON<br>_USER_ASSUMPTIONS", "x": 20, "y": 175, "w": 210, "h": 75, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#D5E8D4;strokeColor=#82B366;"},
        # Warning box
        {"id": "v6", "val": "Cảnh báo: không chứng minh tối ưu,<br>không bảo đảm tránh thiếu hàng", "x": 255, "y": 285, "w": 300, "h": 60, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#F8CECC;strokeColor=#B85450;"}
    ],
    "edges": [
        # Row 1 straight horizontal at Y=97.5
        {"id": "e0", "src": "v0", "tgt": "v1", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=1;exitY=0.5;entryX=0;entryY=0.5;"},
        {"id": "e1", "src": "v1", "tgt": "v2", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=1;exitY=0.5;entryX=0;entryY=0.5;"},
        # Straight vertical drop v2 -> v3 at X=607.5
        {"id": "e2", "src": "v2", "tgt": "v3", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=0.5;exitY=1;entryX=0.5;entryY=0;"},
        # Row 2 straight horizontal right-to-left at Y=212.5
        {"id": "e3", "src": "v3", "tgt": "v4", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=0;exitY=0.5;entryX=1;entryY=0.5;"},
        {"id": "e4", "src": "v4", "tgt": "v5", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=0;exitY=0.5;entryX=1;entryY=0.5;"},
        # Warning connector to v6
        {"id": "e5", "src": "v5", "tgt": "v6", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=0.5;exitY=1;entryX=0;entryY=0.5;dashed=1;", "pts": [(125.0, 250.0), (125.0, 315.0), (255.0, 315.0)], "drawio_pts": [(125.0, 315.0)]}
    ]
}

print("Batch 2 compiled.")
