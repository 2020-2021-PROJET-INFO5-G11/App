import unittest
import requests

class userTest(unittest.TestCase):
    API_URL = "http://localhost:5000/api"
    USERS_URL = "{}/user".format(API_URL)
    USER_OBJ = {
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

    def _get_each_user_url(self, id):
        return "{}/{}".format(userTest.USERS_URL, id)

    # POST request to /api/user to create a new user
    def test_1_post_single_user(self):
        r = requests.post(userTest.USERS_URL, json = userTest.USER_OBJ)
        self.assertEqual(r.status_code, 201)

    # GET request to /api/user returns the details of all users
    def test_2_get_all_users(self):
        r = requests.get(userTest.USERS_URL)
        self.assertEqual(r.status_code, 200)

    # GET request to /api/user returns the details of a single user
    def test_3_get_single_user(self):
        r = requests.get(self._get_each_user_url(1))
        self.assertEqual(r.status_code, 200)

    # GET request to /api/user trying to get non existing user --> shouldn't work
    def test_4_get_non_existing_user(self):
        r = requests.get(self._get_each_user_url(509))
        self.assertEqual(r.status_code, 404)

    # PUT request to /api/user to update a user
    def test_5_update_user(self):
        r = requests.put(self._get_each_user_url(2), json = 
            {
                "bio": "test_update",
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
