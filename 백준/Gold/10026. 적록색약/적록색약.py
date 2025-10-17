line_num = int(input())

arr1 = []
arr2 = []

for _ in range(line_num):
    line = input()
    arr1.append(list(line))
    arr2.append(list(line))
    
movements = [(-1,0),(1,0),(0,-1),(0,1)]

def segment_count(arr, line_num, movements):  
    count = 0  
    stack = []
    stack_same_color = []

    stack.append((0,0))
    
    while len(stack) != 0:
        (row, col) = stack.pop()
        if arr[row][col] != 'o':
            color = arr[row][col]
            arr[row][col] = 'o'
            stack_same_color.append((row,col))
            count +=1
            while len(stack_same_color) != 0:
                (row, col) = stack_same_color.pop()
                for movement in movements:
                    row_move = row + movement[0]
                    col_move = col + movement[1]
                    if (row_move>=0 and row_move<line_num) and (col_move>=0 and col_move<line_num):
                        if arr[row_move][col_move] == color:
                            arr[row_move][col_move] = 'o'
                            stack_same_color.append((row_move, col_move))
                        else:
                            if arr[row_move][col_move] != 'o':
                                stack.append((row_move, col_move))
    return count

count1 = segment_count(arr1, line_num, movements)

for row in range(line_num):
    for col in range(len(arr2[row])):
        if (arr2[row][col] == 'R' or arr2[row][col] == 'G'):
            for movement in movements:
                row_move = row + movement[0]
                col_move = col + movement[0]
                if (row_move>=0 and row_move<line_num) and (col_move>=0 and col_move<len(arr2[row])):
                    if (arr2[row_move][col_move] == 'R' or arr2[row_move][col_move] == 'G'):
                        arr2[row][col] = 'R'

count2 = segment_count(arr2, line_num, movements)

print(count1, count2)