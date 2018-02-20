import socket
socket = socket.socket(socket. AF_INET , socket. SOCK_DGRAM )
server_address = ( 'localhost' , 1207 )
print ( 'Server waiting for connection' )
socket.bind(server_address)
def math (message):
message = message.split( ',' )
operation = message[0]
first_variable = int(message[1])
second_variable = int(message[2])
if operation == '0' :
return first_variable - second_variable
elif operation == '1' :
return first_variable + second_variable
elif operation == '2' :
return first_variable * second_variable
elif operation == '3' :
return first_variable / second_variable
elif operation == '4' :
return first_variable % second_variable
else:
print ('PLS SELECT A VALID OPERARION (subtract=0, add=1, multiply=2, divide=3, mod=4)' )
while True :
print('waiting for a connection' )
client_message, client_address = socket.recvfrom( 3072 )
result =str(math(client_message))
socket.sendto(result, client_address)
print ('Result forwarded!')
