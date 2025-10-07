import pytest
import random
'''
@pytest.fixture
def sample_data():
    return {"name": "John", "age": 30}

def test_something(sample_data):
    assert sample_data["name"] == "John" 

def test_another_thing(sample_data):
    assert sample_data["age"] > 20

'''
# Other options: scope = "function"

@pytest.fixture(scope="session")
def get_sample_data():
    return random.randint(0,100)

def test_validate(get_sample_data, setup_teardown):
    print("1:",get_sample_data)

'''
@pytest.fixture(scope="session")
def setup_teardown():
    print("before")
    yield
    print("after")

def test_caller(setup_teardown):
    print("doing")

'''
@pytest.fixture(scope="function")
def setup_teardown():
    print("before")
    yield
    print("after")

def test_caller(setup_teardown):
    print("doing")

def test_validate2(get_sample_data):
    print("2:",get_sample_data)
    