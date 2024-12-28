
from models.concrete_models.flightcard import FlightCard
from models.concrete_models.states import ArriveStates
from models.model import Model


class Luggage(Model):
    flightcard: FlightCard
    states: ArriveStates
    weight: float