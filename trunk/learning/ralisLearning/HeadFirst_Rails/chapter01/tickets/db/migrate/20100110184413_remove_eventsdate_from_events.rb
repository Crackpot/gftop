class RemoveEventsdateFromEvents < ActiveRecord::Migration
  def self.up
    remove_column :events, :events_date
  end

  def self.down
    add_column :events, :events_date, :date
  end
end
