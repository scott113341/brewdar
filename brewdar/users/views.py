from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from models import User, Device


def index(request):
    template = loader.get_template('index.html')
    context = RequestContext(request, {
        'meow': 'swagmoney'
    })
    return HttpResponse(template.render(context))


def verify(request):
    device_id = request.GET.get('device_id', False)
    verification_token = request.GET.get('verification_token', False)

    if device_id is not False and verification_token is not False:
        devices = Device.objects.filter(device_id=device_id,
                                        verification_token=verification_token)
        if devices.count() == 1:
            device = devices.first()
            device.verified = True
            device.save()
            return HttpResponse(device)
        else:
            return HttpResponse("invalid device_id and/or verification_token")

    else:
        return HttpResponse("device_id and verification_token are required")


def authenticate(request):
    return HttpResponse("authenticateeeeeeeeeeeee")
