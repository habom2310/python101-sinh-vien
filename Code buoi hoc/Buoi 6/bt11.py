Input = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]

# output = {}
# ten = []
# tong = []
# for m in range(len(Input)):
#     t = Input[m]
#     ten.append(t.get('item'))
#     tong.append(t.get('amount'))
# ten = ['item1', 'item2', 'item1']

# for m in range(len(ten)):
#     for n in range(m+1,len(ten)):
#         if ten[m] == ten[n]:
#             tong[m] = tong[m] + tong[n]
#             ten.pop(n)
#             tong.pop(n)
# for m in range(len(ten)):
#     output[ten[m]]= tong[m]
# print(output)

output = {}
for i in range(len(Input)):
    d = Input[i]
    item = d.get("item")
    amount = d.get("amount")

    if output.get(item) != None: # neu dict output da co item hien tai thi cong them, neu chua co thi khoi tao
        output[item] += amount
    else:
        output[item] = amount

print(output)