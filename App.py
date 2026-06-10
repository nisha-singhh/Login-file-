import streamlit as st
import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    username TEXT,
    password TEXT
)
""")

conn.commit()

st.title("🔐 Login Page")


col1, col2 = st.columns([1.3, 1])

with col1:
    st.markdown("""
    <div style='margin-top:180px; color:white;'>
        <h1 style='font-size:55px;'>Start for free and get attractive offers today !</h1>
        <p style='font-size:18px; color:#d1d5db;'>
        Discover thousands of opportunities and manage your account easily.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:

    st.markdown("<h2 style='color:white;'>Wonder Sign In</h2>", unsafe_allow_html=True)

    username = st.text_input("Email Address")

    password = st.text_input(
        "Password",
        type="password"
    )

    remember = st.checkbox("Keep me logged in")

    login = st.button(
        "Sign In",
        use_container_width=True
    )

    signup = st.button(
        "Sign Up",
        use_container_width=True
    )



st.markdown("""
<style>

.stApp{
background: linear-gradient(rgba(0,0,0,0.55), rgba(0,0,0,0.55)),
url("https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=1600");
background-size: cover;
background-position: center;
background-attachment: fixed;
}

div[data-testid="column"]:nth-child(2){
background: rgba(255,255,255,0.12);
backdrop-filter: blur(18px);
padding:40px;
border-radius:25px;
border:1px solid rgba(255,255,255,0.2);
box-shadow:0 8px 32px rgba(0,0,0,0.4);
}

h1,h2,h3,label{
color:white !important;
}

.stButton button{
background:#ff5a2c;
color:white;
border:none;
border-radius:30px;
height:50px;
font-size:18px;
font-weight:bold;
}

</style>
""", unsafe_allow_html=True)
