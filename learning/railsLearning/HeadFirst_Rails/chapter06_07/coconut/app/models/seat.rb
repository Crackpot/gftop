class Seat < ActiveRecord::Base
    belongs_to :flight
    def validate
        if name == flight_id
            errors.add_to_base("Your name is the same as your flight number")
        end

        # 行李重量
        if baggage > flight.baggage_allowance
            errors.add_to_base("You have too much baggage")
        end

        # 座位数
        if flight.seats.size >= flight.capacity
            errors.add_to_base("The flight is fully booked")
        end
    end
end
