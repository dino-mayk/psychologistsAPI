from rest_framework import serializers

from contacts.models import Address, BaseContact, Email, PhoneNumber


class BaseContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseContact
        fields = ['name', 'type']


class PhoneNumberSerializer(BaseContactSerializer):
    class Meta(BaseContactSerializer.Meta):
        model = PhoneNumber
        fields = BaseContactSerializer.Meta.fields + ['phone_number']


class AddressSerializer(BaseContactSerializer):
    class Meta(BaseContactSerializer.Meta):
        model = Address
        fields = BaseContactSerializer.Meta.fields + ['address']


class EmailSerializer(BaseContactSerializer):
    class Meta(BaseContactSerializer.Meta):
        model = Email
        fields = BaseContactSerializer.Meta.fields + ['email']
