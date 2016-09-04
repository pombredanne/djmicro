''' demoing star import on djmicro '''
from djmicro import *
configure()

@route(r'^$')
def hello(request):
    return render(request, 'index.html', {})

if __name__ == '__main__':
    run()