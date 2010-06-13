if Car.count.zero?
    puts "No cars have been produced yet."
elsif Car.count >= 10
    puts "Production capacity has been reached."
else
    puts "New cars can still be produced."
end
