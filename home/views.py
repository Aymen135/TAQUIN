from ast import Try
from django.shortcuts import render
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
# from .Aiscript import Taquin
from . import Aiscript




def index(request):

    response = json.dumps([{}])
    return HttpResponse(response, content_type="text/json")


@csrf_exempt
def resolve(request):
    if(request.method == "POST"):
        br = []
        data = json.loads(request.body)
        n = data["n"]
        for i in range(n):
            l = []
            for j in range(n):
                l.append(int(data["data"]["a"+str(i)+str(j)]))
            br.append(l)
        
        # Aiscript.END=Aiscript.makegoal(br)
        if(n==4):
            Aiscript.END=[[1,2,3,4], [ 5,6,7,8], [9,10,11,12],[13,14,15,0]]
        b = Aiscript.main(br,n)
        response = json.dumps([{'table': b}])
    return HttpResponse(response,status=200)
