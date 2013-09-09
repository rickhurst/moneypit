from rest_framework import serializers
from tcoapp.models import Journey


class JourneySerializer(serializers.Serializer):
    pk = serializers.Field()
    name = serializers.CharField(required=False, max_length=100)
    miles = serializers.DecimalField(max_digits=10, decimal_places=2)
    litres = serializers.DecimalField(max_digits=10, decimal_places=2)

    def restore_object(self, attrs, instance=None):

        if instance:
            instance.name = attrs.get('name', instance.name)
            instance.miles = attrs.get('miles', instance.miles)
            instance.litres = attrs.get('litres', instance.litres)
            return instance

        return Journey(**attrs)
