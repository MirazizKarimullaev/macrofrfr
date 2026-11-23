import random
import time
hi = int(input("give me year"))
data = []
for i in range(hi):
    data.append(i+1)


def is_sorted(sub_arr):
  return all(sub_arr[i] <= sub_arr[i + 1] for i in range(len(sub_arr) - 1))


def progressive_bogosort(arr):
  attempts = 0

  while True:
    attempts += 1
    random.shuffle(arr)

    # Check progressively: first 1 element, then 2, then 3, up to the full list
    for length in range(1, len(arr) + 1):
      if not is_sorted(arr[:length]):
        # Failed at this length! Break out and restart from length 1
        break
    else:
      # The loop finished all lengths without breaking — the whole list is sorted!
      print(f"Sorted in {attempts} attempts!")
      return arr


# Example usage
data = [4, 2, 7, 1, 3]
sorted_data = progressive_bogosort(data)
print("Result:", sorted_data)
