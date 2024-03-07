def greet(fx):
    def mfx(*args , **kwargs):
        print("Good morning")
        fx(*args,**kwargs)
        print("Thanks for using this")
    return mfx

@greet
def hello():
    print("hello world")
hello()

@greet
def add(a,b):
    print(a*b)
add(2,3)