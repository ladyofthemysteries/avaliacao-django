from dataclasses import field
from rest_framework.serializers import ModelSerializer
from .models import Cidade, Estado

# componente de software que converte dados complexos, como objetos ou estruturas de dados, em algum formato que pode ser facilmente transmitido ou armazenado e, posteriormente, reconstruído

class CidadeSerializer(ModelSerializer):
    class Meta:
        model = Cidade
        fields = '__all__'

# queremos uma representação mais simples dos dados, como em uma lista de dicionários ou uma lista de strings
# serializers permitem a transformação eficiente de objetos complexos, como modelos de banco de dados Django, em formatos facilmente transmitidos pela web, como JSON

class EstadoSerializer(ModelSerializer):
    cidades = CidadeSerializer(many = True, read_only = True)
    class Meta:
        model = Estado
        fields = ['id', 'nome', 'sigla', 'cidades']

# são querysets ou instâncias da classe criada no Model, que podemos definir como uma representação da consulta ao banco de dados no Django em formato de objetos complexos.

