#_*_utf:8_*_

class Node(object):
	'''节点'''
	def __init__(self, elem):
		self.elem = elem
		self.next = None

class SingleLinkList(object):
	'''单链表的实现'''
	def __init__(self, node = None):#设置默认头结点为空
		'''头结点，设置为私有'''
		self._head = node
	
	def is_empty(self):
		'''判断链表是否为空'''
		return self._head == None
	
	def length(self):
		'''链表长度'''
		cur = self._head #游标指针
		count = 0        #记录链表长度
		while cur is not None:   #可以直接用while cur，但是用上判断意思更明确
			count += 1
			cur = cur.next
		return count

	def travel(self):
		'''遍历整个链表'''
		cur = self._head #扫描游标指针
		while cur:
			print(cur.elem, end = " ")
			cur = cur.next

	def add(self, elem):
		'''链表头部增加元素，头插法，时间复杂度O(1)'''
		node = Node(elem)
		node.next = self._head
		self._head = node

	def append(self, elem):
		'''尾插法，最坏和平均时间复杂度为O(n)'''
		node = Node(elem)
		if self.is_empty():
			self.__head = node
		else:
			cur = self.__head
			while cur.next != None:
				cur = cur.next
			cur.next = node

	def insert(self, pos, item):
		'''指定位置添加元素 时间复杂度O(n)，顺序表为O(n) '''
		#:param pos 从0开始
		if pos < 0:
			self.add(item)
		elif pos >= self.length():
			self.append(item)
		else:
			pre = self.__head
			count = 0
			while count < (pos - 1):
				pre = pre.next
				count += 1
			#当循环退出后，pre指向pos-1位置
			node = Node(item)
			node.next = pre.next
			pre.next = node


	def remove(self, item):
		'''删除节点'''
		pre = self.__head

		if pre.elem == item:
			self.__head = pre.next
		else:
			while pre.next != None:
				if pre.next.elem == item:
					pre.next = pre.next.next
				else:
					pre = pre.next

	def conatain(self, item):
		'''查找节点是否存在 时间复杂度O(n)'''
		cur = self.__head
		while cur != None:
			if cur.elem == item:
				return True
			else:
				cur = cur.next
		return False

if __name__ == "__main__":

	link_list = SingleLinkList()
	print(link_list.is_empty())
	print(link_list.length())

	link_list.append(1)

	link_list.append(2)
	link_list.add(10)
	link_list.append(3)
	link_list.append(4)

	link_list.insert(-1, 9) 

	
	
	link_list.travel()









