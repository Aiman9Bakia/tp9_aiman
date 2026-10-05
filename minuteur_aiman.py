import time

# compte à rebours

start = int(input("Donnez un nombre"))
while start > 0:
    print(start)
    start -= 1
    time.sleep(1)

print("Happy new year")
