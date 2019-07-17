from django.db import models

# Create your models here.

from django.db import models
 
# Create your models here.
class Information(models.Model):
 
    title = models.CharField('新闻标题',max_length=100)
    number = models.CharField('点击量排名',max_length=32)
    clicks = models.CharField('点击量',max_length=32)
    time = models.CharField('时间',max_length=32)
    participate = models.CharField('参与人数',max_length=32)
    comment_num = models.CharField('评论人数',max_length=32)
    comment = models.TextField('评论内容')
    created = models.DateTimeField('发布时间',auto_now_add=True)
 
    def __str__(self):
        return self.title
