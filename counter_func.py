# cats_list = ['A', 'B', 'C', 'D', 'E','F','G','H','I','J','K','L']
cats_list = ['A', 'B']
# fix 2/3 case
checked_numbers = [3, 2]

# count = len(cats_list)
for i in range(1, 200):
    count = i

    response = []
    potential_cols = []
    offset_flag = []

    if count < 1:
        response = f'{count} is less than than 1.'
    else:
        for number in checked_numbers:
            if count % number == 0:
                response.append(f'{count} is divisible by {number}.')
                potential_cols.append(number)
                offset_flag.append(False)
            elif (count+1) % number == 0:
                response.append(f'{count}+1 is divisible by {number}.')
                potential_cols.append(number)
                offset_flag.append(True)

    result = [i, response, response[0], potential_cols, potential_cols[0], offset_flag, offset_flag[0]]

    print(result)
