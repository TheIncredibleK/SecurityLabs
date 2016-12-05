import Crypto.Hash.HMAC as hmac
secret_string = "MessageFromKeith"

maccer = hmac.new(secret_string)

plain_text_message = "Attack At Dawn"
maccer.update(plain_text_message)
hex_for_authenticity = maccer.digest().encode("HEX").upper()

sent_message = (plain_text_message, hex_for_authenticity)

######################################################################
#Above, the receiever recieves the message, and a hex value for them to check the authenticity of the message
#So it is assumed theknow the secret string 'MessageFromKeith'
######################################################################
print "If sender message is uncompromised"
print "Recieved HEX: " + hex_for_authenticity
reciever_hmac = hmac.new(secret_string)
reciever_hmac.update(sent_message[0])
generated_hex_for_authenticity = maccer.digest().encode("HEX").upper()
print "Generated HEX: " + generated_hex_for_authenticity

print "This message is genuine: " + str(generated_hex_for_authenticity == sent_message[1])
print "\nIn the case of a compromised message"
#######
# In the case of it being compromised
#######
false_plain_text = "Attack At Midnight"
false_message = (false_plain_text, hex_for_authenticity)
false_hmac = hmac.new(secret_string)
reciever_hmac.update(false_message[0])
false_hex_for_authenticity= false_hmac.digest().encode("HEX").upper()
print "Recieved HEX: " + hex_for_authenticity
print "Generated HEX: " + false_hex_for_authenticity
print "This message is genuine: " + str(false_hex_for_authenticity == false_message[1])


