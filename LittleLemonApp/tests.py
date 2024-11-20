from django.test import TestCase
from .models import Menu
from .serializers import MenuSerializer

# Create your tests here.
class MenuModelTest(TestCase):
  def test_creation(self):
    item = Menu.objects.create(title="IceCream", price=80, inventory=100)
    self.assertEqual(item.title, "IceCream")
    self.assertEqual(item.price, 80)
    self.assertEqual(item.inventory, 100)
    
class MenuViewTest(TestCase):
  def setUp(self):
    self.greekSalad = Menu.objects.create(
      title="GreekSalad", price=9.99, inventory=50
    )
    self.grilledFish = Menu.objects.create(
      title="GrilledFish", price=14.99, inventory=30
    )
    
  def test_all(self):
    menuItems = Menu.objects.all()
    serializer = MenuSerializer(menuItems, many=True)
    expectedResponse = [
      {
        'id': self.greekSalad.id,
        'title': 'GreekSalad',
        'price': '9.99',
        'inventory': 50,
      },
      {
        'id': self.grilledFish.id,
        'title': 'GrilledFish',
        'price': '14.99',
        'inventory': 30,
      },
    ]
    self.assertEqual(serializer.data, expectedResponse)