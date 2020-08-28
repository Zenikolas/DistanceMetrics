from dataclasses import dataclass


@dataclass
class ElemInfo:
    num_left: int
    num_right: int
    sum_left: int
    sum_right: int
    last_idx: int


def calc_metrics(arr):
    res = [0] * len(arr)
    elem_infos = dict()

    for idx, elem in enumerate(arr):
        if elem not in elem_infos:
            elem_infos[elem] = ElemInfo(num_left=0, num_right=0, sum_left=0, sum_right=0, last_idx=idx)
        else:
            elem_infos[elem].num_right += 1
            elem_infos[elem].sum_right += idx - elem_infos[elem].last_idx

    for idx, elem in enumerate(arr):
        if elem_infos[elem].last_idx == idx:
            res[idx] = elem_infos[elem].sum_right
            continue
            
        distance = idx - elem_infos[elem].last_idx
        elem_infos[elem].num_left += 1
        elem_infos[elem].sum_left += elem_infos[elem].num_left * distance
        elem_infos[elem].sum_right -= elem_infos[elem].num_right * distance
        elem_infos[elem].num_right -= 1
        res[idx] = elem_infos[elem].sum_right + elem_infos[elem].sum_left
        elem_infos[elem].last_idx = idx

    return res

def main():
    print(f"Result: {calc_metrics([1, 2, 1, 3, 1]) == [6, 0, 4, 0, 6]}")
    print(f"Result: {calc_metrics([3, 5, 10, 5, 3, 10]) == [4, 2, 3, 2, 4, 3]}")

if __name__ == "__main__":
    main()