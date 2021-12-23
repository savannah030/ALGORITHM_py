# 각 자리의 합이 3의 배수이면 그 수는 3의 배수임을 이용
# 위 조건이 맞다면, 제일 큰 수가 답(모든 자리수를 다 써야 하니까)
nums = list(input())
if '0' not in nums:
    print(-1)
else:
    nums.sort(reverse=True)
    sum = 0
    for digit in nums:
        sum += int(digit)
    if sum % 3 != 0:
        print(-1)
    else:
        print(''.join(nums))