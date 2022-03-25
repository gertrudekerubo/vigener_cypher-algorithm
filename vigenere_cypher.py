alphabet="a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z"
letter_to_index =dict(zip(alphabet,range(len(alphabet))))
index_to_letter =dict(zip(range(len(alphabet)),alphabet))
def encrypt(message, key):
	encrypted =""
	#split the message to the lenght of the key
	split_message=[message[i:i+len(key)]for i in range(0, len(message),)]
	# want to convert the message to index and add the key(mod 26)
	# write encrypted text message

	pass 
	def decrypt(cipher, key):
		#split the cipher to the lenght of the key
		#convert cipher to index and subtract the key(mod 26)
		#write decrypted message text

		pass
		def main():
			pass
