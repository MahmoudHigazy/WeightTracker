from django.shortcuts import render, redirect
from django.contrib import messages
from .models import WorkoutEntry
from .forms import WorkoutEntryForm
from .utils import EXERCISE_CATEGORIES, create_progress_charts
from datetime import datetime

def home(request):
    if request.method == 'POST':
        form = WorkoutEntryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Exercise logged successfully!')
            return redirect('home')
    else:
        form = WorkoutEntryForm()
    
    # Get recent entries
    recent_entries = WorkoutEntry.objects.all()[:5]
    
    # Get all entries for history
    all_entries = WorkoutEntry.objects.all()
    
    # Create progress charts
    selected_exercise = request.GET.get('exercise', 'Bench Press')
    charts = create_progress_charts(selected_exercise)
    
    context = {
        'form': form,
        'recent_entries': recent_entries,
        'all_entries': all_entries,
        'exercise_categories': EXERCISE_CATEGORIES,
        'selected_exercise': selected_exercise,
        'charts': charts,
    }
    
    return render(request, 'tracker/home.html', context)
