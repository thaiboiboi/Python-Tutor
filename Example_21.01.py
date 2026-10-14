# Class structure implementing a simple hash table, hash function
# and accompanying functionality:
class Hash_table:
    def __init__(self, number_of_slots):
        self.number_of_slots = number_of_slots
        self.slots = [[] for i in range(number_of_slots)]

    def simple_hash_function(self, key):
        str_key = str(key)
        n = len(str_key)
        total = 0
        for i in range(n):
            total += ord(str_key[i])
        return total % self.number_of_slots

    def append_to_table(self, key, value):
        hash_value = self.simple_hash_function(key)
        slot = self.slots[hash_value]
        n = len(slot)
        for i in range(n):
            if slot[i][0] == key:
                slot[i] = (key, value)
                return
        slot.append((key, value))

    def print_table(self):
        for i in range(self.number_of_slots):
            slot = self.slots[i]
            n = len(slot)
            for j in range(n):
                print("Slot", i, "Position", j, "Content =", slot[j])

    def search_table(self, key):
        hash_value = self.simple_hash_function(key)
        slot = self.slots[hash_value]
        n = len(slot)
        for j in range(n):
            if slot[j][0] == key:
                print("Key", key, "is found in Slot", hash_value,
                      "at position", j, "with content =", slot[j])
                return
        print("Key", key, "does not occur")

# Create a hash table with 11 slots:
table = Hash_table(11)
# Add tuples of the form (key, value):
table.append_to_table(12345, "Test1")
table.append_to_table("2a4zloj", "Test2")
table.append_to_table("125", "Test3")
table.append_to_table("a49loj", "Test4")
table.append_to_table("1s345", "Test5")
table.append_to_table("vghy9loj", "Test6")
table.append_to_table("14747h5", "Test7")
table.append_to_table("745zse54j", "Test8")
table.append_to_table("1274233445", "Test9")
table.append_to_table("254aadftj", "Test10")
# Print the hash table:
table.print_table()
print()
# Find two keys in the hash table:
table.search_table("vghy9loj")
table.search_table("11111")
