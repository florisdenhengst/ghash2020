def read(filename):
    with open(filename) as f:
        l = f.readline()
        max_slices, types = l.split()
        l = f.readline()
        n_slices = map(int, l.split())
    return int(max_slices), int(types), n_slices

def greedy(slice_budget, items):
    solution = []
    for idx, slices in items:
        if slice_budget > slices:
            solution += [idx,]
            slice_budget -= slices
        if slice_budget == 0:
            break
    return solution[::-1]

def score(solution):
    # TODO
    pass

def output(solution):
    print(len(solution))
    print(' '.join(map(str, solution)))



max_slices, types, n_slices = read('a_example.in')
slices_by_idx = [(idx, n) for idx, n in enumerate(n_slices)][::-1]
solution = greedy(max_slices, slices_by_idx)
output(solution)


