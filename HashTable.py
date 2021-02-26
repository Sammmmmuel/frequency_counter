from LinkedList import LinkedList

class HashTable:

  def __init__(self, size):
    self.size = size
    self.arr = self.create_arr(size)


  def create_arr(self, size):
    arr = []

    for i in range(size):
      new_ll = LinkedList()
      arr.append(new_ll)

    return arr

# Still have to change this with your own hash function. Do not use this one unless you wanna lose hella points.
  def hash_func(self, key):
# gets the first letter of the word 
    first_letter = key[0]
    # The ord function returns the number representing the unicode code of a specified character. also known as the ascii value
    ascii_value = ord(first_letter)
    # i then mod the number with the size and get a number 
    index = ascii_value % self.size

    return index





  # 3️⃣ TODO: Complete the insert method.

  # Should insert a key value pair into the hash table, where the key is the word and the value is a counter for the number of times the word appeared. When inserting a new word in the hash table, be sure to check if there is a Node with the same key in the table already.
  
  def insert(self, key, value):

    # First find the index where key:val pair should be placed
    key_hash = self.hash_func(key)

    # Check if the "bucket/slot/index" is empty
    if self.arr[key_hash] == None:
      self.arr[key_hash] = (key, value)
      return key_hash

    # Else, in the case where there's collision
    else:
      
      ptr = (key_hash + 1) % self.size

      while ptr != key_hash:

        if self.arr[ptr] == None:
          self.arr[ptr] = (key, value)
          return ptr

        else:
          ptr = (ptr + 1) % self.size
      self.arr[key_hash].append((key,value))


      return key_hash



# See LinkedList.py, print_nodes()
  def print_key_values(self):
    
    for ll in self.arr:
      ll.print_nodes()




