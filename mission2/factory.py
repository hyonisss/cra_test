from mission2.engine import *
from mission2.brake import *
from mission2.steering import *


class EngineFactory:
    @staticmethod
    def create(engine_type: int) -> Engine:
        if engine_type == EngineType.GM.value:
            return GMEngine()
        if engine_type == EngineType.TOYOTA.value:
            return ToyotaEngine()
        if engine_type == EngineType.WIA.value:
            return WIAEngine()
        if engine_type == EngineType.BROKEN.value:
            return BrokenEngine()
        raise ValueError("Invalid Engine Type")


class BrakeFactory:
    @staticmethod
    def create( brake_type: int) -> Brake:
        if brake_type == BrakeType.MANDO.value:
            return MandoBrake()
        if brake_type == BrakeType.CONTINENTAL.value:
            return ContinentalBrake()
        if brake_type == BrakeType.BOSCH.value:
            return BoschBrake()
        raise ValueError("Invalid Brake Type")


class SteeringFactory:
    @staticmethod
    def create(steering_type: int) -> Steering:
        if steering_type == SteeringType.BOSCH.value:
            return BoschSteering()
        if steering_type == SteeringType.MOBIS.value:
            return MobisSteering()
        raise ValueError("Invalid Steering Type")
