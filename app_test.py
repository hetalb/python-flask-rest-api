from app import app
import unittest

class FlaskTest(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass
    
    def setUp(self):
        self.app = app.test_client()
        
    def tearDown(self): 
        pass        
        
    def test_index_return_code(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)

    def test_index_content(self):
        result = self.app.get('/')
        self.assertIn('Hello', result.data.decode('utf-8'))

    def test_api_return_code(self):
        result = self.app.get('/api')
        self.assertEqual(result.status_code, 200)

    def test_api_content(self):
        result = self.app.get('/api')
        self.assertIn('city', result.data.decode('utf-8'))

    def test_pagenot_found(self):
        result = self.app.get('/missing-page')
        self.assertEqual(result.status_code, 404)

# runs the unit tests in the module
if __name__ == '__main__':
    unittest.main()