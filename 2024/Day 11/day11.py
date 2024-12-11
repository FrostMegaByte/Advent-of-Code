# Part 1
with open("input.txt", "r") as file:
    line = file.readline()
    stones = list(line.split())
    
for blink in range(25):
    reordered_stones = []
    
    for stone in stones:
        if stone == "0":
            reordered_stones.append("1")
        elif len(stone) % 2 == 0:
            reordered_stones.append(str(int(stone[:len(stone)//2])))
            reordered_stones.append(str(int(stone[len(stone)//2:])))
        else:
            new_stone_value = int(stone) * 2024
            reordered_stones.append(str(new_stone_value))
    
    stones = reordered_stones
    
print(len(stones))

# Part 2 (Slow, not yet working. Need to optimize)
with open("small1.txt", "r") as file:
    line = file.readline()
    stones = list(line.split())
    
cached_stones = {}

for blink in range(75):
    reordered_stones = []
    
    def order_stones(stones: list[str]) -> list[str]:
        if len(stones) == 1:
            stone = stones[0]
            if stone in cached_stones:
                return cached_stones[stone]
            
            if stone == "0":
                cached_stones[stone] = ["1"]
                return ["1"]
            elif len(stone) % 2 == 0:
                cached_stones[stone] = [str(int(stone[:len(stone)//2])), str(int(stone[len(stone)//2:]))]
                return [str(int(stone[:len(stone)//2])), str(int(stone[len(stone)//2:]))]
            else:
                new_stone_value = int(stone) * 2024
                cached_stones[stone] = [str(new_stone_value)]
                return [str(new_stone_value)]
            
        
        if len(stones) > 1:
            mid = len(stones) // 2
            left_half = stones[:mid]
            right_half = stones[mid:]

            left = order_stones(left_half)
            right = order_stones(right_half)
            result = left + right
            return result

    reordered_stones = order_stones(stones)
    stones = reordered_stones
    
print(len(stones))