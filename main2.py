import random
from typing import List

import pandas as pd

# Read lottery data
df = pd.read_csv("./data/lottery.csv")
row_len = len(df)


# Make random int list helper function
def random_int_list(num: int, length: int):
    result = []
    for i in range(length):
        result.append(random.randrange(num))
    return result


# Make new columns, save to csv, and print out first 20 lines
# Column explanation
# win: (win, 1), (lose, 0)
# weather: (sunny, 0), (cloudy, 1), (dizzy, 2), (rainy, 3)
# no_prev_winner: (no, 1), (yes, 1)
rnd_win: List[int] = random_int_list(2, row_len)
rnd_weather: List[int] = random_int_list(4, row_len)
rnd_no_prev_winner: List[int] = random_int_list(2, row_len)

adding_df = pd.DataFrame(
    {"win": rnd_win, "weather": rnd_weather, "no_prev_winner": rnd_no_prev_winner}
)
new_df = df.join(adding_df)
new_df.to_csv("./data/new_lottery.csv", mode="w")
print(new_df[:20])
