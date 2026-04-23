from typing import Union

def rows_and_cols(count: int, desired_cols: Union[int, list]):

    count = abs(count)
    desired_cols = desired_cols if isinstance(desired_cols, list) else [desired_cols]

    potential_cols = []
    offset_flag = []

    for number in desired_cols:
        number = abs(number)
        if count == 0 or number == 0:
            potential_cols.append(1)
            offset_flag.append(True)
        elif count % number == 0:
            potential_cols.append(number)
            offset_flag.append(False)
        elif (count+1) % number == 0:
            potential_cols.append(number)
            offset_flag.append(True)

    offset = offset_flag[0]
    num_array = count if offset == False else count+1
    needed_cols = potential_cols[0]
    needed_rows = num_array//needed_cols

    return {"records": count, "cells": num_array, "columns": needed_cols, "rows": needed_rows, "offset": offset}

checked_numbers = [3, 2]
for num in range(0, 201):
    x = rows_and_cols(num, checked_numbers)
    print(x)


