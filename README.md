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
 

 

 
