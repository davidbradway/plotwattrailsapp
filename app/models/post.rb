class Post < ActiveRecord::Base
  # This line below was intended to plug a security vulnerability, but I got errors:
  #RuntimeError: `attr_accessible` is extracted out of Rails into a gem. Please use new recommended protection model for params(strong_parameters) or add `protected_attributes` to your Gemfile to use old one.
  #attr_accessible :title, :content
end
