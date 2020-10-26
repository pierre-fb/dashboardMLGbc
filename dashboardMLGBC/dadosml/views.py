from django.shortcuts import render
from rest_framework import viewsets
from .models import Dadosml
from .serializers import DadosMLSerializer

# Create your views here.
class DadosMLViewSet(viewsets.ModelViewSet):
    queryset = Dadosml.objects.all()
    serializer_class = DadosMLSerializer

def indexPage (request):
    context = {'a':'a'}
    return render(request,'index.html',context)