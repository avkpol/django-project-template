# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
<<<<<<< HEAD
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger
from ..models import Group
def groups_list(request):
    groups = Group.objects.all()
	# try to order group list
    order_by= request.GET.get('order_by', '')
    if order_by in ('title','leader'):
		groups= groups.order_by(order_by)
		if request.GET.get('reverse','') == '1':
			groups=groups.reverse()
	# paginate groups
    paginator = Paginator(groups, 3)
    page = request.GET.get('page')
    try:
		groups = paginator.page(page)
    except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		groups = paginator.page(1)
    except EmptyPage:
		# If page is out of range (e.g. 9999), deliver
		# last page of results.
		groups = paginator.page(paginator.num_pages)
=======

# Views for Groups
def groups_list(request):
    groups = (
        {'id': 1,
         'name': u'Мтм-1',
         'leader': {'id': 1, 'name': u'Тарас Мельник'}},
        {'id': 2,
         'name': u'Мтм-22',
         'leader': {'id': 2, 'name': u'Микола Садовський'}},
    )
>>>>>>> a83d2d578620aae3f409aba2a4e17a0ec48f0334
    return render(request, 'students/groups_list.html',
        {'groups': groups})

def groups_add(request):
    return HttpResponse('<h1>Group Add Form</h1>')

def groups_edit(request, gid):
    return HttpResponse('<h1>Edit Group %s</h1>' % gid)

def groups_delete(request, gid):
    return HttpResponse('<h1>Delete Group %s</h1>' % gid)
<<<<<<< HEAD
=======

>>>>>>> a83d2d578620aae3f409aba2a4e17a0ec48f0334
