# 3.6.5 符号

# 在Ruby中，符号是一个文本标识符。类似字符串，使用文本创建符号，区别是符号前加一个冒号前缀。
:fox
puts :fox
puts :fox.class

# 使用符号而非字符串的主要好处是符号拥有较少的功能。在某些情况下可能是个优点。
# 例如，之前的Car_colors散列表可以重写如下：
car_colors = {
    :kitt => 'blue',
    :herbie => 'white',
    :larry => 'green',
    :batmobile => 'black',
}
puts car_colors
puts car_colors.keys
puts car_colors.values

# String类的对象可以转换成符号类，并且可以反过来转换：
puts "fox".to_sym.class
puts :fox.to_s.class
