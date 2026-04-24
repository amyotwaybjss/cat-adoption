from typing import Union

def rows_and_cols(test_list: list, desired_cols: Union[int, list], offset_format):

    count = len(test_list)
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

    grid = []

    for i in range(0, count, needed_cols):
        grid.append(test_list[i:i+needed_cols])

    if offset:
        grid[-1].append(offset_format)

    return {"records": count, "cells": num_array, "columns": needed_cols, "rows": needed_rows, "offset": offset, "grid": grid}
