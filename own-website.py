import streamlit as st

# Page config
st.set_page_config(page_title="Job Ready Training Program", layout="wide")

# ── Global CSS Styling ──
st.markdown("""
    <style>
        .stApp {
            background-color: #1a1a2e;
        }
        .stButton > button {
            background-color: #e94560;
            color: white;
            border-radius: 10px;
            padding: 15px;
            font-size: 15px;
            font-weight: bold;
            border: none;
            transition: background-color 0.3s;
        }
        .stButton > button:hover {
            background-color: #f5a623;
            color: white;
        }
        .card {
            background-color: #16213e;
            border-radius: 15px;
            padding: 20px;
            box-shadow: 0px 4px 12px rgba(0,0,0,0.4);
            margin-bottom: 20px;
            color: #ffffff;
        }
        .img-card {
            background-color: #16213e;
            border-radius: 15px;
            padding: 15px;
            box-shadow: 0px 4px 12px rgba(0,0,0,0.4);
            margin-bottom: 20px;
            text-align: center;
        }
        .img-card img {
            border-radius: 12px;
            width: 100%;
            max-width: 700px;
            height: 300px;
            object-fit: cover;
        }
        .img-card-small img {
            border-radius: 12px;
            width: 100%;
            height: 200px;
            object-fit: cover;
        }
        .img-caption {
            color: #f5a623;
            font-size: 13px;
            margin-top: 8px;
            text-align: center;
        }
        h1, h2, h3 {
            color: #f5a623;
        }
        p, li {
            color: #e0e0e0;
        }
        .banner {
            background: linear-gradient(135deg, #e94560, #0f3460);
            color: white;
            padding: 40px;
            border-radius: 15px;
            text-align: center;
            margin-bottom: 20px;
        }
        [data-testid="stMetric"] {
            background-color: #16213e;
            border-radius: 12px;
            padding: 15px;
        }
        [data-testid="stMetricLabel"] {
            color: #f5a623 !important;
        }
        [data-testid="stMetricValue"] {
            color: #ffffff !important;
        }
        [data-testid="stMetricDelta"] {
            color: #4caf50 !important;
        }
        table {
            background-color: #16213e !important;
            color: #ffffff !important;
        }
        th {
            background-color: #0f3460 !important;
            color: #f5a623 !important;
        }
        td {
            color: #e0e0e0 !important;
        }
        .stTextInput > div > div > input {
            background-color: #16213e;
            color: white;
            border: 1px solid #e94560;
        }
        hr {
            border-color: #0f3460;
        }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if "page" not in st.session_state:
    st.session_state.page = "Home"

# ── Top Navigation Bar ──
st.markdown("""
    <div class="banner" style="padding: 20px; margin-bottom: 10px;">
        <h2 style="color:white; margin:0;">🚀 Job Ready Training Program</h2>
    </div>
""", unsafe_allow_html=True)

nav1, nav2, nav3, nav4, nav5 = st.columns(5)
with nav1:
    if st.button("🏠 Home", use_container_width=True):
        st.session_state.page = "Home"
        st.rerun()
with nav2:
    if st.button("📊 Dashboard", use_container_width=True):
        st.session_state.page = "Dashboard"
        st.rerun()
with nav3:
    if st.button("📚 Training Details", use_container_width=True):
        st.session_state.page = "Training Details"
        st.rerun()
with nav4:
    if st.button("📖 Subject Details", use_container_width=True):
        st.session_state.page = "Subject Details"
        st.rerun()
with nav5:
    if st.button("💼 Internship Program", use_container_width=True):
        st.session_state.page = "Internship Program"
        st.rerun()

st.write("---")

# ══════════════════════════════════════════
# ── Home ──
# ══════════════════════════════════════════
if st.session_state.page == "Home":

    st.markdown("""
        <div class="banner">
            <h1 style="color:white; font-size:42px;">Welcome to Job Ready Training Program</h1>
            <p style="font-size:18px; color:#f5a623;">Industry-Focused Training | Real Projects | Job Assistance</p>
        </div>
    """, unsafe_allow_html=True)

    # Hero image inside markdown card
    st.markdown("""
        <div class="img-card">
            <img src="https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=1200&h=400&fit=crop&q=80" />
            <p class="img-caption">Build Your Career with Industry Experts</p>
        </div>
    """, unsafe_allow_html=True)

    st.write("---")

    st.markdown("""
        <div class="card">
            <h2>🎯 About Our Program</h2>
            <p style="font-size:16px;">
                We provide <b>industry-level training</b> designed to help students and job seekers
                build real-world skills and land their dream jobs. Our program covers the most
                in-demand technologies used in top companies today.
            </p>
        </div>
    """, unsafe_allow_html=True)

    st.write("### ✨ Why Choose Us?")

    home_r1c1, home_r1c2, home_r1c3 = st.columns(3)
    with home_r1c1:
        st.markdown("""
            <div class="card">
                <div class="img-card-small">
                    <img src="https://images.unsplash.com/photo-1507537297725-24a1c029d3ca?w=600&h=200&fit=crop&q=80" />
                </div>
                <br>👨‍🏫 <b>Industry Expert Trainers</b><br><br>
                Learn from professionals with 10+ years of experience
            </div>
        """, unsafe_allow_html=True)
    with home_r1c2:
        st.markdown("""
            <div class="card">
                <div class="img-card-small">
                    <img src="https://images.unsplash.com/photo-1515879218367-8466d910aaa4?w=600&h=200&fit=crop&q=80" />
                </div>
                <br>💻 <b>Real-World Projects</b><br><br>
                Work on live projects used in top companies
            </div>
        """, unsafe_allow_html=True)
    with home_r1c3:
        st.markdown("""
            <div class="card">
                <div class="img-card-small">
                    <img src="https://images.unsplash.com/photo-1521737711867-e3b97375f902?w=600&h=200&fit=crop&q=80" />
                </div>
                <br>🏢 <b>Internship Opportunities</b><br><br>
                Get hands-on experience before your first job
            </div>
        """, unsafe_allow_html=True)

    home_r2c1, home_r2c2, home_r2c3 = st.columns(3)
    with home_r2c1:
        st.markdown("""
            <div class="card">
                <div class="img-card-small">
                    <img src="https://images.unsplash.com/photo-1573497019940-1c28c88b4f3e?w=600&h=200&fit=crop&q=80" />
                </div>
                <br>💼 <b>Job Assistance</b><br><br>
                Resume building, mock interviews and referrals
            </div>
        """, unsafe_allow_html=True)
    with home_r2c2:
        st.markdown("""
            <div class="card">
                <div class="img-card-small">
                    <img src="https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?w=600&h=200&fit=crop&q=80" />
                </div>
                <br>💰 <b>Affordable Fees</b><br><br>
                High quality training at the most affordable price
            </div>
        """, unsafe_allow_html=True)
    with home_r2c3:
        st.markdown("""
            <div class="card">
                <div class="img-card-small">
                    <img src="https://images.unsplash.com/photo-1496181133206-80ce9b88a853?w=600&h=200&fit=crop&q=80" />
                </div>
                <br>🏆 <b>Certificate on Completion</b><br><br>
                Industry recognized certificate for your profile
            </div>
        """, unsafe_allow_html=True)

    st.write("---")

    # Team image inside markdown card
    st.markdown("""
        <div class="img-card">
            <img src="https://images.unsplash.com/photo-1600880292203-757bb62b4baf?w=1200&h=400&fit=crop&q=80" />
            <p class="img-caption">Our Professional Team of Trainers</p>
        </div>
    """, unsafe_allow_html=True)

# ══════════════════════════════════════════
# ── Dashboard ──
# ══════════════════════════════════════════
elif st.session_state.page == "Dashboard":

    st.markdown("""
        <div class="banner">
            <h1 style="color:white;">📊 Dashboard</h1>
            <p style="color:#f5a623;">Overview of our Training Program</p>
        </div>
    """, unsafe_allow_html=True)

    # Dashboard image inside markdown card
    st.markdown("""
        <div class="img-card">
            <img src="https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=1200&h=400&fit=crop&q=80" />
            <p class="img-caption">Training Program Analytics</p>
        </div>
    """, unsafe_allow_html=True)

    st.write("---")

    dash_m1, dash_m2, dash_m3 = st.columns(3)
    dash_m1.metric("Total Students Enrolled", "350", "+50 this month")
    dash_m2.metric("Total Courses", "7", "+2 new")
    dash_m3.metric("Placement Rate", "85%", "+5%")

    dash_m4, dash_m5, dash_m6 = st.columns(3)
    dash_m4.metric("Internships Offered", "120", "+20")
    dash_m5.metric("Hiring Partners", "30+", "+5 new")
    dash_m6.metric("Batches Completed", "15", "+3")

    st.write("---")

    # Placed students image inside markdown card
    st.markdown("""
        <div class="img-card">
            <img src="https://images.unsplash.com/photo-1517245386807-bb43f82c33c4?w=1200&h=400&fit=crop&q=80" />
            <p class="img-caption">Students Successfully Placed</p>
        </div>
    """, unsafe_allow_html=True)

# ══════════════════════════════════════════
# ── Training Details ──
# ══════════════════════════════════════════
elif st.session_state.page == "Training Details":

    st.markdown("""
        <div class="banner">
            <h1 style="color:white;">📚 Training Details</h1>
            <p style="color:#f5a623;">Industry-Focused Course Curriculum</p>
        </div>
    """, unsafe_allow_html=True)

    # Training image inside markdown card
    st.markdown("""
        <div class="img-card">
            <img src="https://images.unsplash.com/photo-1524178232363-1fb2b075b655?w=1200&h=400&fit=crop&q=80" />
            <p class="img-caption">Learn from Industry Experts</p>
        </div>
    """, unsafe_allow_html=True)

    st.write("---")
    st.write("### Our Industry-Focused Courses")
    st.table({
        "Course":   ["Java", "Spring Boot", "Microservices", "Kafka", "Database", "JUnit", "Mockito"],
        "Duration": ["30 days", "25 days", "20 days", "15 days", "20 days", "10 days", "10 days"],
        "Level":    ["Beginner", "Intermediate", "Advanced", "Advanced", "Beginner", "Intermediate", "Intermediate"],
        "Status":   ["Available", "Available", "Available", "Available", "Available", "Available", "Available"]
    })

    st.write("---")

    train_side_left, train_side_right = st.columns(2)
    with train_side_left:
        st.markdown("""
            <div class="img-card">
                <div class="img-card-small">
                    <img src="https://images.unsplash.com/photo-1515879218367-8466d910aaa4?w=600&h=200&fit=crop&q=80" />
                </div>
                <p class="img-caption">Hands-on Coding Sessions</p>
            </div>
        """, unsafe_allow_html=True)
    with train_side_right:
        st.markdown("""
            <div class="img-card">
                <div class="img-card-small">
                    <img src="https://images.unsplash.com/photo-1531482615713-2afd69097998?w=600&h=200&fit=crop&q=80" />
                </div>
                <p class="img-caption">Live Project Training</p>
            </div>
        """, unsafe_allow_html=True)

# ══════════════════════════════════════════
# ── Subject Details ──
# ══════════════════════════════════════════
elif st.session_state.page == "Subject Details":

    st.markdown("""
        <div class="banner">
            <h1 style="color:white;">📖 Subject Details</h1>
            <p style="color:#f5a623;">Detailed Curriculum for Each Course</p>
        </div>
    """, unsafe_allow_html=True)

    # Subject image inside markdown card
    st.markdown("""
        <div class="img-card">
            <img src="https://images.unsplash.com/photo-1434030216411-0b793f4b4173?w=1200&h=400&fit=crop&q=80" />
            <p class="img-caption">Structured Learning Path</p>
        </div>
    """, unsafe_allow_html=True)

    st.write("---")

    subjects = {
        "☕ Java": "Core Java, OOPs, Collections, Exception Handling, Multithreading, Streams",
        "🌱 Spring Boot": "REST APIs, Spring MVC, Spring Security, Spring Data JPA, Auto Configuration",
        "🔗 Microservices": "Service Discovery, API Gateway, Load Balancing, Circuit Breaker, Docker Basics",
        "📨 Kafka": "Kafka Architecture, Producers, Consumers, Topics, Partitions, Kafka Streams",
        "🗄️ Database": "SQL Basics, Joins, Stored Procedures, Indexing, MySQL, PostgreSQL",
        "🧪 JUnit": "Unit Testing, Test Cases, Assertions, Test Suites, JUnit 5 Features",
        "🎭 Mockito": "Mocking, Stubbing, Verify, ArgumentCaptor, Integration with JUnit"
    }

    for subject, topics in subjects.items():
        st.markdown(f"""
            <div class="card">
                <h3>{subject}</h3>
                <p style="font-size:15px;">📌 {topics}</p>
            </div>
        """, unsafe_allow_html=True)

# ══════════════════════════════════════════
# ── Internship Program ──
# ══════════════════════════════════════════
elif st.session_state.page == "Internship Program":

    st.markdown("""
        <div class="banner">
            <h1 style="color:white;">💼 Industry Internship Program</h1>
            <p style="color:#f5a623;">Get Real-World Experience Before Your First Job!</p>
        </div>
    """, unsafe_allow_html=True)

    # Internship image inside markdown card
    st.markdown("""
        <div class="img-card">
            <img src="https://images.unsplash.com/photo-1521737711867-e3b97375f902?w=1200&h=400&fit=crop&q=80" />
            <p class="img-caption">Professional Work Environment</p>
        </div>
    """, unsafe_allow_html=True)

    st.write("---")
    st.write("### 🌟 Internship Highlights")

    intern_h1, intern_h2 = st.columns(2)
    with intern_h1:
        st.markdown("""
            <div class="card">
                <div class="img-card-small">
                    <img src="https://images.unsplash.com/photo-1517694712202-14dd9538aa97?w=600&h=200&fit=crop&q=80" />
                </div>
                <br>
                ✅ Duration: 2 to 3 Months<br><br>
                ✅ Work on Live Projects<br><br>
                ✅ Mentorship by Industry Experts<br><br>
            </div>
        """, unsafe_allow_html=True)
    with intern_h2:
        st.markdown("""
            <div class="card">
                <div class="img-card-small">
                    <img src="https://images.unsplash.com/photo-1498050108023-c5249f4df085?w=600&h=200&fit=crop&q=80" />
                </div>
                <br>
                ✅ Certificate of Internship<br><br>
                ✅ Mock Interviews<br><br>
                ✅ Job Referrals
            </div>
        """, unsafe_allow_html=True)

    st.write("---")
    st.info("🎓 Who Can Apply: Final year students | Fresh graduates | Career switchers looking for IT jobs")

    st.write("---")
    st.write("### 📝 How to Apply?")
    st.markdown("""
        <div class="card">
            <p>Contact:</p><br>
            <p>Email: jobs.market.all@gmail.com</p><br>
            <p>link: training-freshers.streamlit.app</p>
            
        </div>
    """, unsafe_allow_html=True)

    st.write("---")
