def solution(numer1, denom1, numer2, denom2):
    numerator = numer1 * denom2 + numer2 * denom1
    denominator = denom1 * denom2
    result = max(denominator, numerator)
    for num in range(result, 0, -1):
        if numerator % num == 0 and denominator % num == 0:
            answer = [numerator / num, denominator / num]
            break
    return answer

print(solution(1, 2, 3, 4))
print(solution(9, 2, 1, 3))