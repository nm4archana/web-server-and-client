from socket import *
from time import gmtime, strftime
import sys
import time

# Name - Neelipalayam Masilamani,Archana

# Code for Web Client

# Get the host from the input
serverHost = sys.argv[1]
# Get the port from the input
serverPort = int(sys.argv[2])

# Get the requested file in server from input
requestFile = sys.argv[3]
host = '%s:%s' %(serverHost,serverPort)

try:
	# Reference - Textbook
	# Creation of client socket
	client_socket = socket(AF_INET,SOCK_STREAM)
	#Initialize a TCP connection between client and server
	client_socket.connect((serverHost,serverPort))
	
	# Get the client details
	timeout = "Timeout: "+str(client_socket.gettimeout())
	address_family = "Address Family: AF_INET";
	socket_type = "Socket Type: SOCK_STREAM";
	peer_name = "Peer Name: "+ str(client_socket.getpeername()[0])
    # To calculate RTT
	startTime = time.time()
	  
        print strftime('\n%a, %d %b %Y %H:%M:%S\n', gmtime())
     # Reference - http://stackoverflow.com/questions/10114224/how-to-properly-send-http-response-with-python-using-socket-library-only   
     # create a header message to send to server as request
	header_text = {
	'Header' : 'GET /%s HTTP/1.1 ' %(requestFile),
	'Host': host,
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	'Accept-Language': 'en-us,en;q=0.5',
	}
	httpHeader = ''.join('%s:%s\r\n' %(header,header_text[header]) for header in header_text)
	# Request the server for the required file
	client_socket.send('%s' %(httpHeader))
	client_socket.send(timeout+"\r\n")
	client_socket.send(address_family+"\r\n")
	client_socket.send(socket_type+"\r\n")
	client_socket.send(peer_name+"\r\n")
	

# Catch any exception
except IOError:
	sys.exit(1)

appendMessage=''
#  To get the message returned from the server
returnMessage=client_socket.recv(1024)
#Append every returned message
while returnMessage:
	appendMessage += returnMessage
	returnMessage = client_socket.recv(1024)

totalTime = str(time.time() - startTime)
# Close the socket connection
client_socket.close()
#Print the message from the server on client
print 'Message From Server: \n%s\n'  %(appendMessage)
print 'RTT: %s sec\n' %(totalTime) 

