from rest_framework import serializers

from job.models import joboffer


class joboffer_serializer(serializers.ModelSerializer):
    class Meta:
        model =  joboffer
        fields =  '__all__'

    