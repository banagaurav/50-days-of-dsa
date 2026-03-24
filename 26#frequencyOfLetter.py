def CountFreq(str):
    freq = {}
    for ch in str:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1
    return freq


str = "geeksforgeeks"
result = CountFreq(str)

# Print vertically
for char in sorted(result.keys()):
    print(f"{char} : {result[char]}")