def inspect(func):
    name = func.__name__
    print(f"Название: {name}")
    for attr, type in func.__annotations__.items():
          print(f"Аргумент: {attr}, тип: {type}")
    
def test(a: int, b: str, c: bool):
	return a, b, c

inspect(test)