# -*- coding: utf-8 -*-
"""Calendar

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1VlGGRnsVYbNbdMLltot-v_T_SInijzjW
"""

import streamlit as st
import pandas as pd
from datetime import datetime
import calendar

# Sample dataframe for testing
data = {
    "Scholarship Name": [
        "Kuru Footsteps to Your Future Scholarship",
        "Alert1 Students for Seniors Scholarship",
        "Blankstyle Scholarship Opportunity #1",
        "Innovation In Education Scholarship",
        "The Bert & Phyllis Lamb Prize in Political Science",
        "New Beginnings Immigrant Scholarship",
    ],
    "Date Due": [
        "2024-12-20",
        "2025-01-10",
        "2024-12-31",
        "2024-10-15",
        "2025-02-14",
        "2024-10-18",
    ],
    "Summary": [
        "Amount: $1,000. Deadline: December 20, 2024.",
        "Amount: $500. Deadline: January 10, 2025.",
        "Amount: $1,000. Deadline: December 31, 2024.",
        "Amount: $500 each month. Deadline: 15th of each month.",
        "This prize is awarded for excellence in Political Science. Deadline: February 14, 2025.",
        "Supports immigrant students. Deadline: October 18, 2024.",
    ],
}

# Create DataFrame
df = pd.DataFrame(data)
df["Date Due"] = pd.to_datetime(df["Date Due"])

# Function to create calendar data
def generate_calendar_events(df):
    events = {}
    for _, row in df.iterrows():
        date = row["Date Due"]
        events[date] = f"{row['Scholarship Name']}\n{row['Summary']}"
    return events

# Initialize Streamlit app
st.title("Scholarship Calendar")
st.sidebar.header("Filter Scholarships")

# Sidebar filters
min_date = st.sidebar.date_input("Start Date", value=datetime(2024, 1, 1))
max_date = st.sidebar.date_input("End Date", value=datetime(2025, 12, 31))

# Filter DataFrame based on date
filtered_df = df[(df["Date Due"] >= pd.Timestamp(min_date)) & (df["Date Due"] <= pd.Timestamp(max_date))]

# Generate calendar events
calendar_events = generate_calendar_events(filtered_df)

# Display the calendar
st.subheader("Scholarship Due Dates")
current_year, current_month = datetime.now().year, datetime.now().month

# Allow users to change the displayed month
selected_year = st.sidebar.selectbox("Select Year", range(2024, 2026), index=0)
selected_month = st.sidebar.selectbox(
    "Select Month",
    list(calendar.month_name)[1:],
    index=current_month - 1,
)

# Generate calendar for the selected month
st.write(f"### {selected_month} {selected_year}")
month_days = calendar.Calendar().monthdayscalendar(selected_year, list(calendar.month_name).index(selected_month))

for week in month_days:
    week_display = []
    for day in week:
        if day == 0:
            week_display.append("")
        else:
            date_key = datetime(selected_year, list(calendar.month_name).index(selected_month), day)
            event = calendar_events.get(date_key, "")
            week_display.append(f"{day}\n\n{event}" if event else day)
    st.write(" | ".join([str(item) if item else " " for item in week_display]))

# Display the filtered scholarships
st.subheader("Scholarship Details")
if not filtered_df.empty:
    st.write(filtered_df)
else:
    st.write("No scholarships available for the selected date range.")