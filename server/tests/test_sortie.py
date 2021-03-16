import unittest
import requests

class sortieTest(unittest.TestCase):
    API_URL = "http://localhost:5000/api"
    SORTIES_URL = "{}/sortie".format(API_URL)
    SEARCH_URL = "{}/search".format(API_URL)
    FILTER_URL = "{}/filter".format(API_URL)
    SORTIE_OBJ = {
                    "capaciteMax": 10,
                    "capaciteMin": 3,
                    "date": "2021-03-12",
                    "dateLimite": "2021-03-11",
                    "description": "Petit tournoi de basket",
                    "duree": "04:30",
                    "heure": "09:00",
                    "id_groupe": 0,
                    "lieu": "Les taillés",
                    "nbInscrits": 0,
                    "nom": "Basket aux taillés",
                    "photo": "pas-de-photo",
                    "point_rdv": "DLST",
                    "privee": True,
                    "typeSortie": "Sport"
                }
    SORTIE_OBJ_BIS = {
                        "capaciteMax": 10,
                        "capaciteMin": 3,
                        "date": "2021-03-12",
                        "dateLimite": "2021-03-11",
                        "description": "Petite balade en ville",
                        "duree": "04:30",
                        "heure": "09:00",
                        "id_groupe": 0,
                        "lieu": "Centre-ville",
                        "nbInscrits": 0,
                        "nom": "Balade en ville",
                        "photo": "pas-de-photo",
                        "point_rdv": "Chavant",
                        "privee": True,
                        "typeSortie": "Autre"
                    }

    # Get single sortie api url
    def _get_each_sortie_url(self, id):
        return "{}/{}".format(sortieTest.SORTIES_URL, id)

    # Get sorties by expression api url
    def _get_search_sorties_url(self, search):
        return "{}/{}".format(sortieTest.SEARCH_URL, search)

    # Get sorties by type api url
    def _get_filter_sorties_url(self, type_sortie):
        return "{}/{}".format(sortieTest.FILTER_URL, type_sortie)

    # POST request to create a new sortie
    def test_0_post_single_sortie(self):
        r = requests.post(sortieTest.SORTIES_URL, json = sortieTest.SORTIE_OBJ)
        self.assertEqual(r.status_code, 201)

    # POST request to create a new sortie but with existing name and type
    def test_1_post_existing_sortie(self):
        r = requests.post(sortieTest.SORTIES_URL, json = sortieTest.SORTIE_OBJ)
        self.assertEqual(r.status_code, 409)

    # GET request returns the details of all sorties
    def test_2_get_all_sorties(self):
        r = requests.get(sortieTest.SORTIES_URL)
        self.assertEqual(r.status_code, 200)

    # GET request returns the details of a single sortie
    def test_3_get_single_sortie(self):
        r = requests.get(self._get_each_sortie_url(1))
        self.assertEqual(r.status_code, 200)

    # GET request trying to get non existing sortie --> shouldn't work
    def test_4_get_non_existing_sortie(self):
        r = requests.get(self._get_each_sortie_url(509))
        self.assertEqual(r.status_code, 404)

    # PUT request to update a sortie
    def test_5_update_sortie(self):
        r = requests.put(self._get_each_sortie_url(4), json = 
            {
                "capaciteMax": 10,
                "capaciteMin": 3,
                "date": "2021-03-12",
                "dateLimite": "2021-03-11",
                "description": "Petit tournoi de foot",
                "duree": "04:30",
                "heure": "09:00",
                "id_groupe": 0,
                "lieu": "Les taillés",
                "nbInscrits": 0,
                "nom": "Foot aux taillés",
                "photo": "pas-de-photo",
                "point_rdv": "DLST",
                "privee": True,
                "typeSortie": "Sport"
            }
        )
        self.assertEqual(r.status_code, 201)

    # PUT request to update a non existing sortie --> shouldn't work
    def test_6_update_non_existing_sortie(self):
        r = requests.put(self._get_each_sortie_url(14), json = 
            {
                "capaciteMax": 10,
                "capaciteMin": 3,
                "date": "2021-03-12",
                "dateLimite": "2021-03-11",
                "description": "Petit tournoi de foot",
                "duree": "04:30",
                "heure": "09:00",
                "id_groupe": 0,
                "lieu": "Les taillés",
                "nbInscrits": 0,
                "nom": "Foot aux taillés",
                "photo": "pas-de-photo",
                "point_rdv": "DLST",
                "privee": True,
                "typeSortie": "Sport"
            }
        )
        self.assertEqual(r.status_code, 404) 

    # DELETE request to delete existing sortie
    def test_7_delete_existing_sortie(self):
        r = requests.delete(self._get_each_sortie_url(3))
        self.assertEqual(r.status_code, 204)
    
    # DELETE request trying to delete non existing sortie --> shouldn't work
    def test_8_delete_non_existing_sortie(self):
        r = requests.delete(self._get_each_sortie_url(509))
        self.assertEqual(r.status_code, 404)

    # GET request search sortie by expression
    def test_9_search_sortie(self):
        r = requests.get(self._get_search_sorties_url("Randonnée"))
        self.assertEqual(r.status_code, 200)

    # GET request search sortie by type
    def test_10_search_sortie_type(self):
        r = requests.get(self._get_filter_sorties_url("Sport"))
        self.assertEqual(r.status_code, 200)

