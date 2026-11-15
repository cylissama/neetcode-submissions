class MyHashSet:
    # Keys are always >= 0, so negative values are safe sentinels.
    _EMPTY = -1    # slot has never been used
    _DELETED = -2  # tombstone: slot held a key that was removed

    def __init__(self, capacity: int = 8):
        self._slots = [self._EMPTY] * capacity
        self._size = 0   # live keys
        self._used = 0   # live keys + tombstones

    def _probe(self, key: int):
        """Yield slot indices to check for key, in linear-probing order."""
        n = len(self._slots)
        start = key % n
        for offset in range(n):          # at most one full lap
            yield (start + offset) % n

    def _insert(self, key: int) -> None:
        """Place a key that is known not to be in the table."""
        for i in self._probe(key):
            slot = self._slots[i]
            if slot < 0:                 # EMPTY or DELETED: both are reusable
                if slot == self._EMPTY:
                    self._used += 1      # reusing a tombstone doesn't change _used
                self._slots[i] = key
                self._size += 1
                return

    def _resize(self, new_capacity: int) -> None:
        old_slots = self._slots
        self._slots = [self._EMPTY] * new_capacity
        self._size = 0
        self._used = 0
        for key in old_slots:
            if key >= 0:                 # copy only live keys; tombstones are dropped
                self._insert(key)

    def add(self, key: int) -> None:
        if self.contains(key):
            return
        # Resize when load would exceed 0.7. Integer math avoids floats.
        if (self._used + 1) * 10 > len(self._slots) * 7:
            self._resize(len(self._slots) * 2)
        self._insert(key)

    def remove(self, key: int) -> None:
        for i in self._probe(key):
            slot = self._slots[i]
            if slot == self._EMPTY:      # an empty slot ends the search: key isn't here
                return
            if slot == key:
                self._slots[i] = self._DELETED   # tombstone, not EMPTY
                self._size -= 1
                return

    def contains(self, key: int) -> bool:
        for i in self._probe(key):
            slot = self._slots[i]
            if slot == self._EMPTY:
                return False
            if slot == key:
                return True              # tombstones are skipped by falling through
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)