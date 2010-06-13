class Car
    @@number_of_cars = 0
    def self.count
        @@number_of_cars
        puts "读取当前number_of_cars为: #{@@number_of_cars}"
    end
    def initialize
        @@number_of_cars += 1
        puts "number_of_cars自增为: #{@@number_of_cars}"
    end
end
kitt = Car
herbie = Car.new
batmobile = Car.new
Car.count
kitt.count
