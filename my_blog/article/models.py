#coding=utf-8
#Python默认是以ASCII作为编码方式的，如果在自己的Python源码中包含了中文（或者其他非英语系的语言），此时即使你把自己编写的Python源文件以UTF-8格式保存了，但实际上，这依然是不行的。解决方法见
from django.db import models

# Create your models here.
class Article(models.Model):
	title = models.CharField(max_length = 100) #博客题目
	#CharField 储存字符串
	category = models.CharField(max_length = 50,blank = True) #博客标签
	date_time = models.DateTimeField(auto_now_add = True) #博客日期
	#DateTimeField 储存时间 auto_now_add = True 表示自动设置对象增加时间
	content = models.TextField(blank = True,null = True) #博客文章正文
	#TextField 储存大量文本

	#python3使用__str__
	def __unicode__(self):
		return self.title