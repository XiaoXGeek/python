#计算BMI
sHight = input('请输入身高：')
hight = float(sHight)
sWeight = input('请输入体重: ')
weight = float(sWeight)
bmi = weight / (hight * hight)
if bmi < 18.5:
	print('%.2f  过轻' %bmi)
elif bmi <= 25:
	print('%.2f  正常' %bmi)
elif bmi <= 28:
	print('%.2f  过重' %bmi)
elif bmi <= 32:
	print('%.2f  肥胖' %bmi)
else:
	print('%.2f  严重肥胖' %bmi)