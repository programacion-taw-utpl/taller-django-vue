from rest_framework import serializers
from .models import Proyecto


class ProyectoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Proyecto

        fields = [
            "id",
            "titulo",
            "responsable",
            "descripcion",
            "estado",
            "fecha_creacion"
        ]

        read_only_fields = [
            "id",
            "fecha_creacion"
        ]
