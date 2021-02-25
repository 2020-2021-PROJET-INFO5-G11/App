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
    sorties = Sortie.query.all()

    # Serialize the data for the response
    sortie_schema = SortieSchema(many=True)
    return sortie_schema.dump(sorties)