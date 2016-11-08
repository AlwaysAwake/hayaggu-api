from django.http import JsonResponse
from django.forms.models import model_to_dict

import json
import datetime

from .models import DemoInfo


def demo_list(request):
    params = request.GET

    demo_list = DemoInfo.objects.all().order_by('sdate')

    if 'start' in params:
        start = params['start']

        demo_list = demo_list.filter(sdate__gte=start)

    if 'end' in params:
        end = datetime.datetime.strptime(params['end'], '%Y-%m-%d') + datetime.timedelta(days=1)

        demo_list = demo_list.filter(sdate__lt=end)

    demo_list = list(demo_list)

    demo_list = [model_to_dict(demo) for demo in demo_list]

    return JsonResponse({'result': 1, 'demo_list': demo_list})


def demo_detail(request, demo_id):
    try:
        demo = model_to_dict(DemoInfo.objects.get(id=demo_id))

        return JsonResponse({'result': 1, 'demo': demo})

    except KeyError as e:
        return JsonResponse({"result": 0, 'message': "KeyError " + str(e)})

    except Exception as e:
        return JsonResponse({"result": 0, 'message': str(e)})
