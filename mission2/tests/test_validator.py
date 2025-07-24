from mission2.validator import CarValidator, ValidationRule
from mission2.car import Car
from mission2.engine import *
from mission2.brake import *
from mission2.steering import *

def test_validation_failure():
    car = Car("TRUCK", WIAEngine(), MandoBrake(), BoschSteering())
    validator = CarValidator()
    validator.add_rule(ValidationRule(
        lambda c: c.car_type == "TRUCK" and isinstance(c.engine, WIAEngine),
        "WIA 엔진 금지"
    ))
    errors = validator.validate(car)
    assert errors == ["WIA 엔진 금지"]

def test_validation_pass():
    car = Car("TRUCK", WIAEngine(), MandoBrake(), BoschSteering())
    validator = CarValidator()
    validator.add_rule(ValidationRule(
        lambda c: c.car_type == "SEDAN", "세단만 허용"
    ))
    errors = validator.validate(car)
    assert errors == []