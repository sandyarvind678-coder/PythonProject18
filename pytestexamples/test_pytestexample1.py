#fixtures-- if we set fixture then we can reuse the method wherever we want in the test cases
#test_ or _test--if we give only python will understand it's a pytest


import pytest
#IMPORTANT NOTES
#if you give "module" in scope then it will execute only once

#if you give "function" in scope then it will execute every time before executing every test case

#if you give "class" in scope then it will execute only once

#if you give "session" it will execute only once in your entire project

#Ex: I have ten classes and for me common for ten classes is link,username and password

#Ex1: if i given "session" in conftest file-- it will execute before only once for ten classes

#Ex2: if i given "class" in conftest file-- it will execute before for every classes

#Ex3: if i given "module" in conftest file-- it will execute before for every classes

#Ex4: if i given "function" in conftest file-- it will execute before for each method in every class


def test_testcase1(precondition):
    print("Testcase 1")
@pytest.fixture(scope="function")
def test_testcase2():
    print("Testcase 2")
    return "value"

#@pytest.mark.skip #-- skip the method
def test_testcase3(test_testcase2):
    assert test_testcase2 == "value"

@pytest.mark.smoketest
def test_testcase44():
    print("Testcase 44")
