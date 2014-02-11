class Post < ActiveRecord::Base
  # This line below was intended to plug a security vulnerability, but I got errors:
  #RuntimeError: `attr_accessible` is extracted out of Rails into a gem. Please use new recommended protection model for params(strong_parameters) or add `protected_attributes` to your Gemfile to use old one.
  #attr_accessible :title, :content

  validates :title, :content, :presence => true
  validates :title, :length => { :minimum => 2 }
  validates :title, :uniqueness => { :message => "title taken" }
end
