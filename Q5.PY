x = 0
y = 20

while True:
    y -= 4 
    x += 2 / y

    if y < 6:
        break

print(f"Final Value: {round(x)}")
