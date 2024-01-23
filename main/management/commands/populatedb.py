from django.core.management.base import BaseCommand
from main.models import Category, Product


class Command(BaseCommand):
    help = 'Populate the database with sample data'

    def handle(self, *args, **options):
        # очистка данных
        Category.objects.all().delete()
        Product.objects.all().delete()

        category1 = Category.objects.create(name='Category 1', description='Description 1')
        category2 = Category.objects.create(name='Category 2', description='Description 2')
        Product.objects.create(name='Product 1', description='Description 1', category=category1, price=19.99)
        Product.objects.create(name='Product 2', description='Description 2', category=category2, price=29.99)

        self.stdout.write(self.style.SUCCESS('Database successfully populated'))
