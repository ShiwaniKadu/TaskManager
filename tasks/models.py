from django.db import models


class Task(models.Model):
    STATUS_CHOICES = [
        ("NS", "Not Started"),
        ("IP", "In Progress"),
        ("C", "Completed"),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateField()
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default="NS")

    def __str__(self):
        return self.title
