import streamlit as st
import pandas as pd
from datetime import datetime
import utils
import data_manager
import visualization

# Page config
st.set_page_config(
    page_title="Weightlifting Tracker",
    page_icon="💪",
    layout="wide"
)

# Initialize session state
if 'workout_data' not in st.session_state:
    st.session_state.workout_data = data_manager.load_or_create_data()

# App title
st.title("💪 Weightlifting Tracker")

# Sidebar
st.sidebar.header("Add New Entry")

# Exercise input form
with st.sidebar.form("exercise_form"):
    date = st.date_input("Date", datetime.now())
    
    exercise = st.selectbox(
        "Exercise",
        options=utils.EXERCISE_CATEGORIES.keys()
    )
    
    weight = st.number_input(
        "Weight (kg)",
        min_value=0.0,
        max_value=500.0,
        step=0.5
    )
    
    reps = st.number_input(
        "Repetitions",
        min_value=1,
        max_value=100,
        step=1
    )
    
    sets = st.number_input(
        "Sets",
        min_value=1,
        max_value=20,
        step=1
    )
    
    notes = st.text_area("Notes (optional)")
    
    submitted = st.form_submit_button("Log Exercise")
    
    if submitted:
        data_manager.add_entry(
            st.session_state.workout_data,
            date,
            exercise,
            weight,
            reps,
            sets,
            notes
        )
        st.sidebar.success("Exercise logged successfully!")

# Main content area
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("Progress Charts")
    
    # Exercise selector for charts
    selected_exercise = st.selectbox(
        "Select Exercise to Visualize",
        options=utils.EXERCISE_CATEGORIES.keys(),
        key="chart_exercise"
    )
    
    # Display progress charts
    fig = visualization.create_progress_chart(
        st.session_state.workout_data,
        selected_exercise
    )
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("Recent Activity")
    recent_data = data_manager.get_recent_entries(st.session_state.workout_data, 5)
    if not recent_data.empty:
        st.dataframe(
            recent_data[['date', 'exercise', 'weight', 'reps', 'sets']],
            hide_index=True
        )
    else:
        st.info("No workout data available. Start logging your exercises!")

# Exercise History
st.subheader("Exercise History")
if not st.session_state.workout_data.empty:
    st.dataframe(
        st.session_state.workout_data.sort_values('date', ascending=False),
        hide_index=True
    )
else:
    st.info("No workout history available yet.")
