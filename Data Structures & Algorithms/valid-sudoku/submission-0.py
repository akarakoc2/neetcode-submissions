class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        #here handling the row levels
        for i in range(len(board)):
            cur_set = set()
            for j in range(len(board[i])):
                if board[i][j] in cur_set and board[i][j] != "." :
                    return False
                elif board[i][j] != ".":    
                    cur_set.add(board[i][j])               
            
            
        #here the column level
        for i in range(len(board)):
            cur_set = set()
            for j in range(len(board[i])):
                if board[j][i] in cur_set and board[j][i] != "." :
                    return False
                elif board[j][i] != ".":    
                    cur_set.add(board[j][i])             
             

        #here checking the boxes

        col_offset = [0,3,6]

        row_offset = [0,3,6]

        for i in col_offset:
                for j in row_offset:
                    cur_set = set()
                    for r in range(3):
                        for c in range(3):
                            seen = board[j + r][i + c]
                            if seen != ".":
                                if seen in cur_set:
                                    return False
                                cur_set.add(seen)
                             
        return True
            
                
                
                

        
                
            

        

        