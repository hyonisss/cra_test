from mission2.car import *
from mission2.engine import *
from mission2.brake import *
from mission2.steering import *


def test_car_describe():
    car = Car(CarType.SEDAN, GMEngine(), MandoBrake(), BoschSteering())
    desc = car.describe()
    assert desc["Engine   "] == "GM"
    assert desc["Brake    "] == "MANDO"
    assert desc["Steering "] == "BOSCH"

def test_car_can_run_true():
    car = Car(CarType.SUV, GMEngine(), MandoBrake(), BoschSteering())
    assert car.can_run()

def test_car_can_run_false():
    car = Car(CarType.SUV, BrokenEngine(), MandoBrake(), BoschSteering())
    assert not car.can_run()