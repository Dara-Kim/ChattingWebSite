import json
import os

from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def index(request):
    return render(request, "chat/index.html")

def login(req):
    if req.is_ajax and req.method == "POST":
        data = json.loads(req.body)
        user_id = data.get("user_id")
        pw = data.get("pw")

        with open("./chat/db/idpw.json", 'r') as jsonfile:
            idpw = json.load(jsonfile)

            if user_id in idpw:
                if idpw[user_id] == pw:
                    return JsonResponse({"stat": 1})
            else:
                return JsonResponse({"stat": 0})

        return JsonResponse({"stat": 0})
    else:
        return render(req, "chat/login.html")