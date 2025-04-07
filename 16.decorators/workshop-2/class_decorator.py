class DecoratorClass:
    
    def __init__(self, f):
        self.f = f
        
    def __call__(self):
        print("Decorating", self.f.__name__)
        self.f()

@DecoratorClass
def custom_function():
    print("inside custom_function()")

custom_function()

