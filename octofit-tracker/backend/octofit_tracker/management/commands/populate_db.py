from django.core.management.base import BaseCommand
from octofit_tracker.test_data import test_data
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        # Populate users
        for user_data in test_data['users']:
            User.objects.create_user(**user_data)

        # Populate teams
        for team_data in test_data['teams']:
            Team.objects.create(**team_data)

        # Populate activities
        for activity_data in test_data['activities']:
            Activity.objects.create(**activity_data)

        # Populate leaderboard
        for leaderboard_data in test_data['leaderboard']:
            user = User.objects.get(username=leaderboard_data['user'])
            Leaderboard.objects.create(user=user, points=leaderboard_data['points'])

        # Populate workouts
        for workout_data in test_data['workouts']:
            activity = Activity.objects.get(name=workout_data['activity'])
            Workout.objects.create(name=workout_data['name'], duration_minutes=workout_data['duration_minutes'], activity=activity)

        self.stdout.write(self.style.SUCCESS('Database populated with test data.'))