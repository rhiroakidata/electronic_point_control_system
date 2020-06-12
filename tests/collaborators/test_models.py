# Third

from mongoengine import (
    BooleanField,
    StringField,
    IntField
)

# Apps

from apps.collaborators.models import Collaborator


class TestCollaborator:

    def setup_method(self):
        self.data = {
            'email': 'teste1@pontotel.com',
            'password': 'teste123',
            'name': 'Teste',
            'cpf': '1234567890',
            'rf':'12345678'
        }

        # Instance of Collaborator model
        self.model = Collaborator(**self.data)

    def test_email_field_exists(self):
        """
        Verifico se o campo email existe
        """
        assert 'email' in self.model._fields

    def test_email_field_is_required(self):
        """
        Verifico se o campo email é requirido
        """
        assert self.model._fields['email'].required is True

    def test_email_field_is_unique(self):
        """
        Verifico se o campo email é unico
        """
        assert self.model._fields['email'].unique is True

    def test_email_field_is_str(self):
        """
        Verifico se o campo email é do tipo string
        """
        assert isinstance(self.model._fields['email'], StringField)

    def test_rf_field_exists(self):
        """
        Verifico se o campo rf existe
        """
        assert 'rf' in self.model._fields

    def test_rf_field_is_required(self):
        """
        Verifico se o campo rf é requirido
        """
        assert self.model._fields['rf'].required is True
        
    def test_rf_field_is_int(self):
        """
        Verifico se o campo rf é do tipo int
        """
        assert isinstance(self.model._fields['rf'], IntField)

    def test_name_field_exists(self):
        """
        Verifico se o campo name existe
        """
        assert 'name' in self.model._fields

    def test_name_field_is_str(self):
        assert isinstance(self.model._fields['name'], StringField)

    def test_all_fields_in_model(self):
        """
        Verifico se todos os campos estão de fato no meu modelo
        """
        fields = [
            'rf', 'cpf', 'created', 'email',
            'name', 'id', 'password', 'active'
        ]

        model_keys = [i for i in self.model._fields.keys()]

        fields.sort()
        model_keys.sort()

        assert fields == model_keys
