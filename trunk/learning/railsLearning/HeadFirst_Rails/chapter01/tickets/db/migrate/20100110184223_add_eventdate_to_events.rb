class AddEventdateToEvents < ActiveRecord::Migration
  def self.up
    add_column :events, :events_date, :date
  end

  def self.down
    remove_column :events, :events_date
  end
end
