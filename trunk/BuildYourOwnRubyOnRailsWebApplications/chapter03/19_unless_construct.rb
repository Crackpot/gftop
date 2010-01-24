# unless条件是if条件的否定版本。当某个特定条件不满足时，在执行某些语句的情况下是很有用的。
kitt = PontiacFirebird.new
kitt.mileage = 5667

herbie = VolksWagen.new
herbie.mileage = 33014

batmobile = PontiacFirebird.new
batmobile.mileage = 4623

larry = StretchLimo.new
larry.mileage = 20140

unless kitt.is_a?(StretchLimo)
    puts "This car is only licensed to seat two people."
end
