""""
Day 3 Part 1

--- Day 3: Binary Diagnostic ---
The submarine has been making some odd creaking noises, so you ask it to produce a diagnostic report just in case.

The diagnostic report (your puzzle input) consists of a list of binary numbers which, when decoded properly, can tell you many useful things about the conditions of the submarine. The first parameter to check is the power consumption.

You need to use the binary numbers in the diagnostic report to generate two new binary numbers (called the gamma rate and the epsilon rate). The power consumption can then be found by multiplying the gamma rate by the epsilon rate.

Each bit in the gamma rate can be determined by finding the most common bit in the corresponding position of all numbers in the diagnostic report. For example, given the following diagnostic report:

00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
Considering only the first bit of each number, there are five 0 bits and seven 1 bits. Since the most common bit is 1, the first bit of the gamma rate is 1.

The most common second bit of the numbers in the diagnostic report is 0, so the second bit of the gamma rate is 0.

The most common value of the third, fourth, and fifth bits are 1, 1, and 0, respectively, and so the final three bits of the gamma rate are 110.

So, the gamma rate is the binary number 10110, or 22 in decimal.

The epsilon rate is calculated in a similar way; rather than use the most common bit, the least common bit from each position is used. So, the epsilon rate is 01001, or 9 in decimal. Multiplying the gamma rate (22) by the epsilon rate (9) produces the power consumption, 198.

Use the binary numbers in your diagnostic report to calculate the gamma rate and epsilon rate, then multiply them together. What is the power consumption of the submarine? (Be sure to represent your answer in decimal, not binary.)
"""


character_sum = [[0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0]]
gamma_rate = []

with open("./d3-01_input.txt", "r") as input_file:
    raw_data = input_file.readlines()
    for line in raw_data:
        line = list(line)
        line.remove("\n")
        for i in range(len(line)):
            if int(line[i]) == 1:
                character_sum[0][i] += 1
            elif int(line[i]) == 0:
                character_sum[1][i] += 1

for i in range(12):
    print(f"{character_sum[0][i]} | {character_sum[1][i]}")
    if int(character_sum[0][i]) > int(character_sum[1][i]):
        gamma_rate.append(1)
    elif int(character_sum[0][i]) < int(character_sum[1][i]):
        gamma_rate.append(0)

gamma_rate = ''.join(str(x) for x in gamma_rate)
converted_gamma_rate = int(gamma_rate, 2)

reverse_table = {ord('0'): '1', ord('1'): '0'}
epsilon_rate = gamma_rate.translate(reverse_table)
converted_epsilon_rate = int(epsilon_rate, 2)

power_consumption = converted_gamma_rate * converted_epsilon_rate
print(f"Epsilon rate: {epsilon_rate}")
print(f"Epsilon rate converted: {converted_gamma_rate}")
print(f"Gamma rate: {gamma_rate}")
print(f"Gamma rate converted: {converted_epsilon_rate}")
print(f"Power consumption of the submarine: {power_consumption}")
