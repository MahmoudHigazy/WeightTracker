import pandas as pd
import streamlit as st
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, Float, String, Date, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Database setup
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)
Base = declarative_base()
Session = sessionmaker(bind=engine)

class WorkoutEntry(Base):
    __tablename__ = 'workout_entries'

    id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False)
    exercise = Column(String, nullable=False)
    weight = Column(Float, nullable=False)
    reps = Column(Integer, nullable=False)
    sets = Column(Integer, nullable=False)
    notes = Column(String)
    volume = Column(Float, nullable=False)

# Create tables
Base.metadata.create_all(engine)

def load_or_create_data():
    """
    Load existing data from database
    """
    session = Session()
    entries = session.query(WorkoutEntry).all()
    session.close()

    if not entries:
        return pd.DataFrame(
            columns=['date', 'exercise', 'weight', 'reps', 'sets', 'notes', 'volume']
        )

    data = [{
        'date': entry.date,
        'exercise': entry.exercise,
        'weight': entry.weight,
        'reps': entry.reps,
        'sets': entry.sets,
        'notes': entry.notes,
        'volume': entry.volume
    } for entry in entries]

    return pd.DataFrame(data)

def add_entry(df, date, exercise, weight, reps, sets, notes=""):
    """
    Add new workout entry to database
    """
    volume = weight * reps * sets

    session = Session()
    new_entry = WorkoutEntry(
        date=date,
        exercise=exercise,
        weight=weight,
        reps=reps,
        sets=sets,
        notes=notes,
        volume=volume
    )

    session.add(new_entry)
    session.commit()
    session.close()

    # Update session state with new data
    st.session_state.workout_data = load_or_create_data()

def get_recent_entries(df, n=5):
    """
    Get n most recent entries from database
    """
    session = Session()
    entries = session.query(WorkoutEntry)\
        .order_by(WorkoutEntry.date.desc())\
        .limit(n)\
        .all()
    session.close()

    if not entries:
        return pd.DataFrame()

    data = [{
        'date': entry.date,
        'exercise': entry.exercise,
        'weight': entry.weight,
        'reps': entry.reps,
        'sets': entry.sets,
        'notes': entry.notes,
        'volume': entry.volume
    } for entry in entries]

    return pd.DataFrame(data)

def get_exercise_history(df, exercise):
    """
    Get history for specific exercise from database
    """
    session = Session()
    entries = session.query(WorkoutEntry)\
        .filter(WorkoutEntry.exercise == exercise)\
        .order_by(WorkoutEntry.date)\
        .all()
    session.close()

    if not entries:
        return pd.DataFrame()

    data = [{
        'date': entry.date,
        'exercise': entry.exercise,
        'weight': entry.weight,
        'reps': entry.reps,
        'sets': entry.sets,
        'notes': entry.notes,
        'volume': entry.volume
    } for entry in entries]

    return pd.DataFrame(data)