def sum(*args):
    for i in args:
        i+=i
    print(i)
    
sum(1,2,3)
        
def greet(name, **kwargs):
    print(f'Hello, {name}')
    for key, value in kwargs.items():
        print(key , value)
        
greet('aubree', age = 28, program = 'compscience')
    