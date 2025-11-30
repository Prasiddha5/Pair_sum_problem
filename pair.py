def find_pair(nums, target):
    seen = set()

    for num in nums:
        needed = target - num

        if needed in seen:
            print(f"Pair found ({num}, {needed})")
            return

        seen.add(num)

    print("Pair not found.")


nums = [8, 7, 2, 5, 3, 1]
target = 10

nums = [5, 2, 6, 8, 1, 9]
target = 12
find_pair(nums, target)