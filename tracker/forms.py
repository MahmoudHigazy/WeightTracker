from django import forms
from .models import WorkoutEntry
from .utils import EXERCISE_CATEGORIES

class WorkoutEntryForm(forms.ModelForm):
    exercise = forms.ChoiceField(
        choices=[(k, k) for k in EXERCISE_CATEGORIES.keys()]
    )
    
    class Meta:
        model = WorkoutEntry
        fields = ['date', 'exercise', 'weight', 'reps', 'sets', 'notes']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'notes': forms.Textarea(attrs={'rows': 3}),
        }
