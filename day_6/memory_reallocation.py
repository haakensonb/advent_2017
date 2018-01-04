import math

with open('./day_6/input.txt') as f:
    mem_bank = [int(num) for num in f.read().split()]
f.close

def mem_reallocation(mem_bank):
    cycles = 0
    history = []

    while mem_bank not in history:
        history.append(mem_bank[:])
        m = max(mem_bank)
        index = mem_bank.index(m)
        mem_bank[index] = 0

        while m:
            index = (index + 1) % len(mem_bank)
            mem_bank[index] += 1
            m -= 1

        cycles += 1
    return cycles, len(history)-history.index(mem_bank)


print(mem_reallocation(mem_bank))