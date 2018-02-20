

import socket
socket = socket.socket(socket. AF_INET , socket. SOCK_DGRAM )
message = []
operation = input (
"""
***2014/1/50710CT***
Math Server
select an operation to perform:
0 - Subtraction
1 - Addition
2 - Multiplication
3 - Division
4 - modulo
>_
"""
)
message.append( str(operation))
first_variable = input ( 'enter the first value:' )
second_variable = input ('enter the second value:' )
message.append(  str(first_variable))
message.append(  str(second_variable))
message = ','.join(message)
socket.sendto(message, ( 'localhost' , 1207))
server_result, server_address = socket.recvfrom( 3072 )
print ( 'server result: ' + server_result)
socket.close() ;



