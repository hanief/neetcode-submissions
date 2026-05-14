from typing import List, Set, Tuple


def grid_to_set(grid: List[List[int]]) -> Set[Tuple[int, int]]:
    st = set()

    for rowIdx, row in enumerate(grid):
        if 1 in row:
            for colIdx, col in enumerate(row):
                if col == 1:
                    st.add((rowIdx, colIdx))

    return st
# do not modify below this line

output1 = grid_to_set([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
print(type(output1))
print(sorted(list(output1)))
      
output2 = grid_to_set([[1, 0, 0], [0, 0, 0]])
print(type(output2))
print(sorted(list(output2)))

output3 = grid_to_set([[1, 1, 1], [1, 1, 1]])
print(type(output3))
print(sorted(list(output3)))

output4 = grid_to_set([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
print(type(output4))
print(sorted(list(output4)))
