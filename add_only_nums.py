def add_only_nums(inp_list):
    int_value = [x for x in inp_list if isinstance(x, int)]
    return f"""There are total of {len(int_value)} numbers in the list
And the sum of the numbers = {sum(int_value)}"""

print(add_only_nums("abcd1234"))