import time
from django.shortcuts import render
# from network.ping_ip import ping_ip
import ping3

IP_ADDRESS = {
    "lol":'185.40.65.1'
}
data = {
    "lol":0,
    "valorant":0,
}# initial values yazılacak bu değeler sayfaya gönderielcek:
def ping_page(request):
    ip_address = '104.160.143.212'  
    response = ping3.ping(ip_address, unit='ms') * 1
    return render(request, 'network/index.html', {'response': int(response)})
    