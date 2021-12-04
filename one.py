

import io


# Part 1
f = open("one_input.txt","r")


pre = None 
cnt = 0

for line in f.readlines():


    if pre is not None and int(line) > pre:
        cnt += 1

    pre = int(line)


print(cnt)

# Part 2
import pandas as pd
f = open("one_input.txt","r")

all_lines = f.readlines()

df = pd.DataFrame()

df["line"] = pd.Series(all_lines)

df["line"] = df["line"].apply(lambda x: int(x.replace("\n","")))

df["rolling"] = df.rolling(3).sum()

df["next_rolling"] = df["rolling"].shift(-1)

print(len((df[df["next_rolling"] > df["rolling"]]).index))

