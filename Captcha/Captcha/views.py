from rest_framework.views import APIView
from django.http.response import HttpResponse
import os
from django.shortcuts import render
from .CaptchaGenerator import Captcha
from uuid import uuid4
from django.core.cache import cache
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIR = os.path.join(BASE_DIR, 'assets/templates/')


class CaptchaGenerate(APIView):
    def get(self, request):

        captcha_instance = Captcha()
        resp = captcha_instance.generate_captcha()

        uid = uuid4()
        results = cache.get('results', {})
        results["{}".format(uid)] = resp.get("answer")
        cache.set("results", results, None)
        return render(request, 'captcha.html', {'img': resp.get('data'), 'uuid': uid})


class CaptchaVerify(APIView):
    def post(self, request):
        try:
            if "uid" not in request.data or "ans" not in request.data:
                raise Exception("Key Missing")

            uid = request.data["uid"]
            ans = request.data["ans"]
            results = cache.get('results', {})

            if uid not in results:
                raise Exception("UID not Present")

            if results[uid] != ans:
                raise Exception("Invalid Captcha")

            return HttpResponse(json.dumps({"success": True}), content_type="application/json")

        except Exception:
            return HttpResponse(json.dumps({"success": False}), content_type="application/json")