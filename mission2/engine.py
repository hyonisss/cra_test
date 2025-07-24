from abc import ABC, abstractmethod
from enum import IntEnum

class EngineType(IntEnum):
    GM = 1
    TOYOTA = 2
    WIA = 3
    BROKEN = 4

    @classmethod
    def get_menu(cls):
        print("어떤 엔진을 탑재할까요?")
        print("0. 뒤로가기")
        for engine in cls:
            if engine.name == "BROKEN":
                print(f"{engine.value}. 고장난 엔진")
            else:
                print(f"{engine.value}. {engine.name}")

class Engine(ABC):
    @abstractmethod
    def name(self) -> str: ...

    @abstractmethod
    def is_broken(self) -> bool: ...


class GMEngine(Engine):
    def name(self) -> str:
        return "GM"

    def is_broken(self) -> bool:
        return False


class ToyotaEngine(Engine):
    def name(self) -> str:
        return "TOYOTA"

    def is_broken(self) -> bool:
        return False

class WIAEngine(Engine):
    def name(self) -> str:
        return "WIA"

    def is_broken(self) -> bool:
        return False

class BrokenEngine(Engine):
    def name(self) -> str:
        return "고장난"

    def is_broken(self) -> bool:
        return True