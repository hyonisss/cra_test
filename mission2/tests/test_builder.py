from mission2.builder import CarBuilder
from mission2.engine import GMEngine
from mission2.brake import MandoBrake
from mission2.steering import BoschSteering
from mission2.car import CarType

def test_builder_builds_car_correctly(mocker):

    cal_type = CarType(1)

    builder = CarBuilder()
    car = (
        builder.set_car_type(cal_type)
               .set_engine(GMEngine())
               .set_brake(MandoBrake())
               .set_steering(BoschSteering())
               .build()
    )
    assert car.car_type.name == "SEDAN"
    assert car.engine.name() == "GM"
    assert car.brake.name() == "MANDO"
    assert car.steering.name() == "BOSCH"