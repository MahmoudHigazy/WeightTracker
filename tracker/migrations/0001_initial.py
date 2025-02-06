from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='WorkoutEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('exercise', models.CharField(max_length=100)),
                ('weight', models.FloatField()),
                ('reps', models.IntegerField()),
                ('sets', models.IntegerField()),
                ('notes', models.TextField(blank=True)),
                ('volume', models.FloatField()),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
