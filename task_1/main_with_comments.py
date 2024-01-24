# Задача 1:
# Имеется список, положительных целых чисел(integer). Необходимо сформировать все
# триплеты [nums[i], nums[j], nums[k]], для которых выполняются следующие условия: i != j !=
# k и nums[i] * nums[j] * nums[k] == 0. Каждый триплет должен быть записан в качестве списка
# в выходную последовательность.
# Пример:
# Input:
# nums = [1, 2, 0, 3, 0, 4]
# Output:
# result = [[1, 2, 0], [1, 0, 3], [2, 0, 3], [0, 3, 0], [0, 0, 4]]

nums: list[int] = [1, 2, 0, 3, 0, 4]

kpi_count: int = 0

print(f'{nums=}')

zero_indexes: list[int] = [i for i, j in enumerate(nums) if j == 0]
print(f'{zero_indexes=}')
result: list[list[int]] = []
j_start: int = 0


for i_ind, i in enumerate(zero_indexes):
                                             # if many zeroes ahead:
    if i > 0 and i + 2 < len(nums) and \
            nums[i-1] == 0 and \
            nums[i] == 0 and \
            nums[i+1] == 0 and \
            nums[i+2] == 0:
        continue

    if i_ind > 0:
        j_start = zero_indexes[i_ind-1]+1

    for j in range(j_start, len(nums)):
        k_start = j_start + 1
        for k in range(k_start, len(nums)):
            if i < j < k:
                print(f'{i=} {j=} {k=}', end = '')
                triplet = [nums[i], nums[j], nums[k]]
                print(f'   {triplet}')
            elif j < i < k:
                print(f'{j=} {i=} {k=}', end = '')
                triplet = [nums[j], nums[i], nums[k]]
                print(f'   {triplet}')
            elif j < k < i:
                print(f'{j=} {k=} {i=}', end = '')
                triplet = [nums[j], nums[k], nums[i]]
                print(f'   {triplet}')
            else:
                continue
            kpi_count += 1
            if triplet not in result:
                print(triplet)
                result.append(triplet)
            else:
                print(f'{triplet} - dropped')


print(f'\n {result=}')
print(f'{kpi_count=}')


