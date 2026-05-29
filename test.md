# write a text to existing file
- to write to an existing file, you must add a parameter to the open() function:
- "a" - Append : will append to the end of the file 
- "w" - Write : will overwrite any existing content
  
      `f= open(demofile.txt,"a")
      f.write("Now the file has more content!")`
  
another way 

    with open("demofile.txt","a") as f:
       f.write("Now the file has more content!")