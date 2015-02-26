
# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse

# Views for Students
def students_list(request):
	students = (
	{'id': 1,
	'first_name': u'Корост',
	'last_name': u'Андрій',
	'ticket': 2123,
	'image': 'img/img1.png'},
	{'id': 2,
	'first_name': u'Заєць',
	'last_name': u'Андрій',
	'ticket': 2125,
	'image': 'img/img2.png'},
    {'id': 3,
	'first_name': u'Подоба',
	'last_name': u'Віталій',
	'ticket': 2130,
	'image': 'img/img3.png'},
)
	return render(request, 'students/students_list.html',
		{'students': students})

def students_add(request):
	return HttpResponse('<h1>Student Add Form</h1>')

def students_edit(request, sid):
	return HttpResponse('<h2>Edit Student %s</h2>' % sid)

def students_delete(request, sid):
	return HttpResponse('<h1>Delete Student %s</h1>' % sid)

