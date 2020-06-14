# Third

from mongoengine import (
    BooleanField,
    StringField,
    IntField
)

# Apps

from apps.points.models import Point


class TestPoint:

    def setup_method(self):
        self.data = {
            'date': '2020-06-14',
            'time': '11:40:00',
            'rf':'12345678'
        }

        # Instance of Point model
        self.model = Point(**self.data)

    def test_date_field_exists(self):
        """
        Verifico se o campo date existe
        """
        assert 'date' in self.model._fields

    def test_date_field_is_required(self):
        """
        Verifico se o campo date é requirido
        """
        assert self.model._fields['date'].required is True

    def test_date_field_is_str(self):
        """
        Verifico se o campo date é do tipo string
        """
        assert isinstance(self.model._fields['date'], StringField)

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

    def test_time_field_exists(self):
        """
        Verifico se o campo time existe
        """
        assert 'time' in self.model._fields
        
    def test_time_field_is_required(self):
        """
        Verifico se o campo time é requirido
        """
        assert self.model._fields['time'].required is True

    def test_time_field_is_str(self):
        assert isinstance(self.model._fields['time'], StringField)

    def test_all_fields_in_model(self):
        """
        Verifico se todos os campos estão de fato no meu modelo
        """
        fields = [
            'rf', 'id', 'date', 'time', 'active'
        ]

        model_keys = [i for i in self.model._fields.keys()]

        fields.sort()
        model_keys.sort()

        assert fields == model_keys
