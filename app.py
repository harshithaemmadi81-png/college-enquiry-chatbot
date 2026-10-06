import streamlit as st

# =========================================================
# PAGE CONFIGURATION
# =========================================================
st.set_page_config(
    page_title="MRECW College Enquiry Chatbot",
    page_icon="🎓",
    layout="centered"
)

# =========================================================
# CUSTOM DESIGN
# =========================================================
st.markdown("""
<style>

.stApp {
    background-color: #F2F2F2;
}

h1 {
    color: #800000 !important;
    text-align: center;
    font-weight: 800;
}

h2, h3 {
    color: #800000 !important;
}

.stApp p, .stApp li {
    color: #333333;
}

label {
    color: #800000 !important;
    font-weight: 700 !important;
}

div[data-baseweb="input"] {
    background-color: #FFD6E0 !important;
    border: 2px solid #E8A9B8 !important;
    border-radius: 12px !important;
}

div[data-baseweb="input"] input {
    background-color: #FFD6E0 !important;
    color: #5C2633 !important;
    font-weight: 500 !important;
}

.answer-box {
    background-color: #E8DFFF;
    border: 2px solid #CDB8F0;
    border-radius: 15px;
    padding: 18px;
    margin-top: 12px;
    margin-bottom: 15px;
    color: #333333;
}

div[data-testid="stAlert"] {
    border-radius: 12px !important;
}

.stButton > button {
    background-color: #E8DFFF;
    color: #5A3478;
    border-radius: 10px;
    border: 1px solid #CDB8F0;
}

.stButton > button:hover {
    background-color: #DCCBFA;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# TITLE
# =========================================================
st.title("🎓 MRECW College Enquiry Chatbot")
st.write("Welcome! Ask me anything about the college.")


# =========================================================
# COLLEGE INFORMATION
# =========================================================
college_name = "Malla Reddy Engineering College for Women (MRECW)"
location = "Maisammaguda, Hyderabad, Telangana"


# =========================================================
# COURSES
# =========================================================
courses = [
    "B.Tech Artificial Intelligence and Machine Learning (AIML)",
    "B.Tech Computer Science and Engineering (CSE)",
    "B.Tech Information Technology (IT)",
    "B.Tech Computer Science and Data Science (CSD)",
    "B.Tech Electrical and Electronics Engineering (EEE)",
    "B.Tech Electronics and Communication Engineering (ECE)"
]


# =========================================================
# DEPARTMENTS
# =========================================================
departments = [
    "AIML - Artificial Intelligence and Machine Learning",
    "CSE - Computer Science and Engineering",
    "IT - Information Technology",
    "CSD - Computer Science and Data Science",
    "EEE - Electrical and Electronics Engineering",
    "ECE - Electronics and Communication Engineering"
]


# =========================================================
# BLOCKS
# =========================================================
blocks = [
    "AIML Block",
    "CSE Block",
    "IT Block",
    "CSD Block",
    "EEE Block",
    "ECE Block"
]


# =========================================================
# HOSTELS
# =========================================================
hostels = [
    "Hostel 1",
    "Hostel 2",
    "Apartment Hostel"
]


# =========================================================
# QUESTIONS
# =========================================================
st.subheader("💬 Please ask about:")

st.write("""
• College Name
• Location
• Courses
• Departments
• Blocks
• Admissions
• EAMCET / TG EAPCET
• ECET
• Management Admission
• Examinations
• Library
• Hostel
• Placements
• Companies
• Packages
• Canteen
• Einstein Block
• Labs
• Sports
• Transport / Local Buses
""")


# =========================================================
# USER QUESTION
# =========================================================
question = st.text_input(
    "Ask your question:",
    placeholder="Type your question here..."
)


# =========================================================
# ANSWERS
# =========================================================
if question:

    q = question.lower().strip()

    # -----------------------------------------------------
    # COLLEGE NAME
    # -----------------------------------------------------
    if "college name" in q or "name of college" in q:

        st.subheader("🏫 College Information")

        st.markdown(f"""
        <div class="answer-box">

        <b>College Name:</b> {college_name}

        <br><br>

        MRECW is a women's engineering college located in
        Maisammaguda, Hyderabad, Telangana.

        </div>
        """, unsafe_allow_html=True)


    # -----------------------------------------------------
    # LOCATION
    # -----------------------------------------------------
    elif "location" in q or "where is" in q or "address" in q:

        st.subheader("📍 College Location")

        st.markdown(f"""
        <div class="answer-box">

        <b>Location:</b> {location}

        </div>
        """, unsafe_allow_html=True)


    # -----------------------------------------------------
    # COURSES
    # -----------------------------------------------------
    elif "course" in q or "courses" in q:

        st.subheader("📚 Courses Offered")

        answer = "<div class='answer-box'>"

        for i, course in enumerate(courses, 1):
            answer += f"<b>{i}. {course}</b><br>"

        answer += "<br><b>Total Courses: 6</b></div>"

        st.markdown(answer, unsafe_allow_html=True)


    # -----------------------------------------------------
    # AIML
    # -----------------------------------------------------
    elif "aiml" in q or "artificial intelligence" in q:

        st.subheader("🤖 Artificial Intelligence and Machine Learning")

        st.markdown("""
        <div class="answer-box">

        <b>B.Tech Artificial Intelligence and Machine Learning (AIML)</b>

        <br><br>

        This programme generally focuses on:

        <br><br>

        • Artificial Intelligence<br>
        • Machine Learning<br>
        • Python Programming<br>
        • Data Analysis<br>
        • Algorithms<br>
        • Deep Learning<br>
        • Intelligent Applications

        </div>
        """, unsafe_allow_html=True)


    # -----------------------------------------------------
    # CSE
    # -----------------------------------------------------
    elif "cse" in q or "computer science" in q:

        st.subheader("💻 Computer Science and Engineering")

        st.markdown("""
        <div class="answer-box">

        <b>B.Tech Computer Science and Engineering (CSE)</b>

        <br><br>

        Major areas generally include:

        <br><br>

        • Programming<br>
        • Data Structures<br>
        • Database Management<br>
        • Operating Systems<br>
        • Computer Networks<br>
        • Software Development

        </div>
        """, unsafe_allow_html=True)


    # -----------------------------------------------------
    # IT
    # -----------------------------------------------------
    elif (
        "information technology" in q
        or q == "it"
        or " it " in f" {q} "
    ):

        st.subheader("💻 Information Technology")

        st.markdown("""
        <div class="answer-box">

        <b>B.Tech Information Technology (IT)</b>

        <br><br>

        Major areas generally include:

        <br><br>

        • Programming<br>
        • Database Systems<br>
        • Networking<br>
        • Information Systems<br>
        • Web Technologies<br>
        • IT Applications

        </div>
        """, unsafe_allow_html=True)


    # -----------------------------------------------------
    # CSD
    # -----------------------------------------------------
    elif "csd" in q or "data science" in q:

        st.subheader("📊 Computer Science and Data Science")

        st.markdown("""
        <div class="answer-box">

        <b>B.Tech Computer Science and Data Science (CSD)</b>

        <br><br>

        Major areas generally include:

        <br><br>

        • Programming<br>
        • Data Analysis<br>
        • Statistics<br>
        • Databases<br>
        • Machine Learning<br>
        • Data Visualization

        </div>
        """, unsafe_allow_html=True)


    # -----------------------------------------------------
    # EEE
    # -----------------------------------------------------
    elif "eee" in q or "electrical" in q:

        st.subheader("⚡ Electrical and Electronics Engineering")

        st.markdown("""
        <div class="answer-box">

        <b>B.Tech Electrical and Electronics Engineering (EEE)</b>

        <br><br>

        Major areas generally include:

        <br><br>

        • Electrical Systems<br>
        • Electronics<br>
        • Electrical Machines<br>
        • Power Systems<br>
        • Control Systems<br>
        • Electrical Applications

        </div>
        """, unsafe_allow_html=True)


    # -----------------------------------------------------
    # ECET
    # IMPORTANT: ECET MUST COME BEFORE ECE
    # -----------------------------------------------------
    elif (
        "ecet" in q
        or ("diploma" in q and "second year" in q)
        or ("diploma" in q and "2nd year" in q)
    ):

        st.subheader("🎓 ECET Admissions")

        st.markdown("""
        <div class="answer-box">

        <b>ECET (Engineering Common Entrance Test)</b>

        <br><br>

        ECET is for students who have completed a
        <b>Diploma</b> and want to join B.Tech through
        <b>lateral entry</b>.

        <br><br>

        <b>Diploma → ECET → B.Tech 2nd Year</b>

        <br><br>

        Eligible Diploma students can get admission
        directly into the <b>second year of B.Tech</b>
        through the counselling process, depending on
        rank, eligibility and seat availability.

        </div>
        """, unsafe_allow_html=True)


    # -----------------------------------------------------
    # ECE
    # -----------------------------------------------------
    elif (
        "electronics and communication" in q
        or q == "ece"
        or " ece " in f" {q} "
    ):

        st.subheader("📡 Electronics and Communication Engineering")

        st.markdown("""
        <div class="answer-box">

        <b>B.Tech Electronics and Communication Engineering (ECE)</b>

        <br><br>

        Major areas generally include:

        <br><br>

        • Digital Electronics<br>
        • Communication Systems<br>
        • Signals and Systems<br>
        • Embedded Systems<br>
        • Electronics

        </div>
        """, unsafe_allow_html=True)


    # -----------------------------------------------------
    # DEPARTMENTS
    # -----------------------------------------------------
    elif "department" in q or "departments" in q:

        st.subheader("🏢 Departments")

        answer = "<div class='answer-box'>"

        for i, department in enumerate(departments, 1):
            answer += f"<b>{i}. {department}</b><br>"

        answer += "<br><b>Total Departments: 6</b></div>"

        st.markdown(answer, unsafe_allow_html=True)


    # -----------------------------------------------------
    # BLOCKS
    # -----------------------------------------------------
    elif "block" in q or "blocks" in q:

        st.subheader("🏫 College Blocks")

        answer = "<div class='answer-box'>"

        for i, block in enumerate(blocks, 1):
            answer += f"<b>{i}. {block}</b><br>"

        answer += "<br><b>Total Blocks: 6</b></div>"

        st.markdown(answer, unsafe_allow_html=True)


    # -----------------------------------------------------
    # HOSTEL
    # -----------------------------------------------------
    elif "hostel" in q or "hostels" in q or "hostle" in q:

        st.subheader("🏠 Hostel Facilities")

        answer = "<div class='answer-box'>"
answer = ... 
