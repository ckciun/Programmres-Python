def solution(numbers):
    answer = []
    for i in numbers:
        answer.append(i * 2)
    return answer

numbers1 = [1, 2, 3, 4, 5]
numbers2 = [1, 2, 100, -99, 1, 2, 3]
print(solution(numbers1))
print(solution(numbers2))