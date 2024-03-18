from django.db import models

# Create your models here.
class LessonsModel(models.Model):
    title = models.CharField(max_length=200, verbose_name="Lesson Title")
    img = models.ImageField(verbose_name="Lesson image")


    def __str__(self) -> str:
        return f"{self.pk} {self.title}"