#一个简单的闭包程序
def make_printer():
	msg = 'test'
	def printer():
		print(msg) #夹带私货（外部变量）
	return printer  #返回的是函数，带私货的函数
printer = make_printer()
printer()