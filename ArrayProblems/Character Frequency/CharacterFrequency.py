
def characterFrequency(str):
    res = {}
    for keys in str:
        res[keys] = res.get(keys, 0) + 1

# printing result
    return res


if __name__ == "__main__":
    str = "Shaswata Tripathy"
    print(characterFrequency(str))