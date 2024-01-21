class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        key_hash = self.hash_function(key)
        key_value = [key, value]

        if self.table[key_hash] is None:
            self.table[key_hash] = list([key_value])
            return True
        else:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.table[key_hash].append(key_value)
            return True

    def get(self, key):
        key_hash = self.hash_function(key)
        if self.table[key_hash] is not None:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    def delete(self, key):
        key_hash = self.hash_function(key)
        if self.table[key_hash] is not None:
            for i, pair in enumerate(self.table[key_hash]):
                if pair[0] == key:
                    del self.table[key_hash][i]
                    return True
        return False


def main():
    hash_table = HashTable(size=10)

    hash_table.insert("key1", "value1")
    hash_table.insert("key2", "value2")
    hash_table.insert("key3", "value3")

    assert hash_table.get("key1") == "value1"
    assert hash_table.get("key2") == "value2"
    assert hash_table.get("key3") == "value3"

    hash_table.delete("key2")

    assert hash_table.get("key1") == "value1"
    assert hash_table.get("key2") is None
    assert hash_table.get("key3") == "value3"

    result = hash_table.delete("key4")
    assert not result

    print("Тестування пройшло успішно.")


if __name__ == "__main__":
    main()
