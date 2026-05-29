# python-file-i-o
The key function for working with files in Python is the open() function.
There are four different methods (modes) for opening a file:
    
    "r" - Read - Default value. Opens a file for reading, error if the file does not exist
    
    "a" - Append - Opens a file for appending, creates the file if it does not exist
    
    "w" - Write - Opens a file for writing, creates the file if it does not exist
    
    "x" - Create - Creates the specified file, returns an error if the file exists
 In addition you can specify if the file should be handled as binary or text mode
    
    "t" - Text - Default value. Text mode
    
    "b" - Binary - Binary mode (e.g. images)
 ##syntax
     f= open("demofile.txt")
    or 
     f= open("demofile.txt","rt")
 where as "r" is for read , and "t" for text they are default values.
 To open the file, use the built-in open() function.

The open() function returns a file object, which has a read() method for reading the content of the file:
             ``` f = open("demofile.txt")
              print(f.read())```
 

 

 
## write a text to existing file
- to write to an existing file, you must add a parameter to the open() function:
- "a" - Append : will append to the end of the file 
- "w" - Write : will overwrite any existing content
  
      `f= open(demofile.txt,"a")
      f.write("Now the file has more content!")`
  
another way 

    ```
    with open("demofile.txt","a") as f:
       f.write("Now the file has more content!")
    ```

##  Overwrite Existing Content

**To overwrite the existing content to the file, use the w parameter:**
Example

Open the file "demofile.txt" and overwrite the content:
```
with open("demofile.txt", "w") as f:
  f.write("Woops! I have deleted the content!")

#open and read the file after the overwriting:
with open("demofile.txt") as f:
  print(f.read()) 
```


## to create a new file 

```
f=open ("myfile.txt","x")
```

## Delete a File

To delete a file, you must import the OS module, and run its **os.remove()** function:
    ```
    import os
    os.remove("demofile.txt") 
    ```

    