
# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
<<<<<<< HEAD
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger
from ..models import Student


# Views for Students
def students_list(request):
	students = Student.objects.all()

  # try to order students list
	order_by= request.GET.get('order_by', '')
	if order_by in ('student_id','last_name','first_name','ticket'):
		students= students.order_by(order_by)
		if request.GET.get('reverse','') == '1':
			students=students.reverse()
	# paginate students
	paginator = Paginator(students, 5)
	page = request.GET.get('page')
	try:
		students = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		students = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver
		# last page of results.
		students = paginator.page(paginator.num_pages)

=======

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
>>>>>>> a83d2d578620aae3f409aba2a4e17a0ec48f0334
	return render(request, 'students/students_list.html',
		{'students': students})

def students_add(request):
	return HttpResponse('<h1>Student Add Form</h1>')

def students_edit(request, sid):
	return HttpResponse('<h2>Edit Student %s</h2>' % sid)

def students_delete(request, sid):
	return HttpResponse('<h1>Delete Student %s</h1>' % sid)

