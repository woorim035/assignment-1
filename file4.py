print("assignment")

def find_min_max(lst):
    return min(lst), max(lst)

# 함수 호출
numbers = [1, 2, 3, 4, 5]
min_val, max_val = find_min_max(numbers)
print(f"리스트의 최소값: {min_val}, 최대값: {max_val}")