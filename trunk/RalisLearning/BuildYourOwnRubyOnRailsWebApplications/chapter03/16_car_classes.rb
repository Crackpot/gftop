class Car
    # 类层变量
    @@wheels = 4
    @@number_of_cars = 0

    # 实例变量
    @mileage = 0

    # 初始化方法
    def initialize
        @@number_of_cars = @@number_of_cars + 1
    end

    # 写变量方法
    def mileage = (x)
        @mileage = x
    end
    def mileage
        @mileage
    end
end

# 类StretchLimo继承自Car
class StretchLimo < Car
    @@wheels = 6
    @@television = 1
    def turn_on_television
        puts "打开电视"
    end
end

class PontiacFirebird < Car
end

class VolksWagen < Car
end
