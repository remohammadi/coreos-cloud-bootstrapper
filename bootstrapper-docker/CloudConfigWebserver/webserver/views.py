from django.shortcuts import render

from . import get_version

def home(request):
    context = {'version': get_version()}
    return render(request, 'index.html', context)

def pxe_cloud_config(request):
    ip = request.META.get('REMOTE_ADDR')
    node_num = ip.split('.')[3];
    context = {
        'private_ip': ip,
        'public_ip': ip,
        'node_num' : node_num,
    }
    return render(request, 'pxe-cloud-config.yml', context,
                  content_type="text/yaml")
