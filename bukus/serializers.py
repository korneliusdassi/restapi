from rest_framework import serializers
from bukus.models import Bukus, LANGUAGE_CHOICE, STYLE_CHOISE

class BukusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bukus
        field = ['id','judul','deskripsi','harga','rating','code','lineos','style']