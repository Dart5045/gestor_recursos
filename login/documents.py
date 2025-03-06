# documents.py
from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from django.contrib.auth.models import User
from datetime import datetime

@registry.register_document
class UserDocument(Document):
    last_login_attempt = fields.DateField(attr='last_login_attempt', null=True)
    login_success = fields.BooleanField(attr='login_success', null=True)
    ip_address = fields.KeywordField(attr='ip_address', null=True)

    class Index:
        name = 'user_logins'  # Nombre del índice en Elasticsearch

    class Django:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
        ]
