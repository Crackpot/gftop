# 3.4.3 类层功能
class Car
    # 在类层次上，类变量负责数据存储。它们通常用来存储状态信息，或是作为新对象配置默认值的方法。
    # 类变量通常设置在类体内，可以通过其前缀————双at符号(@@)来进行识别。
    @@number_of_cars = 0
    def initialize
        @@number_of_cars = @@number_of_cars + 1
        puts "number_of_cars自增为: #{@@number_of_cars}"
    end
end
kitt = Car
herbie = Car
