from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200) # 글자수 200자 제한
    text = models.TextField() # 글자 수 제한이 없음
    created_data = models.DateTimeField( # 날짜와 시간
                default=timezone.now)
    published_data = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_data = timezone.now()
        self.save()

    def __str__(self):
        return self.title
