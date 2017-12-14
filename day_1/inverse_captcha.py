with open('./day_1/input.txt') as f:
    puzzle_data = f.read()
f.closed

def captcha_1(nums):
    sum = 0
    for i in range(len(nums)):
        # Modulus is needed to keep index within the circular list
        if nums[i] == nums[(i+1) % len(nums)]:
            sum += int(nums[i])
    return sum

print(captcha_1(puzzle_data))

def captcha_2(nums):
    sum = 0
    for i in range(len(nums)):
        # Check number halfway around circular list
        if nums[i] == nums[(i+(len(nums)//2)) % len(nums)]:
            sum += int(nums[i])
    return sum

print(captcha_2(puzzle_data))