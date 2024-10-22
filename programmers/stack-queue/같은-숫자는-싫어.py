"""
https://school.programmers.co.kr/learn/courses/30/lessons/12906

### better solution ###
def no_continuous(s):
    a = []
    for i in s:
        if a[-1:] == [i]: continue
        a.append(i)
    return a

index 에러를 피하기 위해
if i==0: answer.append(arr[i]) 라고 작성했는데,

a[-1:]라고 작성하면 애초에 피할 수 있음...!! (슬라이싱이 키포인트)

"""


def solution(arr):
    answer = []
    for i in range(len(arr)):
        if i==0: answer.append(arr[i])
        if answer[-1] != arr[i]: 
            answer.append(arr[i])
    return answer