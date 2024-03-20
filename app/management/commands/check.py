from django.http import HttpResponse
from django.core.management.base import BaseCommand, CommandError
from ._query import check_query, _prepare_data
from app.models import Author
from rest_framework import serializers
from django.http import HttpResponse, JsonResponse


class Command(BaseCommand):
    help = "Closes the specified poll for voting"

    def handle(self, *args, **options):
        print(check_query())
        # print(auther_api_list())
        self.stdout.write(self.style.SUCCESS('Query Executed successfully'))


def auther_api_list(request):
    print("Hello")
    quey_set = Author.objects.order_by('id')[50:]
    seializer = AuthorSerializer(quey_set, many=True)
    return JsonResponse(data={"data": seializer.data})


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('name', 'age')
