# d = {"a": 1, "b": 2, "c": 5, "f": 10}
d = {"a": 1, "b": 2, "c": 1, "f": 10}
d_reversed = {}
can_reversed = True

for k, v in d.items():
    print(k, v)
    if d_reversed.get(v):
        can_reversed = False
        break
    else:
        d_reversed[v] = k

if can_reversed == True:
    print(d_reversed)
else:
    print(-1)