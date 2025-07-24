from mission2.engine import *

def test_engine_names():
    assert GMEngine().name() == "GM"
    assert ToyotaEngine().name() == "TOYOTA"
    assert WIAEngine().name() == "WIA"
    assert BrokenEngine().name() == "고장난"

def test_engine_broken_status():
    assert not GMEngine().is_broken()
    assert BrokenEngine().is_broken()

def test_all_engines_is_broken_status():
    assert not ToyotaEngine().is_broken()
    assert not WIAEngine().is_broken()