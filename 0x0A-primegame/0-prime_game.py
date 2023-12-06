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
    def sieve_of_eratosthenes(limit):
        """ Core algorithm """
        primes = [True] * (limit + 1)
        primes[0] = primes[1] = False

        for i in range(2, int(limit**0.5) + 1):
            if primes[i]:
                for j in range(i * i, limit + 1, i):
                    primes[j] = False

        return [num for num, is_prime in enumerate(primes) if is_prime]

    def game_winner(n):
        """ Determines the winner """
        primes = sieve_of_eratosthenes(n)
        num_moves = [0] * (n + 1)

        for i in range(n, 1, -1):
            if i in primes:
                num_moves[i] = 1
                for j in range(i * 2, n + 1, i):
                    num_moves[j] += num_moves[i]

        return "Maria" if num_moves[1] % 2 == 0 else "Ben"

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = game_winner(n)
        if winner == "Maria":
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
