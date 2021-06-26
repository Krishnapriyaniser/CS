#linked list
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LL:
    def __init__(self):
        self.head=None
    def inserth(self,new):
        temp=self.head
        self.head=new
        self.head.next=temp
        del temp
    def insertat(self,new,position):
        currn=self.head
        currp=0
        while True:
            if currp==position:
                prenode.next=new
                new.next=currn
                break
            prenode=currn
            currn=currn.next
            currp=currp+1

    def insert(self,new): 
        if self.head is None:
            self.head=new
        else:
            last=self.head
            while True:
                if last.next is None:
                    break
                else:
                    last=last.next
            last.next=new
    
    def delend(self):
	last=self.head
	while last.next is not None:
	    pnode=last
	    last=last.next
	pnode.next=None   

    def delat(self,pos):
	curr=self.head
	currp=0
	while True:
	    if currp==pos:
		prenode.next=curr.next
		curr.next=None
		break
	    prenode=curr
	    curr=curr.next
	    currp=currp+1
    def delh(self):
	self.head=self.head.next
    def search(self,pos):
	curr=self.head
	currp=0
        while True:
	    if currp==pos:
		print(str(pos)+"-->"+curr.data)
	        break
	    curr=curr.next
	    currp=currp+1
    def rev(self):
	prev=None
	curr=self.head
	fwd=self.head.next
	while True:
	 
	    if fwd is None:
		curr.next=prev
	        prev=curr
		break
	    curr.next=prev
	    prev=curr
	    curr=fwd
	    fwd=fwd.next
	self.head=prev
    def pri(self):
        current=self.head
        while True:
            if current is None:
                break
            else:
                print(current.data)
                current=current.next


fnode=Node("john")
ll=LL()
ll.insert(fnode)
snode=Node('ben')
ll.insert(snode)
tnode=Node('jake')
ll.insert(tnode)
fo=Node('gia')
ll.inserth(fo)
er=Node('dia')
ll.insert(er)
qe=Node("nia")
ll.insert(qe)

fi=Node('tia')
ll.insertat(fi,3)
ll.delend()
ll.delat(1)
ll.delh()
ll.search(1)
ll.rev()
ll.pri()


#bubble sort
import random

min = 9
max = 99
count = 10

RandomListOfIntegers = [random.randint(min, max) for iter in range(count)]

print(RandomListOfIntegers)

# Code for Bubble Sort here 
def sor(num):
	for i in range(0,len(num)-1):
		for j in range(0,len(num)-1-i):
			if num[j]>num[j+1]:
				num[j],num[j+1]=num[j+1],num[j]
	
num=RandomListOfIntegers
sor(num)
print(num)

# quick sort
# Creating a list of 10 random integers. 
import random

min = 9
max = 99
count = 10

RandomListOfIntegers = [random.randint(min, max) for iter in range(count)]

print(RandomListOfIntegers)

# Code for Quick Sort here 

def parti(a,low,hi):
	piv=a[low]
	i=low+1
	j=low+1
	for j in range(low+1,hi):
		if a[j]<piv:
			a[i],a[j]=a[j],a[i]
			i=i+1
	a[low],a[i-1]=a[i-1],a[low]
	return(i-1)
def qs(a,low,hi):
	if low<hi:
		pp=parti(a,low,hi)
		qs(a,low,pp)
		qs(a,pp+1,hi)
a=RandomListOfIntegers
qs(a,0,len(a))
print(a)




#queue
class node():
    def __init__(self,val):
        self.next=None
        self.val=val

class q():
    def __init__(self):
        self.front=self.rear=None
    def empt(self):
        return self.rear==None
    def enq(self,val):
        item=node(val)
        if self.rear is None:
            self.front=self.rear=item
            return self.front.val
        
        self.rear.next=item
        self.rear=item
        return self.front.val
    def deq(self):
        if self.empt():
            return
        k=self.front
        self.front=k.next
        if self.front is None:
            self.rear=None
    def fnt(self):
        if self.empt():
            print('list is empty')
            return
        print ('front is'+ str(self.front.val))
    def rar(self):
        if self.empt():
            print('list is empty')
            return
        print('rear is '+str(self.rear.val))


qq=q()
print(qq.enq(3))
print(qq.enq(2))
qq.deq()
print(qq.enq(1))                                                                                                
print(qq.enq(4))
qq.fnt()
qq.rar()
qq.deq()
qq.deq()
qq.deq()
qq.fnt()
qq.rar()

#stacks

class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
class stack:
    def __init__(self):
        self.top=None
    def empt(self):
        if self.top is None:
            print('stack is empty')
        else:
            print('stack is not empty')
    def size(self):
        k=1
        a= self.top
        if self.top is None:
            k=0
            print(k)
           
        else:
            
            
            while a.next is not None:
                k=k+1
                a=a.next
        
            print(k)
    def insert(self,val):
        item=Node(val)
    
        a=self.top
        if a==None:
            
            self.top=item
            self.top.next=None
        else:
            item.next=self.top
            self.top=item
        
    def pop(self):
        if self.top==None:
            print("unable to pop")
        else:
            self.top=self.top.next
    def dis(self):
        if self.top is None:
            self.empt()
        else:
            print("top ="+str(self.top.val))


st=stack()
st.empt()
st.pop()
st.insert(1)
st.dis()
st.insert(2)
st.dis()
st.insert(3)
st.dis()
st.insert(4)
st.dis()
st.insert(5)
st.dis()
st.empt()
st.size()



