from django.test import TestCase
from .models import Machine

test = Machine.objects.values_list('category', flat=True).distinct().exclude(category__isnull=True)

print(test)

# Create your tests here.
