import streamlit as st

# Page config
st.set_page_config(page_title="My Website", layout="wide")

# Sidebar navigation
page = st.sidebar.selectbox("Navigation", ["Home", "Dashboard", "Training Details", "Subject Details"])

# ── Home ──
if page == "Home":
    st.title("Welcome to My Website")
    st.write("This is the home page with basic information.")

# ── Dashboard ──
elif page == "Dashboard":
    st.title("Dashboard")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Students", "120")
    col2.metric("Total Subjects", "10")
    col3.metric("Training Completed", "75%")

# ── Training Details ──
elif page == "Training Details":
    st.title("Training Details")
    st.write("### Ongoing Trainings")
    st.table({
        "Training": ["Python", "SQL", "ML"],
        "Duration": ["30 days", "20 days", "45 days"],
        "Status": ["Completed", "Ongoing", "Upcoming"]
    })

# ── Subject Details ──
elif page == "Subject Details":
    st.title("Subject Details")
    st.write("### Subjects Offered")
    st.table({
        "Subject": ["Math", "Science", "English"],
        "Credits": [4, 3, 3],
        "Instructor": ["John", "Jane", "Smith"]
    })