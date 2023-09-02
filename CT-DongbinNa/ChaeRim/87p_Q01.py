# 500, 100, 50, 10 무한 존재
N = int(input()) #10의 배수 돈
money = [500,100,50,10]
coin = 0

for i in money: #화폐의 종류가 N개면 O(N)
    tmp = N // i #동전개수 저장 (몫)
    N %= i #나머지 갱신
    coin += tmp # coin개수 올리기
print(coin)
