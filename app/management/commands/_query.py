from django.db.models.functions import Extract
from django.db.models.functions import Concat
from django.db.models import F, Func, Value
from django.db.models import Count
from django.db.models import Avg
from app.models import *
from faker import Faker
import random

fake = Faker()


def _prepare_data():

    # for _ in range(10000):
    #     Author.objects.create(
    #         name=fake.name(),
    #         age=random.randint(20, 80)
    #     )

    # # Create 20 Publishers
    # for _ in range(10000):
    #     Publisher.objects.create(
    #         name=fake.company()
    #     )

    authors = [
        Author(name=fake.name(), age=random.randint(20, 80))
        for _ in range(10000)
    ]
    Author.objects.bulk_create(authors)

    # Bulk create 10,000 Publishers
    publishers = [
        Publisher(name=fake.company())
        for _ in range(10000)
    ]
    Publisher.objects.bulk_create(publishers)

    # Create 20 Books
    # for _ in range(20):
    #     authors_count = random.randint(1, 3)
    #     authors = random.sample(list(Author.objects.all()), authors_count)
    #     publisher = random.choice(list(Publisher.objects.all()))
    #     Book.objects.create(
    #         name=fake.text(max_nb_chars=30),
    #         pages=random.randint(100, 500),
    #         price=random.uniform(10, 50),
    #         rating=random.uniform(1, 5),
    #         pubdate=fake.date_between(start_date='-5y', end_date='today'),
    #         publisher=publisher
    #     ).authors.add(*authors)

    # # Create 20 Stores
    # for _ in range(20):
    #     books_count = random.randint(1, 5)
    #     books = random.sample(list(Book.objects.all()), books_count)
    #     Store.objects.create(
    #         name=fake.company()
    #     ).books.add(*books)

def check_query():
    books = Book.objects.annotate(day=Extract('pubdate', 'weekday'))
    return books[0].day

