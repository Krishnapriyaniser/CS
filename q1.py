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

















