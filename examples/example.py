import pytest

@pytest.fixture
def sample_data():
    return {"name": "John", "age": 30}

def test_something(sample_data):
    assert sample_data["name"] == "John" 


@pytest.fixture(scope="session")
def sample_data_validation(sample_data):
    assert sample_data["name"] == "Johx" 

'''
@pytest.fixture
def setup_teardown():
    print("before")
    yield
    print("after")

def test_caller(setup_teardown):
    print("doing")
'''

@pytest.fixture(autouse=True, scope="session")
def setup_teardown():
    print("before")
    yield
    print("after")

def test_caller():
    print("doing")