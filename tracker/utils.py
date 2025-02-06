import plotly.graph_objects as go
from plotly.subplots import make_subplots
from .models import WorkoutEntry

# Exercise categories
EXERCISE_CATEGORIES = {
    "Bench Press": "Chest",
    "Squat": "Legs",
    "Deadlift": "Back",
    "Overhead Press": "Shoulders",
    "Barbell Row": "Back",
    "Pull-ups": "Back",
    "Dips": "Chest",
    "Lunges": "Legs",
    "Bicep Curls": "Arms",
    "Tricep Extensions": "Arms",
    "Power Clean": "Olympic",
    "Squat Clean": "Olympic",
    "Clean and Jerk": "Olympic",
    "Squat Clean and Jerk": "Olympic"
}

def create_progress_charts(exercise):
    """Create progress visualization for selected exercise"""
    entries = WorkoutEntry.objects.filter(exercise=exercise).order_by('date')
    
    if not entries:
        return None
    
    fig = make_subplots(
        rows=2, cols=1,
        subplot_titles=('Weight Progress', 'Volume Progress'),
        vertical_spacing=0.15
    )
    
    dates = [entry.date for entry in entries]
    weights = [entry.weight for entry in entries]
    volumes = [entry.volume for entry in entries]
    
    # Weight progress
    fig.add_trace(
        go.Scatter(
            x=dates,
            y=weights,
            mode='lines+markers',
            name='Weight (kg)',
            line=dict(color='#FF4B4B')
        ),
        row=1, col=1
    )
    
    # Volume progress
    fig.add_trace(
        go.Scatter(
            x=dates,
            y=volumes,
            mode='lines+markers',
            name='Volume (kg)',
            line=dict(color='#1f77b4')
        ),
        row=2, col=1
    )
    
    fig.update_layout(
        height=600,
        showlegend=True,
        title_text=f"{exercise} Progress Over Time",
        hovermode='x unified',
        template='plotly_white'
    )
    
    return fig.to_html()
