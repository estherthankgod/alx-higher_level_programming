#!/usr/bin/python3
if _name_ == "_main_":
    import sys
    result = 0
    for arg in sys.argv:
        if arg != sys.argv[0]:
         result += int(arg)
    print(result)
