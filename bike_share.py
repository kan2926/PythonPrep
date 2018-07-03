# /*
#   ******** Design a bike sharing service ********
#   
#   **** Part 1 - Bike Tracking ****
#   
#   A new bike sharing service, called SF Bike Share, wants to track bikes as they are checked out.
#   
#   For example, when Bike 1 is checked out, they store it in an array, like:
#   
#   [ 1 ]
#   
#   And when it is returned, they store it in the array again, like:
#   
#   [ 1, 1 ]
#   
#   In other words, a bike that is returned will always have a second entry in the array.
#   
#   For example:
#   
#   [1, 2, 7, 2, 1, 1, 1, 2, 1, 2, 1]
#   
#   Means that:
#   
#   Bike 1 was checked out and returned 3 times.
#   
#   Bike 2 was checked out and returned 2 times.
#   
#   Bike 7 was checked out, but not yet returned.
#   
#   Write a function that returns all bikes that are currently checked out.
#   
# */
from collections import Counter
def get_checked_out(arr): 
    
    if arr:
        
        cnt = Counter()
        for i in arr:
            cnt[i] += 1
        
        result = []
        for k,v in dict(cnt).items():
            if v %2 != 0:
                result.append(k)
        return result


arr = [1, 2, 7, 2, 1, 1, 1, 2, 1, 2, 1]
print(get_checked_out(arr))
    

# /*
# #  **** Part 2 - Object Design ****
  
#  # Design SF Bike Share.
  
#   #* SF Bike Share consists of many Bikes.
  
#   #* New Bikes should be able to be created and added to SF Bike Share.

#   #* Bikes should be able to be checked out and returned.
  
#   #* The function for seeing checked out bikes from Part 1 should be part of SF Bike Share.
    
#   #* On each Bike, you should be able to track how many times it has been checked out and returned. From the example in Part 1, this means that Bike 1 would show 3, Bike 2 would show 2, and Bike 7 would show 0.

#   #* To test your design, create Bike 1, Bike 2, and Bike 7. Then check out and return Bike 1 three times, Bike 2 two times. Check out but do not return Bike 7.
  
# */
class Bike_Share:
    bikes ={}
    checked_out = {}
    def __init__(self, num):
        self.bike_num = num
        self.bikes[num] = 1
        self.checked_out[num] = 0
        print(self.bikes)
    def check_out(self):
        if self.bikes[self.bike_num] == 1:
            self.bikes[self.bike_num] = 0
            self.checked_out[self.bike_num]  += 1
        else:
            print('bike already checked out')

    def return_bike(self):
        if self.bikes[self.bike_num] == 0:
            self.bikes[self.bike_num] = 1
        else:
            print('bike not checked out')
        

if __name__ == '__main__':
    b1 = Bike_Share(1)
    b2 = Bike_Share(2)
    b7 = Bike_Share(7)

    b1.check_out()
    b1.return_bike()
    b2.check_out()
    b2.return_bike()
    b2.check_out()
    b2.return_bike()    

    
    

