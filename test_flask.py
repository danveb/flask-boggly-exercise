from unittest import TestCase

from app import app
from models import db, User

# test database 
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly_test' 
# test db
app.config['SQLALCHEMY_ECHO'] = False
app.config['TESTING'] = True
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar'] 

db.drop_all()
db.create_all() 

class UserTestCase(TestCase):
    """Tests User Class"""

    def setUp(self):
        User.query.delete() 
        user = User(first_name="Daniel", last_name="Parker", image_url='https://cdn.vox-cdn.com/thumbor/G_w4Nyo9IJx5q5xa5E92vJCVyUQ=/21x0:539x345/1200x800/filters:focal(21x0:539x345)/cdn.vox-cdn.com/assets/3727699/Dogecoin_logo.png')
        db.session.add(user)
        db.session.commit()
        self.user_id = user.id 
    
    def tearDown(self):
        db.session.rollback() 

    def test_users_list(self):
        with app.test_client() as client:
            res = client.get('/users')
            html = res.get_data(as_text=True)
            self.assertEqual(res.status_code, 200)
            self.assertIn('<h1>Users</h1>', html)
            self.assertIn('Daniel Parker', html)
        
    def test_new_user(self):
        with app.test_client() as client:
            res = client.get('/users/new')
            html = res.get_data(as_text=True)
            self.assertEqual(res.status_code, 200)
            self.assertIn('<h1>Create a user</h1>', html)