# File: tests/test_sales.py

import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
from backend.database.config import Base
from backend.models.sales import Sales
from datetime import date

class TestSalesModel(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(cls.engine)
        cls.Session = sessionmaker(bind=cls.engine)

    def setUp(self):
        self.session = self.Session()

    def tearDown(self):
        self.session.rollback()
        self.session.close()

    def test_create_sales_record(self):
        sale = Sales(date=date(2023, 1, 1), amount=100.0, category='Electronics', product_id=1)
        self.session.add(sale)
        self.session.commit()
        self.assertIsNotNone(sale.id)

    def test_create_sales_record_null_date(self):
        sale = Sales(date=None, amount=100.0, category='Electronics', product_id=1)
        self.session.add(sale)
        with self.assertRaises(IntegrityError):
            self.session.commit()
        self.session.rollback()

    def test_create_sales_record_null_amount(self):
        sale = Sales(date=date(2023, 1, 1), amount=None, category='Electronics', product_id=1)
        self.session.add(sale)
        with self.assertRaises(IntegrityError):
            self.session.commit()
        self.session.rollback()

    def test_create_sales_record_null_category(self):
        sale = Sales(date=date(2023, 1, 1), amount=100.0, category=None, product_id=1)
        self.session.add(sale)
        with self.assertRaises(IntegrityError):
            self.session.commit()
        self.session.rollback()

    def test_create_sales_record_null_product_id(self):
        sale = Sales(date=date(2023, 1, 1), amount=100.0, category='Electronics', product_id=None)
        self.session.add(sale)
        with self.assertRaises(IntegrityError):
            self.session.commit()
        self.session.rollback()

    def test_create_sales_record_boundary_amount(self):
        sale = Sales(date=date(2023, 1, 1), amount=0.0, category='Electronics', product_id=1)
        self.session.add(sale)
        self.session.commit()
        self.assertIsNotNone(sale.id)

    def test_create_sales_record_negative_amount(self):
        sale = Sales(date=date(2023, 1, 1), amount=-100.0, category='Electronics', product_id=1)
        self.session.add(sale)
        self.session.commit()
        self.assertIsNotNone(sale.id)

    def test_create_sales_record_large_amount(self):
        sale = Sales(date=date(2023, 1, 1), amount=1e6, category='Electronics', product_id=1)
        self.session.add(sale)
        self.session.commit()
        self.assertIsNotNone(sale.id)

if __name__ == '__main__':
    unittest.main()
