from routes import agendamento
from routes import quadra
from routes import bloco
from routes import esporte
from routes import evento

blueprints = [
    agendamento.blue,
    quadra.blue,
    bloco.blue,
    esporte.blue,
    evento.blue,
]
