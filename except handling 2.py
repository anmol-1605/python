print("starting line")

a=[10,34,23]

try:
    
    a=11/0
    print(arr[0])   
    print(y)
except ZeroDivisionError:
    print("ZERO DIVISION exception raised") 
except IndexError:
    print("Array Index Out of bound")
except NameError:
    print("undefined variable")
except:
    print("some exception is raised")
else:
    print("no exception")
finally:
    print("this is final block")
print("outside the try")

Output
starting line
ZERO DIVISION exception raised
this is final block
outside the try
