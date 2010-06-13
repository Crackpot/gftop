# 3.6 Ruby核心类

# 3.6.1 数组
# 定义一个数组并对其赋值
service_mileage = [
    5000,
    15000,
    30000,
    60000,
    100000
]
puts service_mileage # 输出该数组
puts service_mileage[0] # 输出数组中第一个元素
puts service_mileage[2] # 输出数组中第三个元素

# Ruby还有另外一个快捷方法，它允许我们从String列表创建一个数组，即%w()语法，这个方法可以免去使用很多的双引号
availabe_colors = %w( red green blue black )

puts availabe_colors # 输出该数组
puts availabe_colors[0] # 输出数组中第一个元素
puts availabe_colors[2] # 输出数组中第三个元素

puts availabe_colors.empty? # 输出数组是否为空

puts availabe_colors.size # 输出数组中的元素个数

# first和last，分别返回数组的第一个和最后一个元素
puts availabe_colors.first
puts availabe_colors.last

# delete，从数组中移除同名的元素并返回它
puts availabe_colors.delete "red"
puts availabe_colors # 输出该数组
puts availabe_colors.size # 输出数组中的元素个数
