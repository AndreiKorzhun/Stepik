# number of known words
d = int(input())
# put known words in the list
lst_d = [i.lower() for _ in range(d) for i in input().split()]

# the number of lines of text to check
w = int(input())
# lines of text
lst_l = [i.lower() for _ in range(w) for i in input().split()]

# set of wrong words
mist = set()
# chech lines of text
for i in range(len(lst_l)):
    if lst_l[i] not in lst_d:
        mist.add(lst_l[i])

for i in mist:
    print(i)
