import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="MRECW College Enquiry Chatbot",
    page_icon="🎓",
    layout="centered"
)

# Title
st.title("🎓 MRECW College Enquiry Chatbot")
st.write("Welcome! Ask me anything about the college.")

# College Information
college_name = "Malla Reddy Engineering College for Women (MRECW)"
location = "Maisammaguda, Hyderabad, Telangana"

# Courses
courses = [
    "B.Tech Artificial Intelligence and Machine Learning (AIML)",
    "B.Tech Computer Science and Engineering (CSE)",
    "B.Tech Information Technology (IT)",
    "B.Tech Computer Science and Data Science (CSD)",
    "B.Tech Electrical and Electronics Engineering (EEE)",
    "B.Tech Electronics and Communication Engineering (ECE)"
]

# Departments
departments = [
    "AIML - Artificial Intelligence and Machine Learning",
    "CSE - Computer Science and Engineering",
    "IT - Information Technology",
    "CSD - Computer Science and Data Science",
    "EEE - Electrical and Electronics Engineering",
    "ECE - Electronics and Communication Engineering"
]

# Blocks
blocks = [
    "AIML Block",
    "CSE Block",
    "IT Block",
    "CSD Block",
    "EEE Block",
    "ECE Block"
]

# Hostels
hostels = [
    "Hostel 1",
    "Hostel 2",
    "Apartment Hostel"
]

# Questions
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
• Transport
""")

# User Question
question = st.text_input("Ask your question:")

if question:

    q = question.lower().strip()

    # College Name
    if "college name" in q or "name of college" in q:
        st.subheader("🏫 College Information")
        st.write(f"**College Name:** {college_name}")
        st.write(
            "MRECW is a women's engineering college located in "
            "Maisammaguda, Hyderabad, Telangana."
        )

    # Location
    elif "location" in q or "where is" in q or "address" in q:
        st.subheader("📍 College Location")
        st.write(f"**Location:** {location}")

    # Courses
    elif "course" in q or "courses" in q:
        st.subheader("📚 Courses Offered")

        for i, course in enumerate(courses, 1):
            st.write(f"**{i}. {course}**")

        st.info("Total Courses: 6")

    # AIML
    elif "aiml" in q or "artificial intelligence" in q:
        st.subheader("🤖 Artificial Intelligence and Machine Learning")

        st.write("""
        **B.Tech Artificial Intelligence and Machine Learning (AIML)**

        This programme generally focuses on:

        • Artificial Intelligence
        • Machine Learning
        • Python Programming
        • Data Analysis
        • Algorithms
        • Deep Learning
        • Intelligent Applications
        """)

    # CSE
    elif "cse" in q or "computer science" in q:
        st.subheader("💻 Computer Science and Engineering")

        st.write("""
        **B.Tech Computer Science and Engineering (CSE)**

        Major areas generally include:

        • Programming
        • Data Structures
        • Database Management
        • Operating Systems
        • Computer Networks
        • Software Development
        """)

    # IT
    elif (
        "information technology" in q
        or q == "it"
        or " it " in f" {q} "
    ):
        st.subheader("💻 Information Technology")

        st.write("""
        **B.Tech Information Technology (IT)**

        Major areas generally include:

        • Programming
        • Database Systems
        • Networking
        • Information Systems
        • Web Technologies
        • IT Applications
        """)

    # CSD
    elif "csd" in q or "data science" in q:
        st.subheader("📊 Computer Science and Data Science")

        st.write("""
        **B.Tech Computer Science and Data Science (CSD)**

        Major areas generally include:

        • Programming
        • Data Analysis
        • Statistics
        • Databases
        • Machine Learning
        • Data Visualization
        """)

    # EEE
    elif "eee" in q or "electrical" in q:
        st.subheader("⚡ Electrical and Electronics Engineering")

        st.write("""
        **B.Tech Electrical and Electronics Engineering (EEE)**

        Major areas generally include:

        • Electrical Systems
        • Electronics
        • Electrical Machines
        • Power Systems
        • Control Systems
        • Electrical Applications
        """)

    # ECE
    elif "ece" in q or "electronics and communication" in q:
        st.subheader("📡 Electronics and Communication Engineering")

        st.write("""
        **B.Tech Electronics and Communication Engineering (ECE)**

        Major areas generally include:

        • Digital Electronics
        • Communication Systems
        • Signals and Systems
        • Embedded Systems
        • Electronics
        """)

    # Departments
    elif "department" in q or "departments" in q:
        st.subheader("🏢 Departments")

        for i, department in enumerate(departments, 1):
            st.write(f"**{i}. {department}**")

        st.info("Total Departments: 6")

    # Blocks
    elif "block" in q or "blocks" in q:
        st.subheader("🏫 College Blocks")

        for i, block in enumerate(blocks, 1):
            st.write(f"**{i}. {block}**")

        st.info("Total Blocks: 6")

    # Hostel
    elif "hostel" in q or "hostels" in q or "hostle" in q:
        st.subheader("🏠 Hostel Facilities")

        for hostel in hostels:
            st.write(f"• {hostel}")

        st.info("Total: 2 Hostels + 1 Apartment Hostel")

        st.write("""
        Hostel facilities are available for students.

        For exact information about rooms, food, fees, security,
        availability and other facilities, students should contact
        the college administration.
        """)

    # Canteen
    elif "canteen" in q:
        st.subheader("🍽️ Canteen")

        st.write("""
        The college has **1 canteen** facility.

        Students can use the canteen for food and refreshments.
        """)

        st.info("Total Canteens: 1")

    # Einstein Block
    elif "einstein" in q:
        st.subheader("🏢 Einstein Block")

        st.write("""
        Einstein Block is an important facility on the college campus.

        It is used for:

        • Placement-related activities
        • Student programmes
        • Training sessions
        • Events and other college activities
        """)

        st.info("Einstein Blocks: 1")

    # Admissions
    elif (
        "admission" in q
        or "admissions" in q
        or "mcet" in q
        or "eamcet" in q
        or "eapcet" in q
        or "ecet" in q
        or "management" in q
    ):
        st.subheader("🎓 Admissions")

        st.write("""
        MRECW admissions are available through different admission routes.
        """)

        st.write("""
        **1. EAMCET / TG EAPCET**

        • Students can seek B.Tech admission through the state-level
          engineering entrance examination and counselling process.

        • Seat allotment depends on eligibility, rank, counselling
          and seat availability.
        """)

        st.write("""
        **2. ECET**

        • Diploma students can apply for B.Tech lateral-entry admission
          through ECET.

        • Eligible students can join directly into the second year
          through the counselling process.
        """)

        st.write("""
        **3. Management Quota**

        • Admissions may also be available through the management quota.

        • Eligibility, fee structure and seat availability should be
          confirmed with the college admissions office.
        """)

        st.info(
            "Admission rules, fees, eligibility and seat availability "
            "may change every academic year. Please contact the college "
            "admissions office for the latest information."
        )

    # Placements
    elif (
        "placement" in q
        or "placements" in q
        or "companies" in q
        or "company" in q
        or "package" in q
        or "salary" in q
    ):
        st.subheader("💼 Placements")

        st.write("""
        The college provides placement support and conducts
        recruitment drives for eligible students.

        Some companies/recruiters associated with placement activities:
        """)

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

        for company in companies:
            st.write(f"• {company}")

        st.subheader("💰 Recent Placement Highlights")

        st.write("""
        • VISA – up to ₹32 LPA
        • IBM – up to ₹19.83 LPA
        • Walmart – up to ₹18.65 LPA
        • Cisco – up to ₹18 LPA
        • HSBC – up to ₹16.8 LPA
        • Infosys – up to ₹9.5 LPA
        • TCS – up to ₹9.1 LPA
        """)

        st.success(
            "Placement packages depend on the company, role, "
            "selection process and student performance."
        )

    # Library
    elif "library" in q:
        st.subheader("📖 Library")

        st.write("""
        The college provides library facilities with books and
        academic resources for students.
        """)

    # Exams
    elif (
        "exam" in q
        or "exams" in q
        or "examination" in q
        or "examinations" in q
    ):
        st.subheader("📝 Examinations")

        st.write("""
        Examinations are conducted according to the academic calendar
        and examination schedule.
        """)

    # Labs
    elif "lab" in q or "labs" in q:
        st.subheader("🔬 Laboratories")

        st.write("""
        Engineering departments use laboratory facilities for
        practical learning and academic activities.
        """)

    # Sports
    elif "sport" in q or "sports" in q:
        st.subheader("🏃 Sports")

        st.write("""
        Sports and extracurricular activities support students'
        overall development.
        """)

    # Transport
    elif "transport" in q or "bus" in q:
        st.subheader("🚌 Transport")

        st.write("""
        Transport-related information such as routes, timings,
        fees and availability may change.

        Students should contact the college transport department
        for the latest details.
        """)

    # Help
    elif "help" in q or "what can you answer" in q:
        st.subheader("🤖 I Can Help You With")

        st.write("""
        • College
        • Location
        • Courses
        • Departments
        • Blocks
        • Hostels
        • Canteen
        • Einstein Block
        • Admissions
        • EAMCET / TG EAPCET
        • ECET
        • Management Admission
        • Placements
        • Companies
        • Packages
        • Library
        • Examinations
        • Labs
        • Sports
        • Transport
        """)

    # Unknown Question
    else:
        st.warning(
            "Sorry, I don't have information about that yet. "
            "Please ask about College, Courses, Departments, "
            "Blocks, Admissions, ECET, EAMCET, Management, "
            "Hostel, Placements, Canteen or Einstein Block."
        )