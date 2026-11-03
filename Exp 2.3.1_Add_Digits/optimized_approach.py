
num = int(input("Enter a number: "))

if num == 0:
    answer = 0
else:
    answer = 1 + (num - 1) % 9

print("Single digit result:", answer)