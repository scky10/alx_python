import importlib

if __name__ == "__main__":
    a = 1
    b = 2

    add_module = importlib.import_module('add_0')
    add_function = getattr(add_module, 'add')
    result = add_function(a, b)
    output = "{} + {} = {}\n".format(a, b, result)
    print(output)