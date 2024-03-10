class HashMap(object):
    def __init__(self, size):
        self.data = [[]] * (size)


#  this below given hash function is  muted because , it serves only when the given key is of str type
    # def _hash(self, key):
    
    #     hash_value = 0
        
    #     for i in range(len(key)):
    #         hash_value = (hash_value + ord(key[i]) * i) % len(self.data)
 
    #     return hash_value


# now this below given hash function will work perfectly for any key irrespective of its datatype
    def _hash(self, key):
        return hash(key) % len(self.data)

 
    def set(self, key, value):
        
        address = self._hash(key)
        if not self.data[address]:
            self.data[address] = []
        
        self.data[address].append([key, value])
        return self.data      
    

 
    def get(self, key):
        
        address = self._hash(key)
        
        currentBucket = self.data[address]
 
        if currentBucket:
            
            for i in range(len(currentBucket)):
                
                if currentBucket[i][0] == key:
                    
                    return currentBucket[i][1]
 
       
        return "Data Not Found"

    
    def delete(self, key):
    
        address = self._hash(key)
        
        currentBucket = self.data[address]
    
        if currentBucket:
            
            for i in range(len(currentBucket)):
                
                if currentBucket[i][0] == key:
                    
                    self.data[address].pop(i)
                    return key
    
        
        return "Data Not Found"
 
    
    def __str__(self):
        return "".join(str(item) for item in self.data)
 
 

myHash = HashMap(2)
 
myHash.set("john", 123)
myHash.set("peter", 567)
myHash.set("carrie", 898)
myHash.delete("carrie")
# myHash.set("carrie", 123)
# print(myHash.get("carrie"))


print(myHash)
