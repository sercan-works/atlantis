import threading
import time
from django.shortcuts import render
# from network.ping_ip import ping_ip
import ping3

from django.views.decorators import gzip
from django.http import StreamingHttpResponse


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

@gzip.gzip_page
def camera(request):
    ...

# class VideoCamera(object):
#     def __init__(self):
#        self.video = cv2.VideoCapture("rtsp://wowzaec2demo.streamlock.net/vod/mp4:BigBuckBunny_115k.mp4")
#        (self.grabbed , self.frame) = self.video.read()
#        threading.Thread(target=self.update , args=()).start()
    
    
#     def __del__(self):
#        self.video.release()

#     def get_frame(self):
#        image = self.frame 
#        _ , jpeg = cv2.imencode(' .jpg' , image)
#        return jpeg.tobytes()

#     def update(self):
#        while True:
#            (self.grabbed , self.frame) = self.video.read()