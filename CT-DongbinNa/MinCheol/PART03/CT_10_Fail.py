#key can move and rotate
#key should fill all the blank in lock
import copy

def solution(key, lock):
    answer = False #first set answer to False
    Len_Lock = len(lock)
    Len_Key = len(key)
    New_Key  = [[0]*Len_Key for _ in range(Len_Key)]
    Move=max(Len_Lock,Len_Key)
    Holes = 0

    for A in range(Len_Lock):
        for B in range(Len_Lock):
            if lock[A][B]==0:
                Holes+=1

    for _ in range(4): #rotate key to clock wise
        for A in range(Len_Key):
            for B in range(Len_Key):
                New_Key[B][Len_Key-1-A] = key[A][B]

        key = copy.deepcopy(New_Key)
        
        for A in range(Move*(-1),Move+1): #Move Up and Down
            for B in range(Move*(-1), Move+1): #Move Right and Left
                Count=0 #Count hole that fits key

                for C in range(Move):
                    for D in range(Move):
                        if C+A<0 or Len_Key<=C+A or D+B<0 or Len_Key<=D+B:
                            continue

                        elif lock[C][D]==0 and New_Key[C+A][D+B]==1:
                            Count+=1

                if Count==Holes:
                    answer=True                        
    
    return answer


# key=[[0, 0, 0], [1, 0, 0], [0, 1, 1]]
# lock=[[1, 1, 1], [1, 1, 0], [1, 0, 1]]

# print(solution(key, lock))