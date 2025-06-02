# for loops = execute a block of a code a fixed number of times
#            You can iterate over a range, string, sequence, etc



for x in reversed(range(1,11)):
    print(x)

print("Happy New Year!")

credit_card = "1234-5678-9123-4567"

for x in credit_card:
    print(x)

for x in range(1, 21):
    if x == 13:
        continue # skip the number 13
    else:
        print(x)

for x in range(1, 21):
    if x == 13:
        break  # stop the number before 13
    else:
        print(x)