lst = [-1, 0, 1, 0, -1, -4]

count = 0
for i in range(len(lst) - 2):
    if lst[i] + lst[i+1] + lst[i+2] == 0:
        count += 1
        print(f"{count}) {lst[i]} + {lst[i+1]} + {lst[i+2]} = 0")

if count == 0:
    print("No such sequences found.")
else:
    print(f"There exist {count} such sequences.")
