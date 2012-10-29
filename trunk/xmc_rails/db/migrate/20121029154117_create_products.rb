class CreateProducts < ActiveRecord::Migration
  def change
    create_table :products do |t|
      t.string :title
      t.text :description
      t.string :image_url
      t.decimal :price, :precision =>8, :scale =>2 #8位有效数字，其中小数点后有两位

      t.timestamps
    end
  end
end
