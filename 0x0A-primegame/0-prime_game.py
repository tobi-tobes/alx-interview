#!/usr/bin/python3
"""
0-prime_game.py
Maria and Ben are playing a game. Given a set of consecutive
integers starting from 1 up to and including n, they take turns
choosing a prime number from the set and removing that number and
its multiples from the set. The player that cannot make a move loses
the game.

They play x rounds of the game, where n may be different for each round.
Assuming Maria always goes first and both players play optimally, determine
who the winner of each game is.

  * Prototype: def isWinner(x, nums)
  * where x is the number of rounds and nums is an array of n
  * Return: name of the player that won the most rounds
  * If the winner cannot be determined, return None
  * You can assume n and x will not be larger than 10000
  * You cannot import any packages in this task
"""


def isWinner(x, nums):
    """ Determines the winner """
    def is_prime(num):
        """ Determines if a number is prime """
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def optimal_move(nums):
        """ Determines optimal move """
        for num in nums:
            if is_prime(num):
                return num
        return None

    maria_wins = 0
    ben_wins = 0

    for i in range(x):
        current_nums = list(range(1, nums[i] + 1))

        while True:
            maria_move = optimal_move(current_nums)
            if maria_move is None:
                ben_wins += 1
                break
            current_nums = [num for num in current_nums if num
                            % maria_move != 0]

            ben_move = optimal_move(current_nums)
            if ben_move is None:
                maria_wins += 1
                break
            current_nums = [num for num in current_nums if num % ben_move != 0]

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
