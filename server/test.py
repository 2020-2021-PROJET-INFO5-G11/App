from config import db
from models import User
from models import Sortie
from models import Commentaire

#sort = Sortie.query.outerjoin(Commentaire).first()
sort = Commentaire.query.first()


print('\n\n\n\n\n')
print(sort.__dict__)