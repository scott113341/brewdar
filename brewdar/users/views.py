from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
import json

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
            return HttpResponse("device was successfully verified")
        else:
            return HttpResponse("invalid device_id and/or verification_token")

    else:
        return HttpResponse("device_id and verification_token are required")


def authenticate(request):
    email = request.POST.get('email', False)
    device_id = request.POST.get('device_id', False)
    device_name = request.POST.get('device_name', False)
    authentication_token = request.POST.get('authentication_token', False)

    print email, device_id, device_name, authentication_token

    # create or fetch user if needed
    users = User.objects.filter(email=email)
    if users.count() == 0:
        user = User(email=email)
        if user.is_valid() is True:
            user.save()
        else:
            return HttpResponse(json.dumps({
                'error': 1,
                'english': 'invalid email address'
            }), content_type="application/json")
    else:
        user = users.first()

    # create or fetch device
    devices = Device.objects.filter(device_id=device_id)
    if devices.count() == 0:
        device = Device(device_id=device_id,
                        name=device_name,
                        user=user)
        device.generate_tokens()
        if device.is_valid() is True:
            device.save()
        else:
            return HttpResponse(json.dumps({
                'error': 2,
                'english': 'invalid device parameters'
            }), content_type="application/json")
    else:
        device = devices.first()

    # make sure device is verified
    if device.verified is not True:
        return HttpResponse(json.dumps({
            'error': 3,
            'english': 'device not verified'
        }), content_type="application/json")

    # authenticate device
    if device.authentication_token == authentication_token:
        device.authenticated = True
        device.save()
        return HttpResponse(json.dumps({
            'error': 0,
            'english': 'successfully authenticated'
        }), content_type="application/json")
    else:
        return HttpResponse(json.dumps({
            'error': 4,
            'english': 'incorrect authentication token'
        }), content_type="application/json")
