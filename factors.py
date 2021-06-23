# def prime_factors(x):
#     # Also returns 1
#     values = [1]
#     actual = x
#     current = 2
#     while current <= int(x / 2) + 1:
#         while actual % current == 0:
#             # print(current)
#             values.append(current)
#             actual /= current
#         current += 1
#     return values
def format_prime_dict(prime_dict):
    """
    :param prime_dict: dict
    :return: str
    """
    keys = list(prime_dict.keys())
    out = ""
    for key in keys:
        if prime_dict[key] > 1:
            out += f"{key}^{prime_dict[key]} x "
        else:
            out += f"{key} x "
    out = out[:-3]
    return out


def prime_factors(x):
    # Also returns 1
    values = [1]
    actual = x
    current = 2
    while current <= int(x / 2) + 1:
        while actual % current == 0:
            # print(current)
            values.append(current)
            actual /= current
        current += 1
    compressed_values = dict()
    for value in values:
        if value not in compressed_values:
            compressed_values[value] = 1
        else:
            compressed_values[value] += 1
    return compressed_values


def factors(x):
    values = [1]
    current = 2
    while current <= x // 2 + 1:
        if x % current == 0:
            values.append(current)
        current += 1
    return values


if __name__ == '__main__':
    print(prime_factors(28))
    print(factors(28124))
    print(format_prime_dict(prime_factors(28)))
