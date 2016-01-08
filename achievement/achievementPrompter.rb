require 'addressable/uri'
require 'open-uri'

def prompt(*args)
    print(*args)
    gets
end

text = prompt "Input the Achievement: "
text.strip!

email = prompt "Email address: "
email.strip!

# add the text with %20s instead of spaces
url = "http://www.achievement-maker.com/xbox/" + text.gsub(/ /, '%20')

# build the uri
uri = Addressable::URI.parse(url)
uri.query_values = {
  'header'  => 'ACHIEVEMENT UNLOCKED',
  'email' => email
}

stringURI = uri.to_s

# get the thing
open('achieve.png', 'wb') do |file|
  file << open(stringURI).read
end

