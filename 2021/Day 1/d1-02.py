"""""
DAY 1 - 02


Considering every single measurement isn't as useful as you expected: there's just too much noise in the data.

Instead, consider sums of a three-measurement sliding window. Again considering the above example:

199  A      
200  A B    
208  A B C  
210    B C D
200  E   C D
207  E F   D
240  E F G  
269    F G H
260      G H
263        H
Start by comparing the first and second three-measurement windows. The measurements in the first window are marked A (199, 200, 208); their sum is 199 + 200 + 208 = 607. The second window is marked B (200, 208, 210); its sum is 618. The sum of measurements in the second window is larger than the sum of the first, so this first comparison increased.

Your goal now is to count the number of times the sum of measurements in this sliding window increases from the previous sum. So, compare A with B, then compare B with C, then C with D, and so on. Stop when there aren't enough measurements left to create a new three-measurement sum.

In the above example, the sum of each three-measurement window is as follows:

A: 607 (N/A - no previous sum)
B: 618 (increased)
C: 618 (no change)
D: 617 (decreased)
E: 647 (increased)
F: 716 (increased)
G: 769 (increased)
H: 792 (increased)
In this example, there are 5 sums that are larger than the previous sum.

Consider sums of a three-measurement sliding window. How many sums are larger than the previous sum?
"""""

input = open("d1-01_input.txt", "r")
lines = input.readlines()

sumNumbers = []
numbers = []
increased = 0
decreased = 0

for line in lines:
    numbers.append(int(line))

    if len(numbers) < 3:
        continue

    newSum = numbers[0] + numbers[1] + numbers[2]
    sumNumbers.append(newSum)
    numbers.pop(0)

    if len(sumNumbers) < 2:
        print(f"{int(line)} (N/A - no previous measurement)")
        continue

    if sumNumbers[1] > sumNumbers[0]:
        increased += 1
        print(f"{sumNumbers[1]} (increased)")
    elif sumNumbers[1] < sumNumbers[0]:
        decreased += 1
        print(f"{sumNumbers[1]} (decreased)")
    else:
        print(f"{sumNumbers[1]} (no change)")
    sumNumbers.pop(0)
    

print(f"Increased: {increased}")
print(f"Decreased: {decreased}")
