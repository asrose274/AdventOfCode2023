scratchers = {}

for i, x in enumerate(open("input.txt")):
    if i not in scratchers:
        scratchers[i] = 1

    x = x.split(":")[1].strip()
    winners, numbers = [list(map(int, k.split())) for k in x.split(" | ")]
    j = sum(q in winners for q in numbers)

    for n in range(i+1, i+j+1):
        scratchers[n] = scratchers.get(n, 1) + scratchers[i]

print(sum(scratchers.values()))
