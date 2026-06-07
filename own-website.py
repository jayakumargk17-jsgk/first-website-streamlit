import streamlit as st

# Page config
st.set_page_config(page_title="Job Ready Training Program", layout="wide")

# Sidebar navigation
page = st.sidebar.selectbox("Navigation", ["Home", "Dashboard", "Training Details", "Subject Details", "Internship Program"])

# ── Home ──
if page == "Home":
    st.title("🚀 Job Ready Training Program")
    st.write("### Welcome to Industry-Focused Training!")
    st.write("""
        We provide **industry-level training** designed to help students and job seekers 
        build real-world skills and land their dream jobs. Our program covers the most 
        in-demand technologies used in top companies today.
    """)
    st.success("🎯 Our Goal: Make you Job Ready!")

    st.write("---")
    st.write("### Why Choose Us?")
    col1, col2, col3 = st.columns(3)
    col1.info("✅ Industry Expert Trainers")
    col2.info("✅ Real-World Projects")
    col3.info("✅ Internship Opportunities")

    col4, col5, col6 = st.columns(3)
    col4.info("✅ Job Assistance")
    col5.info("✅ Affordable Fees")
    col6.info("✅ Certificate on Completion")

# ── Dashboard ──
elif page == "Dashboard":
    st.title("📊 Dashboard")
    st.write("---")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Students Enrolled", "350")
    col2.metric("Total Courses", "7")
    col3.metric("Placement Rate", "85%")

    col4, col5, col6 = st.columns(3)
    col4.metric("Internships Offered", "120")
    col5.metric("Hiring Partners", "30+")
    col6.metric("Batches Completed", "15")

# ── Training Details ──
elif page == "Training Details":
    st.title("📚 Training Details")
    st.write("### Our Industry-Focused Courses")
    st.table({
        "Course": ["Java", "Spring Boot", "Microservices", "Kafka", "Database", "JUnit", "Mockito"],
        "Duration": ["30 days", "25 days", "20 days", "15 days", "20 days", "10 days", "10 days"],
        "Level": ["Beginner", "Intermediate", "Advanced", "Advanced", "Beginner", "Intermediate", "Intermediate"],
        "Status": ["Available", "Available", "Available", "Available", "Available", "Available", "Available"]
    })

# ── Subject Details ──
elif page == "Subject Details":
    st.title("📖 Subject Details")

    st.write("### Java")
    st.write("Core Java, OOPs, Collections, Exception Handling, Multithreading, Streams")

    st.write("---")
    st.write("### Spring Boot")
    st.write("REST APIs, Spring MVC, Spring Security, Spring Data JPA, Auto Configuration")

    st.write("---")
    st.write("### Microservices")
    st.write("Service Discovery, API Gateway, Load Balancing, Circuit Breaker, Docker Basics")

    st.write("---")
    st.write("### Kafka")
    st.write("Kafka Architecture, Producers, Consumers, Topics, Partitions, Kafka Streams")

    st.write("---")
    st.write("### Database")
    st.write("SQL Basics, Joins, Stored Procedures, Indexing, MySQL, PostgreSQL")

    st.write("---")
    st.write("### JUnit")
    st.write("Unit Testing, Test Cases, Assertions, Test Suites, JUnit 5 Features")

    st.write("---")
    st.write("### Mockito")
    st.write("Mocking, Stubbing, Verify, ArgumentCaptor, Integration with JUnit")

# ── Internship Program ──
elif page == "Internship Program":
    st.title("💼 Industry Internship Program")
    st.write("### Get Real-World Experience Before Your First Job!")
    st.write("""
        Our internship program is designed for students and freshers who are 
        looking for jobs. You will work on **live industry projects** using the 
        technologies you have learned.
    """)

    st.write("---")
    st.write("### Internship Highlights")
    col1, col2 = st.columns(2)
    with col1:
        st.success("✅ Duration: 2 to 3 Months")
        st.success("✅ Work on Live Projects")
        st.success("✅ Mentorship by Industry Experts")
        st.success("✅ Certificate of Internship")
    with col2:
        st.success("✅ Resume Building Support")
        st.success("✅ Mock Interviews")
        st.success("✅ LinkedIn Profile Review")
        st.success("✅ Job Referrals")

    st.write("---")
    st.write("### Who Can Apply?")
    st.info("🎓 Final year students | 🎓 Fresh graduates | 🎓 Career switchers looking for IT jobs")

    st.write("---")
    st.write("### How to Apply?")
    st.write("1. Complete at least **2 courses** from our Training Program")
    st.write("2. Submit your details using the form below")
    st.write("3. Our team will contact you within **2 business days**")

    st.write("---")
    st.write("### Apply for Internship")
    name = st.text_input("Full Name")
    email = st.text_input("Email Address")
    phone = st.text_input("Phone Number")
    course = st.multiselect("Courses Completed", ["Java", "Spring Boot", "Microservices", "Kafka", "Database", "JUnit", "Mockito"])
    experience = st.selectbox("Experience Level", ["Student", "Fresh Graduate", "Career Switcher"])

    if st.button("Submit Application"):
        if name and email and phone and course:
            st.success(f"✅ Thank you {name}! Your application has been submitted. We will contact you at {email} within 2 business days.")
        else:
            st.error("❌ Please fill in all the fields before submitting.")