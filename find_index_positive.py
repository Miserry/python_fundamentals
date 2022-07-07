def find_positive(num_list):
    idx_positive = []
    for idx in range(len(num_list)):
        if num_list[idx] > 0:
            idx_positive.append(idx)

    return idx_positive
