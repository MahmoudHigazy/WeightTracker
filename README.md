# 💪 Weightlifting Tracker

A Streamlit-based application for tracking your weightlifting progress and visualizing your fitness journey.

## Features

- 📝 Log workout sessions with exercise details
- 📊 Visualize progress with interactive charts
- 📅 Track workout history
- 📈 Monitor weight and volume progression
- 💾 Persistent data storage with PostgreSQL
- 📱 Responsive design for desktop and mobile

## Tech Stack

- **Frontend & Backend**: Streamlit
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy
- **Data Processing**: Pandas
- **Visualization**: Plotly

## Setup Instructions

1. Ensure you have Python 3.8+ installed
2. Clone this repository
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up PostgreSQL database and configure environment variables:
   - `DATABASE_URL`: PostgreSQL connection string
   - Other database configuration (host, port, user, password, database name)

5. Run the application:
   ```bash
   streamlit run main.py
   ```

## Usage Guide

### Adding a New Workout Entry
1. Use the sidebar form to input workout details:
   - Date
   - Exercise type
   - Weight (kg)
   - Number of repetitions
   - Number of sets
   - Optional notes

2. Click "Log Exercise" to save your entry

### Viewing Progress
- Select an exercise from the dropdown to view its progress charts
- Progress is displayed in two charts:
  - Weight progression over time
  - Volume progression over time

### Recent Activity
- View your most recent workouts in the "Recent Activity" section
- Complete workout history is available in the "Exercise History" table

## Exercise Categories

The application supports tracking various exercises including:
- Bench Press (Chest)
- Squat (Legs)
- Deadlift (Back)
- Overhead Press (Shoulders)
- Barbell Row (Back)
- Pull-ups (Back)
- Dips (Chest)
- Lunges (Legs)
- Bicep Curls (Arms)
- Tricep Extensions (Arms)

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is licensed under the MIT License - see the LICENSE file for details.
