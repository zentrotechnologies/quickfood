from django.shortcuts import render, redirect, HttpResponse
import requests
import json
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from helpers.validations import hosturl
# API URLs
login_url = hosturl + "/api/User/login"
logout_url = hosturl + "/api/User/logout"
from rest_framework.response import Response

# Trip API URLs

def landing_page(request):
    """Landing page with state-wise destination filtering"""
    # Get states with the most destinations

    context = {
    }
    
    return render(request, 'Home/landing.html', context)
