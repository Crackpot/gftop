# 3.4 在Ruby中使用面向对象编程
class Car
    @mileage = 0
    # 写方法
    def set_mileage(x)
        @mileage = x
        puts "修改对象里程数为: #{@mileage}"
    end

    # 读方法
    def get_mileage
        @mileage
        puts "读出对象里程数为: #{@mileage}"
    end

    # 开动方法
    def open_trunk
        # code to open trunk goes here
        puts "开动trunk"
    end
end
kitt = Car.new
kitt.set_mileage(5667)
kitt.get_mileage
kitt.open_trunk
