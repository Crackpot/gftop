# 3.4.4 继承
class Car
    @@wheels = 4
    def initialize
        puts "该对象的默认车轮数为#{@@wheels}"
    end
end

class StrechLimo < Car # StrechLimo继承自Car
    @@wheels = 6
    def turn_on_television
        puts '打开电视'
    end
end

larry = StrechLimo.new
larry.turn_on_television
