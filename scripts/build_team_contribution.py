import os
import shutil
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

def build_team_contribution():
    wb = openpyxl.Workbook()

    # Define Colors and Fonts exactly matching Sample_TEAM Contribution.xlsx
    font_title = Font(name='Times New Roman', size=20, bold=True, color='CC4125')
    fill_title = PatternFill(start_color='E6B8AF', end_color='E6B8AF', fill_type='solid')

    font_header = Font(name='Times New Roman', size=13, bold=True, color='980000')
    fill_header = PatternFill(start_color='F4CCCC', end_color='F4CCCC', fill_type='solid')

    font_bold = Font(name='Times New Roman', size=12.5, bold=True, color='000000')
    font_regular = Font(name='Times New Roman', size=12, bold=False, color='000000')

    align_title = Alignment(horizontal='center', vertical='center', wrap_text=True)
    align_header = Alignment(horizontal='center', vertical='center', wrap_text=True)
    align_center_top = Alignment(horizontal='center', vertical='top', wrap_text=True)
    align_left_top = Alignment(horizontal='left', vertical='top', wrap_text=True)

    thin_border_side = Side(style='thin', color='000000')
    border_all = Border(left=thin_border_side, right=thin_border_side, top=thin_border_side, bottom=thin_border_side)

    # ==============================================================================
    # SHEET 1: CONTRIBUTION EVALUATION (ENGLISH - EXACT TEMPLATE MATCH)
    # ==============================================================================
    ws1 = wb.active
    ws1.title = 'Contribution Evaluation'

    # Title Row 1
    ws1.merge_cells('A1:E1')
    cell_a1 = ws1['A1']
    cell_a1.value = 'Contribution Evaluation'
    cell_a1.font = font_title
    cell_a1.fill = fill_title
    cell_a1.alignment = align_title
    ws1.row_dimensions[1].height = 42.0

    for col in range(1, 6):
        ws1.cell(1, col).border = border_all
        ws1.cell(1, col).fill = fill_title

    # Header Row 2
    headers_en = ['Full Name', 'Student ID', 'Assigned task', 'Attitude', 'Contribution']
    ws1.row_dimensions[2].height = 28.0
    for c_idx, h in enumerate(headers_en, 1):
        c = ws1.cell(2, c_idx, h)
        c.font = font_header
        c.fill = fill_header
        c.alignment = align_header
        c.border = border_all

    # Data Rows EN
    data_en = [
        (
            'Nguyễn An Thái',
            'K244060805',
            'Led Machine Learning core & data pipeline; performed 6-step waterfall data cleaning (UCI Online Retail II); engineered 7 causal feature groups (71 features, Shift-before-roll, strict leakage prevention); trained & evaluated models (Baselines, CatBoost MAE, LightGBM, TiDE Sequence, TFT); designed Model Registry & SHA-256 model freeze; created all 18 system & ML architecture diagrams in Draw.io/SVG/PNG; wrote Chapter 3 and Chapter 4 in final report.',
            'Highly proactive, dedicated, and demonstrated strong technical leadership in Machine Learning architecture, data pipeline engineering, and comprehensive empirical verification.',
            0.23
        ),
        (
            'Lý Lê Minh',
            'K244060789',
            'Built FastAPI backend (29 endpoints, JWT authentication & RBAC Analyst/Planner); optimized SQLite & MySQL database schemas, connection pooling & transactions; configured CI/CD, Git Flow & GitHub repository operations; implemented 30+ automated unit tests; deployed cloud infrastructure (render.yaml, vercel.json); wrote Chapter 3 (Sections 3.10–3.12: Backend Architecture, Security, Database & Deployment).',
            'Hardworking, highly reliable, and collaborative; ensured backend stability, high API performance, and rigorous repository operations.',
            0.22
        ),
        (
            'Trương Thanh Phong',
            'K244060795',
            'Formulated business problem & methodology ideas (multi-item retail demand, ABC/XYZ/SBC segmentation, safety stock & reorder simulation); conducted literature review (CatBoost vs Deep Learning TiDE/TFT); formatted and standardized the entire report document (Word styles, captions, table of contents, academic formatting); wrote Chapter 1, Chapter 5, and Chapter 6 in report.',
            'Creative, meticulous, and responsible; contributed valuable business ideas and ensured exceptional quality in academic report formatting and presentation.',
            0.20
        ),
        (
            'Nguyễn Ngọc Khánh',
            'K244060780',
            'Developed frontend web application using React 18 SPA, Vite, and Tailwind CSS (10 pages including SKU Demand Explorer & Model Comparison); integrated REST APIs for real-time inference; designed data visualization dashboards (Recharts); supported process integration; contributed to Chapter 3 (Section 3.10.4: Frontend Architecture & UI/UX Integration) and slide presentation.',
            'Active, cooperative, and demonstrated strong initiative in frontend web development, dashboard visualization, and API integration.',
            0.18
        ),
        (
            'Võ Thị Thanh Vy',
            'K244060818',
            'Designed end-to-end retail business workflows, UX wireframes & system interaction diagrams; designed Desktop PyQt6 client interface for internal analytics; defined inventory replenishment simulation flow; conducted retail data survey; wrote Chapter 2 (Business Context & Retail Workflow Survey) and contributed to Chapter 3 (Section 3.10.5: Desktop PyQt6 Client & User Experience).',
            'Dedicated, supportive, and demonstrated great attention to detail in business process design, user journey mapping, and report contribution.',
            0.17
        ),
    ]

    row_heights_en = [115.0, 105.0, 105.0, 105.0, 105.0]

    for idx, (name, sid, task, att, contrib) in enumerate(data_en, 3):
        ws1.row_dimensions[idx].height = row_heights_en[idx-3]

        c1 = ws1.cell(idx, 1, name)
        c1.font = font_bold
        c1.alignment = align_center_top
        c1.border = border_all

        c2 = ws1.cell(idx, 2, sid)
        c2.font = font_bold
        c2.alignment = align_center_top
        c2.border = border_all

        c3 = ws1.cell(idx, 3, task)
        c3.font = font_regular
        c3.alignment = align_left_top
        c3.border = border_all

        c4 = ws1.cell(idx, 4, att)
        c4.font = font_regular
        c4.alignment = align_left_top
        c4.border = border_all

        c5 = ws1.cell(idx, 5, contrib)
        c5.font = font_bold
        c5.alignment = align_center_top
        c5.number_format = '0%'
        c5.border = border_all

    # Total Row
    ws1.row_dimensions[8].height = 28.0
    c_tot_lbl = ws1.cell(8, 1, 'Total')
    c_tot_lbl.font = font_bold
    c_tot_lbl.alignment = align_center_top
    c_tot_lbl.border = border_all

    for col in range(2, 5):
        c = ws1.cell(8, col, '')
        c.border = border_all

    c_tot_val = ws1.cell(8, 5, '=SUM(E3:E7)')
    c_tot_val.font = font_bold
    c_tot_val.alignment = align_center_top
    c_tot_val.number_format = '0%'
    c_tot_val.border = border_all

    # Set column widths EN
    ws1.column_dimensions['A'].width = 24.0
    ws1.column_dimensions['B'].width = 16.0
    ws1.column_dimensions['C'].width = 54.0
    ws1.column_dimensions['D'].width = 40.0
    ws1.column_dimensions['E'].width = 16.0

    # ==============================================================================
    # SHEET 2: PHÂN CÔNG CÔNG VIỆC (TIẾNG VIỆT)
    # ==============================================================================
    ws2 = wb.create_sheet(title='Đánh giá đóng góp (Tiếng Việt)')

    ws2.merge_cells('A1:E1')
    c2_a1 = ws2['A1']
    c2_a1.value = 'BẢNG PHÂN CHIA CÔNG VIỆC VÀ ĐÁNH GIÁ ĐÓNG GÓP THÀNH VIÊN'
    c2_a1.font = Font(name='Times New Roman', size=17, bold=True, color='CC4125')
    c2_a1.fill = fill_title
    c2_a1.alignment = align_title
    ws2.row_dimensions[1].height = 42.0

    for col in range(1, 6):
        ws2.cell(1, col).border = border_all
        ws2.cell(1, col).fill = fill_title

    headers_vi = ['Họ và Tên', 'MSSV', 'Nhiệm vụ được giao & Kết quả', 'Thái độ làm việc', 'Tỷ lệ đóng góp']
    ws2.row_dimensions[2].height = 28.0
    for c_idx, h in enumerate(headers_vi, 1):
        c = ws2.cell(2, c_idx, h)
        c.font = font_header
        c.fill = fill_header
        c.alignment = align_header
        c.border = border_all

    data_vi = [
        (
            'Nguyễn An Thái',
            'K244060805',
            'Chủ trì kiến trúc Machine Learning & đường ống dữ liệu; thực hiện làm sạch dữ liệu giao dịch 6 bước (UCI Online Retail II); xây dựng 7 nhóm đặc trưng nhân quả (71 features, Shift-before-roll, chống rò rỉ tuyệt đối); huấn luyện & đánh giá các mô hình (Baselines, CatBoost MAE, LightGBM, TiDE Sequence, TFT); thiết lập Model Registry & đóng băng mô hình SHA-256; thiết kế và hoàn thiện toàn bộ 18 sơ đồ kiến trúc Draw.io/SVG/PNG; phụ trách viết Chương 3 và Chương 4 trong Báo cáo tốt nghiệp.',
            'Chủ động, nhiệt tình, có tinh thần trách nhiệm rất cao; dẫn dắt xuất sắc mảng kiến trúc Machine Learning và thực nghiệm đánh giá mô hình.',
            0.23
        ),
        (
            'Lý Lê Minh',
            'K244060789',
            'Xây dựng Backend FastAPI (29 API endpoints, xác thực JWT & phân quyền RBAC Analyst/Planner); tối ưu hóa cơ sở dữ liệu SQLite & MySQL, connection pooling và transaction; thiết lập quy trình CI/CD, Git Flow và quản trị GitHub repository; phát triển hơn 30 unit tests tự động; đóng gói và vận hành triển khai đám mây Cloud Deployment (Render, Vercel); phụ trách viết Chương 3 (Mục 3.10–3.12 về Backend, Bảo mật, CSDL và Triển khai).',
            'Chăm chỉ, kỷ luật, có trách nhiệm cao, phối hợp đồng đội hiệu quả và đảm bảo hệ thống backend vận hành ổn định, an toàn.',
            0.22
        ),
        (
            'Trương Thanh Phong',
            'K244060795',
            'Xây dựng và phát triển ý tưởng bài toán kinh doanh (dự báo bán lẻ đa mặt hàng, phân loại ABC/XYZ/SBC, mô phỏng tồn kho an toàn & điểm đặt hàng lại); khảo sát tài liệu nghiên cứu khoa học (Literature Review CatBoost vs TiDE/TFT); định dạng, chuẩn hóa cấu trúc và biên tập toàn bộ Báo cáo đồ án (format Word chuẩn học thuật, mục lục tự động, bảng biểu, hình ảnh); phụ trách viết Chương 1, Chương 5 và Chương 6 trong Báo cáo tốt nghiệp.',
            'Sáng tạo, cẩn thận, có tinh thần trách nhiệm cao; đóng góp tích cực vào phát triển ý tưởng bài toán kinh doanh và kiểm soát chất lượng báo cáo.',
            0.20
        ),
        (
            'Nguyễn Ngọc Khánh',
            'K244060780',
            'Phát triển ứng dụng Web Frontend React 18 SPA bằng Vite và Tailwind CSS (10 trang giao diện gồm SKU Demand Explorer, So sánh mô hình tương tác); tích hợp REST API dự báo thời gian thực; xây dựng biểu đồ trực quan hóa dữ liệu (Recharts); hỗ trợ kết nối quy trình hệ thống; phụ trách viết Chương 3 (Mục 3.10.4 về Kiến trúc Frontend Web & Trực quan hóa UI/UX) và thiết kế slide thuyết trình.',
            'Nhiệt tình, sáng tạo, hợp tác tốt; hoàn thành xuất sắc các màn hình giao diện web tương tác và trực quan hóa dữ liệu người dùng.',
            0.18
        ),
        (
            'Võ Thị Thanh Vy',
            'K244060818',
            'Thiết kế toàn bộ quy trình nghiệp vụ bán lẻ, UX wireframes và luồng tương tác hệ thống; thiết kế giao diện máy trạm Desktop PyQt6 phục vụ phân tích nội bộ; xây dựng quy trình mô phỏng bổ sung tồn kho; khảo sát bài toán thực tế; phụ trách viết Chương 2 (Bối cảnh kinh doanh & Khảo sát quy trình nghiệp vụ) và Chương 3 (Mục 3.10.5 về Giao diện PyQt6 & Trải nghiệm người dùng).',
            'Tận tâm, chu đáo, có tinh thần đồng đội cao; đóng góp nổi bật trong việc thiết kế quy trình nghiệp vụ và xây dựng giao diện ứng dụng.',
            0.17
        ),
    ]

    row_heights_vi = [115.0, 105.0, 105.0, 105.0, 105.0]

    for idx, (name, sid, task, att, contrib) in enumerate(data_vi, 3):
        ws2.row_dimensions[idx].height = row_heights_vi[idx-3]

        c1 = ws2.cell(idx, 1, name)
        c1.font = font_bold
        c1.alignment = align_center_top
        c1.border = border_all

        c2 = ws2.cell(idx, 2, sid)
        c2.font = font_bold
        c2.alignment = align_center_top
        c2.border = border_all

        c3 = ws2.cell(idx, 3, task)
        c3.font = font_regular
        c3.alignment = align_left_top
        c3.border = border_all

        c4 = ws2.cell(idx, 4, att)
        c4.font = font_regular
        c4.alignment = align_left_top
        c4.border = border_all

        c5 = ws2.cell(idx, 5, contrib)
        c5.font = font_bold
        c5.alignment = align_center_top
        c5.number_format = '0%'
        c5.border = border_all

    # Total Row VI
    ws2.row_dimensions[8].height = 28.0
    c2_tot_lbl = ws2.cell(8, 1, 'Tổng cộng')
    c2_tot_lbl.font = font_bold
    c2_tot_lbl.alignment = align_center_top
    c2_tot_lbl.border = border_all

    for col in range(2, 5):
        c = ws2.cell(8, col, '')
        c.border = border_all

    c2_tot_val = ws2.cell(8, 5, '=SUM(E3:E7)')
    c2_tot_val.font = font_bold
    c2_tot_val.alignment = align_center_top
    c2_tot_val.number_format = '0%'
    c2_tot_val.border = border_all

    ws2.column_dimensions['A'].width = 24.0
    ws2.column_dimensions['B'].width = 16.0
    ws2.column_dimensions['C'].width = 54.0
    ws2.column_dimensions['D'].width = 40.0
    ws2.column_dimensions['E'].width = 16.0

    # ==============================================================================
    # SHEET 3: CHI TIẾT PHÂN CÔNG THEO CHƯƠNG BÁO CÁO (CHƯƠNG 1 - 6)
    # ==============================================================================
    ws3 = wb.create_sheet(title='Chi tiết theo Chương Báo cáo')

    ws3.merge_cells('A1:F1')
    c3_a1 = ws3['A1']
    c3_a1.value = 'BẢNG PHÂN BỔ NHIỆM VỤ CHI TIẾT THEO CÁC CHƯƠNG BÁO CÁO ĐỒ ÁN V5'
    c3_a1.font = Font(name='Times New Roman', size=16, bold=True, color='CC4125')
    c3_a1.fill = fill_title
    c3_a1.alignment = align_title
    ws3.row_dimensions[1].height = 42.0

    for col in range(1, 7):
        ws3.cell(1, col).border = border_all
        ws3.cell(1, col).fill = fill_title

    headers_ch = ['Chương / Phần', 'Nội dung chính trong Báo cáo V5', 'Người chủ trì', 'Người phối hợp', 'Sản phẩm bàn giao', 'Tiến độ']
    ws3.row_dimensions[2].height = 28.0
    for c_idx, h in enumerate(headers_ch, 1):
        c = ws3.cell(2, c_idx, h)
        c.font = font_header
        c.fill = fill_header
        c.alignment = align_header
        c.border = border_all

    chapters_data = [
        (
            'Chương 1: Tổng quan đề tài & Bài toán kinh doanh',
            'Bối cảnh bán lẻ đa kênh, tầm quan trọng dự báo SKU–tuần, lý do chọn đề tài, mục tiêu nghiên cứu, phạm vi dữ liệu và cấu trúc báo cáo.',
            'Trương Thanh Phong',
            'Nguyễn An Thái',
            'Bản thảo Chương 1, ma trận mục tiêu nghiên cứu, cơ sở lý luận đề tài',
            '100%'
        ),
        (
            'Chương 2: Khảo sát thực trạng & Thiết kế quy trình',
            'Khảo sát tập dữ liệu UCI Online Retail II, phân tích hành vi đơn hàng, thiết kế quy trình nghiệp vụ bán lẻ và luồng vận hành người dùng.',
            'Võ Thị Thanh Vy',
            'Nguyễn Ngọc Khánh',
            'Bản thảo Chương 2, sơ đồ luồng quy trình nghiệp vụ, tài liệu khảo sát',
            '100%'
        ),
        (
            'Chương 3: Phương pháp luận & Kiến trúc Machine Learning',
            'Pipeline làm sạch waterfall 6 bước, panel hóa SKU–tuần, 71 causal features (Shift-before-roll), phân chia 5-fold OOF + Holdout, Model Freeze & SHA-256 manifest, 18 sơ đồ kiến trúc Draw.io.',
            'Nguyễn An Thái',
            'Lý Lê Minh,\nNguyễn Ngọc Khánh,\nVõ Thị Thanh Vy',
            'Bản thảo Chương 3 (Mục 3.1–3.9), 18 sơ đồ Draw.io/SVG/PNG, pipeline code src/',
            '100%'
        ),
        (
            'Chương 3 (Tiếp theo): Kiến trúc Backend, Frontend & Triển khai',
            'FastAPI backend (29 endpoints, RBAC JWT), CSDL SQLite & MySQL, Frontend React 18 SPA, Desktop PyQt6, hạ tầng CI/CD và triển khai Render/Vercel.',
            'Lý Lê Minh (Backend)\nNguyễn Ngọc Khánh (Web)\nVõ Thị Thanh Vy (App)',
            'Nguyễn An Thái',
            'Bản thảo Chương 3 (Mục 3.10–3.12), mã nguồn FastAPI, React 18, PyQt6, tests',
            '100%'
        ),
        (
            'Chương 4: Kết quả thực nghiệm & Đánh giá mô hình',
            'Đánh giá hiệu năng 5-fold OOF & Holdout niêm phong (MAE, RMSE, WAPE, Pinball), giải thích SHAP, phân rã ABC/XYZ/SBC, phân tích 15 ca lỗi lớn nhất, so sánh CatBoost với TiDE/TFT.',
            'Nguyễn An Thái',
            'Trương Thanh Phong',
            'Bản thảo Chương 4, bảng metric đối chiếu, 11 biểu đồ trực quan hóa kết quả',
            '100%'
        ),
        (
            'Chương 5: Ứng dụng thực tiễn & Mô phỏng tồn kho',
            'Mô phỏng chính sách bổ sung tồn kho an toàn (Safety Stock, Reorder Point), đánh giá lợi ích kinh tế, tối ưu hóa vốn lưu động và cảnh báo rủi ro.',
            'Trương Thanh Phong',
            'Võ Thị Thanh Vy',
            'Bản thảo Chương 5, công thức mô phỏng tồn kho, bảng ước lượng tài chính',
            '100%'
        ),
        (
            'Chương 6: Kết luận & Hướng phát triển',
            'Tổng kết các đóng góp chính của đề tài, các giới hạn vận hành (lead time cố định, SKU mới phát sinh muộn), bài học kinh nghiệm và hướng nghiên cứu mở rộng.',
            'Trương Thanh Phong',
            'Nguyễn An Thái',
            'Bản thảo Chương 6, tổng kết đánh giá phản biện, phụ lục tài liệu',
            '100%'
        ),
    ]

    row_heights_ch = [55.0, 55.0, 75.0, 75.0, 75.0, 55.0, 55.0]

    for idx, (ch, desc, lead, supp, deliv, prog) in enumerate(chapters_data, 3):
        ws3.row_dimensions[idx].height = row_heights_ch[idx-3]

        c1 = ws3.cell(idx, 1, ch)
        c1.font = font_bold
        c1.alignment = align_left_top
        c1.border = border_all

        c2 = ws3.cell(idx, 2, desc)
        c2.font = font_regular
        c2.alignment = align_left_top
        c2.border = border_all

        c3 = ws3.cell(idx, 3, lead)
        c3.font = font_bold
        c3.alignment = align_center_top
        c3.border = border_all

        c4 = ws3.cell(idx, 4, supp)
        c4.font = font_regular
        c4.alignment = align_center_top
        c4.border = border_all

        c5 = ws3.cell(idx, 5, deliv)
        c5.font = font_regular
        c5.alignment = align_left_top
        c5.border = border_all

        c6 = ws3.cell(idx, 6, prog)
        c6.font = font_bold
        c6.alignment = align_center_top
        c6.border = border_all

    ws3.column_dimensions['A'].width = 28.0
    ws3.column_dimensions['B'].width = 44.0
    ws3.column_dimensions['C'].width = 22.0
    ws3.column_dimensions['D'].width = 22.0
    ws3.column_dimensions['E'].width = 36.0
    ws3.column_dimensions['F'].width = 14.0

    # Save to all target locations
    target_paths = [
        r'c:\Users\thain\Downloads\ML Đồ Án\TEAM_Contribution_Evaluation.xlsx',
        r'c:\Users\thain\Downloads\TEAM_Contribution_Evaluation.xlsx',
        r'c:\Users\thain\Downloads\ML Đồ Án\FINAL_ML_PROJECT_REPORT_V5\01_FINAL_REPORT\TEAM_Contribution_Evaluation.xlsx',
        r'c:\Users\thain\Downloads\ML Đồ Án\FINAL_ML_PROJECT_REPORT_V2\FINAL_ML_PROJECT_REPORT_V2\TEAM_Contribution_Evaluation.xlsx'
    ]

    for path in target_paths:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        wb.save(path)
        print(f'Successfully saved: {path}')

if __name__ == '__main__':
    build_team_contribution()
