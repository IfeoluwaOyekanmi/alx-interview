#!/usr/bin/python3
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def isWinner(x, nums):
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if n == 1:
            ben_wins += 1
            continue
       
        if n % 2 == 0:
            maria_wins += 1
        else:
            if is_prime(n):
                maria_wins += 1
            else:
                ben_wins += 1
   
    if maria_wins > ben_wins:
        return "Maria"
    elif maria_wins < ben_wins:
        return "Ben"
    else:
        return None

# Test the function
x = 3
nums = [4, 5, 1]
print(isWinner(x, nums))  # Output: "Maria" 