guillaume@ubuntu:~/0x06$ cat 101-main.py

#!/usr/bin/python3

Square = __import__('101-square').Square



my_square = Square(5, (0, 0))

print(my_square)



print("--")



my_square = Square(5, (4, 1))

print(my_square)