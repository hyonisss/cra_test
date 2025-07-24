from dataclasses import dataclass
from enum import IntEnum
from typing import *
import time
import sys

CLEAR_SCREEN = "\033[H\033[2J"


class CarType(IntEnum):
    SEDAN = 1
    SUV = 2
    TRUCK = 3

class Engine(IntEnum):
    GM = 1
    TOYOTA = 2
    WIA = 3
    BROKEN = 4

class Brake(IntEnum):
    MANDO = 1
    CONTINENTAL = 2
    BOSCH = 3

class Steering(IntEnum):
    BOSCH = 1
    MOBIS = 2


@dataclass
class CarConfig:
    car_type: Optional[CarType] = None
    engine: Optional[Engine] = None
    brake: Optional[Brake] = None
    steering: Optional[Steering] = None


def delay(ms):
    t = ms / 1000.0
    time.sleep(t)

def clear():
    sys.stdout.write(CLEAR_SCREEN)
    sys.stdout.flush()

def show_menu(step):
    clear()
    if step == 0:
        print("        ______________")
        print("       /|            |")
        print("  ____/_|_____________|____")
        print(" |                      O  |")
        print(" '-(@)----------------(@)--'")
        print("===============================")
        print("어떤 차량 타입을 선택할까요?")
        print("1. Sedan")
        print("2. SUV")
        print("3. Truck")
    elif step == 1:
        print("어떤 엔진을 탑재할까요?")
        print("0. 뒤로가기")
        print("1. GM")
        print("2. TOYOTA")
        print("3. WIA")
        print("4. 고장난 엔진")
    elif step == 2:
        print("어떤 제동장치를 선택할까요?")
        print("0. 뒤로가기")
        print("1. MANDO")
        print("2. CONTINENTAL")
        print("3. BOSCH")
    elif step == 3:
        print("어떤 조향장치를 선택할까요?")
        print("0. 뒤로가기")
        print("1. BOSCH")
        print("2. MOBIS")
    elif step == 4:
        print("멋진 차량이 완성되었습니다.")
        print("0. 처음 화면으로 돌아가기")
        print("1. RUN")
        print("2. Test")
    print("===============================")

def update_car_type(cfg: CarConfig, selected: int) -> None:
    cfg.car_type = CarType(selected)

def print_selected_car_type(car_type: CarType)-> None:
    print(f"차량 타입으로 {car_type.name.title()}을 선택하셨습니다.")

def update_engine(cfg: CarConfig, selected: int) -> None:
    cfg.engine = Engine(selected)

def print_selected_engine(engine: Engine)-> None:
    if engine == Engine.BROKEN:
        print("고장난 엔진을 선택하셨습니다.")
    else:
        print(f"{engine.name} 엔진을 선택하셨습니다.")


def update_brake(cfg: CarConfig, selected: int) -> None:
    cfg.brake = Brake(selected)


def print_selected_brake(brake: Brake)-> None:
    print(f"{brake.name.title()} 제동장치를 선택하셨습니다.")

def update_steering(cfg: CarConfig, selected: int) -> None:
    cfg.steering = Steering(selected)


def print_selected_steering(steering: Steering)-> None:
    print(f"{steering.name.title()} 조향장치를 선택하셨습니다.")

def is_valid_configuration(config: CarConfig) -> bool:
    if config.car_type == CarType.SEDAN and config.brake == Brake.CONTINENTAL:
        return False

    if config.car_type == CarType.SUV and config.engine == Engine.TOYOTA:
        return False

    if config.car_type == CarType.TRUCK and config.engine == Engine.WIA:
        return False

    if config.car_type == CarType.TRUCK and config.brake == Brake.MANDO:
        return False

    if config.brake == Brake.BOSCH and config.steering != Steering.BOSCH:
        return False

    return True

def run_produced_car(config: CarConfig) -> None:
    if not is_valid_configuration(config):
        print("자동차가 동작되지 않습니다")
        return

    if config.engine == Engine.BROKEN:
        print("엔진이 고장나있습니다.")
        print("자동차가 움직이지 않습니다.")
        return

    car_type_name = "SUV" if config.car_type.name=="SUV" else config.car_type.name.title()

    print(f"Car Type: {car_type_name}")
    print(f"Engine: {config.engine.name}")
    print(f"Brake: {config.brake.name.title()}")
    print(f"Steering: {config.steering.name.title()}")
    print("자동차가 동작됩니다.")

def test_produced_car(config: CarConfig) -> str:
    if config.car_type == CarType.SEDAN and config.brake == Brake.CONTINENTAL:
        return "FAIL\nSedan에는 Continental제동장치 사용 불가"

    if config.car_type == CarType.SUV and config.engine == Engine.TOYOTA:
        return "FAIL\nSUV에는 TOYOTA엔진 사용 불가"

    if config.car_type == CarType.TRUCK and config.engine == Engine.WIA:
        return "FAIL\nTruck에는 WIA엔진 사용 불가"

    if config.car_type == CarType.TRUCK and config.brake == Brake.MANDO:
        return "FAIL\nTruck에는 Mando제동장치 사용 불가"

    if config.brake == Brake.BOSCH and config.steering != Steering.BOSCH:
        return "FAIL\nBosch제동장치에는 Bosch조향장치 이외 사용 불가"

    return "PASS"

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
    config = CarConfig()
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

        try:
            if step == 0:
                update_car_type(config, selected)
                print_selected_car_type(config.car_type)
                delay(800)
                step += 1

            elif step == 1:
                update_engine(config, selected)
                print_selected_engine(config.engine)
                delay(800)
                step += 1

            elif step == 2:
                update_brake(config, selected)
                print_selected_brake(config.brake)
                delay(800)
                step += 1

            elif step == 3:
                update_steering(config, selected)
                print_selected_steering(config.steering)
                delay(800)
                step += 1

            elif step == 4:
                if selected == 1:
                    run_produced_car(config)
                    delay(2000)
                elif selected == 2:
                    print("Test...")
                    delay(1500)
                    result = test_produced_car(config)
                    print(result)
                    delay(2000)

        except ValueError as e:
            print(f"{e}")
            delay(1500)


if __name__ == "__main__":
    main()