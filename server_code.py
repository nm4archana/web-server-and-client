# Name - Neelipalayam Masilamani, Archana

from socket import *
import threading
import os
import sys

port = int(sys.argv[1])
# Code for Web Server
def getFile(name, connectionSocket):
	try:
		print name;
		#Recieve the message from the client
 		message =  connectionSocket.recv(1024)
 		#Printing the message on the server
 		print message
 		#To get the file name
 		filename = message.split()[1]
	
		filename = "."+filename
		print "Filename  :%s" %filename
		#To open and read the file
 		f = open(filename)
 		outputdata = f.read()

 		#Print the message in the file
		print outputdata
		
		#print  str(getaddrinfo(gethostname(), 8900))

		#Get the details like Timeout,Socket Family, Socket Type,Peer Name
		timeout = "Timeout: "+str(connectionSocket.gettimeout())
		address_family = "Address Family: AF_INET";
		socket_type = "Socket Type: SOCK_STREAM";
		peer_name = "Peer Name: "+ str(connectionSocket.getpeername()[0])
  		

		#Send success message to client
 		connectionSocket.send("HTTP/1.1 200 OK\r\n")
 		connectionSocket.send(message + "\r\n")
 		
 		#Sending the file read to the client
 		for i in range(0, len(outputdata)):
  			connectionSocket.send(outputdata[i])	
			
		#Close the connection	
		connectionSocket.close()

	#If there is any exception
	except IOError:
 		
 		#Sending a bad request if there is exception
		connectionSocket.send("HTTP/1.1 404 Bad Request\r\n")
		connectionSocket.send("\r\n")
		connectionSocket.send("<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n")
 		
 		#Close the connection
 		connectionSocket.close()

#https://docs.python.org/2/library/socketserver.html
def Main():
	
    # Reference - Text book
    #Creates a server socket and sets socket type and family
	serverSocket = socket(AF_INET, SOCK_STREAM);
	print 'Hostname is: ', gethostname();

     #Associate port number with the created socket
	serverSocket.bind(('', port))
	serverSocket.listen(5)
	
	count =1
	while True:


 		print '\nReady to serve...'
 		# Created a new socket in the server
		connectionSocket, addr = serverSocket.accept() 
		
 		print 'Connected from :' + str(addr)		
		try:
			#Creates thread for each request
			t = threading.Thread(target=getFile, args=("Connection : "+str(count),connectionSocket))
			t.start()
			count += 1
        #Prints error message on any exception during thread execution   
		except:
			print "Error: Not able to start the thread"
    #Close the server socket connection
	serverSocket.close()

if __name__ == '__main__':
	Main()	
