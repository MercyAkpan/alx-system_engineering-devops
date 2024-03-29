#!/usr/bin/env ruby
#MINE
as = /(hbt{2,5}n)/ #NOTE:.scan(line-9), returns array of captured indivdual groups
#so /(hbt{2,5}n)/, gives array of -[substring]
#and /(hb(t){2,5}n)/, gives an array(var) of --[substring, t], as "t", is an individual, 
#capturing group.
var = ARGV.join("")
#puts (var)
#puts (var)
#This joins all C-L args into a string (var).ARGV is an array of strings. Var is of
#type <string>
var.scan(as) do |match| #.scan is a string method to scan for non-overlapping matches substrings
                                                #then each substring is held by the 'match' variable
  puts match #prints each match
end
