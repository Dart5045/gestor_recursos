from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from django.contrib.auth.models import User

@registry.register_document
class UserDocument(Document):
    last_login_attempt = fields.DateField(null=True)  # Quitamos attr, porque no existe en el modelo
    login_success = fields.BooleanField(null=True)
    ip_address = fields.KeywordField(null=True)

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