import random

heart_ranks = {"💚" : 0, "💙" : 1, "💜" : 2, "🖤" : 3}
# sorted_list = sorted(to_sort, key=lambda col:heart_ranks[col])

eg1 = ["💚", "💙", "🖤", "💚", "💙", "💜", "💙", "💚", "💚"]
eg2 = ["💚", "💚", "💙", "💙", "💜", "💜", "💜", "💜", "🖤", "🖤"]
eg3 = ["💚", "💙", "💙", "💜", "💜", "💜", "💜", "💜", "🖤"]

eg4 = ["💚", "💚", "💚", "💚", "💚", "💙", "💙", "💙","💙", "💜", "💜", "💜", "💜", "🖤",  "🖤",  "🖤",  "🖤"]
eg4_sorted = sorted(eg4, key=lambda col: heart_ranks[col])

max_hearts = 4

egX = []
for x in range (10):
    egX.append(random.choice(list(heart_ranks.keys())))
    x += 1

egX_sorted = sorted(egX, key=lambda col: heart_ranks[col])

# No more than 4 hearts on a row. (Max set with a var)
# Where possible, we want to keep hearts together by colour.
# Need Dictionary to define order. So green > blue > purple > black
# Count each case of hearts.
# So count greens and result will be either >4, =4, <4. If =4, that's a row. If >4, make a row, and take the remainder, retest.
# If <4, add number of blues and recalculate. If =4, done. If <4, add the purples. If >4, remove blues and make a row of green with blanks.

a_list = []

row_num = 0
index_num = 0
test_case = eg4_sorted

for rank in heart_ranks: # first, this will review the green hearts.
    items = test_case.count(rank)
    if items >= max_hearts:
        row = test_case[index_num:items+index_num]
        a_list.append(row)
        row_num += 1
        index_num += items

print(a_list)

