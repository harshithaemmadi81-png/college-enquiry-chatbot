import streamlit as st

st.set_page_config(
    page_title="MRECW College Enquiry Chatbot",
    page_icon="🎓",
    layout="centered"
)

# =========================================================
# DESIGN
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
• Laboratories
• Sports
• Transport / Local Buses
""")


# =========================================================
# QUESTION INPUT
# =========================================================
question = st.text_input(
    "Ask your question:",
    placeholder="Type your question here..."
)


# =========================================================
# ANSWER LOGIC
# =========================================================
if question:

    q = question.lower().strip()


    # =====================================================
    # COLLEGE NAME
    # =====================================================
    if (
        "college name" in q
        or "name of college" in q
        or q == "college"
    ):

        st.subheader("🏫 College Information")

        st.markdown(f"""
        <div class="answer-box">

        <b>College Name:</b> {college_name}

        <br><br>

        MRECW is a women's engineering college located
        in Maisammaguda, Hyderabad, Telangana.

        </div>
        """, unsafe_allow_html=True)


    # =====================================================
    # LOCATION
    # =====================================================
    elif (
        "location" in q
        or "where is" in q
        or "address" in q
        or "where located" in q
    ):

        st.subheader("📍 College Location")

        st.markdown(f"""
        <div class="answer-box">

        <b>Location:</b> {location}

        </div>
        """, unsafe_allow_html=True)


    # =====================================================
    # ECET
    # MUST COME BEFORE ECE
    # DIPLOMA → B.TECH 2ND YEAR
    # =====================================================
    elif (
        "ecet" in q
        or "lateral entry" in q
        or "diploma student" in q
        or "diploma students" in q
        or (
            "diploma" in q
            and (
                "second year" in q
                or "2nd year" in q
                or "b.tech" in q
            )
        )
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

        Eligible Diploma students can get admission directly
        into the <b>second year of B.Tech</b> through the
        counselling process, depending on rank, eligibility
        and seat availability.

        </div>
        """, unsafe_allow_html=True)


    # =====================================================
    # EAMCET / TG EAPCET / MCET
    # INTER → B.TECH 1ST YEAR
    # =====================================================
    elif (
        "eamcet" in q
        or "eapcet" in q
        or "tg eapcet" in q
        or "mcet" in q
        or q == "inter"
        or "inter student" in q
        or "inter students" in q
        or "intermediate" in q
        or "intermediate student" in q
        or "intermediate students" in q
        or "1st year" in q
        or "first year" in q
    ):

        st.subheader("🎓 EAMCET / TG EAPCET Admissions")

        st.markdown("""
        <div class="answer-box">

        <b>EAMCET / TG EAPCET</b>

        <br><br>

        EAMCET / TG EAPCET is generally for students
        who have completed <b>Intermediate (Inter)</b>
        and want to join B.Tech.

        <br><br>

        <b>Inter → EAMCET / TG EAPCET → B.Tech 1st Year</b>

        <br><br>

        Eligible students can seek B.Tech admission
        through the entrance examination and counselling
        process, depending on rank, eligibility and
        seat availability.

        </div>
        """, unsafe_allow_html=True)


    # =====================================================
    # COURSES
    # =====================================================
    elif "course" in q or "courses" in q:

        st.subheader("📚 Courses Offered")

        answer = "<div class='answer-box'>"

        for i, course in enumerate(courses, 1):
            answer += f"<b>{i}. {course}</b><br>"

        answer += "<br><b>Total Courses: 6</b></div>"

        st.markdown(answer, unsafe_allow_html=True)


    # =====================================================
    # AIML
    # =====================================================
    elif (
        "aiml" in q
        or "artificial intelligence" in q
        or "machine learning" in q
    ):

        st.subheader("🤖 Artificial Intelligence and Machine Learning")

        st.markdown("""
        <div class="answer-box">

        <b>B.Tech Artificial Intelligence and Machine Learning (AIML)</b>

        <br><br>

        Major areas generally include:

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


    # =====================================================
    # CSD
    # =====================================================
    elif (
        "csd" in q
        or "data science" in q
        or "computer science and data science" in q
    ):

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


    # =====================================================
    # CSE
    # =====================================================
    elif (
        q == "cse"
        or "computer science and engineering" in q
    ):

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


    # =====================================================
    # IT
    # =====================================================
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


    # =====================================================
    # EEE
    # =====================================================
    elif (
        q == "eee"
        or "electrical and electronics" in q
        or "electrical engineering" in q
    ):

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


    # =====================================================
    # ECE
    # =====================================================
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


    # =====================================================
    # DEPARTMENTS
    # =====================================================
    elif (
        "department" in q
        or "departments" in q
    ):

        st.subheader("🏢 Departments")

        answer = "<div class='answer-box'>"

        for i, department in enumerate(departments, 1):
            answer += f"<b>{i}. {department}</b><br>"

        answer += "<br><b>Total Departments: 6</b></div>"

        st.markdown(answer, unsafe_allow_html=True)


    # =====================================================
    # BLOCKS
    # =====================================================
    elif (
        "block" in q
        or "blocks" in q
    ):

        st.subheader("🏫 College Blocks")

        answer = "<div class='answer-box'>"

        for i, block in enumerate(blocks, 1):
            answer += f"<b>{i}. {block}</b><br>"

        answer += "<br><b>Total Blocks: 6</b></div>"

        st.markdown(answer, unsafe_allow_html=True)


    # =====================================================
    # HOSTEL
    # =====================================================
    elif (
        "hostel" in q
        or "hostels" in q
        or "hostle" in q
    ):

        st.subheader("🏠 Hostel Facilities")

        answer = "<div class='answer-box'>"

        for hostel in hostels:
            answer += f"• {hostel}<br>"

        answer += """
        <br>
        <b>Total: 2 Hostels + 1 Apartment Hostel</b>

        <br><br>

        Hostel facilities are available for students.

        <br><br>

        For exact information about rooms, food, fees,
        security and availability, students should contact
        the college administration.

        </div>
        """

        st.markdown(answer, unsafe_allow_html=True)


    # =====================================================
    # CANTEEN
    # =====================================================
    elif "canteen" in q:

        st.subheader("🍽️ Canteen")

        st.markdown("""
        <div class="answer-box">

        The college has <b>1 canteen</b> facility.

        <br><br>

        Students can use the canteen for food and refreshments.

        <br><br>

        <b>Total Canteens: 1</b>

        </div>
        """, unsafe_allow_html=True)


    # =====================================================
    # EINSTEIN BLOCK
    # =====================================================
    elif "einstein" in q:

        st.subheader("🏢 Einstein Block")

        st.markdown("""
        <div class="answer-box">

        Einstein Block is an important facility on the
        college campus.

        <br><br>

        It is used for:

        <br><br>

        • Placement-related activities<br>
        • Student programmes<br>
        • Training sessions<br>
        • Events and college activities

        <br><br>

        <b>Einstein Block: 1</b>

        </div>
        """, unsafe_allow_html=True)


    # =====================================================
    # MANAGEMENT ADMISSION
    # =====================================================
    elif "management" in q:

        st.subheader("🎓 Management Admission")

        st.markdown("""
        <div class="answer-box">

        <b>Management Quota</b>

        <br><br>

        Admissions may also be available through
        management quota.

        <br><br>

        Eligibility, fees and seat availability may vary.
        Students should contact the college admissions
        office for the latest information.

        </div>
        """, unsafe_allow_html=True)


    # =====================================================
    # GENERAL ADMISSIONS
    # =====================================================
    elif (
        "admission" in q
        or "admissions" in q
    ):

        st.subheader("🎓 Admissions")

        st.markdown("""
        <div class="answer-box">

        <b>1. EAMCET / TG EAPCET</b>

        <br><br>

        Inter students can seek B.Tech 1st-year admission
        through the entrance examination and counselling process.

        <br><br>

        <b>2. ECET</b>

        <br><br>

        Diploma students can seek B.Tech lateral-entry
        admission and join directly into the second year.

        <br><br>

        <b>3. Management Quota</b>

        <br><br>

        Admissions may also be available through management
        quota. Eligibility, fees and seat availability should
        be confirmed with the college admissions office.

        </div>
        """, unsafe_allow_html=True)


    # =====================================================
    # PLACEMENTS
    # =====================================================
    elif (
        "placement" in q
        or "placements" in q
        or "companies" in q
        or "company" in q
        or "package" in q
        or "salary" in q
    ):

        st.subheader("💼 Placements")

        companies = [
            "VISA",
            "IBM",
            "Walmart",
            "Cisco",
            "HSBC",
            "Infosys",
            "TCS",
            "Cognizant",
            "Deloitte",
            "HCLTech",
            "KPIT",
            "Accenture",
            "Capgemini",
            "Amazon",
            "Flipkart",
            "DBS",
            "KPMG",
            "Tech Mahindra"
        ]

        answer = """
        <div class="answer-box">

        <b>The college provides placement support and conducts
        recruitment drives for eligible students.</b>

        <br><br>

        <b>Some companies/recruiters:</b>

        <br><br>
        """

        for company in companies:
            answer += f"• {company}<br>"

        answer += """
        <br>

        <b>Placement Highlights:</b>

        <br><br>

        • VISA – up to ₹32 LPA<br>
        • IBM – up to ₹19.83 LPA<br>
        • Walmart – up to ₹18.65 LPA<br>
        • Cisco – up to ₹18 LPA<br>
        • HSBC – up to ₹16.8 LPA<br>
        • Infosys – up to ₹9.5 LPA<br>
        • TCS – up to ₹9.1 LPA

        </div>
        """

        st.markdown(answer, unsafe_allow_html=True)

        st.info(
            "Placement packages depend on the company, role, "
            "selection process and student performance."
        )


    # =====================================================
    # LIBRARY
    # =====================================================
    elif "library" in q:

        st.subheader("📖 Library")

        st.markdown("""
        <div class="answer-box">

        The college provides library facilities with books
        and academic resources for students.

        </div>
        """, unsafe_allow_html=True)


    # =====================================================
    # EXAMINATIONS
    # =====================================================
    elif (
        "exam" in q
        or "exams" in q
        or "examination" in q
        or "examinations" in q
    ):

        st.subheader("📝 Examinations")

        st.markdown("""
        <div class="answer-box">

        Examinations are conducted according to the academic
        calendar and examination schedule.

        </div>
        """, unsafe_allow_html=True)


    # =====================================================
    # TRANSPORT
    # MUST COME BEFORE LABORATORIES
    # =====================================================
    elif (
        "transport" in q
        or "bus" in q
        or "buses" in q
        or "local bus" in q
        or "local buses" in q
        or "bus facility" in q
        or "bus availability" in q
        or "bus timings" in q
    ):

        st.subheader("🚌 Transport / Local Buses")

        st.markdown("""
        <div class="answer-box">

        <b>Local Buses</b>

        <br><br>

        Local buses are available near the college area
        and can be used by students for daily transportation.

        <br><br>

        Bus availability and timings may vary depending
        on the route and daily schedule.

        <br><br>

        Students should check the current local bus timings
        before travelling.

        <br><br>

        <b>College Transport</b>

        <br><br>

        Transport-related information such as college bus
        routes, timings, fees and availability may change.

        Students should contact the college transport
        department for the latest college bus details.

        </div>
        """, unsafe_allow_html=True)


    # =====================================================
    # LABORATORIES
    # =====================================================
    elif (
        "laboratory" in q
        or "laboratories" in q
        or q == "lab"
        or q == "labs"
        or "lab facilities" in q
    ):

        st.subheader("🔬 Laboratories")

        st.markdown("""
        <div class="answer-box">

        The college provides laboratory facilities for
        practical learning and academic activities.

        <br><br>

        Laboratories are available according to the
        requirements of different engineering departments.

        </div>
        """, unsafe_allow_html=True)


    # =====================================================
    # SPORTS
    # =====================================================
    elif (
        "sport" in q
        or "sports" in q
    ):

        st.subheader("🏆 Sports")

        st.markdown("""
        <div class="answer-box">

        Sports and extracurricular activities support
        students' overall development.

        </div>
        """, unsafe_allow_html=True)


    # =====================================================
    # HELP
    # =====================================================
    elif (
        "help" in q
        or "what can you answer" in q
    ):

        st.subheader("❓ I Can Help You With")

        st.markdown("""
        <div class="answer-box">

        • College<br>
        • Location<br>
        • Courses<br>
        • Departments<br>
        • Blocks<br>
        • Hostels<br>
        • Canteen<br>
        • Einstein Block<br>
        • Admissions<br>
        • EAMCET / TG EAPCET<br>
        • ECET<br>
        • Management Admission<br>
        • Placements<br>
        • Companies<br>
        • Packages<br>
        • Library<br>
        • Examinations<br>
        • Laboratories<br>
        • Sports<br>
        • Transport / Local Buses

        </div>
        """, unsafe_allow_html=True)


    # =====================================================
    # UNKNOWN QUESTION
    # =====================================================
    else:

        st.warning(
            "Sorry, I don't have information about that yet. "
            "Please ask about College, Courses, Departments, "
            "Admissions, ECET, EAMCET, Hostel, Placements, "
            "Canteen, Laboratories, Sports or Transport."
        )
