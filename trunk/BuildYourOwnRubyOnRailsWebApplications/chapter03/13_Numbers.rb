# 3.6.4 数字

# 返回数值的所属类
puts 123.class
puts 12.5.class

# integer? 当对象是个完全整数时返回真
puts 123.integer?
puts 12.5.integer?

# round 将数字就近取整
puts 12.3.round
puts 12.5.round
puts 12.6.round

# zero? 当数字等于0时返回真
puts 0.zero?
puts 8.zero?

# 此外还有Numric子类之间转换数字的方法。
# to_f将值转换成Float型
# to_i将值转换成Integer型
puts 11.to_f
puts 12.3456.to_i
