import unittest
import requests

class userTest(unittest.TestCase):

    # POST request to /api/user to create a new user
    def test_1_post_single_user(self):
        r = requests.post("http://localhost:5000/api/user", json = 
            {
                "bio": "test_bio",
                "dateNaissance": "12-03-1998",
                "email": "test@gmail.com",
                "feedbacks": "",
                "nom": "test_nom",
                "password_hash": "test_mdp",
                "photo": "",
                "preferences": "Sport, Culture",
                "prenom": "test_prenom",
                "role": "",
                "sexe": "Femme",
                "ville": "Grenoble"
            }
        )
        self.assertEqual(r.status_code, 201)

    # GET request to /api/user returns the details of all users
    def test_2_get_all_users(self):
        r = requests.get("http://localhost:5000/api/user")
        self.assertEqual(r.status_code, 200)