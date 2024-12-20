# -*- coding: utf-8 -*-
"""Scholarship Finder App

Enhanced Scholarship Finder application with improved design and user experience.
"""

import streamlit as st

# Set page configuration
st.set_page_config(page_title="Scholarship Finder Bot", page_icon="🎓", layout="wide")

def main():
    # App Title and Introduction
    st.title("🎓 Scholarship Finder Bot")
    st.markdown(
        """
        Welcome to the **Scholarship Finder Bot**!  
        Fill out the sections below to find scholarships tailored to your profile and preferences.  
        Let's make your scholarship search easier and more effective!
        """
    )
    st.sidebar.image("https://via.placeholder.com/150", caption="Scholarship Finder", use_column_width=True)

    # Section 1: Basic Information
    st.header("📝 Basic Information")
    with st.form("basic_info"):
        name = st.text_input("Full Name", placeholder="Enter your full name")
        email = st.text_input("Email Address", placeholder="Enter your email address")
        age = st.number_input("Age", min_value=13, max_value=100, value=18)
        gender = st.selectbox("Gender", ["Male", "Female", "Non-Binary", "Prefer Not to Say"])
        submitted_basic_info = st.form_submit_button("Save Basic Information")

    if submitted_basic_info:
        st.success(f"Thank you, {name}! Your basic information is saved.")

    # Section 2: Academic Information
    st.header("📚 Academic Information")
    with st.form("academic_info"):
        gpa = st.slider("GPA", 0.0, 4.0, 3.0, step=0.1)
        major = st.text_input("Academic Major", placeholder="Enter your academic major")
        school_year = st.selectbox(
            "School Year",
            [
                "High School Senior",
                "College Freshman",
                "Sophomore",
                "Junior",
                "Senior",
                "Graduate Student",
            ],
        )
        standardized_test_scores = st.number_input(
            "SAT/ACT Score (optional)", min_value=0, max_value=1600, value=1200
        )
        submitted_academic_info = st.form_submit_button("Save Academic Information")

    if submitted_academic_info:
        st.success("Your academic information has been saved.")

    # Section 3: Financial and Demographic Information
    st.header("💵 Financial and Demographic Information")
    with st.form("financial_info"):
        financial_need = st.radio("Do you require need-based scholarships?", ["Yes", "No"])
        ethnicity = st.text_input("Ethnicity (optional)", placeholder="Enter your ethnicity")
        residence_state = st.text_input("State of Residence", placeholder="Enter your state")
        physical_disabilities = st.radio("Do you have any physical disabilities?", ["Yes", "No"])
        submitted_financial_info = st.form_submit_button("Save Financial Information")

    if submitted_financial_info:
        st.success("Your financial and demographic information has been saved.")

    # Section 4: Preferences
    st.header("🎯 Preferences")
    with st.form("preferences"):
        scholarship_type = st.multiselect(
            "Types of Scholarships",
            [
                "Merit Scholarships",
                "Need-Based Scholarships",
                "Federal Grants",
                "Athletic Scholarships",
                "Artistic Scholarships",
                "Graduate Aid",
                "Other",
            ],
        )
        causes = st.multiselect(
            "Causes or Values Important to You",
            ["Community Service", "Sustainability", "Social Justice", "Diversity", "STEM", "Arts"],
        )
        submitted_preferences = st.form_submit_button("Save Preferences")

    if submitted_preferences:
        st.success("Your scholarship preferences have been saved.")

    # Section 5: Scholarship Matching
    st.header("🔍 Find Scholarships")
    if st.button("Find Scholarships"):
        st.info("Searching for scholarships...")
        # Mock Results
        st.success("Here are your matching scholarships!")
        st.markdown(
            """
            - **Scholarship A**: $5,000 (Merit-based)
            - **Scholarship B**: $2,500 (Community Service)
            - **Scholarship C**: Full Ride (Need-based for STEM majors)
            """
        )


# Correctly structured __main__ block
if __name__ == "__main__":
    main()
