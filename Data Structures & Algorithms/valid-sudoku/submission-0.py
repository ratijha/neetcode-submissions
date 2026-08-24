class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    board[i][j] = 0
                else:
                    board[i][j] = int(board[i][j])
        row_val = []
        for i in range(9):
            row_cnt = {}
            for j in range(9):
                try:
                    row_cnt[board[i][j]] +=1
                except KeyError:
                    row_cnt[board[i][j]] = 1
            print(row_cnt)
            res = count_hash_map(row_cnt)
            row_val.append(res)

        col_val = []
        for i in range(9):
            col_cnt = {}
            for j in range(9):
                try:
                    col_cnt[board[j][i]] +=1
                except KeyError:
                    col_cnt[board[j][i]] = 1
            print(col_cnt)
            res = count_hash_map(col_cnt)
            col_val.append(res)
        print(row_val)
        print(col_val)

        map_res = []
        for i in range(0,9,3):
            for j in range(0,9,3):
                cnt = valid_mat_map(board, i, j)
                res = count_hash_map(cnt)
                map_res.append(res)

        if any(row_val) or any(col_val) or any(map_res):
            print("invalid")
            return False
        else:
            print("valid")
            return True


def valid_mat_map(board, row, col):
    map = {}
    for i in range(3):
        for j in range(3):
            try:
                map[board[row+i][col+j]] +=1
            except KeyError:
                map[board[row+i][col+j]] = 1
    return map

def count_hash_map(data):
    for key, values in data.items():
        if key !=0 and values > 1:
            return True
    return False