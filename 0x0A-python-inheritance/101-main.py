#!/usr/bin/python3
add_attribute = __import__('101-add_attribute').add_attribute

class MyClass():
     pass

class M2():
    __slots__='test'

mc = MyClass()
add_attribute(mc, "name", "John")
print(mc.name)

try:
    a = "My String"
    add_attribute(a, "name", "Bob")
    print(a.name)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    test = M2()
    add_attribute(test, "name", "Bob")
    print(test.name)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    test2 = M2()
    add_attribute(test2, "test", "Bob")
    print(test2.test)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
