from django.db import models
from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver


class Student(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    birthday = models.DateField()
    pass_id = models.CharField(max_length=100)
    group = models.ForeignKey('Group', null=False, blank=False)

    def __str__(self):
        return " ".join((self.name, self.middle_name, self.surname))


class Group(models.Model):
    name = models.CharField(max_length=50)
    head = models.ForeignKey(Student, related_name='group_head', null=True, blank=True)

    def __str__(self):
        return self.name


class Logger(models.Model):
    time = models.DateTimeField(auto_now=True)
    object = models.CharField(max_length=200)
    entry = models.CharField(max_length=400)

@receiver(pre_save, sender=Student)
@receiver(pre_save, sender=Group)
def on_save(sender, instance, signal, *args, **kwargs):
    logger = Logger()
    logger.object = sender
    try:
        sender.objects.get(pk=instance.pk)
        logger.entry = " modified"
    except sender.DoesNotExist:
        logger.entry = " created"

    logger.entry = 'Object {0}'.format(instance) + logger.entry
    logger.save()


@receiver(post_delete, sender=Student)
@receiver(post_delete, sender=Group)
def delete_signal(sender, instance, signal, *args, **kwargs):
    logger = Logger()
    logger.object = sender
    logger.entry =  'Object {0} deleted'.format(instance)
    logger.save()