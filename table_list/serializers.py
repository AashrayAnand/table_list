from rest_framework import serializers
from table_list.models import table_items

class tableSerializer(serializers.ModelSerializer):
    class Meta:
        model = table_items
        fields = '__all__'
        # can replace above line with fields = '__all__' as well