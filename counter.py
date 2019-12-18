def luhn(num):
    numbers = [int(el) for el in str(num)]
    result_sum = 0

    for index, el in enumerate(numbers):
        if index % 2 == 0:
            result_sum += el
        else:
            if 2 * el > 9:
                result_sum += el * 2 - 9
            else:
                result_sum += el * 2

    return result_sum % 10 == 0
