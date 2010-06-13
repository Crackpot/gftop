# 3.6.3 字符串

a_phrase = "The quick brown fox"
puts a_phrase

puts a_phrase.class

# 反斜杠，转义
puts 'I\'m a quick brown fox'
puts "Arnie said, \"I'm back!\""

# 指定包含引号的字符串文字的更简易的方法是使用%Q快捷方式
quoteString = %Q(Arnie said, "I'm back!")
puts quoteString

# String对象也支持使用Ruby表达式#{}将Ruby代码替换成字符串文字
puts "The current time is: #{Time.now}"

# String类也包含丰富的修改String对象的内嵌功能。下面有些很有用的方法：
# 1 gsub代替了在String内指定的模式
puts "The quick brown fox".gsub('fox', 'dog') # 将字符串中的fox用dog取代
# 2 include? 当包含其他指定的字符串时返回真
puts "The quick brown fox".include?('fox') # 字符串中是否包含有'fox'
# 3 length返回字符串中字符的长度
puts "The quick brown fox".length
# 4 slice返回字符串的一部分
puts "The quick brown fox".slice(0, 3) # 取出字符串中从0位置开始，向右数3个位置的部分子串
