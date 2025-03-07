from django.db import models
from django.utils.timezone import now
from datetime import datetime  # Import for date conversion

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=100, null=True, blank=True)
    due_date = models.DateField(blank=False)
    status = models.CharField(max_length=20, default='Pending')

    def save(self, *args, **kwargs):
        today = now().date()

        # Convert due_date to a date object if it's a string
        if isinstance(self.due_date, str):
            self.due_date = datetime.strptime(self.due_date, "%Y-%m-%d").date()

        if self.due_date < today:
            self.status = "Overdue"
        elif self.due_date == today:
            self.status = "Due Today"
        else:
            self.status = "Upcoming"

        super().save(*args, **kwargs)
