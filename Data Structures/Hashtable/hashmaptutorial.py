class HashMap(object):
    def __init__(self, size):
        """Initializing the list with the argument size for our HashMap"""
        self.data = [[]] * (size)
 
    def _hash(self, key):
        """Hash Function:
        marked as a private method in the Object"""
 
        # Initialize
        hash_value = 0
 
        # Iterating and generating hashed values using the logic below
        # Logic: Taking the initial value of 0 and adding to it the ASCII encoding for each character,
        # and multiplying by the index value. After that we are taking the modulus of the result using the
        # length of the array
        # This becomes our hashed value i.e. the index position of the input to be placed
        # in the output space
        for i in range(len(key)):
            hash_value = (hash_value + ord(key[i]) * i) % len(self.data)
 
        return hash_value
 
    def set(self, key, value):
        # Represents the index position where we want to store our data
        address = self._hash(key)
 
        if not self.data[address]:
            self.data[address] = []
        # If there is a collision of index value i.e. our hashed value
        # then simply add on to that array
        self.data[address].append([key, value])
        return self.data
 
    def get(self, key):
        # Getting the hashed value again, with the same hash function to locate the value
        # for the given key
        address = self._hash(key)
        # assigning the entire array to a variable in-order to operate later
        currentBucket = self.data[address]
 
        if currentBucket:
            # Iterating over the entire list to get the value
            for i in range(len(currentBucket)):
                # Check to retrieve the value
                if currentBucket[i][0] == key:
                    # If found, return the current bucket
                    return currentBucket[i][1]
 
        # If no value present
        return "Data Not Found"
 
    # In order to print the hashmap to see the structure
    def __str__(self):
        return "".join(str(item) for item in self.data)
 
 
# Instantiating from our Object Class with 50 buckets
myHash = HashMap(3)
 
# Setting the values to the hash table
myHash.set("john", 123)
myHash.set("peter", 567)
myHash.set("carrie", 898)
myHash.set("aravind", 908)

# print(myHash.get("aravind"))
 
# Printing the entire hash table
print(myHash)