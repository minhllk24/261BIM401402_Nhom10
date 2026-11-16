DIAGRAMS_PART3 = {}

# ==============================================================================
# 14. KIẾN TRÚC GIẢI PHÁP TÍCH HỢP (Hình 3.3)
# ==============================================================================
DIAGRAMS_PART3["14_system_architecture"] = {
    "page_w": 1040, "page_h": 410,
    "vertices": [
        {"id": "t", "val": "Hình: Kiến trúc giải pháp tích hợp (Desktop PyQt6 – Backend – MySQL – Cloud)", "x": 0, "y": 5, "w": 1040, "h": 30, "style": "text;html=1;align=center;verticalAlign=middle;fontStyle=1;fontSize=15;fontColor=#1F3864;", "is_title": True},
        # Tier 1: Presentation (y=55, h=75)
        {"id": "u1", "val": "Ứng dụng Desktop PyQt6<br>(Màn hình chính, Đăng nhập, Dự báo,<br>Hoạch định tồn kho, Quản lý SKU)", "x": 40, "y": 55, "w": 280, "h": 75, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;"},
        {"id": "u2", "val": "Ứng dụng Web React 18 SPA<br>(10 trang phân tích, biểu đồ trực quan,<br>Vercel CDN hosting)", "x": 380, "y": 55, "w": 280, "h": 75, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;"},
        {"id": "u3", "val": "Người dùng cuối (End-Users)<br>Analyst, Supply Chain Planner,<br>System Administrator", "x": 720, "y": 55, "w": 280, "h": 75, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;"},
        # Tier 2: Logic & Services (y=175, h=80)
        {"id": "s1", "val": "Cơ chế phòng vệ Hybrid Fallback<br>Desktop ưu tiên kết nối MySQL cục bộ;<br>tự động chuyển sang Cloud API khi cần", "x": 40, "y": 175, "w": 280, "h": 80, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFF2CC;strokeColor=#D6B656;"},
        {"id": "s2", "val": "FastAPI Cloud Web Service<br>29 API Endpoints: Auth, Forecasts,<br>SKU Catalog, Planning, Health Check", "x": 380, "y": 175, "w": 280, "h": 80, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#1F3864;"},
        {"id": "s3", "val": "Động cơ Học máy & Tồn kho<br>CatBoost Rollout, TiDE Sequence,<br>Bộ tính toán bổ sung định kỳ (R, S)", "x": 720, "y": 175, "w": 280, "h": 80, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#1F3864;"},
        # Tier 3: Data & Artifacts (y=300, h=75)
        {"id": "d1", "val": "MySQL Server 8.0 (Doanh nghiệp)<br>8 bảng quan hệ: online_retail, sku_catalog,<br>app_users, inventory_audit_log", "x": 40, "y": 300, "w": 280, "h": 75, "style": "shape=cylinder3;boundedLbl=1;whiteSpace=wrap;html=1;fillColor=#E1D5E7;strokeColor=#7E5A9B;"},
        {"id": "d2", "val": "SQLite Embedded Database<br>Lưu lịch sử chạy dự báo (forecast_runs),<br>bản ghi dự báo & export_artifacts", "x": 380, "y": 300, "w": 280, "h": 75, "style": "shape=cylinder3;boundedLbl=1;whiteSpace=wrap;html=1;fillColor=#E1D5E7;strokeColor=#7E5A9B;"},
        {"id": "d3", "val": "Model Registry & Artifacts<br>Trọng số mô hình (.cbm, .pt),<br>Manifest, Feature allowlist (Parquet)", "x": 720, "y": 300, "w": 280, "h": 75, "style": "shape=cylinder3;boundedLbl=1;whiteSpace=wrap;html=1;fillColor=#D5E8D4;strokeColor=#4F8A3C;"}
    ],
    "edges": [
        {"id": "e0", "src": "u1", "tgt": "s1", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=0.5;exitY=1;entryX=0.5;entryY=0;"},
        {"id": "e1", "src": "u2", "tgt": "s2", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=0.5;exitY=1;entryX=0.5;entryY=0;"},
        {"id": "e2", "src": "u3", "tgt": "s3", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=0.5;exitY=1;entryX=0.5;entryY=0;"},
        {"id": "e3", "src": "s1", "tgt": "d1", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=0.5;exitY=1;entryX=0.5;entryY=0;"},
        {"id": "e4", "src": "s2", "tgt": "d2", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=0.5;exitY=1;entryX=0.5;entryY=0;"},
        {"id": "e5", "src": "s3", "tgt": "d3", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=0.5;exitY=1;entryX=0.5;entryY=0;"},
        {"id": "e6", "src": "s1", "tgt": "s2", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=1;exitY=0.5;entryX=0;entryY=0.5;dashed=1;"},
        {"id": "e7", "src": "s2", "tgt": "s3", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=1;exitY=0.5;entryX=0;entryY=0.5;"}
    ]
}

# ==============================================================================
# 15. LUỒNG TƯƠNG TÁC API (Hình 3.15)
# ==============================================================================
DIAGRAMS_PART3["15_api_sequence"] = {
    "page_w": 1040, "page_h": 680,
    "vertices": [
        {"id": "t", "val": "Hình: Luồng tương tác API (đăng nhập → dự báo → lưu → phản hồi)", "x": 0, "y": 5, "w": 1040, "h": 30, "style": "text;html=1;align=center;verticalAlign=middle;fontStyle=1;fontSize=15;fontColor=#1F3864;", "is_title": True},
        # 5 Lifeline Headers
        {"id": "g1", "val": "Người dùng / Client<br>(PyQt6 / React SPA)", "x": 30, "y": 50, "w": 180, "h": 50, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;"},
        {"id": "g2", "val": "FastAPI Router<br>(Cổng tiếp nhận)", "x": 240, "y": 50, "w": 170, "h": 50, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#1F3864;"},
        {"id": "g3", "val": "Auth & RBAC<br>(Xác thực & quyền)", "x": 440, "y": 50, "w": 170, "h": 50, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#1F3864;"},
        {"id": "g4", "val": "Forecast Service<br>(Động cơ dự báo)", "x": 640, "y": 50, "w": 170, "h": 50, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#1F3864;"},
        {"id": "g5", "val": "Database & Storage<br>(MySQL / SQLite)", "x": 840, "y": 50, "w": 170, "h": 65, "style": "shape=cylinder3;boundedLbl=1;whiteSpace=wrap;html=1;fillColor=#E1D5E7;strokeColor=#7E5A9B;"},
        # 5 Lifeline End circles
        {"id": "end1", "val": "", "x": 115, "y": 645, "w": 10, "h": 10, "style": "ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#8497B0;"},
        {"id": "end2", "val": "", "x": 320, "y": 645, "w": 10, "h": 10, "style": "ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#8497B0;"},
        {"id": "end3", "val": "", "x": 520, "y": 645, "w": 10, "h": 10, "style": "ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#8497B0;"},
        {"id": "end4", "val": "", "x": 720, "y": 645, "w": 10, "h": 10, "style": "ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#8497B0;"},
        {"id": "end5", "val": "", "x": 920, "y": 645, "w": 10, "h": 10, "style": "ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#8497B0;"},
        # 8 Steps
        {"id": "s1", "val": "1. POST /auth/login<br>(username + password)", "x": 120, "y": 115, "w": 205, "h": 45, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#1F3864;"},
        {"id": "s2", "val": "2. PBKDF2 verify<br>Cấp JWT Token (HS256)", "x": 325, "y": 180, "w": 200, "h": 45, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#1F3864;"},
        {"id": "s3", "val": "3. Phản hồi 200 OK<br>Kèm JWT Bearer Token", "x": 120, "y": 245, "w": 205, "h": 45, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#D5E8D4;strokeColor=#4F8A3C;"},
        {"id": "s4", "val": "4. POST /forecasts/run<br>(Bearer Token, SKU, H=4)", "x": 120, "y": 310, "w": 205, "h": 45, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#1F3864;"},
        {"id": "s5", "val": "5. Xác thực Token<br>& Phân quyền RBAC", "x": 325, "y": 375, "w": 200, "h": 45, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#1F3864;"},
        {"id": "s6", "val": "6. Thực thi suy luận đa bước<br>(Rollout đệ quy / TiDE Sequence)", "x": 325, "y": 440, "w": 400, "h": 45, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#1F3864;"},
        {"id": "s7", "val": "7. Lưu kết quả phiên chạy<br>& chi tiết 4 tuần dự báo", "x": 725, "y": 505, "w": 200, "h": 45, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#1F3864;"},
        {"id": "s8", "val": "8. Trả về 200 JSON<br>(run_id & mảng dự báo)", "x": 120, "y": 570, "w": 205, "h": 45, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#D5E8D4;strokeColor=#4F8A3C;"}
    ],
    "edges": [
        # Lifelines: dashed drops
        {"id": "l1", "src": "g1", "tgt": "end1", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#8497B0;dashed=1;exitX=0.5;exitY=1;entryX=0.5;entryY=0;"},
        {"id": "l2", "src": "g2", "tgt": "end2", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#8497B0;dashed=1;exitX=0.5;exitY=1;entryX=0.5;entryY=0;"},
        # Lifeline 3 (Auth & RBAC): Split into 2 segments with gap over s6 to eliminate line running across s6 text
        {"id": "l3a", "src": "g3", "tgt": "s6", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#8497B0;dashed=1;exitX=0.5;exitY=1;entryX=0.5;entryY=0;"},
        {"id": "l3b", "src": "s6", "tgt": "end3", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#8497B0;dashed=1;exitX=0.5;exitY=1;entryX=0.5;entryY=0;"},
        {"id": "l4", "src": "g4", "tgt": "end4", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#8497B0;dashed=1;exitX=0.5;exitY=1;entryX=0.5;entryY=0;"},
        {"id": "l5", "src": "g5", "tgt": "end5", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#8497B0;dashed=1;exitX=0.5;exitY=1;entryX=0.5;entryY=0;"}
    ]
}

# ==============================================================================
# 16. SƠ ĐỒ THỰC THỂ - QUAN HỆ CƠ SỞ DỮ LIỆU SQLITE (Hình 3.17)
# ==============================================================================
DIAGRAMS_PART3["16_database_erd"] = {
    "page_w": 960, "page_h": 490,
    "vertices": [
        {"id": "t", "val": "Hình: Sơ đồ thực thể – quan hệ của cơ sở dữ liệu SQLite", "x": 0, "y": 5, "w": 960, "h": 30, "style": "text;html=1;align=center;verticalAlign=middle;fontStyle=1;fontSize=15;fontColor=#1F3864;", "is_title": True},
        # Left column
        {"id": "t1", "val": "forecast_runs (Phiên chạy dự báo)<br>─────────────────────────────<br>• PK forecast_run_id : VARCHAR(36)<br>• created_at_utc : DATETIME<br>• model_name : VARCHAR(64)<br>• model_version : VARCHAR(32)<br>• horizon : INTEGER<br>• num_skus : INTEGER<br>• triggered_by : VARCHAR(64)", "x": 30, "y": 50, "w": 380, "h": 200, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;"},
        {"id": "t4", "val": "schema_version (Quản lý phiên bản DB)<br>─────────────────────────────<br>• PK version : INTEGER<br>• applied_at_utc : DATETIME", "x": 30, "y": 280, "w": 380, "h": 85, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#1F3864;"},
        {"id": "t5", "val": "app_users & revoked_tokens (Bảo mật)<br>• Quản trị danh tính, băm mật khẩu & thu hồi JWT", "x": 30, "y": 395, "w": 380, "h": 65, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFF2CC;strokeColor=#D6B656;"},
        # Right column
        {"id": "t2", "val": "forecast_records (Bản ghi dự báo chi tiết)<br>─────────────────────────────<br>• PK id : INTEGER AUTOINCREMENT<br>• FK forecast_run_id : VARCHAR(36)<br>• sku_id : VARCHAR(32)<br>• forecast_date : DATE<br>• horizon_step : INTEGER (1..4)<br>• predicted_demand : DOUBLE<br>• lower_bound / upper_bound : DOUBLE", "x": 520, "y": 50, "w": 410, "h": 200, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#1F3864;"},
        {"id": "t3", "val": "export_artifacts (Lịch sử xuất tệp dữ liệu)<br>─────────────────────────────<br>• PK export_id : VARCHAR(36)<br>• FK forecast_run_id : VARCHAR(36)<br>• export_type : VARCHAR(16) (CSV, XLSX)<br>• file_path : TEXT<br>• row_count : INTEGER<br>• created_at_utc : DATETIME", "x": 520, "y": 280, "w": 410, "h": 180, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#1F3864;"}
    ],
    "edges": [
        # Edge 0: Straight horizontal t1 -> t2
        {"id": "e0", "src": "t1", "tgt": "t2", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=1;exitY=0.5;entryX=0;entryY=0.5;"},
        # Edge 1: t1 -> t3 via the empty central corridor X=465, completely avoiding t4 (schema_version)
        {"id": "e1", "src": "t1", "tgt": "t3", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=1;exitY=0.65;entryX=0;entryY=0.5;", "pts": [(410.0, 180.0), (465.0, 180.0), (465.0, 370.0), (520.0, 370.0)], "drawio_pts": [(465.0, 180.0), (465.0, 370.0)]}
    ]
}

# ==============================================================================
# 17. XÁC THỰC VÀ PHÂN QUYỀN RBAC (Hình 3.16)
# ==============================================================================
DIAGRAMS_PART3["17_auth_rbac"] = {
    "page_w": 1040, "page_h": 320,
    "vertices": [
        {"id": "t", "val": "Hình: Xác thực và phân quyền RBAC (Role-Based Access Control)", "x": 0, "y": 5, "w": 1040, "h": 30, "style": "text;html=1;align=center;verticalAlign=middle;fontStyle=1;fontSize=15;fontColor=#1F3864;", "is_title": True},
        # Row 1 (y=55, h=70)
        {"id": "a1", "val": "POST /auth/login<br>username + password", "x": 30, "y": 55, "w": 210, "h": 70, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;"},
        {"id": "a2", "val": "PBKDF2-HMAC-SHA256<br>600.000 vòng, salt 16 bytes", "x": 280, "y": 55, "w": 220, "h": 70, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#1F3864;"},
        {"id": "a3", "val": "Cấp phát JWT HS256<br>Payload: sub, role, jti, exp", "x": 540, "y": 55, "w": 200, "h": 70, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#1F3864;"},
        {"id": "a4", "val": "Mỗi Request gửi lên:<br>Xác thực chữ ký & Blacklist", "x": 780, "y": 55, "w": 230, "h": 70, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFF2CC;strokeColor=#D6B656;"},
        # Row 2 (y=180, h=65)
        {"id": "r1", "val": "Vai trò: VIEWER<br>• Quyền xem báo cáo & tra cứu", "x": 30, "y": 180, "w": 220, "h": 65, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#1F3864;"},
        {"id": "r2", "val": "Vai trò: ANALYST<br>• Quyền chạy dự báo & xuất file", "x": 280, "y": 180, "w": 220, "h": 65, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#1F3864;"},
        {"id": "r3", "val": "Vai trò: PLANNER<br>• Quyền mô phỏng bổ sung tồn kho", "x": 530, "y": 180, "w": 220, "h": 65, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#1F3864;"},
        {"id": "r4", "val": "Vai trò: ADMIN<br>• Toàn quyền quản trị & phân quyền", "x": 780, "y": 180, "w": 230, "h": 65, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#D5E8D4;strokeColor=#4F8A3C;"}
    ],
    "edges": [
        {"id": "e0", "src": "a1", "tgt": "a2", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=1;exitY=0.5;entryX=0;entryY=0.5;"},
        {"id": "e1", "src": "a2", "tgt": "a3", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=1;exitY=0.5;entryX=0;entryY=0.5;"},
        {"id": "e2", "src": "a3", "tgt": "a4", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=1;exitY=0.5;entryX=0;entryY=0.5;"},
        # 100% straight vertical drop into ADMIN (both centered at X=895.0)
        {"id": "e6", "src": "a4", "tgt": "r4", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=0.5;exitY=1;entryX=0.5;entryY=0;"},
        # Clean bus branches to PLANNER, ANALYST, VIEWER (bus at Y=152.5)
        {"id": "e5", "src": "a4", "tgt": "r3", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=0.5;exitY=1;entryX=0.5;entryY=0;", "pts": [(895.0, 152.5), (640.0, 152.5), (640.0, 180.0)], "drawio_pts": [(895.0, 152.5), (640.0, 152.5)]},
        {"id": "e4", "src": "a4", "tgt": "r2", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=0.5;exitY=1;entryX=0.5;entryY=0;", "pts": [(640.0, 152.5), (390.0, 152.5), (390.0, 180.0)], "drawio_pts": [(895.0, 152.5), (390.0, 152.5)]},
        {"id": "e3", "src": "a4", "tgt": "r1", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=0.5;exitY=1;entryX=0.5;entryY=0;", "pts": [(390.0, 152.5), (140.0, 152.5), (140.0, 180.0)], "drawio_pts": [(895.0, 152.5), (140.0, 152.5)]}
    ]
}

# ==============================================================================
# 18. MÔ HÌNH TRIỂN KHAI HẠ TẦNG ĐÁM MÂY (RENDER & VERCEL) (Hình 3.18)
# ==============================================================================
DIAGRAMS_PART3["18_deployment_architecture"] = {
    "page_w": 1040, "page_h": 280,
    "vertices": [
        {"id": "t", "val": "Hình: Mô hình triển khai hạ tầng Render và Vercel", "x": 0, "y": 5, "w": 1040, "h": 30, "style": "text;html=1;align=center;verticalAlign=middle;fontStyle=1;fontSize=15;fontColor=#1F3864;", "is_title": True},
        # Row 1 (y=55, h=80)
        {"id": "p1", "val": "Trình duyệt & Client<br>Người dùng truy cập ứng dụng<br>(HTTPS / TLS 1.3)", "x": 30, "y": 55, "w": 210, "h": 80, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;"},
        {"id": "p2", "val": "Frontend CDN (Vercel)<br>React 18 SPA tĩnh<br>Cấu hình qua vercel.json", "x": 280, "y": 55, "w": 220, "h": 80, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#1F3864;"},
        {"id": "p3", "val": "Backend Service (Render)<br>uvicorn src.api.main:app<br>Cấu hình qua render.yaml", "x": 540, "y": 55, "w": 230, "h": 80, "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#1F3864;"},
        {"id": "p4", "val": "Bộ nhớ & CSDL (Cloud)<br>• SQLite Database (Disk)<br>• Model Registry Artifacts", "x": 810, "y": 55, "w": 200, "h": 80, "style": "shape=cylinder3;boundedLbl=1;whiteSpace=wrap;html=1;fillColor=#E1D5E7;strokeColor=#7E5A9B;"},
        # Support CI/CD (y=180, h=65)
        {"id": "p6", "val": "GitHub CI/CD Repository<br>minhllk24/Machine_Learning_Backend<br>(Tự động kích hoạt Build & Deploy)", "x": 540, "y": 180, "w": 230, "h": 65, "style": "rounded=1;dashed=1;whiteSpace=wrap;html=1;fillColor=#F8FAFC;strokeColor=#8497B0;"}
    ],
    "edges": [
        {"id": "e0", "src": "p1", "tgt": "p2", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=1;exitY=0.5;entryX=0;entryY=0.5;"},
        {"id": "e1", "src": "p2", "tgt": "p3", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=1;exitY=0.5;entryX=0;entryY=0.5;"},
        {"id": "e2", "src": "p3", "tgt": "p4", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#1F3864;exitX=1;exitY=0.5;entryX=0;entryY=0.5;"},
        {"id": "e3", "src": "p6", "tgt": "p3", "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#8497B0;dashed=1;exitX=0.5;exitY=0;entryX=0.5;entryY=1;"}
    ]
}

print("Batch 3 compiled.")
