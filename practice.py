
import sys

if len(sys.argv)<3:
    print("Usage: python3 practice.py <filename> <newfilename>")
    sys.exit(1)
filename =sys.argv[1]
newfilename=sys.argv[2]

try:
    with open(filename,'r') as file:
        word_set=set(line.strip() for line in file)
        filtered= sorted(word_set)

except Exception as e:
    print(f"error occured: {e}")


try:
    with open(newfilename ,'x') as newer:
        for item in filtered:
            newer.write(f"{item}\n")
except FileExistsError:
    print("use another name for the filtered file pls")

except Exception as e:
    print(f"error {e}")