from mission2.engine import Engine
from mission2.brake import Brake
from mission2.steering import Steering
from mission2.car import Car, CarType

class CarBuilder:
    def __init__(self):
        self._car_type = None
        self._engine: Engine = None
        self._brake: Brake = None
        self._steering: Steering = None

    def set_car_type(self, car_type: CarType) -> "CarBuilder":
        self._car_type = car_type
        return self

    def set_engine(self, engine: Engine) -> "CarBuilder":
        self._engine = engine
        return self

    def set_brake(self, brake: Brake) -> "CarBuilder":
        self._brake = brake
        return self

    def set_steering(self, steering: Steering) -> "CarBuilder":
        self._steering = steering
        return self

    def build(self) -> Car:
        return Car(self._car_type, self._engine, self._brake, self._steering)