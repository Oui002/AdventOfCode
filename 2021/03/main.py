with open('data.txt', 'r') as file:
    data = file.readlines()

def get_cols(data, row):
    return [col[row] for col in data]

def most_common(_0, _1):
    if _0 > _1:
        return 0
    else:
        return 1

def get_counts(bin_list: list):
    _0 = 0
    _1 = 0

    for num in bin_list:
        if int(num) == 0:
            _0 += 1
        else:
            _1 += 1

    if most_common(_0, _1) == 0:
        return 0, 1
    else:
        return 1, 0

gamma_result = str()
epsilon_result = str()

for row in range(len(data[0])-1):
    gamma_num, epsilon_num = get_counts(get_cols(data, row))

    gamma_result = gamma_result + str(gamma_num)
    epsilon_result = epsilon_result + str(epsilon_num)

result = int(gamma_result, 2) * int(epsilon_result, 2)
print(result)