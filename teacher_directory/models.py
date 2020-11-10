from django.db import models
from django.urls import reverse

class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='images/') 
    email_address = models.EmailField(unique=True)
    phone_number = models.IntegerField()
    room_number = models.CharField(max_length=3)

    def __str__(self):
        return self.first_name + " " + self.last_name + "\n(" + self.email_address + ")"

class Subjects(models.Model):
    subject = models.CharField(max_length=100)
    teacher = models.ForeignKey(to=Teacher, on_delete=models.CASCADE)
    
    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if Teacher.objects.get(email_address=self.teacher.email_address).subjects_set.count() < 5:
            super(Subjects, self).save()
        else:
            raise Exception(f'{self.teacher} not allowed to add')
    
    def __str__(self):
        return self.teacher.email_address + " - " + self.subject 





