from rest_framework.generics import CreateAPIView,ListAPIView
from django.contrib.auth.models import User
from studentcity.models import Agent
from .serializers import RegisterSerializer, StaffCheckSerializer
from rest_framework.response import Response

class RegisterAPI(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
   
    
    def post(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)
      
        serializer.is_valid(raise_exception=True)
        serializer.save(request)
        return Response (
            {
                "message" : "Kullanıcı oluşturuldu.",
                "data": serializer.data
                
            }
        )

class StaffCheckView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = StaffCheckSerializer

    def list(self, request, *args, **kwargs):
        serializer = StaffCheckSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        is_staff = User.objects.get(username=request.user).is_staff
        is_superuser = User.objects.get(username = request.user).is_superuser
        agent = Agent.objects.filter(author=request.user.id).first()
    
        if agent:
            return Response(
            {   
                "user": request.user.email,
                "is_agent": True,
                "is_staff": is_staff,
                "is_superuser":is_superuser,
            }
        )
        else:
            return Response({
                "user": request.user.email,
                "is_agent": False,
                "is_staff": is_staff,
                "is_superuser":is_superuser,
            })
        
        
        

        # return Response(
        #     {
        #         "is_agent": agent.name,
        #         "is_staff": is_staff,
        #     }
        # )


