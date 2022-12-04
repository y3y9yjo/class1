class Node:
    def __init__(self,value=None,next=None) -> None:
        self.value = value
        self.next = next

class LinkList:
    def __init__(self,root=None) -> None:
        self.root = root
    
    def add(self,node_value):
        if self.root == None:
            self.root = Node(node_value)
        else:
            temp = self.root
            while temp.next != None:
                temp = temp.next
            temp.next = Node(node_value)
    def dump(self):
        if self.root == None:
            print(None)
        changing_node = self.root
        print(changing_node.next)
        while changing_node != None:
            print(changing_node.value,end="->")
            changing_node = changing_node.next

if __name__ == "__main__":
    linklist_test = LinkList()
    while True:
        print("""
            添加:1
            顯示:2
            退出:9
        """)
        n = int(input())
        if n == 9 :
            break
        if n == 1:
            print("結束添加請打入leave")
            while True:
                node = input()
                if node == "leave":
                    break
                linklist_test.add(node)
        if n == 2:
            linklist_test.dump()


    


