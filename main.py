def power(a, b):
    if a <= 0 or b <= 0:
        return -1
    if b == 1:
        return a
    return a * power(a, b - 1)


# I assume that end is one bigger than the last allowed index.
def binary_search(numbers, num, start, end):
    # Stop when no possible indices are left.
    if start >= end:
        return -1

    # Fetch the middle element, to achieve overall logarithmic runtime even in the worst case.
    mid = (start + end) // 2
    num_at_mid = numbers[mid]

    # Recurse down to the first half, the second half, or find the correct number and stop.
    if num_at_mid > num:
        return binary_search(numbers, num, start, mid)
    if num_at_mid < num:
        return binary_search(numbers, num, mid + 1, end)
    return mid


class HashTable:
    def __init__(self, buckets):
        self.buckets = [[] for _ in range(buckets)]
        self.size = 0

    def __str__(self):
        return self.buckets

    def __my_hash(self, element):
        if isinstance(element, int):
            return element
        else:
            return len(element)

    def insert(self, element):
        self.buckets[self.__my_hash(element) % len(self.buckets)].append(element)
        self.size += 1

    def get_element(self, element):
        bucket = self.buckets[self.__my_hash(element) % len(self.buckets)]

        if element not in bucket:
            return False

        bucket.remove(element)
        self.size -= 1
        return element

    def get_number_elements(self):
        return self.size

    def get_size(self):
        return len(self.buckets)
