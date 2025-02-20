from django.db import models


class Theory(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='media/', null=True, blank=True)
    video_url = models.URLField(null=True, blank=True)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Theory"
        verbose_name_plural = "Theories"
