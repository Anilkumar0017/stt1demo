

from dataclasses import dataclass
from typing import Iterable, List


@dataclass(frozen=True)
class Stats:
    
    count: int
    total: int
    minimum: int
    maximum: int

    @property
    def mean(self) -> float:
        
        if self.count == 0:
            return 0.0
        return self.total / self.count


def is_prime(n: int) -> bool:
    
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def fibonacci(k: int) -> List[int]:
   
    if k < 0:
        raise ValueError("k must be >= 0")
    seq: List[int] = []
    a, b = 0, 1
    for _ in range(k):
        seq.append(a)
        a, b = b, a + b
    return seq


def summarize(nums: Iterable[int]) -> Stats:
   
    values = list(nums)
    if not values:
        return Stats(count=0, total=0, minimum=0, maximum=0)
    return Stats(
        count=len(values),
        total=sum(values),
        minimum=min(values),
        maximum=max(values),
    )


def main() -> None:
   
    nums = list(range(1, 21))
    primes = [n for n in nums if is_prime(n)]
    fib = fibonacci(10)
    stats = summarize(nums)

    print("Numbers:", nums)
    print("Primes:", primes)
    print("Fibonacci:", fib)
    print("Stats:", stats, "Mean:", round(stats.mean, 2))


if __name__ == "__main__":
    main()
