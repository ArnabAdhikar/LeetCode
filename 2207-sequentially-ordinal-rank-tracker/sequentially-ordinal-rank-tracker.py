class CString:
    def __init__(self,word):
        self.word=word
    
    def __lt__(self,other):
        return self.word>other.word
    
    def __eq__(self,other):
        return self.word==other.word
        
class SORTracker:
    def __init__(self):
        self.upperPart=[] #minHeap
        self.lowerPart=[] #maxHeap
        
    def add(self, name, score):
        name=CString(name)
		#first check if there is any element in minHeap
        if self.upperPart:
            upperScore,upperName=self.upperPart[0]
			#check if we got a better location than the i-1th location
            if (upperScore<score) or (upperScore==score and upperName.word>name.word):
                heapq.heappop(self.upperPart)
                heapq.heappush(self.upperPart,(score,name))
				#negative score used below because its a maxheap
                heapq.heappush(self.lowerPart,(-upperScore,upperName.word))
                
            else:
			#if not we just add the new location to lower part
                heapq.heappush(self.lowerPart,(-score,name.word))
        else:
		#if not we just add the new location to lower part
            heapq.heappush(self.lowerPart,(-score,name.word))             
    
    def get(self):
		#remove from the ith position
        score,name=heapq.heappop(self.lowerPart)
		#add to the upper part of the tracker or minHeap
        heapq.heappush(self.upperPart,(-score,CString(name)))
        return name
        
# Your SORTracker object will be instantiated and called as such:
# obj = SORTracker()
# obj.add(name,score)
# param_2 = obj.get()