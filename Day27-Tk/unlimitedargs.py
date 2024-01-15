def operation(*args, operation="+"):
    result = args[0]
    for n in args[1:]:
        if operation == "+":
            result += n
        elif operation == "-":
            result -= n
    return result

print(operation(19,6,operation="+"))

print(operation(19,6,7,operation="-"))


mystr = "angele"
print(mystr[::-1])

print(''.join(reversed(mystr)))


def calculate(n, **kwargs):
    print(type(kwargs))

    n += kwargs.get("add")
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)



mySet = {"A", 2, "C"}

print( "A" in mySet)