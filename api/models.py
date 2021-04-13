from django.db import models


class DateTime(models.Model):
    dateTime = models.DateTimeField(null=True, blank = True)


class HistoryModel(models.Model):
    solved = models.IntegerField()
    partiallySolved = models.IntegerField()
    attemped = models.IntegerField()
    score = models.IntegerField()
    rank = models.IntegerField()
    problemsSolved = models.TextField(blank=True, null=True)
    problemPartiallySolved = models.TextField(blank=True, null=True)
    dateTime = models.ManyToManyField(DateTime)


class UserModel(models.Model):
    firstName = models.CharField(max_length = 20)
    lastName = models.CharField(max_length = 20)
    userName = models.TextField()       
    eMail = models.EmailField()
    passWord = models.TextField()
    userDetail = models.ForeignKey(HistoryModel, on_delete = models.CASCADE)

    def __str__(self):
        return self.userName
    