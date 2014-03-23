#Rails Plotwatt App

##Changes
- Did this (http://stackoverflow.com/questions/4410794/ruby-on-rails-import-data-from-a-csv-file)
- Added the CSV file to `lib/assets`
- Wrote a new Rakefile and put it in `lib/tasks`

##Rails Command Reference
```bash
sudo apt-get install rails

sudo gem install jquery-rails
sudo gem install coffee-rails
sudo gem update rails
sudo gem install bundler
sudo gem update -V
sudo gem install sqlite3
sudo gem install rb-libsvm

rails new railsPlotwattApp
cd railsPlotwattApp/

rails server
rails s

rails g controller posts
rails g model post
rails g model post title:string content:text
rails g model post title:string content:text --force
rails generate scaffold Measurement AlwaysOn:decimal HeatingAC:decimal Refrigeration:decimal Dryer:decimal Cooking:decimal Other:decimal DatetimeMidpoint:datetime
bundle exec rake db:migrate

rails console
rails c

git remote add origin git@bitbucket.org:davidbradway/plotwattrailsapp.git

history | grep rails
```

##Future Plans
Do charts next
Look here http://railscasts.com/episodes/223-charts
and here http://ankane.github.io/chartkick https://github.com/ankane/chartkick