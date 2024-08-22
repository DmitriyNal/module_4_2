def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function()  # вызов функции
test_function() # вызов функции