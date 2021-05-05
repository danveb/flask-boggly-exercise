from unittest import TestCase

from app import app
from models import db, User

# test database 
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly_test' 
# test db
app.config['SQLALCHEMY_ECHO'] = False

db.drop_all()
db.create_all() 

class UserModelTestCase(TestCase):
    """Tests for model for Users"""

    def setUp(self):
        """Clear database"""
        User.query.delete()

    def tearDown(self):
        """Clear any fouled transaction"""
        db.session.rollback() 
    
    def test_first_name(self):
        user = User(first_name="Daniel")
        self.assertEqual(user.first_name, "Daniel")
    
    def test_last_name(self):
        user = User(last_name="Doe")
        self.assertEqual(user.last_name, "Doe")

        user = User(last_name="Johnson")
        self.assertEqual(user.last_name, "Johnson")