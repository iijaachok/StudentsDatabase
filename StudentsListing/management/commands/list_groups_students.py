from django.core.management.base import BaseCommand
from StudentsListing.models import Group
import sys


class Command(BaseCommand):
    def handle(self, *args, **options):
        groups = Group.objects.all()
        for group in groups:
            print('\nGroup "%s":\n' % group.name)

            students = group.student_set.all()
            for student in students:
                print ("%s %s" % (student.id, student.surname.encode('utf8'))) # Hack for cyrillic charmap