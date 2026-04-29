from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        Leaderboard.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='DC', description='DC Superheroes')

        # Users
        users = [
            User.objects.create(email='ironman@marvel.com', name='Iron Man', team=marvel.name),
            User.objects.create(email='captain@marvel.com', name='Captain America', team=marvel.name),
            User.objects.create(email='spiderman@marvel.com', name='Spider-Man', team=marvel.name),
            User.objects.create(email='batman@dc.com', name='Batman', team=dc.name),
            User.objects.create(email='superman@dc.com', name='Superman', team=dc.name),
            User.objects.create(email='wonderwoman@dc.com', name='Wonder Woman', team=dc.name),
        ]

        # Workouts
        workouts = [
            Workout.objects.create(name='Pushups', description='Upper body strength', suggested_for='Marvel'),
            Workout.objects.create(name='Running', description='Cardio', suggested_for='DC'),
        ]

        # Activities
        Activity.objects.create(user=users[0], type='Pushups', duration=30, date=timezone.now().date())
        Activity.objects.create(user=users[3], type='Running', duration=45, date=timezone.now().date())
        Activity.objects.create(user=users[1], type='Pushups', duration=20, date=timezone.now().date())
        Activity.objects.create(user=users[4], type='Running', duration=60, date=timezone.now().date())

        # Leaderboard
        Leaderboard.objects.create(user=users[0], score=100)
        Leaderboard.objects.create(user=users[3], score=120)
        Leaderboard.objects.create(user=users[1], score=90)
        Leaderboard.objects.create(user=users[4], score=110)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
