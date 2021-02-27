def saddle_points(matrix: list):

    if len(set(map(len,matrix))) > 1:
        raise ValueError("Not a valid matrix")

    p = []

    for r,row in enumerate(matrix):
        for c in row_max_positions(row):
            if row[c]==col_min_value(matrix,c):
                p.append({"row":r+1, "column":c+1})
    
    return p
                
def row_max_positions(row: list) -> list:
    return [c for c,val in enumerate(row) if val==max(row)]

def col_min_value(matrix: list, col: int) -> int:
    return min(list(zip(*matrix))[col])
