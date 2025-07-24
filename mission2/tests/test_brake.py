from mission2.brake import *

def test_brake_names():
    assert MandoBrake().name() == "MANDO"
    assert ContinentalBrake().name() == "CONTINENTAL"
    assert BoschBrake().name() == "BOSCH"