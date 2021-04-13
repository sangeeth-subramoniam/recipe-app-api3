from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_succesful(self):
        """ this test checks if the model succesfully \
            creates an user with email id """
        email = "sangeeth@gmail.com"
        password = "testpass123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_email_normalized_succesful(self):
        """ Tests if the email entered is normalized """

        email = "sangeeth@GMAIL.com"
        user = get_user_model().objects.create_user(email, "testpass123")

        self.assertEqual(user.email, email.lower())

    def test_empty_email_raise_error(self):
        """ test to raise error if user created with no Email """
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'testpass123')

    def test_create_super_user(self):
        """ Test to create super_user """
        user = get_user_model().objects.create_super_user(
            'sangeeth@gmail.com',
            'testpass123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
