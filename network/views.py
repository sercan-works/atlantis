import time
from django.shortcuts import render
# from network.ping_ip import ping_ip
import ping3

       

def ping_page(request):
    ip_address = '104.160.143.212'  
    response = ping3.ping(ip_address, unit='ms') *1
    return render(request, 'network/index.html', {'response': int(response)})
    