def say_hello(name):
    return f"Hello , {name}"
def say_bye(name):
    return f"Bye,{name}"

print("This always runs, no matter what")

if __name__ == "__main__":
    print("This only runs if greetings.py is run directly")
    print(say_hello("Test"))

def say_name(name):
    return f"greet ,{name}"