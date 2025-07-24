from mission2.steering import *

def test_steering_names():
    assert BoschSteering().name() == "BOSCH"
    assert MobisSteering().name() == "MOBIS"