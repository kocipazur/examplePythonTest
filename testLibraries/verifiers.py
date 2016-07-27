import sys


def verify_equals(actual, expected):
    testFunctionName = sys._getframe().f_code.co_name #get current function name
    defaultResult = testFunctionName + " passed." #set default test result
    result = defaultResult
    try:
        assert actual == expected #actual assertion - check if values are true
    except AssertionError: #catch Assertion Error if above assert returns false (exception)
        result = testFunctionName + " failed: Expected value: " + str(expected) + " is not equal to actual value: "\
              + str(actual) #assign description of fail
    except: #catch any other possible error
        result = Exception.message
    print result

def verify_type(value, expected_type):
    testFunctionName = sys._getframe().f_code.co_name
    defaultResult = testFunctionName + " passed."
    result = defaultResult
    try:
        assert value.__class__.__name__ == expected_type
    except AssertionError:
        result = testFunctionName + " failed: Actual value type is: " + value.__class__.__name__ + " instead of expected: "\
              + str(expected_type)
    except:
        result = Exception.message
    print result

def verify_not_equals(actual, expected):
    testFunctionName = sys._getframe().f_code.co_name
    defaultResult = testFunctionName + " passed."
    result = defaultResult
    try:
        assert not (actual == expected)
    except AssertionError:
        result = testFunctionName + " failed: Actual value: " + str(actual) + " is equal to expected value"
    except:
        result = Exception.message
    print result

def verify_returns(testedMethod, methodParameters, expectedType): #pass method, args and expected type of result
    testFunctionName = sys._getframe().f_code.co_name
    defaultResult = testFunctionName + " passed."
    result = defaultResult
    try:
        testedMethodType = type(testedMethod(*methodParameters)) #assign method result to variable
        assert testedMethodType is expectedType #check if assigned variable passes assert
    except AssertionError:
        result = testFunctionName + "failed: Actual type is: " + str(testedMethodType) + " instead of expected: "\
              + str(expectedType)
    except:
        result = Exception.message
    print result
