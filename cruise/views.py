from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from users.models import User
from django.core.paginator import Paginator
from django.contrib import messages
from django.conf import settings
import json
from django.views.decorators.csrf import csrf_exempt

def initial(request):
   
    context = {
		'title': 'About',
		# 'click':run(),
	}
    return render(request,'ecom/index_tobe.html',context)




