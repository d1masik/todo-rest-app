from rest_framework import serializers

from todo.models import Card


class CreateTodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ('title', 'body')

    def save(self, **kwargs):
        card = Card(
            title=self.validated_data['title'],
            body=self.validated_data['body'],
            **kwargs
        )
        card.save()
        return card


class UpdateTodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ('done',)


class AllTodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = '__all__'

