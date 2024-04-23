from django.db import models


#Imports from other apps
from apps.users.models import User

# Create your models here.
class Project(models.Model):
    owner = models.ForeignKey(User, on_delete = models.DO_NOTHING , null=True)
    name = models.CharField(max_length = 60 , null = False, blank = False)
    init_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()


    def __str__(self) -> str:
        return self.name


class Task(models.Model):
    description = models.CharField(max_length =250)
    end_date = models.DateTimeField()
    project = models.ForeignKey(Project, on_delete = models.DO_NOTHING)
    is_complete = models.BooleanField(default=False)
    # user = models.ForeignKey(User, on_delete = models.DO_NOTHING, null=True)


class Comment(models.Model):
    init_date = models.DateTimeField()
    content = models.CharField(max_length = 120)
    task = models.ForeignKey(Task, on_delete = models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete = models.DO_NOTHING)



class Member(models.Model):
    
    ROLES = (
        ("DEV", "DEVELOPER"),
        ("MAS", "SCRUM MASTER"),
        ("PRO", "PRODUCT OWNER"),
    )
    
    date_joined = models.DateField(null=True)
    role = models.CharField(max_length=3,choices=ROLES,default="DEV")
    project = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING)



class OwnersTasks (models.Model):
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    task = models.ForeignKey(Task,on_delete=models.DO_NOTHING)
