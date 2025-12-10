import pytest

#conftest- it's a global or common class for all classes- if any method is common then we can
#define the method in conftest file, so python will identify the method in our test class
@pytest.fixture(scope='session')
def precondition():
    print("sample test")