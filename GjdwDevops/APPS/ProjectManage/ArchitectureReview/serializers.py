from rest_framework import serializers
from .models import ArchitectureReviewModel, ArchitectureReviewModelDetail


class ArchitectureReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArchitectureReviewModel
        fields = '__all__'


class ArchitectureReviewModelDetailSerializers(serializers.ModelSerializer):
    pro_arc_rev = ArchitectureReviewSerializer()
    class Meta:
        model = ArchitectureReviewModelDetail
        fields = '__all__'
        # exclude = ['pub_date']

    def create(self, validated_data):
        print(validated_data)
        user_data = validated_data.pop('pro_arc_rev')

        user = ArchitectureReviewModel.objects.create(**user_data)
        account = ArchitectureReviewModelDetail.objects.create(pro_arc_rev=user, **validated_data)
        return account