from django.test import TestCase
from expense.models import Expense


class ExpenseModelTest(TestCase):
    '''
    Test suite for Expense model
    '''
    def setUp(self):
        '''
        Create a expense instance for testing
        '''
        Expense.objects.create(
            id=1,
            date="2020-01-01",
            expense_type="Food",
            amount=10.00,
        )

    def tearDown(self):
        '''
        Delete expense instance after testing
        '''
        Expense.objects.all().delete()

    def test_expense_type(self):
        ''' Test expense type '''
        expense = Expense.objects.get(id=1)
        self.assertEqual(expense.expense_type, 'Food')

    def test_expense_amount(self):
        ''' Test expense amount '''
        expense = Expense.objects.get(id=1)
        self.assertEqual(expense.amount, 10.00)
