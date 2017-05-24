#计算 ax2 + bx + c = 0 的根
import math
def quaaratic(a, b, c):
	d = b*b - 4*a*c ;
	if d < 0:
		print('这个方程没有根！');
		return
	else:
		t = ((-b + math.sqrt(d)) / 2*a*b, (-b - math.sqrt(d)) / 2*a*b)
		return t