''' demoing db usage on djmicro '''
from djmicro import *
import os.path
configure(dict(
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join( os.path.dirname(__file__), 'djmicro.db3')
        }
    },

    INSTALLED_APPS= ('django.contrib.auth',
                     'django.contrib.contenttypes',
                     'django.contrib.sessions',
                     'django.contrib.sites',
                     'django.contrib.messages',
                     'web_db')

))

from django.db import models
from django.forms import ModelForm
import sys
# TODO: find a way to hide this in djmicro
# and actually make this work..
# currently the DB for Task isn't been created
sys.modules['web_db.web'] = sys.modules[__name__]
sys.modules[__name__].__name__ = 'web_db.web'

class Task(models.Model):
    title = models.CharField(max_length=255)

class TaskForm(ModelForm):
    class Meta:
        model = Task

@route(r'^$')
def index(request):
    context = dict(
        form = TaskForm(),
        tasks = Task.objects.all()
    )
    return render(request, 'db_index.html', context)

@route(r'^add$')
def add(request):
    if request.method == 'POST':
        f = TaskForm(request.POST)
        f.save()
    return redirect("/")

if __name__ == 'web_db.web':
    run()