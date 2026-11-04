#定义字符串的三种方式
s1 = "Hello"  #双引号定义
s2 = 'Python'  #单引号定义
s3 = """
Hello:
      欢迎大家
      大家好
"""  #三引号定义（多行字符串）



print(s1)
print(s2)
print(s3)

#定义字符串
#转义字符\'    \"   \n  \t
#\'--->单引号-->表示单引号'
#\"--->双引号--->表示双引号"
#\n--->换行符--->开始新的一行
#\t--->制表符--->增加缩进，缩进一个制表符（ta b）的大小
me = 'It\'s very good'
print(me)

me1 = 'Hello \n Good morning'
print(me1)



#字符串拼接案例------->str(int数字)----〉将int类型数字转化为字符串
name = "zyk"
age = 18#这18是int类型
study = "软件工程"
hobby = "python"
print("大家好， 我是" + name + "，今年" + str(age) + "我学习的专业是" + study + "爱好" + hobby) 

#字符串格式化1---〉 %s  占位符
name = "zyk"
age = 18#这18是int类型
study = "软件工程"
hobby = "python"
print("大家好， 我是%s,今年 %s 岁 我学习的专业是 %s 爱好 %s" %(name,age,study,hobby) ) 

#字符串格式化2--->f"..{变量名/表达式}.."----->推荐方式(重点)
name = "zyk"
age = 18#这18是int类型
study = "软件工程"
hobby = "python"
print(f"大家好， 我是 {name},今年{age}岁 我学习的专业是{study} 爱好 {hobby}"  ) 