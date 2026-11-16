x = "Global Variable"
def outer():
    y = "Outer Variable"

    def inner():
        nonlocal y
        y = "Nonlocal Variable"
        z = "Local Variable"

        print("Inside inner function:")
        print("Global:", x)
        print("Nonlocal:", y)
        print("Local:", z)

    inner()
    print("Inside outer function:", y)
outer()
print("Outside function:", x)
