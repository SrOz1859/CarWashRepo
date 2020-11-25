from rest_framework import serializers
from myCar.models import Insumos

class InsumosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insumos
        fields = ["nombre","precio","descripcion","stock"]# "__all__"
        