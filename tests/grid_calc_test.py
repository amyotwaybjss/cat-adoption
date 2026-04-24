from counter_func import rows_and_cols

example1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']
example2 = ['A', 'B', 'C', 'D', 'E', 'F']
example3 = ['A', 'B', 'C', 'D', 'E']
example4 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']
desired_cols = [3, 2]
offset = 'X'

test_example = example4

result = rows_and_cols(test_example, desired_cols, offset)
print(result)


# We know the number of columns is 3. We want to take the first 3 cats and make a list, then the next 3, until we have a list of len 3 lists. If offset true we add X to the end.
# 'rows' is not needed but can be used to check.
# Could this be embedded in the counter_func?

# check = [['A', 'B', 'C'], ['D', 'E', 'F']]
# print(len(check)) # this should = rows

if result["offset"]:
    test_example.append(offset)
    # should this be done outside or in the function? Outside might be less messy?

desired = result["columns"]

is_split = []

for i in range(0, len(test_example), desired):
    is_split.append(test_example[i:i+desired])


print(is_split)