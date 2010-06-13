# 3.3.3 Ruby中的标点

# 1.句号
# This is a comment. It doesn't actually do anything.
puts 1 # So is this, but this one comes after a statement.
fox = "The quick brown fox" # Assign to a variable
puts fox
puts fox.class
puts fox.length

# 2.连接语句
# 只执行最后一个命令
puts fox.class; puts fox.length; puts fox.upcase

# 3.圆括号的使用
puts fox.class()
puts "jumps over the lazy dog".insert(0, 'The quick brown fox ')

# 4.方法符
puts fox.upcase
puts fox
# 如果一个方法含有潜在的破坏特性(如，它直接修改了接收对象本身而不是其副本)，该方法常常以惊叹号(!)结尾。
puts fox.upcase!
puts fox # 由此看出，fox变量的内容被upcase!方法修改了。

# 问号，返回一个布尔值
puts fox.empty?
puts fox.is_a? String
