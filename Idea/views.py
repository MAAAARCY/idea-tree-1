from django.http import Http404,HttpResponse
from django.shortcuts import render 
from . import keywords
from . import same

def index(request):
    obj = same.keep()
    obj.allclear()
    obj.flag_reset()
    return render(request, 'Idea/index.html')

def detail(request):
    try:
        obj = same.keep()
        a = request.GET.get('key')

        if a == "":
            return render(request, 'Idea/error.html')

        if a not in obj.get_ptr():
            obj.check_flag_up()

        if a not in obj.get_KeyCount():
            #obj.get_ptr() += keywords.word(a)
            obj.add_ptr(keywords.word(a))
            data = {
                'key': request.GET.get('key'),
                'data': obj.get_ptr(),
                'point': obj.get_point(),
                'flag': obj.get_flag(),
            }
            obj.KeyCount_append(a)

        else:
            data = {
                'key': request.GET.get('key'),
                'data': obj.get_ptr(),
                'point': obj.get_point(),
                'flag': obj.get_flag(),
            }

        return render(request, 'Idea/index.html', data)
    except Exception:
        return render(request, 'Idea/error.html')