from django.http import JsonResponse
from django.forms.models import model_to_dict

import json

from .models import DemoInfo

def demo_list(request):
    demo_list = list(DemoInfo.objects.all())

    demo_list = [model_to_dict(demo) for demo in demo_list]
    print(demo_list)

    return JsonResponse({'result': 1, 'demo_list': demo_list})
