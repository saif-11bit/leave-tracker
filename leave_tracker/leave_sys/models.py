from django.db import models
import datetime



class Staff(models.Model):
    staff = models.CharField(max_length=100)

    def __str__(self):
        return self.staff


class LeaveType(models.Model):
    leave_type = models.CharField(max_length=100)

    def __str__(self):
        return self.leave_type


class Leave(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    leave_type = models.ForeignKey(LeaveType, on_delete=models.CASCADE)
    from_date = models.DateField(default=datetime.datetime.today)
    to_date = models.DateField(default=datetime.datetime.today)
    team_email = models.CharField(max_length=100)
    reason = models.TextField()

    def __str__(self):
        return self.staff



class Holiday(models.Model):
    name = models.CharField(max_length=100)
    from_date = models.DateField(default=datetime.datetime.today)
    to_date = models.DateField(default=datetime.datetime.today)
    applicable = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name
