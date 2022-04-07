while True:
    try:
        amount = int(input("How many layers of leaves do you want?\n:"))
        break
    except:
        print("You didn't put a number!\n")

leaves = "*"
leavesNum = 0
for i in range(1, amount + 1):
    if i == 1:
        leavesNum = 1
    else:
        leavesNum += 2
    space = amount - i
    print((space * " ") + (leavesNum * leaves))
print(((amount // 2) * " ") + "| |")


