from mission2.engine import Engine
from mission2.brake import Brake
from mission2.steering import Steering
from enum import IntEnum

class CarType(IntEnum):
    SEDAN = 1
    SUV = 2
    TRUCK = 3

    @classmethod
    def get_menu(cls):
        print("        ______________")
        print("       /|            |")
        print("  ____/_|_____________|____")
        print(" |                      O  |")
        print(" '-(@)----------------(@)--'")
        print("===============================")
        print("어떤 차량 타입을 선택할까요?")
        for car_type in cls:
            print(f"{car_type.value}. {car_type.get_name()}")

    def get_name(self):
        return "SUV" if self.name == "SUV" else self.name.title()


class Car:
    def __init__(self, car_type: CarType, engine: Engine, brake: Brake, steering: Steering):
        self.car_type = car_type
        self.engine = engine
        self.brake = brake
        self.steering = steering

    def describe(self) -> dict :
        return {
            "Engine   ": self.engine.name(),
            "Brake    ": self.brake.name(),
            "Steering ": self.steering.name()
        }

    def can_run(self) -> bool:
        return not self.engine.is_broken()