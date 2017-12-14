with open('input.txt') as f:
    puzzle_data = f.read()
f.closed

def captcha_1(nums):
    sum = 0
    for i in range(len(nums)):
        if nums[i] == nums[(i+1) % len(nums)]:
            sum += int(nums[i])
    return sum

print(captcha_1(puzzle_data))