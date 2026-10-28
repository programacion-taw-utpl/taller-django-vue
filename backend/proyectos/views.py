from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Proyecto
from .serializers import ProyectoSerializer


@api_view(["GET"])
def listar_proyectos(request):

    proyectos = Proyecto.objects.all()

    serializer = ProyectoSerializer(
        proyectos,
        many=True
    )

    return Response(serializer.data)
