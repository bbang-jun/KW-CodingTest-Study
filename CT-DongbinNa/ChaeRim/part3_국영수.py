import sys
input = sys.stdin.readline

def sorting(student):
    # 내림차순은 음수 처리
    li = sorted(a, key=lambda x: (-x[1],x[2],-x[3],x[0]))
    for name in li:
        print(name[0])

N=int(input())
a = []
for _ in range(N):
    name, k, e, m = map(str,input().split())
    k,e,m = int(k),int(e),int(m)
    a.append([name,k,e,m])

sorting(a)

