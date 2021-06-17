from web.services import cep_service
from rest_framework import serializers
from web.models import Diarista
import json

def listar_diaristas_cidade(cep):
    codigo_ibge = buscar_cidade_cep(cep)['ibge']
    try:
        diaristas = Diarista.objects.filter(codigo_ibge=codigo_ibge).order_by('id')
        return diaristas
    except Diarista.DoesNotExist:
        return []

def buscar_cidade_cep(cep):
    response = cep_service.buscar_cidade_cep(cep)
    if response.status_code == 400:
        raise serializers.ValidationError("o CEP informado está incorreto")
    cidade_api = json.loads(response.content)
    if 'erro' in cidade_api:
        raise serializers.ValidationError("CEP não encontrado")
    return cidade_api