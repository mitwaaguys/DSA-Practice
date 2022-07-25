class Heap:
    def __init__(self):
        self.heap_size=0
     
    def build(self, A, n):   
        self.length = n
        self.Arr = [None] * n
        for 1 to A.len:
            
        
	def left(self, i):
     return 2*i

	def right(self, i):
    	return 2*i+1

	def max_heapify (A, i):
    	l = left(i) #left of A
    	r = right(i) #right of A
    	if(A[l]<A.heap_size and A[l] <A[r]):
        	largest =l
    	else:
        	largest = i
         
    	if(r<A.heap_size and A[r] > A[largest]):
        	largest = r
    	if largest!=i:
        	A[i], A[largest] = A[largest], A[i]
			max_heapify(A, largest)

max_heapify
    
    