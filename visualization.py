import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd

def create_progress_chart(df, exercise):
    """
    Create progress visualization for selected exercise
    """
    if df.empty:
        return go.Figure()

    exercise_data = df[df['exercise'] == exercise].sort_values('date')
    
    if exercise_data.empty:
        return go.Figure()

    fig = make_subplots(
        rows=2, cols=1,
        subplot_titles=('Weight Progress', 'Volume Progress'),
        vertical_spacing=0.15
    )

    # Weight progress
    fig.add_trace(
        go.Scatter(
            x=exercise_data['date'],
            y=exercise_data['weight'],
            mode='lines+markers',
            name='Weight (kg)',
            line=dict(color='#FF4B4B')
        ),
        row=1, col=1
    )

    # Volume progress
    fig.add_trace(
        go.Scatter(
            x=exercise_data['date'],
            y=exercise_data['volume'],
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

    fig.update_xaxes(title_text="Date", row=2, col=1)
    fig.update_yaxes(title_text="Weight (kg)", row=1, col=1)
    fig.update_yaxes(title_text="Volume (kg)", row=2, col=1)

    return fig
