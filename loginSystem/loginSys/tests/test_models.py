from django.test import TestCase
from loginSys.models import MyUser 

class TestModels(TestCase):

    def setUp(self):
        self.user_1 = MyUser.objects.create(username='andre', first_name='Andre')
        self.user_1.set_password('dias1234567')
        self.user_1.save()

    def test_user_exists(self):
        user = MyUser.objects.get(pk=1)
        self.assertEquals(MyUser.objects.count(), 1)
        self.assertEquals(user.first_name, 'Andre')

    def test_add_user(self):
        user_2 = MyUser.objects.create(
            username='ElizeuCarlos', 
            email="eli@gmail.com",
            first_name="elizeu",
            last_name="carlos"
            )

        user_2.set_password("elizeu12345")
        user_2.save()
        self.assertEquals(MyUser.objects.count(), 2)
        self.assertIsInstance(user_2, MyUser)
        self.assertEquals(user_2.email, "eli@gmail.com")
        self.assertEquals(user_2.first_name, "Elizeu")
        self.assertEquals(user_2.last_name, "Carlos")
        self.assertEquals(user_2.is_staff, False)
