# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render_to_response

def search_form(requset):
    return render_to_response('search_form.html')# render to response 表示 直接使用模板作为HTTP_response 返回
def search(request):
    request.encoding ='utf-8'
    if 'q' in request.GET:
        message = 'the content you request is ' + request.GET['q']
    else:
        message = 'empty form'
    return HttpResponse(message)