import random

print("=" * 40)
print("       🍀 오늘의 행운 번호 🍀")
print("=" * 40)

for i in range(1, 6):
    pool = random.sample(range(1, 46), 7)
    numbers = sorted(pool[:6])
    bonus = pool[6]
    nums_str = "  ".join(f"{n:2d}" for n in numbers)
    print(f"  {i}세트 | {nums_str}  +보너스: {bonus:2d}")

print("=" * 40)
