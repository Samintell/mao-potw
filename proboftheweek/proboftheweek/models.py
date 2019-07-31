from django.db import models


class Question(models.Model):
    question_text = models.TextField(max_length=1000)
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    active_date = models.DateField()
    answer = models.CharField(max_length=25)
    answer_explaination = models.TextField(max_length=1000)
    def __str__(self):
        return self.question_text + " : " + str(self.active_date.month) + "/" + str(self.active_date.day)

class Response(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    student_id = models.CharField(max_length=8)
    answer_text = models.CharField(max_length=25)
    time = models.DateTimeField('time answered', auto_now_add=True)
    def __str__(self):
        return str(self.id) + ":" + self.answer_text + " | " + time.strftime("%d-%b-%Y (%H:%M:%S.%f)")
    # str function prob needs to be fixed. specifically self.time


    