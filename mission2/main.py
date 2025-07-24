from mission2.builder import CarBuilder
from mission2.factory import EngineFactory, BrakeFactory, SteeringFactory
from mission2.validator import CarValidator, ValidationRule
from mission2.engine import *
from mission2.brake import *
from mission2.steering import *
from mission2.car import CarType

import time
import sys

CLEAR_SCREEN = "\033[H\033[2J"

def build_validator() -> CarValidator:
    v = CarValidator()
    v.add_rule(ValidationRule(
        lambda c: c.car_type.name == "SEDAN" and isinstance(c.brake, ContinentalBrake),
        "FAIL\nSedan에는 Continental제동장치 사용 불가"
    ))
    v.add_rule(ValidationRule(
        lambda c: c.car_type.name == "SUV" and isinstance(c.engine, ToyotaEngine),
        "FAIL\nSUV에는 TOYOTA엔진 사용 불가"
    ))
    v.add_rule(ValidationRule(
        lambda c: c.car_type.name == "TRUCK" and isinstance(c.engine, WIAEngine),
        "FAIL\nTruck에는 WIA엔진 사용 불가"
    ))
    v.add_rule(ValidationRule(
        lambda c: c.car_type.name == "TRUCK" and isinstance(c.brake, MandoBrake),
        "FAIL\nTruck에는 Mando제동장치 사용 불가"
    ))
    v.add_rule(ValidationRule(
        lambda c: isinstance(c.brake, BoschBrake) and not isinstance(c.steering, BoschSteering),
        "FAIL\nBosch제동장치에는 Bosch조향장치 이외 사용 불가"
    ))
    return v

def delay(ms) -> None:
    t = ms / 1000.0
    time.sleep(t)

def clear() -> None:
    sys.stdout.write(CLEAR_SCREEN)
    sys.stdout.flush()

def show_menu(step: int) -> None:
    clear()
    if step == 0:
        CarType.get_menu()

    elif step == 1:
        EngineType.get_menu()

    elif step == 2:
        BrakeType.get_menu()

    elif step == 3:
        SteeringType.get_menu()

    elif step == 4:
        print("멋진 차량이 완성되었습니다.")
        print("0. 처음 화면으로 돌아가기")
        print("1. RUN")
        print("2. Test")
    print("===============================")

def is_valid_range(step: int, selection: int) -> bool:

    valid_ranges = {
        0: (1, 3),  # Car Type
        1: (0, 4),  # Engine
        2: (0, 3),  # Brake
        3: (0, 2),  # Steering
        4: (0, 2),  # Run/Test
    }

    error_messages = {
        0: "차량 타입은 1 ~ 3 범위만 선택 가능",
        1: "엔진은 1 ~ 4 범위만 선택 가능",
        2: "제동장치는 1 ~ 3 범위만 선택 가능",
        3: "조향장치는 1 ~ 2 범위만 선택 가능",
        4: "Run 또는 Test 중 하나를 선택 필요",
    }

    if step not in valid_ranges:
        return False

    min_val, max_val = valid_ranges[step]
    if not (min_val <= selection <= max_val):
        print(f"ERROR :: {error_messages[step]}")
        return False

    return True

def main():

    try:
        step = 0

        while True:
            show_menu(step)

            user_input = input("INPUT > ").strip()
            if user_input == "exit":
                print("바이바이")
                break

            try:
                selected = int(user_input)
            except ValueError:
                print("ERROR :: 숫자만 입력 가능")
                delay(800)
                continue

            if not is_valid_range(step, selected):
                delay(800)
                continue

            if selected == 0:
                step = 0 if step == 4 else max(0, step - 1)
                continue

            if step == 0:
                car_type = CarType(selected)
                print(f"차량 타입으로 {car_type.get_name()}을 선택하셨습니다.")
                delay(800)
                step += 1

            elif step == 1:
                engine = EngineFactory.create(selected)
                print(f"{engine.name()} 엔진을 선택하셨습니다.")
                delay(800)
                step += 1

            elif step == 2:
                brake = BrakeFactory.create(selected)
                print(f"{brake.name()} 제동장치를 선택하셨습니다.")
                delay(800)
                step += 1

            elif step == 3:
                steering = SteeringFactory.create(selected)
                print(f"{steering.name()} 조향장치를 선택하셨습니다.")
                delay(800)
                car = CarBuilder() \
                    .set_car_type(car_type) \
                    .set_engine(engine) \
                    .set_brake(brake) \
                    .set_steering(steering) \
                    .build()
                step += 1

            elif step == 4:
                validator = build_validator()
                errors = validator.validate(car)

                if selected == 1:
                    if errors:
                        print("자동차가 동작되지 않습니다")
                    elif not car.can_run():
                        print("엔진이 고장나있습니다.")
                        print("자동차가 움직이지 않습니다.")
                    else:
                        print(f"Car Type : {car.car_type.get_name()}")
                        for k, v in car.describe().items():
                            print(f"{k}: {v}")
                        print("자동차가 동작됩니다.")
                    delay(2000)

                elif selected == 2:
                    print("Test...")
                    delay(1500)
                    if errors:
                        print(errors[0])
                    else:
                        print("PASS")
                    delay(2000)


    except Exception as e:
        print(f"오류: {e}")

if __name__ == "__main__":
    main()