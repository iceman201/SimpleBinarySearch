class SelectionSort:
    
    def __init__ (self, List):
        self.minimum = 0
        self.total=List
    def swap(self, left, right):
        temp = left
        t_index = self.total.index(left)
        t2_index = self.total.index(right)
        
        self.total[t_index] = right
        self.total[t2_index] = temp
        
    def Selection(self):
        i = 0
        j = 0
        for j in range(len(self.total)):
            i = j + 1
            for i in range(len(self.total)):
                if self.total[i] < self.total[j]:
                    self.swap(self.total[j],self.total[i])
            j+=1
            i+=1
        
    
    
s = SelectionSort([2,4,23,76,555,6,5])
s.Selection()
print(s.total)
