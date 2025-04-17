
from rest_framework import serializers
from .models import Project, Unit, ProjectMedia, UnitMedia

class ProjectMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectMedia
        fields = ['id', 'image']


class UnitMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnitMedia
        fields = ['id', 'image']


class UnitSerializer(serializers.ModelSerializer):
    media_unit = UnitMediaSerializer(many=True, read_only=True)

    class Meta:
        model = Unit
        fields = ['id', 'project', 'type', 'bedrooms_count', 'area_min', 'area_max', 'is_fully_finished', 'price', 'media_unit','whatsapp','phone']


class ProjectSerializer(serializers.ModelSerializer):
    units = UnitSerializer(many=True, read_only=True)
    media_project = ProjectMediaSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ['id', 'name', 'location', 'description', 'starting_price', 'down_payment_percent', 'installment_years', 'whatsapp', 'media_project', 'units']
