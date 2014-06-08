class Solution:
    # @param board, a 2D array
    # Capture all regions by modifying the input board in-place.
    # Do not return any value.
    def solve(self, board):
        visited = {}
        if len(board) == 0 or len(board[0]) == 0:
            return
        h_bound = len(board) - 1
        w_bound = len(board[0]) - 1
        for i in range(len(board[0])):
            if board[0][i] == 'O':
                self.dfs(board, 0, i, visited)
            if board[h_bound][i] == 'O':
                self.dfs(board, h_bound, i, visited)
        for i in range(len(board)):
            if board[i][0] == 'O':
                self.dfs(board, i, 0, visited)
            if board[i][w_bound] == 'O':
                self.dfs(board, i, w_bound, visited)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O' and not (i, j) in visited:
                    board[i][j] = 'X'

    def dfs(self, board, y, x, visited):
        if not (y, x) in visited:
            visited[(y, x)] = True
            stack = [(y, x)]
            while len(stack) > 0:
                h, w = stack.pop()
                width, height, neighbors = [], [], []
                if w > 0:
                    width.append(w-1)
                if w < len(board[0]) - 1:
                    width.append(w+1)
                if h > 0:
                    height.append(h-1)
                if h < len(board)-1:
                    height.append(h+1)
                neighbors += zip([h for i in range(len(width))], width)
                neighbors += zip(height, [w for i in range(len(height))])
                for neigh in neighbors:
                    if not neigh in visited and board[neigh[0]][neigh[1]] == 'O':
                        stack.append(neigh)
                        visited[neigh] = True
