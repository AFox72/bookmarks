from django.contrib.auth.models import User
from account.models import Profile

class EmailAuthBackend:

    def authenticate(self, request, username=None, password=None):
        try:
            user = User.object.get(email=username)
            if user.check_password(password):
                return user
            return None
        except (User.DoesNotExist, User.MultipleObjectsReturned):
            return None

        def get_user(self, user_id):
            try:
                return User.objects.get(pk=user_id)
            except User.DoesNotExist:
                return None

def create_profile(backends, user, *args, **kwargs):
    Profile.objects.get_or_create(user=user)