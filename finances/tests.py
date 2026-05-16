from django.test import TestCase
from .models import Transaction


class TransactionModelTest(TestCase):

    def test_create_transaction(self):
        transaction = Transaction.objects.create(
            title="Salary",
            amount=1000,
            transaction_type="Income",
            description="Monthly Salary"
        )

        self.assertEqual(transaction.title, "Salary")
