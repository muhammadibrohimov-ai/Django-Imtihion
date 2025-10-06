from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=150)
    desc = models.TextField(null=True, blank=True)
    deadline = models.DateField()
    is_complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = 'ToDo'
        verbose_name_plural = 'ToDo'
        db_table = 'ToDo'


    def __str__(self):
        return f'{self.title}'
