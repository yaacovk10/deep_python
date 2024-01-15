import sys

with open (sys.argv[1] , 'r') as file :
    content = file.read()
    if sys.argv[2] in content:
        print( f"{sys.argv[2]} is present in {sys.argv[1]}")
    else:
        print("not present")

