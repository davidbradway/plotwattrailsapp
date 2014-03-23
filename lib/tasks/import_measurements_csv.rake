require 'csv'
namespace :import_measurements_csv do
  task :create_incidents => :environment do
    #"code from the link"  
	filename="../assets/plotwatt_appliance_data.csv"
	CSV.foreach(filename, :headers => true) do |row|
	  Measurement.create!(row.to_hash)
	end
  end
end 
