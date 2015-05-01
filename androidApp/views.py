from django.contrib.auth.models import User
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt

try:
    from django.http import JsonResponse
except:
    from django.utils import simplejson
    from django.http import HttpResponse
 
    class JsonResponse(HttpResponse):

        def __init__(self, content, mimetype='application/json', status=None, content_type=None):
             super(JsonResponse, self).__init__(
                 content=simplejson.dumps(content),
                 mimetype=mimetype,
                 status=status,
                 content_type=content_type,
                   )

@csrf_exempt
def login(request):
    username=request.POST['username']
    password=request.POST['password']
    user=User.objects.filter(username=username)[0]


    if user.check_password(password):
        return HttpResponse(user.profile.user_type)
    else:
        return HttpResponse('false username or password')

def get_diagnose_file(request):


    return JsonResponse({"Saam":2})



        
