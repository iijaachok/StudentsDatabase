from django.test import TestCase
from django.contrib.auth.models import User
from django.test.client import Client
from datetime import date
import unittest
from StudentsListing.models import Student, Group

# Create your tests here.
class TestCase(unittest.TestCase):
    username = 'non_existing_name'
    email = 'nonexisiting@for.sure'
    password = 'test123'

    def setUp(self):
        test_user = User.objects.create_user(self.username, self.email, self.password)
        self.assertTrue(test_user)
        print('User %s was created' % self.username)

    def test_login_and_create_student_in_group(self):
        self.client = Client()
        login = self.client.login(username=self.username, password=self.password)

        self.assertTrue(login)
        print('User %s has logged in' % self.username)

        group = Group.objects.create(name='test_group')
        group = Group.objects.get(name='test_group')

        self.assertTrue(group)
        print('Group %s was created' % group.name)

        student = Student.objects.create(name='student_test',
                                         surname='student_surname',
                                         middle_name='student_midname',
                                         birthday=date.today(),
                                         pass_id='rtyewq',
                                         group=group)
        student = Student.objects.get(surname='student_surname')
        self.assertTrue(student)

        student = Student.objects.get(pass_id='rtyewq')
        self.assertTrue(student)

        print('Student %s was created' % student.surname)

        self.assertTrue(student in group.student_set.all())
        print('Student %s is in group %s' % (student.surname, student.group.name))

        group.delete()
        student.delete()

    def tearDown(self):
        User.objects.get(username=self.username).delete()