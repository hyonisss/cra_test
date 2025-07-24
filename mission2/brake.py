from abc import ABC, abstractmethod
from enum import IntEnum

class BrakeType(IntEnum):
    MANDO = 1
    CONTINENTAL = 2
    BOSCH = 3

    @classmethod
    def get_menu(cls):
        print("어떤 제동장치를 선택할까요?")
        print("0. 뒤로가기")
        for brake in cls:
            print(f"{brake.value}. {brake.name}")

class Brake(ABC):
    @abstractmethod
    def name(self) -> str: ...

class MandoBrake(Brake):
    def name(self) -> str:
        return "MANDO"

class ContinentalBrake(Brake):
    def name(self) -> str:
        return "CONTINENTAL"

class BoschBrake(Brake):
    def name(self) -> str:
        return "BOSCH"