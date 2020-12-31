from pandas import DataFrame, to_numeric

df = DataFrame({
    "t": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    "X": [12.3, 11.5, 11.0, 12.0, 13.5, 12.5, 12.8, 9.9, 12.2, 12.5, 13.0, 10.5],
    "Y": [795, 915, 965, 892, 585, 644, 714, 1180, 851, 779, 625, 1001]
})


def sortDfByKey(key: str):
    df[key] = to_numeric(df[key], errors="coerce")
    return df.sort_values(key, ascending=True)


def getSameRank(val: str, rank: str):
    count = 0
    temp = {}
    for index, row in df.iterrows():
        if temp.get(row[val]) is None:
            temp[row[val]] = [row[rank], 1]
        else:
            count = temp.get(row[val])[1] + 1
            temp[row[val]] = [(row[rank] + temp.get(row[val])[0]) / count, count]

    for index, row in df.iterrows():
        df.loc[index, rank] = temp[row[val]][0]
    return count


n = 12
print(f"n = {n}")

df = sortDfByKey("X")
df["R(X)"] = list(range(1, n + 1))
numberIdenticalRanksA = getSameRank("X", "R(X)")
a = ((numberIdenticalRanksA**3) - numberIdenticalRanksA) / n
print(f"A = {a}")

df = sortDfByKey("Y")
df["R(Y)"] = list(range(1, n + 1))
numberIdenticalRanksB = getSameRank("Y", "R(Y)")
b = ((numberIdenticalRanksB**3) - numberIdenticalRanksB) / n
print(f"B = {b}")

checksum = 0
for i, r in df.iterrows():
    checksum += (r["R(X)"] - r["R(Y)"])**2
    df.loc[i, "(R(X)-R(Y))^2"] = (r["R(X)"] - r["R(Y)"])**2

df = sortDfByKey("t")

print(df)

p = 1 - ((6 * checksum + b + a) / (n**3 - n))
print(f"p = {p}")
