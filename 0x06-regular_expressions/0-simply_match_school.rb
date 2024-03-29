#!/usr/bin/env ruby

as = /(School)?/
string = ARGV
string.each do |arg|
  puts "#{arg}"
#puts "#{as}"
  if arg =~ as  # Replace with your desired pattern
    print "true\n"
  end
end
