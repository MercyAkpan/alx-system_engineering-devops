#!/usr/bin/env ruby
#MINE
as = /hb(t){2,5}n/
var = ARGV.join("")
#puts (var)
#This joins all C-L args into a string (var).ARGV is an array of strings. Var is of
#type <string>
var.scan(as) do |match| #.scan is a string method to scan for non-overlapping matches substrings
                                                #then each substring is held by the 'match' variable
#  print match #prints each match
end
