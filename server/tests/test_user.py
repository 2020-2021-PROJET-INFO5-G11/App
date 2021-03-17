import unittest
import requests

class userTest(unittest.TestCase):
    API_URL = "http://localhost:5000/api"
    USERS_URL = "{}/user".format(API_URL)
    USER_LOGIN_URL = "{}/login".format(USERS_URL)
    USER_LOGOUT_URL = "{}/logout".format(USERS_URL)
    USER_CURRENT_URL = "{}/current".format(USERS_URL)
    USER_MODIFY_PASSWORD_URL = "{}/change_pwd".format(USER_CURRENT_URL)
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
    USER_OBJ_BIS = {
                "bio": "test_bio",
                "dateNaissance": "12-03-1998",
                "email": "test2@gmail.com",
                "feedbacks": "",
                "nom": "test_nom2",
                "password_hash": "test2_mdp",
                "photo": "",
                "preferences": "Sport, Culture",
                "prenom": "test_prenom2",
                "role": "",
                "sexe": "Femme",
                "ville": "Grenoble"
            }

    # Get single user api url
    def _get_each_user_url(self, id):
        return "{}/{}".format(userTest.USERS_URL, id)

    # POST request to create a new user
    def test_0_post_single_user(self):
        r = requests.post(userTest.USERS_URL, json = userTest.USER_OBJ)
        self.assertEqual(r.status_code, 201)

    # POST request to create a new user but with existing name and lastname
    def test_1_post_existing_user(self):
        r = requests.post(userTest.USERS_URL, json = userTest.USER_OBJ)
        self.assertEqual(r.status_code, 409)

    # GET request returns the details of all users
    def test_2_get_all_users(self):
        r = requests.get(userTest.USERS_URL)
        self.assertEqual(r.status_code, 200)

    # GET request returns the details of a single user
    def test_3_get_single_user(self):
        r = requests.get(self._get_each_user_url(1))
        self.assertEqual(r.status_code, 200)

    # GET request trying to get non existing user --> shouldn't work
    def test_4_get_non_existing_user(self):
        r = requests.get(self._get_each_user_url(509))
        self.assertEqual(r.status_code, 404)

    # PUT reques to update a user
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

    # PUT request to update a non existing user --> shouldn't work
    def test_6_update_non_existing_user(self):
        r = requests.put(self._get_each_user_url(14), json = 
            {
                "bio": "test_update",
                "dateNaissance": "12-03-1998",
                "email": "test@gmail.com",
                "feedbacks": "",
                "nom": "test_update",
                "password_hash": "test_mdp",
                "photo": "",
                "preferences": "Sport, Culture",
                "prenom": "test_update",
                "role": "",
                "sexe": "Femme",
                "ville": "Grenoble"
            }
        )
        self.assertEqual(r.status_code, 404) 

    # DELETE request to delete existing user
    def test_7_delete_existing_user(self):
        r = requests.delete(self._get_each_user_url(2))
        self.assertEqual(r.status_code, 204)
    
    # DELETE request trying to delete non existing user --> shouldn't work
    def test_8_delete_non_existing_user(self):
        r = requests.delete(self._get_each_user_url(509))
        self.assertEqual(r.status_code, 404)

    # GET request to login
    def test_9_login(self):
        PARAMS  = { 'email' : "test@gmail.com", 'password' : "test_mdp"}
        requests.post(userTest.USERS_URL, json = userTest.USER_OBJ)
        r = requests.get(userTest.USER_LOGIN_URL, PARAMS)
        self.assertEqual(r.status_code, 200)

    # GET request to get current user
    def test_10_current(self):
        r = requests.get(userTest.USER_CURRENT_URL)
        self.assertEqual(r.status_code, 200)

    # GET request to logout
    def test_11_logout(self):
        r = requests.get(userTest.USER_LOGOUT_URL)
        self.assertEqual(r.status_code, 200)

    # GET request to login with wrong email --> should'nt work
    def test_12_login_wrong_email(self):
        PARAMS  = { 'email' : "t@gmail.com", 'password' : "test_mdp"}
        r = requests.get(userTest.USER_LOGIN_URL, PARAMS)
        self.assertEqual(r.status_code, 404)

    # GET request to login with wrong password --> should'nt work
    def test_13_login_wrong_password(self):
        PARAMS  = { 'email' : "test@gmail.com", 'password' : "wrong"}
        r = requests.get(userTest.USER_LOGIN_URL, PARAMS)
        self.assertEqual(r.status_code, 404)
