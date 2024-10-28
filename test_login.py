import unittest
from app import app, db, User
from flask import session
from werkzeug.security import generate_password_hash

class LoginTestCase(unittest.TestCase):
    def setUp(self):
        # Create an application context
        self.app = app.test_client()
        self.app_context = app.app_context()
        self.app_context.push()

        # Set up the database for testing
        db.create_all()

        # Create a sample user for testing
        hashed_password = generate_password_hash('testpassword')  # Use default hashing method
        user = User(username='testuser', password_hash=hashed_password)
        db.session.add(user)
        db.session.commit()

    def tearDown(self):
        # Tear down the database and app context after each test
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_successful_login(self):
        # Test login with correct credentials
        response = self.app.post('/login', data={
            'username': 'testuser',
            'password': 'testpassword'
        })
        self.assertEqual(response.status_code, 302)  # Check for redirect after successful login
        with self.app.session_transaction() as session:
            self.assertEqual(session['username'], 'testuser')  # Ensure session is set

    def test_invalid_login(self):
        # Test login with invalid credentials
        response = self.app.post('/login', data={
            'username': 'wronguser',
            'password': 'wrongpassword'
        })
        self.assertIn(b'Invalid username or password', response.data)

    def test_deleted_user_login(self):
        # Simulate login with a deleted account
        user = User.query.filter_by(username='testuser').first()
        db.session.delete(user)
        db.session.commit()

        response = self.app.post('/login', data={
            'username': 'testuser',
            'password': 'testpassword'
        })
        self.assertIn(b'This account has been deleted', response.data)

if __name__ == '__main__':
    unittest.main()
