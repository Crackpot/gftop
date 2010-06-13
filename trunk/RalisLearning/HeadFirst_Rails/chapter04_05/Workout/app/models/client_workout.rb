class ClientWorkout < ActiveRecord::Base

    # 验证输入金额为数值
    validates_numericality_of :paid_amount

    # 验证非空项
    validates_presence_of :client_name
    validates_presence_of :trainer
end
