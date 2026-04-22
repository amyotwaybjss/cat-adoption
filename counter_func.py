# from cat_adoption import cats_list

cats_list = ['A', 'B', 'C', 'D', 'E','F','G','H','I','J','K','L']
checked_numbers = [3, 2]

count = len(cats_list)

response = []

if count < 1:
    response = f'{count} is less than than 1.'

for number in checked_numbers:
    if count % number == 0:
        response.append(f'{count} is divisible by {number}.')
    elif (count+1) % number == 0:
        response.append(f'{count}+1 is divisible by {number}.')

print(response)
print(response[0])


# if count < 1:
#     print(f'{count} is less than than 1.')
# elif count % 3 == 0:
#     print(f'{count} is divisible by three.')
# elif count % 2 == 0:
#     print(f'{count} is divisible by two.')
# elif (count+1) % 3 == 0:
#     print(f'{count}+1 is divisible by three.')
# elif (count+1) % 2 == 0:
#     print(f'{count}+1 is divisible by two.')
# else:
#     print(f'{count} is invalid.')

# function takes in a LIST of items and counts them
# it then needs to compare to another list of numbers and see where the first case of it being divisible is.