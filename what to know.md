#Error handling in python

some programs will cause error, to handle those errors we need to prepare our code to by using some tecniques without crashing our program.

## Using Try-Except

```
number = int("hello")  # ❌ Program crashes here
print("This never runs")
```

and the output would be 

```
ValueError: invalid literal for int() with base 10: 'hello'
```

but the solution of this :bug: is 

```
    try:
        number = int("hello")  # Error happens here
        print("This won't run")
    except ValueError:
        print("Oops! That wasn't a valid number")
        number = 0  # Set a default value

    print("Program continues!")  # ✅ This runs
```

so the output of this blessed error handling method will be 
```
        Oops! That wasn't a valid number
        Program continues!
```


