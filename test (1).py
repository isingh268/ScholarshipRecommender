import streamlit as st
import pandas as pd

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
    st.markdown(
        """
        Welcome to the Scholarship Finder Bot!  
        Enter your details below, and we'll help you find scholarships that match your profile and preferences.
        """
    )

    # Section 1: Basic Information
    st.header("📝 Basic Information")
    name = st.text_input("What is your full name?")
    email = st.text_input("Enter your email address:")
    age = st.number_input("Enter your age:", min_value=0, max_value=100, value=18)
    gender = st.selectbox("Select your gender:", ["Male", "Female", "Non-Binary", "Prefer Not to Say"])

    # Section 2: Academic Information
    st.header("📚 Academic Information")
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

    # Section 3: Financial and Demographic Information
    st.header("💵 Financial and Demographic Information")
    financial_need = st.selectbox("Do you require financial need-based scholarships?", ["Yes", "No"])
    ethnicity = st.text_input("Enter your ethnicity (optional):")
    residence_state = st.text_input("Enter your state of residence:")
    physical_disabilities = st.selectbox("Do you have any physical disabilities?", ["Yes", "No"])

    # Section 4: Preferences
    st.header("🎯 Preferences")
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

    # Section 5: Submit Button
    if st.button("Find Scholarships"):
        st.success("Your preferences have been recorded. Matching scholarships are displayed below!")
        
        # Display sample scholarships (can be extended to filter based on user input)
        st.header("🎓 Matching Scholarships")
        df_scholarships = pd.DataFrame(scholarship_data)
        st.dataframe(df_scholarships, use_container_width=True)

# Correctly structured __main__ block
if __name__ == "__main__":
    main()
