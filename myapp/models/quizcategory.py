from django.db import models


class QuizCategory(models.Model):
    title = models.CharField(max_length=100)
    detail = models.TextField()
    image = models.ImageField(upload_to='media/')

    class Meta:
        verbose_name_plural = "Categories"


    def __str__(self):
        return self.title


