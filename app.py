import streamlit as st

st.set_page_config(
    page_title="MRECW College Enquiry Chatbot",
    page_icon="🎓",
    layout="centered"
)

# -------------------- STYLING --------------------

st.markdown("""
<style>
.stApp {
    background-color: #F2F2F2;
}

h1, h2, h3 {
    color: #800000 !important;
}

h1 {
    text-align: center;
}

.stTextInput label {
    color: #800000 !important;
    font-weight: bold !important;
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
    padding: 20px;
    margin-top: 15px;
    color: #333333;
    line-height: 1.6;
}
</style>
""", unsafe_allow_html=True)


# -------------------- COLLEGE DATA --------------------

college_name = "Malla Reddy Engineering College for Women (MRECW)"
location = "Maisammaguda, Hyderabad, Telangana"

courses = [
    "B.Tech Artificial Intelligence and Machine Learning (AIML)",
    "B.Tech Computer Science and Engineering (CSE)",
    "B.Tech Information Technology (IT)",
    "B.Tech Computer Science and Data Science (CSD)",
    "B.Tech Electrical and Electronics Engineering (EEE)",
    "B.Tech Electronics and Communication Engineering (ECE)"
]

departments = [
    "AIML - Artificial Intelligence and Machine Learning",
    "CSE - Computer Science and Engineering",
    "IT - Information Technology",
    "CSD - Computer Science and Data Science",
    "EEE - Electrical and Electronics Engineering",
    "ECE - Electronics and Communication Engineering"
]

blocks = [
    "AIML Block",
    "CSE Block",
    "IT Block",
    "CSD Block",
    "EEE Block",
    "ECE Block"
]

hostels = [
    "Hostel 1",
    "Hostel 2",
    "Apartment Hostel"
]

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
    "Accenture",
    "Capgemini",
    "Amazon",
    "Flipkart",
    "KPMG",
    "Tech Mahindra"
]


# -------------------- ANSWER FUNCTION --------------------

def show_answer(title, content):
    st.markdown(
        f"""
        <div class="answer-box">
            <h3>{title}</h3>
            {content}
        </div>
        """,
        unsafe_allow_html=True
    )


# -------------------- TITLE --------------------

st.title("🎓 MRECW College Enquiry Chatbot")

st.write("Welcome! Ask me anything about the college.")

st.write(
    "💬 Please ask about:"
    "<br>• College Name"
    "<br>• Location"
    "<br>• Courses"
    "<br>• Departments"
    "<br>• Blocks"
    "<br>• Admissions"
    "<br>• EAMCET / TG EAPCET"
    "<br>• ECET"
    "<br>• Management Admission"
    "<br>• Examinations"
    "<br>• Library"
    "<br>• Hostel"
    "<br>• Placements"
    "<br>• Companies"
    "<br>• Packages"
    "<br>• Canteen"
    "<br>• Einstein Block"
    "<br>• Laboratories"
    "<br>• Sports"
    "<br>• Transport / Local Buses",
    unsafe_allow_html=True
)


# -------------------- USER QUESTION --------------------

question = st.text_input(
    "Ask your question:",
    placeholder="Example: What courses are available?"
)


# -------------------- CHATBOT LOGIC --------------------

if question:

    q = question.lower().strip()

    # ---------- EINSTEIN BLOCK ----------

    if any(word in q for word in [
        "einstein",
        "einstein block"
    ]):
        show_answer(
            "🏢 Einstein Block",
            "<b>1 Einstein Block</b> is available."
            "<br><br>"
            "It is used for:"
            "<br>• Placement-related activities"
            "<br>• Student programmes"
            "<br>• Training sessions"
            "<br>• Events"
            "<br>• Other college activities"
        )


    # ---------- COLLEGE NAME ----------

    elif any(word in q for word in [
        "college name",
        "name of college",
        "which college",
        "mrecw",
        "college"
    ]) and not any(word in q for word in [
        "course",
        "hostel",
        "bus",
        "placement",
        "admission"
    ]):

        show_answer(
            "🏫 College Name",
            f"<b>{college_name}</b>"
            "<br><br>"
            "MRECW is a women's engineering college."
        )


    # ---------- LOCATION ----------

    elif any(word in q for word in [
        "location",
        "where is the college",
        "where is college",
        "where located",
        "where is it located",
        "address",
        "located",
        "place"
    ]):

        show_answer(
            "📍 College Location",
            f"<b>{location}</b>"
            "<br><br>"
            "The college is located at Maisammaguda, Hyderabad, Telangana."
        )


    # ---------- COURSES ----------

    elif any(word in q for word in [
        "course",
        "courses",
        "branch",
        "branches",
        "program",
        "programs",
        "programme",
        "programmes",
        "what can i study",
        "what can i join",
        "what are the courses"
    ]):

        body = "<b>Courses Offered:</b><br><br>"

        for i, course in enumerate(courses, 1):
            body += f"{i}. {course}<br>"

        body += "<br><b>Total Courses: 6</b>"

        show_answer(
            "📚 Courses",
            body
        )


    # ---------- AIML ----------

    elif any(word in q for word in [
        "aiml",
        "artificial intelligence",
        "machine learning"
    ]):

        show_answer(
            "🤖 AIML",
            "<b>B.Tech Artificial Intelligence and Machine Learning</b>"
            "<br><br>"
            "Major areas include:"
            "<br>• Artificial Intelligence"
            "<br>• Machine Learning"
            "<br>• Python Programming"
            "<br>• Data Analysis"
            "<br>• Deep Learning"
            "<br>• Intelligent Applications"
        )


    # ---------- CSE ----------

    elif any(word in q for word in [
        "cse",
        "computer science and engineering"
    ]):

        show_answer(
            "💻 CSE",
            "<b>B.Tech Computer Science and Engineering</b>"
            "<br><br>"
            "Major areas include:"
            "<br>• Programming"
            "<br>• Data Structures"
            "<br>• Database Management"
            "<br>• Operating Systems"
            "<br>• Computer Networks"
            "<br>• Software Development"
        )


    # ---------- CSD ----------

    elif any(word in q for word in [
        "csd",
        "data science",
        "computer science and data science"
    ]):

        show_answer(
            "📊 CSD",
            "<b>B.Tech Computer Science and Data Science</b>"
            "<br><br>"
            "Major areas include:"
            "<br>• Programming"
            "<br>• Data Analysis"
            "<br>• Statistics"
            "<br>• Databases"
            "<br>• Machine Learning"
            "<br>• Data Visualization"
        )


    # ---------- IT ----------

    elif (
        "information technology" in q
        or q == "it"
        or "it course" in q
    ):

        show_answer(
            "🖥️ Information Technology",
            "<b>B.Tech Information Technology</b>"
            "<br><br>"
            "Major areas include:"
            "<br>• Programming"
            "<br>• Database Systems"
            "<br>• Networking"
            "<br>• Web Technologies"
            "<br>• Information Systems"
        )


    # ---------- EEE ----------

    elif any(word in q for word in [
        "eee",
        "electrical and electronics",
        "electrical engineering"
    ]):

        show_answer(
            "⚡ EEE",
            "<b>B.Tech Electrical and Electronics Engineering</b>"
            "<br><br>"
            "Major areas include:"
            "<br>• Electrical Systems"
            "<br>• Electronics"
            "<br>• Electrical Machines"
            "<br>• Power Systems"
            "<br>• Control Systems"
        )


    # ---------- ECE ----------

    elif any(word in q for word in [
        "ece",
        "electronics and communication"
    ]):

        show_answer(
            "📡 ECE",
            "<b>B.Tech Electronics and Communication Engineering</b>"
            "<br><br>"
            "Major areas include:"
            "<br>• Digital Electronics"
            "<br>• Communication Systems"
            "<br>• Signals and Systems"
            "<br>• Embedded Systems"
            "<br>• Electronics"
        )


    # ---------- DEPARTMENTS ----------

    elif any(word in q for word in [
        "department",
        "departments",
        "how many departments",
        "number of departments"
    ]):

        body = "<b>Departments:</b><br><br>"

        for i, department in enumerate(departments, 1):
            body += f"{i}. {department}<br>"

        body += "<br><b>Total Departments: 6</b>"

        show_answer(
            "🏢 Departments",
            body
        )


    # ---------- BLOCKS ----------

    elif any(word in q for word in [
        "block",
        "blocks",
        "how many blocks",
        "number of blocks"
    ]):

        body = "<b>College Blocks:</b><br><br>"

        for i, block in enumerate(blocks, 1):
            body += f"{i}. {block}<br>"

        body += "<br><b>Total Blocks: 6</b>"

        show_answer(
            "🏫 College Blocks",
            body
        )


    # ---------- ECET ----------

    elif any(word in q for word in [
        "ecet",
        "diploma",
        "lateral entry",
        "lateral admission"
    ]):

        show_answer(
            "🎓 ECET Admission",
            "<b>ECET is for Diploma students.</b>"
            "<br><br>"
            "Diploma-qualified students can apply for B.Tech "
            "through ECET lateral entry."
            "<br><br>"
            "<b>Diploma → ECET → B.Tech 2nd Year</b>"
            "<br><br>"
            "Admission depends on eligibility, rank, counselling "
            "and seat availability."
        )


    # ---------- EAMCET ----------

    elif any(word in q for word in [
        "eamcet",
        "eapcet",
        "mcet",
        "intermediate",
        "inter student",
        "inter to btech"
    ]):

        show_answer(
            "🎓 EAMCET / TG EAPCET",
            "<b>For Intermediate students:</b>"
            "<br><br>"
            "Students who complete Intermediate can apply for "
            "B.Tech 1st-year admission through the entrance "
            "examination and counselling process."
            "<br><br>"
            "<b>Inter → EAMCET / TG EAPCET → B.Tech 1st Year</b>"
        )


    # ---------- MANAGEMENT ----------

    elif any(word in q for word in [
        "management quota",
        "management admission",
        "management seats",
        "management"
    ]):

        show_answer(
            "🎓 Management Admission",
            "Management quota admissions may be available."
            "<br><br>"
            "Eligibility, fees and seat availability should be "
            "confirmed with the college admissions office."
        )


    # ---------- GENERAL ADMISSIONS ----------

    elif any(word in q for word in [
        "admission",
        "admissions",
        "how to join",
        "join college",
        "how can i join"
    ]):

        show_answer(
            "🎓 Admissions",
            "<b>Admission Routes:</b>"
            "<br><br>"
            "1. <b>EAMCET / TG EAPCET</b> – For Intermediate "
            "students for B.Tech 1st year."
            "<br><br>"
            "2. <b>ECET</b> – For Diploma students for "
            "B.Tech 2nd-year lateral entry."
            "<br><br>"
            "3. <b>Management Quota</b> – Subject to college "
            "eligibility, fees and seat availability."
        )


    # ---------- HOSTEL ----------

    elif any(word in q for word in [
        "hostel",
        "hostels",
        "hostle",
        "accommodation",
        "stay",
        "where can students stay",
        "student accommodation"
    ]):

        body = "<b>Hostel Facilities:</b><br><br>"

        for hostel in hostels:
            body += f"• {hostel}<br>"

        body += (
            "<br><b>Total:</b> 2 Hostels + 1 Apartment Hostel"
            "<br><br>"
            "For exact room details, food, fees, security and "
            "availability, contact the college administration."
        )

        show_answer(
            "🏠 Hostel",
            body
        )


    # ---------- CANTEEN ----------

    elif any(word in q for word in [
        "canteen",
        "food",
        "mess",
        "refreshments",
        "where can students eat"
    ]):

        show_answer(
            "🍴 Canteen",
            "<b>1 canteen facility</b> is available at the college."
            "<br><br>"
            "Students can use the canteen for food and refreshments."
        )


    # ---------- PLACEMENTS / COMPANIES ----------

    elif any(word in q for word in [
        "placement",
        "placements",
        "company",
        "companies",
        "recruiter",
        "recruiters",
        "package",
        "packages",
        "salary",
        "lpa",
        "job opportunities",
        "placement opportunities",
        "which companies"
    ]):

        body = (
            "The college provides placement support and "
            "recruitment opportunities."
            "<br><br>"
            "<b>Recruiters include:</b><br>"
        )

        for company in companies:
            body += f"• {company}<br>"

        body += (
            "<br><b>Recent Placement Highlights:</b><br>"
            "• VISA – up to ₹32 LPA<br>"
            "• IBM – up to ₹19.83 LPA<br>"
            "• Walmart – up to ₹18.65 LPA<br>"
            "• Cisco – up to ₹18 LPA<br>"
            "• HSBC – up to ₹16.8 LPA<br>"
            "• Infosys – up to ₹9.5 LPA<br>"
            "• TCS – up to ₹9.1 LPA<br><br>"
            "Packages and recruiters can change each year."
        )

        show_answer(
            "💼 Placements",
            body
        )


    # ---------- LIBRARY ----------

    elif any(word in q for word in [
        "library",
        "books",
        "reading",
        "study resources",
        "library facilities"
    ]):

        show_answer(
            "📚 Library",
            "MRECW provides library facilities for students."
            "<br><br>"
            "The library supports academic textbooks, "
            "reference materials and study resources."
            "<br><br>"
            "For exact timings, book count and borrowing rules, "
            "contact the college library."
        )


    # ---------- EXAMINATIONS ----------

    elif any(word in q for word in [
        "exam",
        "exams",
        "examination",
        "examinations",
        "internal",
        "external",
        "semester exam",
        "semester exams"
    ]):

        show_answer(
            "📝 Examinations",
            "<b>Internal Examinations</b><br>"
            "Internal examinations are conducted during the "
            "semester as part of academic evaluation."
            "<br><br>"
            "<b>External / Semester Examinations</b><br>"
            "External examinations are conducted according to "
            "the academic examination schedule."
            "<br><br>"
            "<b>Practical Examinations</b><br>"
            "Practical examinations are conducted as part of "
            "academic evaluation."
            "<br><br>"
            "Exact dates depend on the examination timetable."
        )


    # ---------- LABORATORIES ----------

    elif any(word in q for word in [
        "lab",
        "labs",
        "laboratory",
        "laboratories",
        "practical lab",
        "practical labs",
        "laboratory facilities",
        "practical facilities"
    ]):

        show_answer(
            "🔬 Laboratories",
            "The college provides laboratory facilities "
            "for practical learning and academic activities."
            "<br><br>"
            "Labs help students perform experiments, "
            "gain practical knowledge and develop technical skills."
        )


    # ---------- SPORTS ----------

    elif any(word in q for word in [
        "sport",
        "sports",
        "games",
        "sports facilities",
        "physical activities"
    ]):

        show_answer(
            "🏃 Sports",
            "Sports and extracurricular activities support "
            "students' overall development."
            "<br><br>"
            "They help develop physical fitness, teamwork, "
            "discipline and competitive skills."
        )


    # ---------- TRANSPORT / BUSES ----------

    elif any(word in q for word in [
        "transport",
        "bus",
        "buses",
        "bus facility",
        "bus facilities",
        "college bus",
        "college buses",
        "transportation",
        "local bus",
        "local buses",
        "travel to college",
        "how do students travel"
    ]):

        show_answer(
            "🚌 Transport / Local Buses",
            "<b>Yes, transport facilities are available for "
            "local students.</b>"
            "<br><br>"
            "College buses are available on different routes "
            "for students travelling from nearby and local areas."
            "<br><br>"
            "For exact routes, timings and fees, contact the "
            "college transport department."
        )


    # ---------- HELP ----------

    elif any(word in q for word in [
        "help",
        "what can i ask",
        "topics",
        "what do you know"
    ]):

        show_answer(
            "🤖 I Can Help You With",
            "🏫 College Name<br>"
            "📍 Location<br>"
            "📚 Courses<br>"
            "🏢 Departments<br>"
            "🏫 Blocks<br>"
            "🏢 Einstein Block<br>"
            "🎓 Admissions<br>"
            "📝 EAMCET / TG EAPCET<br>"
            "🎓 ECET<br>"
            "🏠 Hostel<br>"
            "🍴 Canteen<br>"
            "💼 Placements<br>"
            "📚 Library<br>"
            "📝 Examinations<br>"
            "🔬 Laboratories<br>"
            "🏃 Sports<br>"
            "🚌 Transport"
        )


    # ---------- UNKNOWN QUESTION ----------

    else:

        st.warning(
            "I don't have that information yet. "
            "Try asking about Courses, Departments, Admissions, "
            "ECET, EAMCET, Hostel, Einstein Block, Placements, "
            "Library, Exams, Laboratories, Sports or Transport."
        )
