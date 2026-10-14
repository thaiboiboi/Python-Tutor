    class Hash_table:
    def __init__(self, slot_num):
        self.slot_num = slot_num
        self.slot = [[] for i in range(slot_num)]

    def simple_hash_function(self, key):
        str_key = str(key)
        n = len(str_key)
        total = 0
        for i in range(n):
            total += ord(str_key[i])
        return total % self.slot_num

    def append_to_table(self, key, value):
        hash_value = self.simple_hash_function(key)
        slot = self.slot[hash_value]
        n = len(slot)
        for i in range(n):
            if slot[i][0] == key:
                slot[i] = (key, value)
                return
        slot.append((key, value))

    def print_table(self):
        for i in range(self.slot_num):
            slot = self.slot[i]
            n = len(slot)
            for j in range(n):
                print("Slot", i, "Position", j, "Content =", slot[j])

    def search_table(self, key):
        hash_value = self.simple_hash_function(key)
        slot = self.slot[hash_value]
        n = len(slot)
        for j in range(n):
            if slot[j][0] == key:
                print("Key", key, "is found in SLot", hash_value, "at position", j, "with content", slot[j])
                return
            print("Key", key, "does not occur")

table = Hash_table(11)
#Add tuples of the form (key, value):
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

table.print_table()
print()

table.search_table("a49loj")
table.search_table("gsd874")

