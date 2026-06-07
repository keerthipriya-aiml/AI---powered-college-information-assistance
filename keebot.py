import streamlit as st

# ------------------------------------------------
# PAGE SETTINGS
# ------------------------------------------------

st.set_page_config(
    page_title="Gojan AI Assistant",
    page_icon="🎓",
    layout="wide"
)

# ------------------------------------------------
# CUSTOM CSS
# ------------------------------------------------

st.markdown("""
<style>

.stApp{
    background-color:#0f172a;
    color:white;
}

/* TITLE */

.main-title{
    text-align:center;
    font-size:42px;
    font-weight:bold;
    color:white;
    margin-top:10px;
}

.sub-title{
    text-align:center;
    color:#cbd5e1;
    margin-bottom:30px;
}

/* SIDEBAR */

.sidebar-title{
    color:white;
    font-size:26px;
    font-weight:bold;
    margin-bottom:15px;
}

.chat-history{
    background:#1e293b;
    padding:10px;
    border-radius:12px;
    margin-bottom:8px;
    color:white;
    font-size:14px;
}

/* CHAT BUBBLES */

.user-message{
    background:#2563eb;
    color:white;
    padding:12px;
    border-radius:15px;
    margin-top:12px;
    margin-left:120px;
    text-align:right;
}

.bot-message{
    background:#1e293b;
    color:white;
    padding:12px;
    border-radius:15px;
    margin-top:12px;
    margin-right:120px;
}

/* INPUT */

[data-testid="stChatInput"]{
    position:fixed;
    bottom:20px;
}

</style>
""", unsafe_allow_html=True)

# ------------------------------------------------
# SESSION STATE
# ------------------------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ------------------------------------------------
# SIDEBAR
# ------------------------------------------------

with st.sidebar:

    st.markdown(
        '<div class="sidebar-title">🎓 GSBT AI Assistant</div>',
        unsafe_allow_html=True
    )

    st.write("### 💬 Recent Chats")

    for title in st.session_state.chat_history[::-1]:

        st.markdown(
            f'<div class="chat-history">{title}</div>',
            unsafe_allow_html=True
        )

    st.divider()

    st.write("### Quick Topics")

    st.write("• Courses")
    st.write("• Admissions")
    st.write("• Placements")
    st.write("• Hostel")
    st.write("• Transport")
    st.write("• AI & ML")

# ------------------------------------------------
# TITLE
# ------------------------------------------------

st.markdown(
    '<div class="main-title">Gojan School of Business and Technology</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-title">AI Powered College Information Assistant</div>',
    unsafe_allow_html=True
)

# ------------------------------------------------
# SHOW OLD MESSAGES
# ------------------------------------------------

for msg in st.session_state.messages:

    if msg["role"] == "user":

        st.markdown(
            f'<div class="user-message">👤 {msg["content"]}</div>',
            unsafe_allow_html=True
        )

    else:

        st.markdown(
            f'<div class="bot-message">🎓 {msg["content"]}</div>',
            unsafe_allow_html=True
        )

# ------------------------------------------------
# CHAT INPUT
# ------------------------------------------------

user_input = st.chat_input("Ask your question here...")

# ------------------------------------------------
# BOT RESPONSE
# ------------------------------------------------

if user_input:

    # SAVE USER MESSAGE

    st.session_state.messages.append(
        {"role":"user","content":user_input}
    )

    # SAVE CHAT HISTORY TITLE

    if len(st.session_state.chat_history) < 15:
        st.session_state.chat_history.append(user_input[:30])

    question = user_input.lower()

    # DEFAULT RESPONSE

    response = """
Welcome to Gojan School of Business and Technology.

Please ask about:
• Courses
• Placements
• Hostel
• Admissions
• AI & ML
"""

    # COURSES

    if "course" in question or "department" in question:

        response = """
AVAILABLE COURSES IN GSBT

UNDERGRADUATE COURSES

• BE-AERONAUTICAL ENGINEERING
• B.E-CSE (ARTIFICIAL INTELLIGENCE AND MACHINE LEARNING)
• B.E-COMPUTER SCIENCE AND ENGINEERING
• B.E-COMPUTER AND COMMUNICATION ENGINEERING
• B.E-CSE (CYBER SECURITY)
• BE-ELECTRONICS AND COMMUNICATION ENGINEERING
• B.E-MECHANICAL AND AUTOMATION ENGINEERING
• B.E-MEDICAL ELECTRONICS
• B.E-ROBOTICS AND AUTOMATION

B.TECH COURSES

• B.TECH-BIOTECHNOLOGY
• B.TECH-INFORMATION TECHNOLOGY
• B.TECH-ARTIFICIAL INTELLIGENCE AND DATA SCIENCE
• B.TECH-COMPUTER SCIENCE AND BUSINESS SYSTEMS
• B.TECH-PHARMACEUTICAL TECHNOLOGY

POST GRADUATE COURSE

• MBA - MASTER OF BUSINESS ADMINISTRATION

Tell me your interests and I will suggest a suitable course for you.
"""

    # AI ML

    elif "aiml" in question or "ai ml" in question:

        response = """
B.E-CSE Artificial Intelligence and Machine Learning focuses on:

• Machine Learning
• Deep Learning
• Python Programming
• AI Applications
• Neural Networks

Suitable for students interested in future AI technologies.
"""

    # AI DS

    elif "data science" in question or "ai ds" in question:

        response = """
B.TECH Artificial Intelligence and Data Science focuses on:

• Data Analytics
• Artificial Intelligence
• Big Data
• Machine Learning
"""

    # CYBER SECURITY

    elif "cyber" in question:

        response = """
B.E-CSE Cyber Security focuses on:

• Ethical Hacking
• Network Security
• Cyber Defence
• Digital Protection
"""

    # ROBOTICS

    elif "robotics" in question:

        response = """
B.E Robotics and Automation focuses on:

• Robotics
• Smart Machines
• Automation
• Embedded Systems
"""

    # MBA

    elif "mba" in question:

        response = """
MBA - Master of Business Administration focuses on:

• Marketing
• Finance
• Leadership
• Human Resources
• Business Management
"""

    # HOSTEL

    elif "hostel" in question:

        response = """
Separate hostel facilities are available for boys and girls with:

• Wi-Fi
• Security
• Food Facilities
• Study Environment
"""

    # PLACEMENTS

    elif "placement" in question:

        response = """
GSBT provides placement training, aptitude sessions, workshops and industry interaction programs.

Top recruiters include IT and core companies.
"""

    # TRANSPORT

    elif "transport" in question or "bus" in question:

        response = """
Transport facilities are available from multiple locations for students and staff members.
"""

    # NEGATIVE QUESTIONS

    elif "bad" in question or "worst" in question or "low review" in question:

        response = """
Every institution receives different opinions based on personal experiences.

GSBT continuously focuses on academic excellence, practical learning, student development and placement opportunities.
"""

    # SAVE BOT MESSAGE

    st.session_state.messages.append(
        {"role":"assistant","content":response}
    )

    st.rerun()