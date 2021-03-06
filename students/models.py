# -*- coding: utf-8 -*-
from django.db import models
# Create your models here.
<<<<<<< HEAD
class Student(models.Model):
	#Student Model
	class Meta(object):
		verbose_name = u"Студент"
		verbose_name_plural = u"Студенти"
 
	student_id=models.CharField(
		max_length=256,
		blank=False,
		verbose_name=u"№")
	first_name = models.CharField(
		max_length=256,
		blank=False,
		verbose_name=u"Ім'я")
	last_name = models.CharField(
		max_length=256,
		blank=False,
		verbose_name=u"Прізвище")
	birthday = models.DateField(
		blank=False,
		verbose_name=u"Дата народження",
		null=True)
	photo = models.ImageField(
		blank=True,
		verbose_name=u"Фото",
		null=True)
	ticket = models.CharField(
		max_length=256,
		blank=False,
		verbose_name=u"Білет")
	student_group = models.ForeignKey('Group',
        verbose_name=u"Група",
        blank=False,
        null=True,
        on_delete=models.PROTECT)
	notes = models.TextField(
		blank=True,
		verbose_name=u"Додаткові нотатки")
	def __unicode__(self):
		return u"%s %s" % (self.first_name, self.last_name)

	#Groups Model
class Group(models.Model):
	class Meta(object):
		verbose_name = u"Група"
		verbose_name_plural = u"Групи"
	title =models.CharField(
		max_length=256,
		blank=False,
		verbose_name=u"Назва")
	leader = models.OneToOneField('Student',
		verbose_name=u"Староста",
		blank=True,
		null=True,
		on_delete=models.SET_NULL)
	notes = models.TextField(
		blank=True,
		verbose_name=u"Додаткові нотатки")
	def __unicode__(self):
		if self.leader:
			return u"%s(%s %s)" % (self.title, self.leader.first_name, self.leader.last_name)
		else:
			return u"%s" % (self.title,)







=======
	#Student Model
class Student(models.Model):
    def __unicode__(self):
	    return u"%s %s" % (self.first_name, self.last_name)
    class Meta(object):
		verbose_name = u"Студент"
		verbose_name_plural = u"Студенти"
    first_name = models.CharField(
		max_length=256,
		blank=False,
		verbose_name=u"Ім'я")
    last_name = models.CharField(
		max_length=256,
		blank=False,
		verbose_name=u"Прізвище")
    birthday = models.DateField(
		blank=False,
		verbose_name=u"Дата народження",
		null=True)
    photo = models.ImageField(
		blank=True,
		verbose_name=u"Фото",
		null=True)
    ticket = models.CharField(
		max_length=256,
		blank=False,
		verbose_name=u"Білет")
    notes = models.TextField(
		blank=True,
		verbose_name=u"Додаткові нотатки")
>>>>>>> a83d2d578620aae3f409aba2a4e17a0ec48f0334
