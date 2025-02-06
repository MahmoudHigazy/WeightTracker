from django.db import models

class WorkoutEntry(models.Model):
    date = models.DateField()
    exercise = models.CharField(max_length=100)
    weight = models.FloatField()
    reps = models.IntegerField()
    sets = models.IntegerField()
    notes = models.TextField(blank=True)
    volume = models.FloatField()
    
    class Meta:
        ordering = ['-date']
    
    def save(self, *args, **kwargs):
        self.volume = self.weight * self.reps * self.sets
        super().save(*args, **kwargs)
