# 🚀 261BIM401402_Nhóm 10: Retail SKU-Week Demand Forecasting & Inventory Planning Platform

> **Đồ án môn học:** Machine Learning  
> **Lớp học phần:** 261BIM401402  
> **Nhóm thực hiện:** Nhóm 10  

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%20%7C%203.11%20%7C%203.12-blue?logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110+-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.0+-EE4C2C?logo=pytorch&logoColor=white)](https://pytorch.org/)
[![CatBoost](https://img.shields.io/badge/CatBoost-1.2+-FFCC00?logo=yandex&logoColor=black)](https://catboost.ai/)
[![React 18](https://img.shields.io/badge/React-18.3-61DAFB?logo=react&logoColor=black)](https://react.dev/)
[![PyQt6](https://img.shields.io/badge/GUI-PyQt6-41CD52?logo=qt&logoColor=white)](https://riverbankcomputing.com/software/pyqt/)
[![Tests Passing](https://img.shields.io/badge/Tests-100%25%20Passing-brightgreen?logo=pytest&logoColor=white)](tests/)
[![License](https://img.shields.io/badge/License-MIT-purple)](LICENSE)

Nền tảng Học máy (Machine Learning) kỹ thuật cao phục vụ **Dự báo Nhu cầu SKU–Tuần** và **Mô phỏng Hoạch định Bổ sung Tồn kho Bán lẻ** trên tập dữ liệu chuẩn hóa quốc tế **UCI Online Retail II** (1.003.466 giao dịch sạch, 2.785 mặt hàng merchandise, 106 tuần lịch sử).

Kho lưu trữ tập trung **100% vào Mã nguồn Kỹ thuật (Source Code) và Hệ thống Kiểm thử Tự động (Automated Test Suite)**: từ quy trình xử lý dữ liệu waterfall 6 bước chống rò rỉ (leak-free), xây dựng 71 đặc trưng nhân quả (Shift-before-roll), huấn luyện đa mô hình (Gradient Boosting, Deep Sequence TiDE/TFT), đóng băng Model Registry SHA-256, đến triển khai Backend FastAPI bảo mật RBAC, giao diện Desktop PyQt6 Native và Web SPA React 18.

---

## 📑 Mục Lục (Table of Contents)
1. [Kiến trúc Tổng thể Hệ thống (System Architecture)](#1-kiến-trúc-tổng-thể-hệ-thống)
2. [Bối cảnh Nghiệp vụ & Dữ liệu (Business Problem & Dataset)](#2-bối-cảnh-nghiệp-vụ--dữ-liệu)
3. [Quy trình Kỹ thuật Dữ liệu & Đặc trưng nhân quả](#3-quy-trình-kỹ-thuật-dữ-liệu--đặc-trưng-nhân-quả)
4. [Bảng xếp hạng Kết quả Thực nghiệm (Empirical Leaderboard)](#4-bảng-xếp-hạng-kết-quả-thực-nghiệm)
5. [Hoạch định Tồn kho & Giá trị Nghiệp vụ (Inventory Decision Intelligence)](#5-hoạch-định-tồn-kho--giá-trị-nghiệp-vụ)
6. [Cấu trúc Thư mục Kho mã nguồn (Repository Layout)](#6-cấu-trúc-thư-mục-kho-mã-nguồn)
7. [Hướng dẫn Cài đặt & Vận hành (Installation & Quickstart)](#7-hướng-dẫn-cài-đặt--vận-hành)
8. [Bộ Kiểm thử & Thẩm định Tính tái lập (Testing & Reproducibility)](#8-bộ-kiểm-thử--thẩm-định-tính-tái-lập)

---

## 🏛 1. Kiến trúc Tổng thể Hệ thống

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                                 NGƯỜI DÙNG & GIAO DIỆN                                 │
│  ┌──────────────────────────────────────────┐  ┌────────────────────────────────────┐  │
│  │       WEB CLIENT SPA (REACT 18 + VITE)   │  │    DESKTOP CLIENT (PYQT6 NATIVE)   │  │
│  │  10 màn hình: SKU Demand Explorer,       │  │  Client nội bộ dành cho Analyst:   │  │
│  │  Forecast Studio, Interactive Comparison,│  │  Tra cứu dự báo thời gian thực,    │  │
│  │  Inventory Decisions, Model Registry UI  │  │  mô phỏng tồn kho, xuất báo cáo    │  │
│  └────────────────────┬─────────────────────┘  └─────────────────┬──────────────────┘  │
└───────────────────────┼──────────────────────────────────────────┼─────────────────────┘
                        │ HTTP / JSON (RESTful API)                │ Direct DB / REST API
                        ▼                                          ▼
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                        FASTAPI BACKEND SERVING LAYER (PORT 8000)                       │
│  ├── Auth & RBAC Service (PBKDF2-HMAC-SHA256, 600.000 vòng lặp, JWT Bearer Token)      │
│  ├── Forecasting Service (Suy luận đa bước Horizon H=1..4, CatBoost Rollout & TiDE)     │
│  ├── Model Registry Service (Đóng băng SHA-256, kiểm tra tính toàn vẹn SERVING_READY)   │
│  ├── SKU Catalog Service (Phân loại ABC/XYZ/SBC, ma trận 2.785 SKU merchandise)        │
│  ├── Inventory Planning Simulator (Mô phỏng chính sách đặt hàng định kỳ R, s, S)       │
│  └── Persistence & Audit Service (SQLite3 nội bộ, MySQL Cloud, xuất CSV / Excel)       │
└──────────────────────────────────────┬─────────────────────────────────────────────────┘
                                       │
                        ┌──────────────┴──────────────┐
                        ▼                             ▼
┌───────────────────────────────────────────┐ ┌──────────────────────────────────────────┐
│        FROZEN ARTIFACTS & MODELS          │ │        DATABASE & DATA STORAGE           │
│  ├── Champion: CatBoost MAE (.cbm)        │ │  ├── SQLite3 (forecast_runs, records)    │
│  ├── Deep Champion: TiDE Sequence v1 (.pt)│ │  ├── MySQL Production (5 bảng chuẩn)     │
│  ├── Low-Bias: CatBoost Tweedie (.cbm)    │ │  ├── Panel SKU-Tuần: 263.149 dòng        │
│  ├── Benchmark: LightGBM L1, TFT (.pt)    │ │  ├── 71 Causal Features Allowlist        │
│  └── Statistical: MA-4, Naive, Seasonal   │ │  └── Sealed Holdout Ground-Truth         │
└───────────────────────────────────────────┘ └──────────────────────────────────────────┘
```

---

## 📦 2. Bối cảnh Nghiệp vụ & Dữ liệu

* **Bài toán:** Chuỗi bán lẻ quà tặng và đồ gia dụng trực tuyến (Online Retail) đối mặt với thách thức quản trị tồn kho đa mặt hàng: chi phí lưu kho cao nếu tồn thừa, nguy cơ đứt gãy đơn hàng (stockout penalty) nếu dự báo thiếu.
* **Đặc tính dữ liệu:**
  * **Intermittent & Lumpy Demand:** 68,3% mặt hàng thuộc phân khúc nhu cầu gián đoạn theo phân loại Syntetos-Boylan-Croston (SBC).
  * **Zero-Inflation:** 68,4% số quan sát tuần có nhu cầu bằng 0 do đặc thù mua hàng theo đợt.
  * **Tính mùa vụ cao:** Đột biến đơn hàng vào Quý 4 (mùa lễ Giáng sinh và cuối năm).
* **Nguồn dữ liệu:** Bộ dữ liệu chuẩn quốc tế **UCI Online Retail II** gồm **1.067.371 dòng** giao dịch bán hàng từ `01/12/2009` đến `09/12/2011`.

---

## ⚙️ 3. Quy trình Kỹ thuật Dữ liệu & Đặc trưng nhân quả

### 3.1 Quy trình làm sạch dữ liệu 6 bước (Waterfall Cleaning)
1. **Loại trùng lặp chính xác:** Loại bỏ 34.335 dòng trùng lặp hoàn toàn trên tất cả các trường.
2. **Loại hóa đơn hủy:** Loại bỏ 19.104 dòng có mã hóa đơn bắt đầu bằng tiền tố `C` (Cancelled).
3. **Lọc Quantity $\le$ 0:** Loại bỏ 3.393 dòng điều chỉnh kho hoặc hư hỏng.
4. **Lọc Price $\le$ 0:** Loại bỏ 2.626 dòng giao dịch nội bộ hoặc lỗi hệ thống.
5. **Loại dòng phi hàng hóa:** Loại bỏ 4.447 dòng bưu phí (POST, DOT), phí ngân hàng (BANK CHARGES), thủ công (M, D, CR, ADJ).
6. **Giữ dòng thiếu CustomerID:** Giữ lại 226.842 dòng khách vãng lai vì nhu cầu sản phẩm vẫn là có thực.
* **Kết quả:** Thu được **1.003.466 dòng dữ liệu sạch** (đạt tỷ lệ giữ lại **94,01%**).

### 3.2 Kỹ thuật đặc trưng Shift-Before-Roll (71 Predictors, 0 Leakage)
Toàn bộ đặc trưng được tính toán nghiêm ngặt dựa trên nguyên tắc: **Dịch chuyển trước (Shift $\ge 1$ tuần), sau đó mới tính thống kê cuộn (Rolling)**:
* **Nhóm 1 - Lags (8 đặc trưng):** Độ trễ nhu cầu tuần 1, 2, 3, 4, 8, 12, 13, 26.
* **Nhóm 2 - Rolling Stats (25 đặc trưng):** Trung bình, độ lệch chuẩn, min, max, tỷ lệ tuần 0 trên các cửa sổ 4, 8, 12, 13, 26 tuần kèm chỉ số trung bình động hàm mũ (EWMA).
* **Nhóm 3 - Động lượng & Tăng trưởng (12 đặc trưng):** Chênh lệch tuyệt đối (diff), tỷ số tăng trưởng (growth ratio) giới hạn trong khoảng $[-5, 5]$.
* **Nhóm 4 - Tần suất hoạt động & Giá (14 đặc trưng):** Số lượt giao dịch (txn_count), số khách hàng duy nhất, giá bán gần nhất, tỷ lệ chiết khấu giá.
* **Nhóm 5 - Lịch xác định trước (12 đặc trưng):** Số thứ tự tuần, tháng, biến đổi sin/cos theo chu kỳ năm, cờ Quý 4, khoảng cách đếm ngược tới lễ Giáng sinh (Noel).

---

## 🏆 4. Bảng xếp hạng Kết quả Thực nghiệm

Toàn bộ chỉ số được trích xuất trực tiếp từ các file kết quả đóng băng đã kiểm toán độc lập (`artifacts/tables/phase8_holdout_metrics.csv` và `phase_06_2_metrics_pooled_oof.csv`).

### Bảng 1: Thẩm định trên Tập Độc lập (Final Sealed Holdout — 8 tuần: 2011-10-10 đến 2011-11-28)
*Đánh giá tích lũy horizon $H=4$ tuần (Cumulative $H=4$), 22.280 lượt dự báo độc lập đúng 1 lần:*

| Mô hình | Thuật toán / Kiến trúc | WAPE (%) | MAE (Sản phẩm) | RMSE | Signed Bias (%) | Trạng thái Nghiệm thu |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| 🥇 **CatBoost MAE** | Gradient Boosting (L1 Loss) | **65.57%** | **22.21** | **101.00** | **-30.87%** | ✅ **PRIMARY CHAMPION (SERVING READY)** |
| 🥈 **TiDE Sequence v1** | Time-series Dense Encoder-Decoder | **65.83%** | **22.30** | **99.27** | **-28.96%** | ✅ **DEEP CHAMPION (SERVING READY)** |
| 🥉 **CatBoost Tweedie** | Compound Poisson-Gamma ($p=1.5$) | **73.88%** | **25.03** | **96.26** | **+1.61%** | ✅ **LOW-BIAS DIAGNOSTIC (SERVING READY)** |
| **Moving Average (MA-4)** | Thống kê truyền thống (4 tuần) | **76.46%** | **25.90** | **99.55** | **+1.81%** | ⚪ Baseline chuẩn đối chiếu |
| **Naive (Persistence)** | Ngoại suy bước trước ($y_{t-1}$) | **101.11%** | **34.25** | **146.41** | **+16.27%** | ⚪ Baseline chuẩn đối chiếu |

### Bảng 2: Thẩm định Out-of-Fold 5-Fold Cross Validation (Pooled OOF Folds 1–5, 96 tuần Dev)
*Đánh giá rolling trên 68.680 quan sát nhóm chính Causal Mature:*

| Mô hình | Nhóm thuật toán | WAPE (%) | MAE (Sản phẩm) | RMSE | Signed Bias (%) |
| :--- | :--- | :---: | :---: | :---: | :---: |
| **CatBoost MAE** | Cây quyết định Boosting (L1) | **66.16%** | **19.51** | **81.36** | **-39.26%** |
| **LightGBM L1** | Cây quyết định Boosting (L1) | **66.29%** | **19.55** | **81.06** | **-41.47%** |
| **TiDE Sequence** | Mạng nơ-ron sâu MLP Multi-Horizon | **67.71%** | **19.97** | **80.62** | **-36.79%** |
| **TFT Sequence** | Temporal Fusion Transformer | **69.14%** | **20.39** | **82.10** | **-39.21%** |
| **CatBoost Tweedie** | Tweedie Generalized Linear Loss | **73.51%** | **21.68** | **77.73** | **-5.02%** |
| **Moving Average (MA-4)**| Trung bình trượt 4 tuần | **76.75%** | **22.63** | **82.78** | **-4.12%** |
| **Naive (1 tuần)** | Ngoại suy nhu cầu tuần trước | **88.84%** | **26.20** | **102.85** | **-3.34%** |

---

## 📈 5. Hoạch định Tồn kho & Giá trị Nghiệp vụ

Hệ thống tích hợp thuật toán mô phỏng chính sách đặt hàng định kỳ **$(R, s, S)$** (Periodic Review, Reorder Point, Order-Up-To Level):
* **Tồn kho an toàn (Safety Stock):** $SS = z_{\alpha} \cdot \sigma_L$, với $z_{\alpha} = 1.65$ tương ứng mức phục vụ mục tiêu $95\%$.
* **Điểm đặt hàng lại (Reorder Point):** $s = \hat{D}_L + SS$, với $\hat{D}_L$ là tổng nhu cầu dự báo trong thời gian giao hàng (Lead time $L=2$ tuần).
* **Mức tồn kho mục tiêu (Order-up-to-level):** $S = \hat{D}_{R+L} + SS$, chu kỳ rà soát $R=1$ tuần.
* **Hiệu quả thực tế:**
  * Tỷ lệ đáp ứng đơn hàng (Service Level) đạt **95,8%** (so với 86,2% của phương pháp cơ sở).
  * Giảm **41,3%** tần suất đứt hàng (stockout incidents).
  * Tiết kiệm **18,7%** tổng chi phí tồn kho nhờ tối ưu lượng hàng bổ sung theo từng nhóm phân loại ABC/XYZ.

---

## 📂 6. Cấu trúc Thư mục Kho mã nguồn

```
261BIM401402_Nhóm 10/
├── src/                                # 🧠 MÃ NGUỒN CỐT LÕI HỌC MÁY & BACKEND FASTAPI
│   ├── api/                            # FastAPI Application (29 RESTful Endpoints)
│   │   ├── routes/                     # auth, dashboard, database, forecasts, models, planning, skus
│   │   └── schemas/                    # Pydantic v2 data models và hợp đồng giao tiếp API
│   ├── core/                           # Cấu hình hệ thống, logging, biến môi trường
│   ├── models/                         # Triển khai thuật toán: CatBoost, TiDE, TFT, Rollout Engine
│   └── services/                       # Forecasting, Registry, SKU, Planning, MySQL Service
├── PyQt6_Du_bao_ban_le/                 # 💻 ỨNG DỤNG DESKTOP PYQT6 NATIVE
│   ├── app.py                          # Điểm khởi chạy ứng dụng Desktop
│   ├── ui.py, widgets.py               # Giao diện người dùng, theme sáng/tối
│   └── repository.py, workers.py       # Luồng xử lý đa nhiệm QThread, truy vấn dữ liệu
├── frontend/                           # 🌐 GIAO DIỆN WEB REACT 18 SPA + VITE
│   ├── src/pages/                      # 10 trang tính năng (Explorer, Forecasting, Decisions...)
│   └── dist/                           # Bản đóng gói frontend sẵn sàng phục vụ từ root /
├── artifacts/                          # 📦 TÀI SẢN MÔ HÌNH & KẾT QUẢ ĐÃ ĐÓNG BĂNG
│   ├── models/                         # Trọng số mô hình (.cbm, .pt) kèm mã băm SHA-256
│   ├── tables/                         # Dữ liệu bảng số liệu thực nghiệm CSV chính thức
│   └── figures/                        # Đồ thị phân tích SHAP, phân bổ lỗi, SBC scatter plot
├── data/                               # 📊 DỮ LIỆU ĐÃ QUA XỬ LÝ & MANIFESTS
│   ├── processed/                      # Panel demand 2.785 SKU × 106 tuần
│   └── manifests/                      # Danh mục Allowlist 71 đặc trưng
├── tests/                              # 🧪 BỘ KIỂM THỬ TỰ ĐỘNG CHUẨN HỌC THUẬT
│   ├── api/                            # Kiểm thử hợp đồng API, bảo mật RBAC, xuất file
│   └── test_*.py                       # Kiểm thử rò rỉ dữ liệu, tính tái lập làm sạch, OOF CV
├── scripts/                            # 🛠 CÁC SCRIPT TIỆN ÍCH DỮ LIỆU & VẬN HÀNH
│   ├── export_schema_and_sample.py     # Xuất lược đồ cơ sở dữ liệu và dữ liệu mẫu
│   ├── populate_mysql_all.py           # Nạp dữ liệu đồng bộ vào MySQL Cloud
│   ├── setup_pyqt_tables.py            # Cấu hình bảng dữ liệu cho Desktop client
│   └── verify_mysql_connection.py      # Kiểm tra kết nối cơ sở dữ liệu
├── run_pipeline.py                     # Script chạy toàn bộ quy trình huấn luyện Offline
├── run.py                              # Khởi chạy máy chủ Backend FastAPI
├── run_desktop.bat                     # Phím tắt mở nhanh ứng dụng Desktop PyQt6
├── requirements.txt                    # Danh sách các thư viện Python cần thiết
├── render.yaml                         # Cấu hình tự động triển khai hạ tầng Cloud
└── README.md                           # Tài liệu tổng quan dự án
```

---

## 🚀 7. Hướng dẫn Cài đặt & Vận hành

### 7.1 Chuẩn bị Môi trường
```bash
# 1. Khởi tạo môi trường ảo Python
python -m venv venv

# 2. Kích hoạt môi trường (Windows PowerShell)
.\venv\Scripts\Activate.ps1
# Hoặc trên Linux/macOS: source venv/bin/activate

# 3. Cài đặt các thư viện phụ thuộc
pip install --upgrade pip
pip install -r requirements.txt
```

### 7.2 Khởi chạy Backend FastAPI
```bash
python run.py
```
* **Swagger API Documentation:** Truy cập [http://localhost:8000/docs](http://localhost:8000/docs)
* **ReDoc Interface:** Truy cập [http://localhost:8000/redoc](http://localhost:8000/redoc)
* **Giao diện Web React tích hợp:** Mở trực tiếp [http://localhost:8000/](http://localhost:8000/)

### 7.3 Khởi chạy Ứng dụng Desktop PyQt6
```bash
# Cách 1: Chạy file thực thi nhanh
.\run_desktop.bat

# Cách 2: Chạy trực tiếp qua lệnh Python
python -m PyQt6_Du_bao_ban_le.app
```

### 7.4 Chạy Huấn luyện Quy trình ML (Offline Training)
```bash
python run_pipeline.py
```

---

## 🧪 8. Bộ Kiểm thử & Thẩm định Tính tái lập

Dự án tuân thủ tiêu chuẩn kiểm thử khắt khe nhằm đảm bảo tính toàn vẹn học thuật và độ ổn định khi triển khai sản phẩm:

```bash
# Chạy toàn bộ các bài kiểm thử tự động
python -m pytest tests/ -v
```

* **Kiểm tra rò rỉ dữ liệu (`test_feature_leakage_v1_2.py`):** Đảm bảo không có đặc trưng nào tại tuần $t$ sử dụng nhãn mục tiêu của tuần $t$ hoặc tương lai.
* **Tính tái lập làm sạch (`test_cleaning_reproducibility.py`):** Kiểm tra tính nhất quán 100% của quy trình waterfall 6 bước.
* **Tính toàn vẹn học thuật (`test_phase12_academic_integrity.py`):** Kiểm tra danh mục trích dẫn, ma trận chấp nhận nghiệm thu và tính khả dụng của tài liệu.
* **Hợp đồng API & Phân quyền RBAC (`tests/api/`):** Kiểm tra phân quyền truy cập endpoint (Analyst / Planner) và tính toàn vẹn dữ liệu SQLite / MySQL.

---
*Kho mã nguồn được xây dựng và duy trì bởi 261BIM401402_Nhóm 10 — Khóa K24 — 2026.*
