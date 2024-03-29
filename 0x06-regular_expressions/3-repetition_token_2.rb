#!/usr/bin/env ruby
#MINE
as = /(hbt+n)/ #NOTE: .scan explanation in file 1-repetition_token_0.rb
var = ARGV.join("")
#NOTE: <MORE EXPLANATION IN FILE: 1-repetition_token_0.rb>
var.scan(as) do |match| #.scan is a string method to scan for non-overlapping matches substrings
                        #then each substring is held by the 'match' variable
  puts match #prints each match
end
