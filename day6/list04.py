# 字符串的切片操作

# s = 'abcdefg'   s[2:5]  ---->cde

# 标号
list1 = ['杨超越','热巴','刘亦菲','杨幂','赵丽颖','刘亦菲','黑嘉嘉',100, 99.9]

print(list1)
print(list1[3])

# 列表也是支持切片
print(list1[3:6])   # 将截取的结果再次保存在一个列表中

print(list1[-1:])
print(list1[-3:-1]) 

print(list1[::2])  # 支持步长
print(list1[-5:-1:2]) # 支持负下标和步长

# 反方向
print(-1::-1) # 逆向从最后一位取所有
print(-1::-2) # 逆向从最后一位取所有，步长为2









 

