def gimme(input_array):
    # Find the middle number
    middle_number = sorted(input_array)[1]
    # Find its index in the original array
    return input_array.index(middle_number) 
