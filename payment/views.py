import time

import firebase_admin
from django.http import (HttpResponse, HttpResponseBadRequest,
                         HttpResponseForbidden, HttpResponseNotAllowed,
                         HttpResponseNotFound, HttpResponseServerError)
from django.shortcuts import render
from firebase_admin import auth, credentials
# Create your views here.
from src.helpers.requestData import getRequestData

from src.firebase.authentication.auth import Authentication

if not firebase_admin._apps:
    cred = credentials.Certificate("secrets/ssspay-app-firebase-adminsdk-ikh7t-54b01b08b1.json")
    firebase_admin.initialize_app(cred)

authHandler = Authentication(auth)

@authHandler.verifyToken
def uptimeHandler(request,verified = False):
    print(request)
    dataType = {
        'authId':{
            'type':'string', 
            'value':'SD&*F^*SD^Fsd6f78^ff89sd7f8&DSf',
        },
        'authToken':{
            'type':'string',
            'value':'fds9sd7f987dsf987dsf987sd9f87sd98f79sd8f'
        }
    }
    try:
        requestData = getRequestData(request,dataType)
        if (verifyToken(requestData['FORMED_DATA']['token'],requestData['FORMED_DATA']['uid'])):
            return HttpResponse('Running since ' + time.ctime(time.time()))
        else:
            return HttpResponseForbidden('Token is not valid')
    except Exception as e:
        return HttpResponseBadRequest(str(e))
