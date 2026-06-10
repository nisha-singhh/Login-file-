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

<h1 style='font-size:55px;'>
Secure User Authentication System
</h1>

<p style='font-size:20px; color:#d1d5db;'>

Build a powerful authentication platform with separate User and Admin panels.
Manage accounts, monitor user data, and create secure dashboards with role-based access.

</p>

</div>
""", unsafe_allow_html=True)

with col2:

    st.markdown("""
    <h2 style='color:white; text-align:center;'>
    Wonder Sign In
    </h2>

    <p style='color:#d1d5db; text-align:center;'>
    Access your account securely
    </p>
    """, unsafe_allow_html=True)

    username = st.text_input(
        "Email Address",
        placeholder="Enter your email"
    )

    password = st.text_input(
        "Password",
        type="password",
        placeholder="Enter your password"
    )

    remember = st.checkbox("Keep me logged in")

    login = st.button(
        "Sign In",
        use_container_width=True
    )

if login:
    if username == "" or password == "":
        st.warning("Please fill all fields")
    else:
        cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        user = cursor.fetchone()

        if user:
            st.success("Login Successful 🎉")
            st.session_state["logged_in"] = True
            st.session_state["user"] = username
        else:
            st.error("Invalid username or password")

    st.markdown(
        "<p style='text-align:center;color:#d1d5db;'>Forgot Password?</p>",
        unsafe_allow_html=True
    )

    signup = st.button(
        "Create Account",
        use_container_width=True
    )

    
    if signup:
        if username == "" or password == "":
            st.warning("Please fill all fields")
        else:
            cursor.execute("SELECT * FROM users WHERE username=?", (username,))
            existing_user = cursor.fetchone()

            if existing_user:
                st.error("User already exists!")
            else:
                cursor.execute("INSERT INTO users(username, password) VALUES(?,?)", (username, password))
                conn.commit()
                st.success("Account created successfully 🎉")



st.markdown("""
<style>

.stApp{
background-image:
linear-gradient(rgba(0,0,0,0.65),rgba(0,0,0,0.65)),
url("https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=1600");

background-size:cover;
background-position:center;
background-attachment:fixed;
}

/* Login card */
div[data-testid="column"]:nth-child(2){

background:
linear-gradient(
135deg,
rgba(255,255,255,0.18),
rgba(255,255,255,0.05)
);

backdrop-filter: blur(25px);

padding:50px;

border-radius:30px;

border:1px solid rgba(255,255,255,0.2);

box-shadow:
0px 8px 32px rgba(0,0,0,0.5);

}
/* Sign In Button */
div.stButton > button:first-child{
    background: #ff5a1f;
    color: white;
    border-radius: 30px;
    height: 50px;
    border: none;
    font-size:18px;
    font-weight:bold;
}

div.stButton > button:first-child:hover{
    background: #ff6f3d;
    color:white;
}

</style>
""", unsafe_allow_html=True)
