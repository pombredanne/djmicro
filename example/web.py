import djmicro
djmicro.configure()

@djmicro.route(r'^$')
def hello(request):
    return djmicro.render(request, 'index.html', {})

@djmicro.route(r'^test/(\d+)/$')
def test(request, id):
    return djmicro.render(request, 'test.html', {'id': id})

if __name__ == '__main__':
    djmicro.run()