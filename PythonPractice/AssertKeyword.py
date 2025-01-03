# assert keyword used as debugging tool 
# test if condition is true or not and if false assertion error

x = "hello world"
assert x == "hello world"

# this will give assertion error
assert x =="bye"

# we can also do like this if instead of AssertionError we want to print our own message
assert x =="bye", "x is not bye but hello"