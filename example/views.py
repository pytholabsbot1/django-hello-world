# example/views.py
from datetime import datetime

from django.http import HttpResponse

def index(request):
    now = datetime.now()
    html = f'''
    <html>
        <body>
            <h1>Hello from Mother fucker!</h1>
            <p>The current time is { now }.</p>
        </body>
    </html>
    '''
    return HttpResponse(html)


from django.shortcuts import render
from django.conf import settings

def home_view(request):
    context = {}
    context['title'] = 'Home Page'
    context['image'] = request.build_absolute_uri(settings.STATIC_URL + 'example/1.png')
    return render(request, 'example/index.html', context=context)