
def solution(arr, target):
    for i in range(len(arr)):
        for j in range(0, len(arr)):
            if arr[i] + arr[j] == target:
                return [i, j]
    return None
