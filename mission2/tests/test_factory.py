import pytest
from mission2.factory import *

def test_engine_factory_valid():
    engine = EngineFactory.create(EngineType.GM.value)
    assert engine.name() == "GM"

def test_brake_factory_valid():
    brake = BrakeFactory.create(BrakeType.MANDO.value)
    assert brake.name() == "MANDO"

def test_steering_factory_valid():
    steering = SteeringFactory.create(SteeringType.BOSCH.value)
    assert steering.name() == "BOSCH"

def test_invalid_engine_type():
    with pytest.raises(ValueError, match="Invalid Engine Type"):
        EngineFactory.create(999)

def test_invalid_brake_type():
    with pytest.raises(ValueError, match="Invalid Brake Type"):
        BrakeFactory.create(-1)

def test_invalid_steering_type():
    with pytest.raises(ValueError, match="Invalid Steering Type"):
        SteeringFactory.create(123)



def test_engine_factory_invalid_after_wia():
    with pytest.raises(ValueError, match="Invalid Engine Type"):
        EngineFactory.create(1234)


def test_brake_factory_invalid_after_bosch():
    with pytest.raises(ValueError, match="Invalid Brake Type"):
        BrakeFactory.create(1234)

def test_steering_factory_invalid_after_mobis():
    with pytest.raises(ValueError, match="Invalid Steering Type"):
        SteeringFactory.create(1234)