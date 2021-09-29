
#IfTest
language = "JavaScript"

if language == "Python":
    print("Language is Python")
elif language == "Java":
    print("Language is Java")
elif language == "JavaScript":
    print("Language is JavaScript")
else:
    print("No match")

#BooleanTest
user = "Admin"
logged_in = False
if not logged_in:
    print("Please Log in")
else:
    print("Welcome")

#IsTest
a = [1,2,3,]
b = [1,2,3,]

print(id(a))
print(id(b))
print("The Statement 'a is b' is", a is not b)

# False Value Test:
    # False
    # None
    # Zero of any numeric type
    # Any empty sequence. i.e., "", (), [].
    # Any empty mapping. i.e., {}.

condition = {}

if condition:
    print("Evaluated to True")
else:
    print("Evaluated to False")
