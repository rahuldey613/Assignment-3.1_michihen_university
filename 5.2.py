largest = None
smallest = None

while True:
    try:
        num = input("Enter a number: ")
        if num == 'done':
            break
        num = int(num)
        if largest is None or num > largest:
            largest = num
        elif smallest is None or num < smallest:
            smallest = num

    except:
        print("Invalid input")
        continue

print("Maximum is", largest)
print("Minimum is", smallest)

# Enter 7, 2, bob, 10, and 4 and match the output below.
#remember to type done o exit the loop of inputs
