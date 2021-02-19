from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    # author = models.ForeignKey(settings.configure(se), on_delete=models.CASCADE)  # 다른 모델에 대한 링크
    id = models.BigAutoField(help_text="Post ID", primary_key=True)
    title = models.CharField(max_length=200)  # 글자수 제한
    text = models.TextField()  # 글자수 제한 없음
    created_date = models.DateTimeField(  # 날짜와 시간
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

'''
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
'''