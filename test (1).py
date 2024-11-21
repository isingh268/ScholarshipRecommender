import streamlit as st
import sqlite3
import hashlib
import pandas as pd

# Initialize the database
def init_db():
    conn = sqlite3.connect("scholarships_users.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                    username TEXT UNIQUE,
                    password TEXT,
                    details TEXT
                 )''')
    conn.commit()
    conn.close()

# Hash passwords securely
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Add a new user to the database
def add_user(username, password):
    conn = sqlite3.connect("scholarships_users.db")
    c = conn.cursor()
    try:
        c.execute("INSERT INTO users (username, password, details) VALUES (?, ?, ?)", 
                  (username, hash_password(password), ""))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

# Authenticate user login
def authenticate_user(username, password):
    conn = sqlite3.connect("scholarships_users.db")
    c = conn.cursor()
    c.execute("SELECT password FROM users WHERE username = ?", (username,))
    result = c.fetchone()
    conn.close()
    return result and result[0] == hash_password(password)

# Update user details in the database
def update_user_details(username, details):
    conn = sqlite3.connect("scholarships_users.db")
    c = conn.cursor()
    c.execute("UPDATE users SET details = ? WHERE username = ?", (details, username))
    conn.commit()
    conn.close()

# Retrieve user details from the database
def get_user_details(username):
    conn = sqlite3.connect("scholarships_users.db")
    c = conn.cursor()
    c.execute("SELECT details FROM users WHERE username = ?", (username,))
    result = c.fetchone()
    conn.close()
    return result[0] if result else ""

# Sample scholarship data
scholarship_data = [
    {
        "Scholarship Name": "STEM Excellence Scholarship",
        "Type": "Merit Scholarships",
        "Award Amount": "$5,000",
        "Eligibility": "STEM majors, GPA ≥ 3.5",
        "Deadline": "March 15, 2024"
    },
    {
        "Scholarship Name": "Diversity Leadership Grant",
        "Type": "Need-Based Scholarships",
        "Award Amount": "$10,000",
        "Eligibility": "Underrepresented minorities, GPA ≥ 3.0",
        "Deadline": "April 1, 2024"
    },
    {
        "Scholarship Name": "Artistic Achievement Award",
        "Type": "Artistic Scholarships",
        "Award Amount": "$3,000",
        "Eligibility": "Artistic talent, portfolio required",
        "Deadline": "February 28, 2024"
    }
]

# Main App
def main():
    st.title("Scholarship Finder Bot 🎓")
    menu = ["Home", "Login", "Sign Up", "Find Scholarships"]
    choice = st.sidebar.selectbox("Menu", menu)

    # Initialize the database
    init_db()

    if choice == "Home":
        st.subheader("Welcome to the Scholarship Finder Bot!")
        st.write("Use the sidebar to create an account, log in, or find scholarships tailored to your preferences.")

    elif choice == "Sign Up":
        st.subheader("Create a New Account")
        new_username = st.text_input("Username")
        new_password = st.text_input("Password", type="password")
        if st.button("Sign Up"):
            if new_username and new_password:
                if add_user(new_username, new_password):
                    st.success("Account created successfully! You can now log in.")
                else:
                    st.error("Username already exists. Please try a different one.")
            else:
                st.error("Please fill out all fields.")

    elif choice == "Login":
        st.subheader("Login to Your Account")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            if username and password:
                if authenticate_user(username, password):
                    st.success(f"Welcome back, {username}!")

                    # Collect scholarship preferences
                    st.subheader("📝 Basic Information")
                    name = st.text_input("What is your full name?")
                    email = st.text_input("Enter your email address:")
                    age = st.number_input("Enter your age:", min_value=0, max_value=100, value=18)
                    gender = st.selectbox("Select your gender:", ["Male", "Female", "Non-Binary", "Prefer Not to Say"])

                    st.subheader("📚 Academic Information")
                    gpa = st.slider("Enter your GPA:", 0.0, 4.0, 3.0, step=0.1)
                    major = st.text_input("Enter your academic major:")
                    school_year = st.selectbox(
                        "Select your school year:",
                        ["High School Senior", "College Freshman", "Sophomore", "Junior", "Senior", "Graduate Student"]
                    )
                    standardized_test_scores = st.number_input(
                        "Enter your SAT/ACT score (if applicable):",
                        min_value=0,
                        max_value=1600
                    )

                    st.subheader("💵 Financial and Demographic Information")
                    financial_need = st.selectbox("Do you require financial need-based scholarships?", ["Yes", "No"])
                    ethnicity = st.text_input("Enter your ethnicity (optional):")
                    residence_state = st.text_input("Enter your state of residence:")
                    physical_disabilities = st.selectbox("Do you have any physical disabilities?", ["Yes", "No"])

                    st.subheader("🎯 Preferences")
                    scholarship_type = st.multiselect(
                        "What types of scholarships are you interested in?",
                        [
                            "Merit Scholarships",
                            "Need-Based Scholarships",
                            "Federal Grants",
                            "Athletic Scholarships",
                            "Artistic Scholarships",
                            "Graduate Aid",
                            "Other"
                        ]
                    )
                    causes = st.multiselect(
                        "Select causes or values important to you (e.g., community service, sustainability, etc.):",
                        ["Community Service", "Sustainability", "Social Justice", "Diversity", "STEM", "Arts"]
                    )

                    if st.button("Save Preferences"):
                        preferences = {
                            "Name": name,
                            "Email": email,
                            "Age": age,
                            "Gender": gender,
                            "GPA": gpa,
                            "Major": major,
                            "School Year": school_year,
                            "SAT/ACT": standardized_test_scores,
                            "Financial Need": financial_need,
                            "Ethnicity": ethnicity,
                            "Residence State": residence_state,
                            "Disabilities": physical_disabilities,
                            "Scholarship Type": scholarship_type,
                            "Causes": causes
                        }
                        update_user_details(username, str(preferences))
                        st.success("Preferences saved successfully!")
                else:
                    st.error("Invalid username or password.")
            else:
                st.error("Please fill out all fields.")

    elif choice == "Find Scholarships":
        st.subheader("Find Scholarships Matching Your Preferences")
        df_scholarships = pd.DataFrame(scholarship_data)
        st.dataframe(df_scholarships, use_container_width=True)

# Correctly structured __main__ block
if __name__ == "__main__":
    main()
