from django import template
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render
import json
import requests
import os

def send_request(request, page):
    domain = request.META['HTTP_HOST']
    # strip www
    if domain.startswith('www.'):
        domain = domain[4:]
    #if domain == '127.0.0.1:8000': domain = 'ronindevelopment.com' # development address
    # url setup
    url = "https://api.bumbol.com/hosting/{}".format(page)
    # api key
    headers = {"x-api-key": os.environ['x_api_key']}
    # include domain in request
    params = {"domain": domain}
    # send request
    r = requests.get(url, headers=headers, params=params)
    if r.status_code == 200:
        data = r.json()
        try: # check response for error
            data["company"] #company is returned on all requests
        except:
            raise Http404
        return data
    else:
        raise Http404

def build_page(request, page):
    # Api Address
    data = send_request(request, page)
    data["bucket"] = "https://s3.amazonaws.com/bumbol"
    #output = json.dumps(data, indent=2)
    #print(output)
    data["display_page"] = data["page"]
    return render(request, 'home.html', data)
    
def build_projects_page(request, page):
    # send request
    data = send_request(request, page)
    data["bucket"] = "https://s3.amazonaws.com/bumbol"
    data["display_page"] = "projects_index"
    #output = json.dumps(data, indent=2)
    #print(output)
    return render(request, 'projects.html', data)
    
def build_category_page(request, slug):
    page = 'category/' + slug
    # send request
    data = send_request(request, page)
    data["bucket"] = "https://s3.amazonaws.com/bumbol"
    data["display_page"] = "project_category"
    #output = json.dumps(data, indent=2)
    #print(output)
    return render(request, 'projects.html', data)
    
def build_gallery_page(request, gallery_id):
    page = 'gallery/' + gallery_id
    # send request
    data = send_request(request, page)
    data["bucket"] = "https://s3.amazonaws.com/bumbol"
    data["display_page"] = "project_gallery"
    #output = json.dumps(data, indent=2)
    #print(output)
    return render(request, 'projects.html', data)

def send_bid_page_request(request, page):
    domain = request.META["HTTP_HOST"]
    token = request.GET.get("token", "")
    # strip www
    if domain.startswith('www.'):
        domain = domain[4:]
    # url setup
    url = "https://api.bumbol.com/app/bids/profiles/landing-page"
    # api key
    headers = {"x-api-key": os.environ['x_api_key']}
    # include domain in request
    params = {"domain": domain, "url":page, "token":token}
    # send request
    r = requests.get(url, headers=headers, params=params)
    if r.status_code == 200:
        data = r.json()
        #try: # check response for error
        #    data["bid_profile_id"] #company is returned on all requests
        #except:
        #    raise Http404
        return data
    else:
        raise Http404

# Bid Landing Page
def build_bid_page(request, page):
    # send request
    data = send_bid_page_request(request, page)
    data["bucket"] = "https://s3.amazonaws.com/bumbol"
    data["display_page"] = "bid_profile"
    #output = json.dumps(data, indent=2)
    #print(output)
    return render(request, 'bids.html', data)