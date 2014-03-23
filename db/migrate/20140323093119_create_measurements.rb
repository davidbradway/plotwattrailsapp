class CreateMeasurements < ActiveRecord::Migration
  def change
    create_table :measurements do |t|
      t.decimal :AlwaysOn
      t.decimal :HeatingAC
      t.decimal :Refrigeration
      t.decimal :Dryer
      t.decimal :Cooking
      t.decimal :Other
      t.datetime :DatetimeMidpoint

      t.timestamps
    end
  end
end
