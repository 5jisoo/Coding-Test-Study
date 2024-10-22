"""
https://school.programmers.co.kr/learn/courses/30/lessons/1845
"""

def solution(nums):
    max_answer = len(nums)/2
    num_set = set(nums)
    set_length = len(num_set)
    if set_length < max_answer:
        return set_length
    else:
        return max_answer