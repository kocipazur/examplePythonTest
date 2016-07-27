from testLibraries import verifiers

def runTests():
    verifiers.verify_equals(1, 1)                     #pass
    verifiers.verify_equals(1, 2)                     #fail
    verifiers.verify_equals("bar", "foo")             #fail

    verifiers.verify_not_equals(1, 1)                 #fail
    verifiers.verify_not_equals(1, 2)                 #pass
    verifiers.verify_not_equals("foo", "bar")         #pass
    verifiers.verify_not_equals("foobar", "foobar")   #fail

    verifiers.verify_type(1, "int")                   #pass
    verifiers.verify_type("foo", "int")               #fail

    verifiers.verify_returns(pow, (1, 1, 1), int)     #pass
    verifiers.verify_returns(pow, (1, 1, 1), str)     #fail

runTests()
