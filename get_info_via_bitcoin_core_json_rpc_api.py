from bitcoin.rpc import RawProxy

# create a connection to local Bitcoin core node 

p = RawProxy()

# Run the getinfo command, store the resulting data in info 

info = p.getinfo()

#Retrive the 'blocks' element from the info 


print(info['blocks'])




