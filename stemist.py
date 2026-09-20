import streamlit as st

# =========================================================
# AIWISE - AI LITERACY PLATFORM FOR STUDENTS
# =========================================================

st.set_page_config(
    page_title="AIWISE - Nền Tảng Năng Lực AI",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================================================
# SESSION STATE INITIALIZATION
# =========================================================

if "page" not in st.session_state:
    st.session_state.page = "home"

if "language" not in st.session_state:
    st.session_state.language = "VI"

if "lesson" not in st.session_state:
    st.session_state.lesson = 1

if "completed_lessons" not in st.session_state:
    st.session_state.completed_lessons = []

if "quiz_score" not in st.session_state:
    st.session_state.quiz_score = -1

if "quiz_done" not in st.session_state:
    st.session_state.quiz_done = False

if "quiz_answers" not in st.session_state:
    st.session_state.quiz_answers = []

# =========================================================
# LANGUAGE HELPER
# =========================================================

def is_vi():
    return st.session_state.language == "VI"

def text(vi_text, en_text):
    return vi_text if is_vi() else en_text

def change_language():
    if st.session_state.lang_radio == "🇻🇳 VI":
        st.session_state.language = "VI"
    else:
        st.session_state.language = "EN"

# =========================================================
# NAVIGATION HELPER
# =========================================================

def go(page):
    st.session_state.page = page
    st.rerun()

def home_button():
    if st.button(
        text("← Quay lại trang chủ", "← Back to Home"),
        key="back_home",
        use_container_width=False
    ):
        go("home")

# =========================================================
# MODERN CSS STYLING
# =========================================================

st.markdown("""
<style>

/* Imports Google Fonts */
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 18px;
}

.stApp {
    background: linear-gradient(180deg, #F0F4FF 0%, #F9FAFF 100%);
}

.block-container {
    max-width: 1280px;
    padding-top: 1.5rem;
    padding-bottom: 5rem;
}

/* Custom Navigation Buttons Style */
div.stButton > button {
    border-radius: 14px !important;
    font-weight: 700 !important;
    font-size: 16px !important;
    transition: all 0.3s ease !important;
    border: 1px solid #E0E7FF !important;
    box-shadow: 0 2px 5px rgba(0,0,0,0.03) !important;
    width: 100%;
}

div.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 15px rgba(108, 99, 255, 0.25) !important;
    border-color: #6C63FF !important;
}

/* ================= HEADER ================= */

.header-box {
    background: linear-gradient(135deg, #FFFFFF 0%, #F5F3FF 100%);
    border: 2px solid #E0E7FF;
    border-radius: 24px;
    padding: 22px 30px;
    margin-bottom: 20px;
    box-shadow: 0 10px 25px rgba(108, 99, 255, 0.08);
}

.logo {
    font-size: 36px;
    font-weight: 900;
    color: #1E1B4B;
    letter-spacing: -0.5px;
}

.logo-purple {
    background: linear-gradient(90deg, #6C63FF, #FF6584);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.tagline {
    color: #64748B;
    font-size: 16px;
    font-weight: 600;
    margin-top: 4px;
}

/* ================= HERO ================= */

.hero {
    background: linear-gradient(135deg, #6C63FF 0%, #FF6584 100%);
    border-radius: 32px;
    padding: 60px 50px;
    margin: 20px 0 35px 0;
    color: white;
    box-shadow: 0 15px 35px rgba(108, 99, 255, 0.3);
}

.hero-small {
    background: rgba(255, 255, 255, 0.25);
    color: #FFFFFF;
    font-size: 15px;
    font-weight: 800;
    letter-spacing: 1.5px;
    padding: 6px 16px;
    border-radius: 20px;
    display: inline-block;
    margin-bottom: 18px;
    text-transform: uppercase;
}

.hero-title {
    color: #FFFFFF;
    font-size: 52px;
    font-weight: 900;
    line-height: 1.15;
    margin-bottom: 20px;
}

.hero-title span {
    color: #FFE600;
    text-shadow: 0 2px 10px rgba(0,0,0,0.15);
}

.hero-description {
    color: #F1F5F9;
    font-size: 20px;
    line-height: 1.7;
    max-width: 850px;
    font-weight: 500;
}

/* ================= SECTIONS & CARDS ================= */

.section-title {
    color: #1E1B4B;
    font-size: 32px;
    font-weight: 800;
    margin-top: 35px;
    margin-bottom: 10px;
}

.section-subtitle {
    color: #475569;
    font-size: 18px;
    line-height: 1.7;
    margin-bottom: 25px;
}

.card {
    background: white;
    border: 2px solid #EEF2FF;
    border-radius: 24px;
    padding: 28px;
    margin-bottom: 20px;
    min-height: 220px;
    box-shadow: 0 8px 20px rgba(0,0,0,0.04);
    transition: all 0.3s ease;
}

.card:hover {
    transform: translateY(-4px);
    border-color: #818CF8;
    box-shadow: 0 12px 28px rgba(99, 102, 241, 0.15);
}

.card-icon {
    font-size: 42px;
    margin-bottom: 12px;
}

.card-title {
    color: #1E1B4B;
    font-size: 22px;
    font-weight: 800;
    margin-bottom: 10px;
}

.card-text {
    color: #475569;
    font-size: 17px;
    line-height: 1.65;
}

/* ================= DETAIL HERO & INFO BOXES ================= */

.detail-hero {
    background: linear-gradient(135deg, #FFFFFF 0%, #EEF2FF 100%);
    border: 2px solid #C7D2FE;
    border-radius: 28px;
    padding: 40px;
    margin: 20px 0 30px 0;
    box-shadow: 0 10px 25px rgba(99, 102, 241, 0.1);
}

.detail-icon {
    font-size: 55px;
}

.detail-title {
    color: #1E1B4B;
    font-size: 38px;
    font-weight: 900;
    margin-top: 12px;
}

.detail-text {
    color: #475569;
    font-size: 19px;
    line-height: 1.7;
    margin-top: 8px;
}

.info-box {
    background: #EEF2FF;
    border-left: 6px solid #6366F1;
    border-radius: 18px;
    padding: 24px;
    color: #1E1B4B;
    font-size: 18px;
    line-height: 1.75;
    margin: 20px 0;
    box-shadow: 0 4px 12px rgba(99, 102, 241, 0.08);
}

.success-box {
    background: #ECFDF5;
    border-left: 6px solid #10B981;
    border-radius: 18px;
    padding: 24px;
    color: #064E3B;
    font-size: 18px;
    line-height: 1.75;
    margin: 20px 0;
    box-shadow: 0 4px 12px rgba(16, 185, 129, 0.08);
}

.warning-box {
    background: #FFFBEB;
    border-left: 6px solid #F59E0B;
    border-radius: 18px;
    padding: 24px;
    color: #78350F;
    font-size: 18px;
    line-height: 1.75;
    margin: 20px 0;
    box-shadow: 0 4px 12px rgba(245, 158, 11, 0.08);
}

.danger-box {
    background: #FEF2F2;
    border-left: 6px solid #EF4444;
    border-radius: 18px;
    padding: 24px;
    color: #7F1D1D;
    font-size: 18px;
    line-height: 1.75;
    margin: 20px 0;
    box-shadow: 0 4px 12px rgba(239, 68, 68, 0.08);
}

/* ================= ROADMAP & SCORE ================= */

.roadmap-card {
    background: white;
    border: 2px solid #F1F5F9;
    border-radius: 20px;
    padding: 22px 28px;
    margin-bottom: 16px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.03);
}

.roadmap-number {
    display: inline-block;
    background: linear-gradient(135deg, #6366F1, #8B5CF6);
    color: white;
    width: 42px;
    height: 42px;
    border-radius: 50%;
    text-align: center;
    line-height: 42px;
    font-weight: 800;
    font-size: 18px;
    margin-right: 14px;
    box-shadow: 0 4px 10px rgba(99, 102, 241, 0.3);
}

.score-box {
    background: linear-gradient(135deg, #6366F1 0%, #A855F7 100%);
    border-radius: 30px;
    padding: 45px;
    text-align: center;
    color: white;
    margin: 25px 0;
    box-shadow: 0 15px 30px rgba(99, 102, 241, 0.25);
}

.score-number {
    font-size: 72px;
    font-weight: 900;
    color: #FFE600;
    text-shadow: 0 4px 12px rgba(0,0,0,0.2);
}

.score-label {
    font-size: 20px;
    font-weight: 600;
    opacity: 0.9;
}

/* ================= SOURCES STYLING ================= */

.source-title {
    font-size: 26px;
    font-weight: 700;
    color: #1E293B;
    margin-bottom: 8px;
}

.source-intro {
    font-size: 15px;
    color: #475569;
    line-height: 1.6;
    margin-bottom: 28px;
}

.source-card {
    background: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 12px;
    padding: 24px;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
    transition: all 0.3s ease;
    text-decoration: none !important;
    color: inherit !important;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    height: 100%;
}

.source-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
    border-color: #3B82F6;
}

.source-container {
    margin-top: 50px;
    padding-top: 30px;
    border-top: 2px solid #E2E8F0;
}

.badge {
    display: inline-block;
    padding: 4px 12px;
    border-radius: 20px;
    font-size: 12px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-bottom: 14px;
}

.badge-unesco {
    background-color: #EFF6FF;
    color: #1D4ED8;
}

.badge-unicef {
    background-color: #F0FDFA;
    color: #0F766E;
}

.card-title {
    font-size: 18px;
    font-weight: 700;
    color: #0F172A;
    margin-bottom: 10px;
    line-height: 1.4;
}

.card-desc {
    font-size: 14px;
    color: #475569;
    line-height: 1.6;
    margin-bottom: 20px;
}

.card-link {
    font-size: 14px;
    font-weight: 600;
    color: #2563EB;
    display: flex;
    align-items: center;
    gap: 6px;
}

/* ================= FOOTER ================= */

.footer {
    text-align: center;
    color: #64748B;
    font-size: 15px;
    font-weight: 600;
    border-top: 2px solid #E2E8F0;
    margin-top: 40px;
    padding-top: 30px;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# DATA SOURCE
# =========================================================

lessons = [
    {
        "vi_title": "AI là gì?",
        "en_title": "What is AI?",
        "icon": "🧠",
        "vi_intro": "Hiểu AI trước khi học cách sử dụng AI.",
        "en_intro": "Understand AI before learning how to use it.",
        "vi_content": """AI – trí tuệ nhân tạo – là lĩnh vực phát triển các hệ thống có khả năng thực hiện những nhiệm vụ thường cần một số khả năng của con người, chẳng hạn như nhận dạng mẫu, xử lý ngôn ngữ, dự đoán hoặc hỗ trợ ra quyết định.

Điều quan trọng: AI không phải là một “bộ não biết tất cả”. Một hệ thống AI hoạt động dựa trên dữ liệu, mô hình và mục tiêu được thiết kế cho những nhiệm vụ cụ thể.""",
        "en_content": """Artificial intelligence is a field concerned with systems that can perform tasks that involve capabilities often associated with human intelligence, such as recognizing patterns, processing language, making predictions or supporting decisions.

Important: AI is not an all-knowing brain. AI systems depend on data, models and objectives designed for particular tasks."""
    },
    {
        "vi_title": "AI hoạt động như thế nào?",
        "en_title": "How does AI work?",
        "icon": "⚙️",
        "vi_intro": "Tìm hiểu cách dữ liệu và mô hình liên quan đến AI.",
        "en_intro": "Explore how data and models are involved in AI.",
        "vi_content": """Một cách đơn giản, có thể hình dung AI như một hệ thống học các mẫu từ dữ liệu để thực hiện một nhiệm vụ.

Ví dụ, một hệ thống nhận dạng hình ảnh có thể được huấn luyện với rất nhiều hình ảnh đã được gắn nhãn. Sau quá trình học, hệ thống có thể sử dụng những mẫu đã học để đưa ra dự đoán khi nhận một hình ảnh mới.

Với AI tạo sinh, mô hình có thể tạo văn bản, hình ảnh, âm thanh hoặc những dạng nội dung khác dựa trên những gì mô hình đã học được.""",
        "en_content": """In simple terms, AI can be viewed as a system that learns patterns from data to perform a task.

For example, an image recognition system may be trained using many labeled images. After learning, it can use those patterns to make predictions about a new image.

Generative AI can produce text, images, audio or other forms of content based on patterns learned by the model."""
    },
    {
        "vi_title": "AI có thể làm gì?",
        "en_title": "What can AI do?",
        "icon": "✨",
        "vi_intro": "Khám phá những ứng dụng quen thuộc của AI.",
        "en_intro": "Explore familiar applications of AI.",
        "vi_content": """AI có thể xuất hiện trong rất nhiều hoạt động:

• Đề xuất nội dung trên MXH & ứng dụng
• Nhận dạng hình ảnh và giọng nói
• Dịch ngôn ngữ tự động
• Phân tích dữ liệu và tìm kiếm thông tin
• Hỗ trợ viết, lập trình và học tập
• Tạo văn bản, hình ảnh, âm thanh

Tuy nhiên, “có thể làm” không đồng nghĩa với “luôn làm đúng”. Người dùng vẫn cần đánh giá kết quả.""",
        "en_content": """AI can be used for many activities:

• Content recommendation
• Image and speech recognition
• Language translation
• Data analysis and search
• Writing, coding and learning support
• Generating text, images and audio

However, being able to perform a task does not mean AI will always perform it correctly."""
    },
    {
        "vi_title": "AI có thể sai như thế nào?",
        "en_title": "How can AI be wrong?",
        "icon": "❗",
        "vi_intro": "Một trong những kỹ năng quan trọng nhất: không tin AI mù quáng.",
        "en_intro": "One of the most important skills: do not blindly trust AI.",
        "vi_content": """AI có thể đưa ra thông tin sai, thiếu ngữ cảnh hoặc không phù hợp với câu hỏi. Một câu trả lời nghe rất tự tin vẫn có thể sai (Hiện tượng AI ảo giác - Hallucination).

Vì vậy, khi tiếp nhận thông tin quan trọng, hãy:
1. Kiểm tra nguồn dẫn chứng.
2. Đối chiếu với các trang tin đáng tin cậy.
3. Kiểm tra ngày tháng và bối cảnh.
4. Tự suy nghĩ xem câu trả lời có hợp lý không.

Đây là lý do “kiểm chứng” là một kỹ năng cốt lõi khi sử dụng AI.""",
        "en_content": """AI can produce incorrect information, miss context or misunderstand a question. A confident answer can still be wrong (Hallucination).

For important information:
1. Check the sources;
2. Compare with reliable sources;
3. Check dates and context;
4. Think critically about whether the answer makes sense.

Verification is therefore a core AI literacy skill."""
    },
    {
        "vi_title": "Nhận biết nội dung AI",
        "en_title": "Recognizing AI-generated content",
        "icon": "🔍",
        "vi_intro": "Luyện quan sát thay vì cố tìm một “dấu hiệu tuyệt đối”.",
        "en_intro": "Practice observation instead of looking for one perfect sign.",
        "vi_content": """Không nên cho rằng chỉ cần nhìn một hình ảnh hoặc đọc một đoạn văn là có thể xác định chắc chắn nó do AI tạo ra.

Hãy kiểm tra:
• Nguồn xuất hiện đầu tiên
• Thời gian đăng tải gốc
• Ngữ cảnh xung quanh
• Báo chí hoặc các nguồn độc lập
• Dấu hiệu bất thường (bàn tay 6 ngón, chữ viết mờ, câu từ gượng gạo...)

Mục tiêu không phải là trở thành “máy phát hiện AI”, mà là trở thành người dùng biết kiểm chứng.""",
        "en_content": """You should not assume that a single visual or textual clue can prove whether something was generated by AI.

Check:
• The original source;
• Publication date;
• Context;
• Independent news sources;
• Unusual details (extra fingers, blurry text, unnatural tone);

The goal is not to become an “AI detector” but an informed verifier."""
    },
    {
        "vi_title": "AI để học tập",
        "en_title": "AI for learning",
        "icon": "🎓",
        "vi_intro": "Dùng AI để tăng khả năng học, không để AI học thay.",
        "en_intro": "Use AI to strengthen learning, not replace it.",
        "vi_content": """AI có thể đóng vai trò như một trợ lý học tập cá nhân.

Bạn có thể yêu cầu AI:
• Giải thích một khái niệm khó hiểu
• Đưa ra gợi ý giải bài
• Tạo câu hỏi luyện tập ôn thi
• Đóng vai người phỏng vấn / đối thoại
• Sửa lỗi ngôn ngữ & văn phong

Nhưng nếu AI làm toàn bộ bài tập và bạn chỉ sao chép, bạn đã bỏ qua phần quan trọng nhất: quá trình tư duy của chính mình.""",
        "en_content": """AI can act as a personal learning assistant.

You can ask AI to:
• Explain a difficult concept;
• Give hints for problems;
• Create practice test questions;
• Act as an interviewer or debate partner;
• Correct language and style errors.

But if AI completes everything and you simply copy it, you lose the most important part: your own thinking process."""
    },
    {
        "vi_title": "Kiểm chứng thông tin",
        "en_title": "Verify information",
        "icon": "🔎",
        "vi_intro": "Biết hỏi AI chưa đủ. Bạn cần biết kiểm tra câu trả lời.",
        "en_intro": "Knowing how to ask AI is not enough. You must verify answers.",
        "vi_content": """Một quy trình 5 bước đơn giản:

ASK → CHECK → COMPARE → THINK → USE

• ASK: Đặt câu hỏi rõ ràng.
• CHECK: Kiểm tra nguồn và bằng chứng.
• COMPARE: Đối chiếu với các nguồn độc lập.
• THINK: Tự đánh giá tính logic của câu trả lời.
• USE: Chỉ sử dụng khi bạn đã thực sự hiểu và thấy phù hợp.""",
        "en_content": """A simple 5-step process:

ASK → CHECK → COMPARE → THINK → USE

• ASK: Ask a clear question.
• CHECK: Check sources and evidence.
• COMPARE: Compare with independent sources.
• THINK: Evaluate whether the answer makes sense.
• USE: Use the information only after understanding and evaluating it."""
    },
    {
        "vi_title": "AI an toàn và có trách nhiệm",
        "en_title": "Safe and responsible AI",
        "icon": "🛡️",
        "vi_intro": "AI literacy cũng là biết bảo vệ bản thân và người khác.",
        "en_intro": "AI literacy also means protecting yourself and others.",
        "vi_content": """Một người dùng AI có trách nhiệm cần quan tâm đến:

🔐 Quyền riêng tư: Không chia sẻ thông tin cá nhân, tài khoản hay bí mật riêng tư.
⚖️ Công bằng: Nhận thức rằng AI có thể mang định kiến từ dữ liệu huấn luyện.
©️ Bản quyền: Tôn trọng quyền sở hữu trí tuệ của tác giả khác.
🧠 Trách nhiệm: Bạn chịu trách nhiệm cuối cùng cho sản phẩm bạn tạo ra từ AI.
🤝 Tự chủ: AI hỗ trợ con người, không thay thế suy nghĩ và quyết định của con người.""",
        "en_content": """A responsible AI user should care about:

🔐 Privacy: Do not share personal or sensitive data.
⚖️ Fairness: Recognize that AI systems can reproduce societal biases.
©️ Copyright: Respect intellectual property.
🧠 Responsibility: You remain responsible for how you use AI outputs.
🤝 Human Agency: AI should support human capabilities rather than remove human judgment."""
    }
]

quiz_questions = [
    {
        "category": "Understanding AI",
        "vi_question": "AI là gì?",
        "en_question": "What is AI?",
        "vi_options": [
            "Một bộ não kỹ thuật số biết mọi thứ.",
            "Một lĩnh vực phát triển các hệ thống có khả năng thực hiện một số nhiệm vụ đòi hỏi khả năng thông minh.",
            "Một công cụ luôn luôn đúng trong mọi trường hợp.",
            "Một phần mềm chỉ dùng để chỉnh sửa ảnh."
        ],
        "en_options": [
            "A digital brain that knows everything.",
            "A field developing systems that can perform tasks involving capabilities associated with intelligence.",
            "A tool that is always correct in all cases.",
            "A software used only for photo editing."
        ],
        "answer": 1
    },
    {
        "category": "Understanding AI",
        "vi_question": "Điều nào sau đây đúng về các câu trả lời do AI tạo ra?",
        "en_question": "Which statement about AI-generated answers is correct?",
        "vi_options": [
            "AI luôn đúng nếu câu trả lời nghe tự tin và mượt mà.",
            "AI không bao giờ mắc lỗi logic.",
            "AI có thể đưa ra thông tin sai lệch hoặc thiếu ngữ cảnh.",
            "AI luôn trích dẫn nguồn chính xác 100%."
        ],
        "en_options": [
            "AI is always correct if the answer sounds confident and fluent.",
            "AI never makes logical mistakes.",
            "AI can produce incorrect information or miss context.",
            "AI always provides 100% accurate citations."
        ],
        "answer": 2
    },
    {
        "category": "Verification",
        "vi_question": "AI đưa ra một số liệu thống kê rất ấn tượng nhưng không kèm nguồn. Bạn nên làm gì?",
        "en_question": "AI gives an impressive statistic without a source. What should you do?",
        "vi_options": [
            "Tin tưởng và sử dụng ngay vào bài phát biểu.",
            "Chia sẻ ngay lập tức lên mạng xã hội.",
            "Kiểm tra lại bằng các nguồn tin chính thống và đáng tin cậy.",
            "Loại bỏ toàn bộ bài viết của AI."
        ],
        "en_options": [
            "Trust it and use it immediately in your speech.",
            "Share it immediately on social media.",
            "Verify it using official and reliable sources.",
            "Discard the entire AI response."
        ],
        "answer": 2
    },
    {
        "category": "Verification",
        "vi_question": "Bạn thấy một video clip quay lại một sự kiện gây sốc trên mạng. Hành động nào đúng đắn nhất?",
        "en_question": "You see a video clip of a shocking event online. What is the most appropriate action?",
        "vi_options": [
            "Chia sẻ ngay để cảnh báo bạn bè.",
            "Kiểm tra nguồn đăng, thời gian, bối cảnh và báo chí chính thống trước khi tin.",
            "Tin ngay vì hình ảnh và video rất khó làm giả.",
            "Chỉ đọc các bình luận bên dưới để kết luận."
        ],
        "en_options": [
            "Share it immediately to warn friends.",
            "Check the source, publication date, context and official news before believing.",
            "Trust it immediately because photos and videos are hard to fake.",
            "Only read the comments below to draw a conclusion."
        ],
        "answer": 1
    },
    {
        "category": "AI for Learning",
        "vi_question": "Cách sử dụng AI nào dưới đây giúp cải thiện năng lực học tập thực sự?",
        "en_question": "Which use of AI below genuinely supports learning capability?",
        "vi_options": [
            "Yêu cầu AI viết toàn bộ bài văn và nộp trực tiếp.",
            "Sao chép đáp án bài tập toán từ AI.",
            "Nhờ AI giải thích lại một khái niệm khó theo nhiều cách dễ hiểu.",
            "Để AI quyết định mọi lựa chọn học tập thay cho bạn."
        ],
        "en_options": [
            "Ask AI to write your entire essay and submit it directly.",
            "Copy math solutions directly from AI.",
            "Ask AI to re-explain a difficult concept in simpler terms.",
            "Let AI make every learning choice for you."
        ],
        "answer": 2
    },
    {
        "category": "Safety",
        "vi_question": "Hành vi nào nên TRÁNH khi tương tác với các công cụ AI công cộng?",
        "en_question": "What behavior should be AVOIDED when using public AI tools?",
        "vi_options": [
            "Đặt câu hỏi rõ ràng và có cấu trúc.",
            "Thường xuyên kiểm chứng thông tin AI cung cấp.",
            "Tải lên thông tin cá nhân, mật khẩu hoặc dữ liệu nhạy cảm.",
            "So sánh kết quả từ nhiều công cụ khác nhau."
        ],
        "en_options": [
            "Asking clear and structured questions.",
            "Frequently verifying the information provided by AI.",
            "Uploading personal information, passwords, or sensitive data.",
            "Comparing outputs from different tools."
        ],
        "answer": 2
    },
    {
        "category": "Responsible AI",
        "vi_question": "Tại sao con người vẫn phải chịu trách nhiệm chính khi sử dụng kết quả từ AI?",
        "en_question": "Why do humans remain responsible when using AI outputs?",
        "vi_options": [
            "Vì AI không tự quyết định cách thông tin được áp dụng vào thực tế.",
            "Vì AI không có khả năng kết nối mạng.",
            "Vì AI chỉ tạo ra các văn bản ngẫu nhiên.",
            "Vì luật pháp cấm AI hoạt động độc lập."
        ],
        "en_options": [
            "Because AI does not decide how information is applied in reality.",
            "Because AI cannot connect to the internet.",
            "Because AI only creates random text.",
            "Because laws forbid AI from operating independently."
        ],
        "answer": 0
    },
    {
        "category": "Prompting",
        "vi_question": "Câu lệnh (Prompt) nào dưới đây sẽ mang lại kết quả tốt và hữu ích nhất?",
        "en_question": "Which prompt below will give the best and most useful response?",
        "vi_options": [
            "Hãy viết về AI.",
            "Giải thích AI cho tôi.",
            "Hãy giải thích khái niệm AI cho học sinh lớp 9 bằng 1 ví dụ thực tế, dài dưới 150 từ.",
            "AI là gì?"
        ],
        "en_options": [
            "Write about AI.",
            "Explain AI to me.",
            "Explain the concept of AI to a grade 9 student using 1 practical example, under 150 words.",
            "What is AI?"
        ],
        "answer": 2
    }
]

# =========================================================
# HEADER & NAVIGATION BAR
# =========================================================

left_col, right_col = st.columns([5, 2])

with left_col:
    st.markdown("""
    <div class="header-box">
        <div class="logo">
            🧠 <span class="logo-purple">AIWISE</span>
        </div>
        <div class="tagline">
            AI literacy for a smarter and safer future
        </div>
    </div>
    """, unsafe_allow_html=True)

with right_col:
    st.write("")
    st.radio(
        "Language",
        ["🇻🇳 VI", "🇺🇸 EN"],
        index=0 if st.session_state.language == "VI" else 1,
        horizontal=True,
        label_visibility="collapsed",
        key="lang_radio",
        on_change=change_language
    )

# MAIN NAVIGATION BUTTONS (Đã xóa AI Lab)
row1 = st.columns(5)
with row1[0]:
    if st.button(text("🏠 Trang chủ", "🏠 Home"), use_container_width=True):
        go("home")
with row1[1]:
    if st.button(text("🧠 Tìm hiểu", "🧠 Learn"), use_container_width=True):
        go("learn")
with row1[2]:
    if st.button(text("📚 Lộ trình", "📚 Roadmap"), use_container_width=True):
        go("learning")
with row1[3]:
    if st.button(text("🔍 Nhận biết", "🔍 Awareness"), use_container_width=True):
        go("awareness")
with row1[4]:
    if st.button(text("🛡️ An toàn", "🛡️ Safety"), use_container_width=True):
        go("safety")

row2 = st.columns(6)
with row2[0]:
    if st.button(text("🎓 Học tập", "🎓 Study"), use_container_width=True):
        go("study")
with row2[1]:
    if st.button(text("⚡ Lợi ích", "⚡ Benefits"), use_container_width=True):
        go("benefits")
with row2[2]:
    if st.button(text("⚠️ Rủi ro", "⚠️ Risks"), use_container_width=True):
        go("risks")
with row2[3]:
    if st.button(text("🎥 Video", "🎥 Videos"), use_container_width=True):
        go("videos")
with row2[4]:
    if st.button("🤖 ChatGPT", use_container_width=True):
        go("chatbot")
with row2[5]:
    if st.button(text("📚 Nguồn", "📚 Sources"), use_container_width=True):
        go("sources")

st.markdown("<hr style='border:1px solid #E0E7FF; margin:20px 0;'>", unsafe_allow_html=True)

# =========================================================
# PAGE 1: HOME
# =========================================================

def page_home():
    st.markdown(f"""
    <div class="hero">
        <div class="hero-small">
            ✨ AI LITERACY PLATFORM FOR STUDENTS
        </div>
        <div class="hero-title">
            Learn AI.<br>
            <span>Think Wise.</span>
        </div>
        <div class="hero-description">
            {text("AIWISE giúp học sinh hiểu sâu về AI, nhận ra giới hạn, kiểm chứng thông tin và sử dụng AI một cách thông minh, an toàn và trách nhiệm nhất.", "AIWISE helps students deeply understand AI, recognize limitations, verify information, and use AI smartly, safely, and responsibly.")}
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        f'<div class="section-title">{text("AI không chỉ là một công cụ đơn thuần.", "AI is more than just a tool.")}</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f'<div class="section-subtitle">{text("AI đang hiện diện khắp nơi trong học tập, mạng xã hội, hình ảnh và video. Kỹ năng quan trọng nhất không chỉ là biết dùng AI, mà là biết khi nào nên tin, khi nào cần kiểm chứng và khi nào tự suy nghĩ.", "AI is everywhere in study, social media, and images. The core skill is not just using AI, but knowing when to trust, verify, and think independently.")}</div>',
        unsafe_allow_html=True
    )

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown(f"""
        <div class="card">
            <div class="card-icon">🧠</div>
            <div class="card-title">{text("AI là gì?", "What is AI?")}</div>
            <div class="card-text">
                {text("Hiểu những khái niệm nền tảng cốt lõi trước khi bắt đầu sử dụng.", "Understand core foundational concepts before you start using AI.")}
            </div>
        </div>
        """, unsafe_allow_html=True)
        if st.button(text("Tìm hiểu ngay →", "Learn now →"), key="home_learn"):
            go("learn")

    with c2:
        st.markdown(f"""
        <div class="card">
            <div class="card-icon">⚡</div>
            <div class="card-title">{text("AI có ích gì?", "What can AI do?")}</div>
            <div class="card-text">
                {text("Khám phá tiềm năng mạnh mẽ giúp hỗ trợ việc học hiệu quả.", "Discover powerful potentials that enhance effective learning.")}
            </div>
        </div>
        """, unsafe_allow_html=True)
        if st.button(text("Xem lợi ích →", "Explore benefits →"), key="home_benefits"):
            go("benefits")

    with c3:
        st.markdown(f"""
        <div class="card">
            <div class="card-icon">⚠️</div>
            <div class="card-title">{text("AI có giới hạn gì?", "What are limits?")}</div>
            <div class="card-text">
                {text("Hiểu rủi ro để tránh phụ thuộc hoặc tin tưởng AI một cách mù quáng.", "Understand risks to avoid blind trust or over-dependence.")}
            </div>
        </div>
        """, unsafe_allow_html=True)
        if st.button(text("Xem rủi ro →", "Explore risks →"), key="home_risks"):
            go("risks")

    st.markdown(
        f'<div class="section-title">{text("Lộ trình AIWISE hoạt động thế nào?", "How AIWISE works")}</div>',
        unsafe_allow_html=True
    )

    flow = [
        ("01", "LEARN", text("Học kiến thức nền tảng quan trọng", "Learn core foundational knowledge")),
        ("02", "PRACTICE", text("Thử thách với các tình huống thực tế", "Practice real-world scenarios")),
        ("03", "VERIFY", text("Luyện kỹ năng kiểm chứng thông tin", "Master information verification skills")),
        ("04", "QUIZ", text("Kiểm tra và đánh giá mức độ hiểu biết", "Evaluate your AI literacy through quizzes")),
        ("05", "REFLECT", text("Nhìn lại điểm mạnh và điểm cần cải thiện", "Reflect on strengths and areas for growth")),
        ("06", "APPLY", text("Áp dụng thông minh vào học tập hàng ngày", "Apply smartly to daily learning tasks"))
    ]

    for number, title, description in flow:
        st.markdown(f"""
        <div class="roadmap-card">
            <span class="roadmap-number">{number}</span>
            <strong style="font-size:20px; color:#1E1B4B;">{title}</strong> - <span style="color:#475569; font-size:17px;">{description}</span>
        </div>
        """, unsafe_allow_html=True)

    st.markdown(
        f'<div class="section-title">🎥 {text("Video giới thiệu AI Literacy", "AI Literacy Overview Video")}</div>',
        unsafe_allow_html=True
    )
    st.video("https://www.youtube.com/watch?v=c0m6yaGlZh4")

# =========================================================
# PAGE 2: LEARN
# =========================================================

def page_learn():
    home_button()

    st.markdown(f"""
    <div class="detail-hero">
        <div class="detail-icon">🧠</div>
        <div class="detail-title">{text("Tìm Hiểu AI Nền Tảng", "Foundational AI Learning")}</div>
        <div class="detail-text">
            {text("Xây dựng tư duy đúng đắn và kiến thức chuẩn xác trước khi áp dụng AI.", "Build the right mindset and accurate knowledge before applying AI.")}
        </div>
    </div>
    """, unsafe_allow_html=True)

    cols = st.columns(2)
    for index, lesson in enumerate(lessons[:4]):
        with cols[index % 2]:
            st.markdown(f"""
            <div class="card">
                <div class="card-icon">{lesson["icon"]}</div>
                <div class="card-title">{text(lesson["vi_title"], lesson["en_title"])}</div>
                <div class="card-text">{text(lesson["vi_intro"], lesson["en_intro"])}</div>
            </div>
            """, unsafe_allow_html=True)

            if st.button(text("Đọc bài học này →", "Open lesson →"), key=f"learn_detail_{index}"):
                st.session_state.lesson = index + 1
                go("lesson")

# =========================================================
# PAGE 3: SINGLE LESSON
# =========================================================

def page_lesson():
    home_button()

    lesson_number = max(1, min(st.session_state.lesson, len(lessons)))
    lesson = lessons[lesson_number - 1]

    st.markdown(f"""
    <div class="detail-hero">
        <div class="detail-icon">{lesson["icon"]}</div>
        <div style="color:#6366F1; font-weight:800; font-size:18px;">
            {text(f"BÀI HỌC {lesson_number} / {len(lessons)}", f"LESSON {lesson_number} / {len(lessons)}")}
        </div>
        <div class="detail-title">{text(lesson["vi_title"], lesson["en_title"])}</div>
    </div>
    """, unsafe_allow_html=True)

    formatted_content = text(lesson["vi_content"], lesson["en_content"]).replace("\n", "<br>")

    st.markdown(f"""
    <div class="info-box">
        {formatted_content}
    </div>
    """, unsafe_allow_html=True)

    if lesson_number not in st.session_state.completed_lessons:
        if st.button(text("✓ Đánh dấu đã hoàn thành bài học", "✓ Mark as completed"), use_container_width=True):
            st.session_state.completed_lessons.append(lesson_number)
            st.rerun()
    else:
        st.success(text("🎉 Bạn đã hoàn thành bài học này!", "🎉 You have completed this lesson!"))

    st.markdown("<br>", unsafe_allow_html=True)
    previous_col, next_col = st.columns(2)

    with previous_col:
        if lesson_number > 1:
            if st.button(text("← Bài trước", "← Previous"), use_container_width=True):
                st.session_state.lesson = lesson_number - 1
                st.rerun()

    with next_col:
        if lesson_number < len(lessons):
            if st.button(text("Bài tiếp theo →", "Next lesson →"), use_container_width=True):
                st.session_state.lesson = lesson_number + 1
                st.rerun()
        else:
            if st.button(text("🎯 Thử sức làm Quiz ngay", "🎯 Take Quiz"), use_container_width=True):
                go("quiz")

# =========================================================
# PAGE 4: LEARNING ROADMAP
# =========================================================

def page_learning():
    home_button()

    st.title(text("📚 Lộ Trình Học Tập AI", "📚 Learning Journey"))
    st.write(text("Hoàn thành tất cả các bài học theo thứ tự để làm chủ kiến thức AI.", "Complete all lessons to master AI skills step by step."))

    completed = len(st.session_state.completed_lessons)
    total = len(lessons)
    st.progress(completed / total)
    st.write(f"**{text('Tiến độ hoàn thành', 'Progress')}: {completed}/{total} {text('bài học', 'lessons')}**")

    for i, lesson in enumerate(lessons):
        status = "✓" if i + 1 in st.session_state.completed_lessons else str(i + 1)
        st.markdown(f"""
        <div class="roadmap-card">
            <span class="roadmap-number">{status}</span>
            <strong style="font-size:20px; color:#1E1B4B;">{text(lesson["vi_title"], lesson["en_title"])}</strong>
            <p style="color:#475569; margin-top:8px; margin-bottom:0px;">{text(lesson["vi_intro"], lesson["en_intro"])}</p>
        </div>
        """, unsafe_allow_html=True)

        if st.button(text("Vào bài học", "Open Lesson"), key=f"road_{i}"):
            st.session_state.lesson = i + 1
            go("lesson")

# =========================================================
# PAGE 5: AWARENESS / SCENARIO
# =========================================================

def page_awareness():
    home_button()

    st.title(text("🔍 Nhận Biết Nội Dung AI", "🔍 AI Content Awareness"))

    st.markdown(f"""
    <div class="warning-box">
        <b>💡 {text("Quy tắc vàng", "Golden Rule")}:</b> {text("Không thể khẳng định 100% nội dung do AI hay con người tạo ra chỉ bằng mắt thường. Bạn luôn cần quy trình kiểm chứng độc lập.", "You cannot prove 100% whether content is AI-generated with the naked eye alone. Always use independent verification.")}
    </div>
    """, unsafe_allow_html=True)

    st.subheader(text("🔎 5 Câu hỏi cần đặt ra trước khi tin tưởng một thông tin:", "🔎 5 Questions to ask before trusting information:"))
    
    questions = [
        text("Ai là người đăng tải nội dung này?", "Who published this content?"),
        text("Nguồn gốc thông tin ban đầu xuất phát từ đâu?", "Where does the original source come from?"),
        text("Nội dung được đăng tải khi nào?", "When was this published?"),
        text("Có cơ quan báo chí hoặc nguồn độc lập nào xác nhận không?", "Is it confirmed by independent news sources?"),
        text("Có dấu hiệu hoặc chi tiết bất thường nào bất hợp lý không?", "Are there any abnormal or illogical details?")
    ]

    for i, q in enumerate(questions):
        st.checkbox(q, key=f"awareness_{i}")

    st.markdown("---")
    st.subheader(text("🎯 Tình huống thực tế", "🎯 Real-world Scenario"))
    st.write(text("Bạn thấy một bức ảnh người nổi tiếng hành động rất kỳ lạ trên mạng. Việc làm đầu tiên của bạn là gì?", "You see a photo of a celebrity acting weird online. What should you do first?"))

    options = [
        text("Chia sẻ ngay lập tức cho bạn bè cùng xem.", "Share it immediately with friends."),
        text("Tin ngay vì hình ảnh nhìn vô cùng chân thực.", "Trust it immediately because it looks realistic."),
        text("Tìm kiếm thông tin xác minh từ các báo lớn hoặc nguồn chính thống.", "Search for verification from trusted news sources."),
        text("Chỉ đọc các bình luận bên dưới để đoán.", "Only read comments below to guess.")
    ]
    ans = st.radio(
        text("Lựa chọn hành động của bạn:", "Select your action:"), options,
        index=None,
        key="awareness_radio"
    )
    if st.button(text("Kiểm tra đáp án", "Check Answer")):
        if ans is None:
            st.warning(text("⚠️ Vui lòng chọn một đáp án trước khi kiểm tra!", "⚠️ Please select an option first!"))
        elif ans == options[2]:
            st.success(text("🎉 Chính xác! Luôn luôn kiểm chứng nguồn trước khi tin hoặc chia sẻ.", "🎉 Correct! Always verify sources before believing or sharing."))
        else:
            st.warning(text("⚠️ Chưa chính xác. Hình ảnh dù chân thật đến đâu vẫn có thể do AI tạo ra. Hãy kiểm chứng trước!", "⚠️ Incorrect. Images can be AI-generated no matter how real they look. Always verify!"))

# =========================================================
# PAGE 6: QUIZ
# =========================================================

def page_quiz():
    home_button()

    st.title(text("📝 Trắc Nghiệm Đánh Giá Năng Lực AI", "📝 AI Literacy Quiz"))

    if not st.session_state.quiz_done:
        answers = []
        unanswered = False

        for i, q in enumerate(quiz_questions):
            st.markdown(f"### {i+1}. {text(q['vi_question'], q['en_question'])}")
            opts = q["vi_options"] if is_vi() else q["en_options"]
            
            selected = st.radio(
                text("Chọn câu trả lời:", "Select answer:"),
                opts,
                index=None,
                key=f"quiz_q_{i}"
            )
            
            if selected is None:
                unanswered = True
                answers.append(None)
            else:
                answers.append(opts.index(selected))

        if st.button(text("🎯 Nộp bài kiểm tra", "🎯 Submit Quiz"), use_container_width=True):
            if unanswered:
                st.error(text("⚠️ Vui lòng trả lời đầy đủ tất cả các câu hỏi trước khi nộp bài!", 
                            "⚠️ Please answer all questions before submitting!"))
            else:
                score = sum(1 for i, q in enumerate(quiz_questions) if answers[i] == q["answer"])
                st.session_state.quiz_score = score
                st.session_state.quiz_answers = answers
                st.session_state.quiz_done = True
                st.rerun()

    else:
        score = st.session_state.quiz_score
        pct = int(score / len(quiz_questions) * 100)

        st.markdown(f"""
        <div class="score-box">
            <div class="score-number">{pct}%</div>
            <div class="score-label">{text(f"Đạt {score} / {len(quiz_questions)} câu đúng", f"Scored {score} / {len(quiz_questions)} correct")}</div>
        </div>
        """, unsafe_allow_html=True)

        if pct >= 80:
            st.success(text("🎉 Tuyệt vời! Bạn có nền tảng năng lực AI rất vững chắc.", "🎉 Excellent! You have a very strong AI literacy foundation."))
        else:
            st.warning(text("💡 Bạn nên ôn lại các bài học để nâng cao kỹ năng nhé.", "💡 Consider reviewing the lessons to strengthen your skills."))

        if st.button(text("🔄 Làm lại bài trắc nghiệm", "🔄 Retake Quiz"), use_container_width=True):
            st.session_state.quiz_done = False
            st.session_state.quiz_score = -1
            st.session_state.quiz_answers = []
            st.rerun()

# =========================================================
# PAGE 7: BENEFITS
# =========================================================

def page_benefits():
    home_button()
    st.title(text("⚡ Lợi Ích Của Trí Tuệ Nhân Tạo", "⚡ Benefits of AI"))

    benefits = [
        ("📚", text("Học tập thông minh", "Smart Learning"), text("Giải thích khái niệm phức tạp, tạo đề luyện tập, chấm điểm và góp ý bài làm.", "Explains complex concepts, creates practice sets, and provides helpful feedback.")),
        ("💡", text("Khơi nguồn sáng tạo", "Boost Creativity"), text("Hỗ trợ lên ý tưởng, viết bản nháp và gợi ý các góc nhìn mới mẻ.", "Brainstorming ideas, drafting content, and suggesting fresh perspectives.")),
        ("🔎", text("Phân tích dữ liệu", "Data Analysis"), text("Tóm tắt tài liệu dài, trích xuất dữ liệu và xử lý thông tin nhanh chóng.", "Summarizes long documents and processes information quickly.")),
        ("🚀", text("Tăng cao năng suất", "Productivity Boost"), text("Tự động hóa các tác vụ lặp đi lặp lại để tiết kiệm thời gian quý báu.", "Automates repetitive tasks to save valuable time."))
    ]

    cols = st.columns(2)
    for i, b in enumerate(benefits):
        with cols[i % 2]:
            st.markdown(f"""
            <div class="card">
                <div class="card-icon">{b[0]}</div>
                <div class="card-title">{b[1]}</div>
                <div class="card-text">{b[2]}</div>
            </div>
            """, unsafe_allow_html=True)

# =========================================================
# PAGE 8: RISKS
# =========================================================

def page_risks():
    home_button()
    st.title(text("⚠️ Rủi Ro & Giới Hạn Của AI", "⚠️ AI Risks & Limitations"))

    st.markdown(f"""
    <div class="danger-box">
        <b>{text("Chờ đã!", "Wait!")}</b> {text("AI không phải lúc nào cũng đúng. Hãy cẩn trọng với các rủi ro bên dưới.", "AI is not always correct. Be mindful of the risks below.")}
    </div>
    """, unsafe_allow_html=True)

    risks = [
        ("🎭", text("Ảo giác thông tin (Hallucination)", "Hallucination"), text("AI có thể bịa đặt thông tin sai lệch nhưng trả lời với phong thái vô cùng tự tin.", "AI can generate incorrect or completely fabricated information confidently.")),
        ("🔐", text("Rò rỉ quyền riêng tư", "Privacy Risks"), text("Tránh nhập mật khẩu, thông tin cá nhân hay tài liệu bí mật vào AI.", "Avoid entering passwords, sensitive personal info, or private data into AI tools.")),
        ("🧠", text("Giảm khả năng tự tư duy", "Loss of Critical Thinking"), text("Phụ thuộc quá mức làm giảm tính sáng tạo và khả năng tự giải quyết vấn đề.", "Over-reliance reduces personal creativity and problem-solving skills."))
    ]

    for r in risks:
        st.markdown(f"""
        <div class="card">
            <div class="card-icon">{r[0]}</div>
            <div class="card-title">{r[1]}</div>
            <div class="card-text">{r[2]}</div>
        </div>
        """, unsafe_allow_html=True)

# =========================================================
# PAGE 10: STUDY
# =========================================================

def page_study():
    home_button()
    st.title(text("🎓 Ứng Dụng AI Trong Học Tập", "🎓 AI for Study"))

    c1, c2 = st.columns(2)
    with c1:
        st.markdown(f"""
        <div class="success-box">
            <b>✅ {text("NÊN DÙNG AI ĐỂ:", "DO USE AI TO:")}</b><br><br>
            • {text("Giải thích khái niệm khó hiểu", "Explain difficult concepts")}<br>
            • {text("Đặt câu hỏi luyện tập ôn thi", "Generate practice quiz questions")}<br>
            • {text("Sửa lỗi chính tả & văn phong", "Check grammar & writing style")}<br>
            • {text("Gợi ý ý tưởng bài viết", "Brainstorm essay ideas")}
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown(f"""
        <div class="danger-box">
            <b>❌ {text("KHÔNG NÊN:", "DO NOT USE AI TO:")}</b><br><br>
            • {text("Chép nguyên văn bài làm của AI", "Copy and paste AI answers verbatim")}<br>
            • {text("Nhờ AI giải toàn bộ bài tập về nhà", "Have AI do all your homework")}<br>
            • {text("Tin 100% không qua kiểm chứng", "Trust 100% without verification")}<br>
            • {text("Nộp bài AI viết như bài của mình", "Pass off AI work as your own")}
        </div>
        """, unsafe_allow_html=True)

# =========================================================
# PAGE 11: SAFETY
# =========================================================

def page_safety():
    home_button()
    st.title(text("🛡️ An Toàn & Trách Nhiệm Với AI", "🛡️ AI Safety & Responsibility"))

    st.markdown(f"""
    <div class="info-box">
        <b>{text("Bảo vệ bản thân trên không gian mạng:", "Protecting yourself online:")}</b><br><br>
        1. {text("Không đưa dữ liệu cá nhân hay hình ảnh riêng tư lên các nền tảng AI.", "Do not share personal data, credentials, or private photos with AI.")}<br>
        2. {text("Tôn trọng bản quyền tác giả và công khai khi có sử dụng AI hỗ trợ.", "Respect copyright and disclose AI usage when appropriate.")}<br>
        3. {text("Bạn là người chịu trách nhiệm cuối cùng cho sản phẩm bạn tạo ra cùng AI.", "You remain fully responsible for the output you create using AI.")}
    </div>
    """, unsafe_allow_html=True)

# =========================================================
# PAGE 12: VIDEOS
# =========================================================

def page_videos():
    home_button()
    st.title(text("🎥 Thư Viện Video Học Tập", "🎥 Video Library"))
    st.video("https://www.youtube.com/watch?v=c0m6yaGlZh4")

# =========================================================
# PAGE 13: CHATBOT
# =========================================================

def page_chatbot():
    home_button()
    st.title(text("🤖 Trải Nghiệm ChatGPT", "🤖 Try ChatGPT"))
    st.write(text("Hãy áp dụng kiến thức Prompting vừa học để thực hành nhé!", "Apply the Prompting skills you just learned!"))
    st.markdown(f"""
    <a href="https://chatgpt.com/" target="_blank">
        <button style="background:#6C63FF; color:white; border:none; padding:16px 32px; border-radius:16px; font-size:18px; font-weight:800; cursor:pointer;">
            🚀 {text("Trực tiếp truy cập ChatGPT", "Access ChatGPT Directly")}
        </button>
    </a>
    """, unsafe_allow_html=True)

# =========================================================
# PAGE 14: SOURCES PAGE
# =========================================================

def page_sources():
    home_button()
    st.title(text("📚 Nguồn & Tài Liệu Tham Khảo", "📚 Sources & References"))

# =========================================================
# GLOBAL FOOTER SOURCES COMPONENT
# =========================================================

def render_footer_sources():
    st.markdown('<div class="source-container"></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="source-title">{text("📚 Nguồn & Tài liệu Tham khảo", "📚 Sources & References")}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="source-intro">{text("Dưới đây là các khung năng lực và hướng dẫn chính thức từ các tổ chức quốc tế hàng đầu về Trí tuệ Nhân tạo (AI) áp dụng trong Giáo dục và Bảo vệ Trẻ em. Bạn có thể nhấn vào từng thẻ để xem tài liệu gốc.", "Below are official competency frameworks and guidance from leading international organizations on Artificial Intelligence (AI) applied in Education and Child Protection. Click on any card to access the original document.")}</div>', unsafe_allow_html=True)

    sources_data = [
        {
            "org": "UNESCO",
            "badge_class": "badge-unesco",
            "title": "AI Competency Framework for Students",
            "desc": text(
                "Khung năng lực AI dành cho học sinh do UNESCO phát hành, định hướng các kiến thức, kỹ năng và nhận thức đạo đức cốt lõi giúp thế hệ trẻ chủ động thích ứng và ứng dụng AI an toàn trong học tập.",
                "UNESCO's AI competency framework for students, outlining core knowledge, skills, and ethical awareness to help young generations adapt and safely apply AI in learning."
            ),
            "url": "https://www.unesco.org/en/articles/ai-competency-framework-students?utm_source=chatgpt.com"
        },
        {
            "org": "UNICEF",
            "badge_class": "badge-unicef",
            "title": "Policy Guidance on AI for Children",
            "desc": text(
                "Hướng dẫn chính sách về AI đối với trẻ em từ UNICEF, đề xuất các nguyên tắc bảo vệ quyền lợi, quyền riêng tư dữ liệu, sự an toàn và phát triển toàn diện của trẻ em trước các công nghệ AI.",
                "UNICEF's policy guidance on AI for children, proposing key principles to protect rights, data privacy, safety, and holistic development of children facing AI technologies."
            ),
            "url": "https://www.unicef.org/innocenti/reports/policy-guidance-ai-children?utm_source=chatgpt.com"
        }
    ]

    col1, col2 = st.columns(2)
    cols = [col1, col2]
    btn_text = text("Xem chi tiết tài liệu ↗", "View full document ↗")

    for idx, item in enumerate(sources_data):
        with cols[idx]:
            card_html = f"""
                <a href="{item['url']}" target="_blank" class="source-card">
                    <div>
                        <span class="badge {item['badge_class']}">{item['org']}</span>
                        <div class="card-title">{item['title']}</div>
                        <div class="card-desc">{item['desc']}</div>
                    </div>
                    <div class="card-link">{btn_text}</div>
                </a>
            """
            st.markdown(card_html, unsafe_allow_html=True)

# =========================================================
# ROUTER & RENDER ENGINE
# =========================================================

pages = {
    "home": page_home,
    "learn": page_learn,
    "lesson": page_lesson,
    "learning": page_learning,
    "quiz": page_quiz,
    "awareness": page_awareness,
    "study": page_study,
    "safety": page_safety,
    "benefits": page_benefits,
    "risks": page_risks,
    "videos": page_videos,
    "chatbot": page_chatbot,
    "sources": page_sources,
}

current_page = st.session_state.get("page", "home")
if current_page in pages:
    pages[current_page]()

# Hiển thị phần Nguồn ở cuối cùng của TẤT CẢ các trang
render_footer_sources()

# =========================================================
# FOOTER
# =========================================================

st.markdown("""
<div class="footer">
    <b>AIWISE</b> • AI Literacy Platform for Students<br>
    Learn AI • Think Critically • Verify Information • Use AI Responsibly
</div>
""", unsafe_allow_html=True)