import pandas as pd
import streamlit as st
from datetime import datetime

def load_or_create_data():
    """
    Load existing data or create new DataFrame
    """
    try:
        return pd.read_csv('workout_data.csv', parse_dates=['date'])
    except FileNotFoundError:
        return pd.DataFrame(
            columns=['date', 'exercise', 'weight', 'reps', 'sets', 'notes', 'volume']
        )

def save_data(df):
    """
    Save DataFrame to CSV
    """
    df.to_csv('workout_data.csv', index=False)

def add_entry(df, date, exercise, weight, reps, sets, notes=""):
    """
    Add new workout entry to DataFrame
    """
    volume = weight * reps * sets
    
    new_entry = pd.DataFrame([{
        'date': date,
        'exercise': exercise,
        'weight': weight,
        'reps': reps,
        'sets': sets,
        'notes': notes,
        'volume': volume
    }])
    
    updated_df = pd.concat([df, new_entry], ignore_index=True)
    save_data(updated_df)
    st.session_state.workout_data = updated_df

def get_recent_entries(df, n=5):
    """
    Get n most recent entries
    """
    return df.sort_values('date', ascending=False).head(n)

def get_exercise_history(df, exercise):
    """
    Get history for specific exercise
    """
    return df[df['exercise'] == exercise].sort_values('date')
