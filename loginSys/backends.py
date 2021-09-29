from django.contrib.auth.backends import BaseBackend
from loginSys.models import MyUser

class EmailAuthBackEnd(BaseBackend):
    def authenticate(self, request, username, password):
        try:
            user = MyUser.objects.filter(email=username).first()
            if user.check_password(password) and getattr(user, "is_active"):
                return user
        except MyUser.DoesNotExist:
            pass
        return None

    def get_user(self, user_id):
        try:
            return MyUser.objects.get(pk=user_id)
        except MyUser.DoesNotExist:
            return None