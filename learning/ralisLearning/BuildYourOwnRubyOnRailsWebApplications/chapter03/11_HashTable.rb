# 3.6.2 散列表

# 相当于python中的元组
car_colors = {
    'kitt' => 'blue',
    'herbie' => 'write',
    'batmobile' => 'black',
    'larry' => 'green',
}

# 查询新建立的散列表时，必须在方括号内写入如下要查询条目的键值：
puts car_colors['kitt']

# 判断散列表car_colors是否为空
puts car_colors.empty?

# 输出散列表中元素的个数
puts car_colors.size

# keys,像数组一样返回散列表中的所有键值
puts car_colors.keys

# values,返回像数组一样的所有值，要注意元素的顺序（在散列表中的键值是以优化存储和获取的方式排序的，这一顺序并不能反映它们的输入顺序）
puts car_colors.values
