def solution(food_times, k):
    answer = 0
    Finished = 0
    Length = len(food_times)
    A = 0

    while Finished != Length :
        if A == Length: #select the dish to first 
            A=0
        if food_times[A]==0: #check if food time is 0
            A+=1
            continue

        answer = A + 1
        if k<=0:
            break
        
        food_times[A]-=1
        if food_times[A]==0:
            Finished+=1
        k-=1
        A+=1
    
    if Finished==Length:
        answer = -1

    return answer

FT = [3,1,2]
K=5

print(solution(FT,K))