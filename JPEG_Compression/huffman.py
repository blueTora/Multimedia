from collections import Counter
import numpy as np


# ***** Part 4 *****
def cal_frequency_table(arr: list) -> dict:
    data = Counter(arr)
    res = {key: value / len(arr) for key, value in data.items()}
    return res


def calculate_huffman(freq: dict) -> dict:
    if len(freq) == 2:
        return dict(zip(freq.keys(), ['0', '1']))

    freq_p = freq.copy()
    sorted_freq = sorted(freq.items(), key=lambda x: x[1])
    f1, f2 = sorted_freq[0][0], sorted_freq[1][0]

    freq1, freq2 = freq_p.pop(f1), freq_p.pop(f2)
    freq_p[f1 + f2] = freq1 + freq2

    res = calculate_huffman(freq_p)
    temp = res.pop(f1 + f2)
    res[f1], res[f2] = temp + '0', temp + '1'

    return res


# ***** Part 5 *****
def zigzag(matrix: np.ndarray) -> np.ndarray:
    h = v = iter = 0
    v_min = h_min = 0

    v_max = matrix.shape[0]
    h_max = matrix.shape[1]

    result = np.zeros((v_max * h_max))

    while v < v_max and h < h_max:

        if (h + v) % 2 == 0:
            if v == v_min:
                result[iter] = matrix[v, h]
                if h == h_max:
                    v = v + 1
                else:
                    h = h + 1

                iter += 1

            elif h == (h_max - 1) and v < v_max:
                result[iter] = matrix[v, h]
                v = v + 1
                iter += 1

            elif v > v_min and h < (h_max - 1):
                result[iter] = matrix[v, h]
                v = v - 1
                h = h + 1
                iter += 1

        else:
            if v == (v_max - 1) and h <= (h_max - 1):
                result[iter] = matrix[v, h]
                h = h + 1
                iter += 1

            elif h == h_min:
                result[iter] = matrix[v, h]
                if v == v_max - 1:
                    h = h + 1
                else:
                    v = v + 1

                iter += 1

            elif v < (v_max - 1) and h > h_min:
                result[iter] = matrix[v, h]
                v = v + 1
                h = h - 1
                iter += 1

        if v == (v_max - 1) and h == (h_max - 1):
            result[iter] = matrix[v, h]
            break

    return result


def run_length_coding(arr: np.ndarray) -> list:
    result = []
    length = 0
    eob = ('EOB',)

    for i in range(len(arr)):
        for j in range(len(arr[i])):

            new_arr = np.trim_zeros(arr[i], 'b')
            if len(new_arr) == 0:
                new_arr = np.zeros(1)

            if j == len(new_arr):
                result.append(eob)
                break

            if i == 0 and j == 0:
                result.append((int(new_arr[j]).bit_length(), new_arr[j]))

            elif j == 0:
                diff = int(arr[i][j] - arr[i - 1][j])

                if diff != 0:
                    result.append((diff.bit_length(), diff))
                else:
                    result.append((1, diff))

                length = 0

            elif new_arr[j] == 0:
                length += 1

            else:
                result.append((length, int(new_arr[j]).bit_length(), new_arr[j]))
                length = 0

        if not (result[len(result) - 1] == eob):
            result.append(eob)

    return result