from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'precio', 'modelo', 'marca', 'códigodeproducto', 'stock', 'nombre', 'fecha')
        read_only_fields = ('fecha',)
