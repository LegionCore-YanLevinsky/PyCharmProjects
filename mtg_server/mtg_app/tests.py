from django.test import TestCase
from mtg_app.models import Card


class TestCard(TestCase):
    def setUp(self):
        card1 = Card(name="card one")
        card1.save()
        card2 = Card(name="card two")
        card2.save()

    def testStr(self):
        card1 = Card.objects.get(name="card one")
        card2 = Card.objects.get(name="card two")

        self.assertEqual(str(card1), 'card one')
        self.assertEqual(str(card2), 'card two')

    def testSum(self):
        card1 = Card.objects.get(name="card one")
        self.assertEqual(card1.sum(card1.name, card1.text), card1.name + " " + card1.text)
