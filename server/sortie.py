from datetime import datetime
from models import Sortie
from models import SortieSchema

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

def read_all_sorties():
    """
    This function responds to a request for /api/sorties
    with the complete lists of sorties

    :return:        json string of list of sorties
    """
    
    # Create the list of sorties from our data
    sortiess = Sortie.query.all()
    #sorties = Sortie.nomSortie

    sorties = sortiess[0]
    return sorties.typeSortie


def get_sorties_names():
    
    # Create the list of sorties from our data
    sorties = Sortie.query.all()
    sor = sorties[0]
    #sorties = Sortie.nomSortie

    return sor.nomSortie