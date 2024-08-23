""" 
insert(key,value)
get(key) -> value
delete(key)
"""


class HashTable:
    def __init__(self, size):
        self.size = size
        self.create_hash_table(size)

    def create_hash_table(self, size):
        self.hash_table = [[] for _ in range(self.size)]

    """ 
    insert key and value pair into hashtable. If key already exists, update its value
    """

    def insert(self, key, value):
        print("Hash table before inserting", self.hash_table)
        hash_val = hash(key) % self.size
        print("hash Value", hash_val)
        bucket = self.hash_table[hash_val]
        print("Bucket value middle ", bucket, len(bucket))
        isFound = False
        idx = -1
        for i in range(len(bucket)):
            stored_key, stored_val = bucket[i]
            if stored_key == key:
                isFound = True
                idx = i
                break
        if isFound:
            self.hash_table[hash_val][idx] = (key, value)
        else:
            self.hash_table[hash_val].append((key, value))
        print("Hash table after inserting ", self.hash_table)

    """ 
    Given a key get its value if exists else return error message
    """

    def get(self, key):
        hash_val = hash(key) % self.size
        bucket = self.hash_table[hash_val]
        for k, v in bucket:
            if k == key:
                return v

        return "Key not found " + str(key).capitalize()

    """ 
    Takes a key and deletes it from hashtable if it exists else prints an error message
    """

    def delete(self, key):
        hash_val = hash(key) % self.size
        bucket = self.hash_table[hash_val]
        isFound = False
        idx = -1
        for i in range(len(bucket)):
            k, v = bucket[i]
            if k == key:
                isFound = True
                idx = i
                break
        if isFound:
            del self.hash_table[hash_val][idx]
        else:
            print("No key found ")


hashtable = HashTable(10)
hashtable.insert("Moin", 99)
hashtable.insert("zara", 98)
print(hashtable.get("Moin"))  # should output 98
print(hashtable.get("zara"))
# hashtable.insert("zara", 97)
# print(hashtable.get("zara"))
hashtable.delete("Moin")
hashtable.delete("Mohsin")
print(hashtable.get("Moin"))
print(hashtable.size)
