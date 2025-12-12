import os

source = "input.txt"
destination = "output.txt"

fd1 = os.open(source, os.O_RDONLY)
fd2 = os.open(destination, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o644)

while True:
    data = os.read(fd1, 1024)
    if not data:
        break
    os.write(fd2, data)

os.close(fd1)
os.close(fd2)

print("Data copied successfully using os.open, os.read, os.write, os.close")
