from mission2.car import Car
from typing import Callable, List, Optional

class ValidationRule:
    def __init__(self, condition: Callable[[Car], bool], error_message: str):
        self.condition = condition
        self.error_message = error_message

    def validate(self, car: Car) -> Optional[str]:
        if self.condition(car):
            return self.error_message
        return None


class CarValidator:
    def __init__(self):
        self.rules: List[ValidationRule] = []

    def add_rule(self, rule: ValidationRule):
        self.rules.append(rule)

    def validate(self, car: Car) -> List[str]:
        errors = []
        for rule in self.rules:
            result = rule.validate(car)
            if result:
                errors.append(result)
        return errors