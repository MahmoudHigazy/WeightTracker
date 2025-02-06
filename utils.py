# Exercise categories and their respective muscle groups
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

def calculate_one_rep_max(weight, reps):
    """
    Calculate estimated one rep max using Brzycki formula
    """
    if reps == 1:
        return weight
    return weight * (36 / (37 - reps))

def calculate_volume(weight, reps, sets):
    """
    Calculate total volume (weight × reps × sets)
    """
    return weight * reps * sets