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

    INSTALLED_APPS= ('tasks',)

))

from tasks.models import Task, TaskForm

@route(r'^$')
def index(request):
    context = dict(
        form = TaskForm(),
        tasks = Task.objects.all()
    )
    return render(request, 'db_index.html', context)

@route(r'^add/$')
def add(request):
    if request.method == 'POST':
        f = TaskForm(request.POST)
        f.save()
    return redirect("/")

if __name__ == '__main__':
    run()