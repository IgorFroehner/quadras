
from flask_mongoengine.wtf import model_form

from model import Esporte

EsporteForm = model_form(Esporte)
