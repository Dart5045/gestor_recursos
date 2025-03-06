from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from .models import Resource  # Asegúrate de que este modelo existe

@registry.register_document
class RecursoDocument(Document):
    class Index:
        name = 'gestor_recursos'  # Nombre del índice en Elasticsearch

    class Django:
        model = Resource
        fields = [
            'name',
            'description',
            'available',
        ]