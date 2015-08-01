#Liguo Jiao
#Python Object Oriented Programming
#Binary search

class BinarySearch:
    def __init__(self, List):
        self.total = List
        
        self.left = 0
        self.right = len(List)-1
    
    def Start_Search(self, goal):
        NotFind = True
        temp = []
        Middle = 0
        while (self.left + 1 < self.right):
            Middle = (self.left + self.right)/2
            if self.total[int(Middle)] > goal:
                self.right = Middle
            else:
                self.left = Middle
        if self.total[int(self.left)] == goal:
            return int(self.left)
        else:
            return -1
        return 0
        

s=BinarySearch([2,31,42,56,89,99,1022,4532,454563,4534675]) #give a list of Number for search
print(s.Start_Search(2)) #return the int of the list postition.

#O(log2 n)