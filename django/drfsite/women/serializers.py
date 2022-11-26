from rest_framework import serializers

from .models import *


class WomenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Women
        fields = ('pk', 'title', 'content', 'cat', )
    
    # def create(self, validated_data):
    #     return Women.objects.create(**validated_data)
    
    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.content = validated_data.get('content', instance.content)
    #     instance.updated = validated_data.get('updated', instance.updated)
    #     instance.is_pub = validated_data.get('is_pub', instance.is_pub)
    #     instance.cat_id = validated_data.get('cat_id', instance.cat_id)
    #     instance.save()
    #     return instance