from django.db import models
from django.core.validators import MaxValueValidator

class ProjectLists(models.Model):
    name = models.CharField(max_length=256)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class TodoItems(models.Model):
    todo_list = models.ForeignKey(ProjectLists, on_delete=models.CASCADE)
    task = models.CharField(max_length=256)
    in_detail = models.CharField(max_length=1024)
    rating_value = models.FloatField(validators=[MaxValueValidator(100.00)])
    completed = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.task
