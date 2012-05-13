class RemoveDataFromEvents < ActiveRecord::Migration
  def self.up
    remove_column :events, :event_data
  end

  def self.down
    add_column :events, :event_date, :date
  end
end
