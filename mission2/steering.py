from abc import ABC, abstractmethod
from enum import IntEnum

class SteeringType(IntEnum):
    BOSCH = 1
    MOBIS = 2

    @classmethod
    def get_menu(cls):
        print("어떤 조향장치를 선택할까요?")
        print("0. 뒤로가기")
        for Steering in cls:
            print(f"{Steering.value}. {Steering.name}")

class Steering(ABC):
    @abstractmethod
    def name(self) -> str: ...

class BoschSteering(Steering):
    def name(self) -> str:
        return "BOSCH"

class MobisSteering(Steering):
    def name(self) -> str:
        return "MOBIS"