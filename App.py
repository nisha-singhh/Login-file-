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


col1, col2 = st.columns([1.5, 1])

with col1:
    st.image("https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=1000")

with col2:
    st.subheader("Wonder Sign In")

    username = st.text_input("Email Address")
    password = st.text_input("Password", type="password")

    login = st.button("Sign In")

    if login:
        if username == "admin" and password == "1234":
            st.success("Login Successful!")
        else:
            st.error("Invalid Username or Password")


st.markdown("""
<style>
.stApp{
background-color:#0f172a;
}

div[data-testid="column"]:nth-child(2){
background-color:rgba(255,255,255,0.1);
padding:40px;
border-radius:20px;
}
</style>
""", unsafe_allow_html=True)
