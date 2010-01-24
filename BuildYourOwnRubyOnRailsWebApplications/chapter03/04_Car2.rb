# 对Car类的改写
class Car
    # 修改对象里程数
    def mileage=(x)
        @mileage = x
        puts "修改对象里程数为: #{@mileage}"
    end
    # 读出对象里程数
    def mileage
        @mileage
        puts "读出对象里程数为: #{@mileage}"
    end
end
# 创建对象
kitt = Car.new
kitt.mileage = 6032
kitt.mileage
