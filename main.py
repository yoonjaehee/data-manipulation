import pandas as pd

# Read lottery data
df = pd.read_csv("./data/lottery.csv")
columns = [df["1"], df["2"], df["3"], df["4"], df["5"], df["6"], df["bonus"]]

# Result variable
numbers = [i for i in range(1, 46)]
counts = [0] * 45

# Set result variable
for col in columns:
    for num in col:
        counts[num - 1] = counts[num - 1] + 1
lottery_frequency = zip(numbers, counts)

# Print lottery frequency result
sorted_lf = sorted(lottery_frequency, key=lambda lf: lf[1], reverse=True)
for idx, val in sorted_lf:
    print(f"{idx+1} --> {val} times")
