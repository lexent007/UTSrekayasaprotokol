import socket
import psutil

s= socket.socket()
host = ""
port = 12346

s.bind((host,port))
s.listen(5)

mem_use = psutil.virtual_memory()
print "Waiting conection from..."
while True:
		c, addr  = s.accept()
		instruksi = str(c.recv(1024))
		print ('Perintah Untuk') ,instruksi
		print ('Dari') , addr

		if instruksi == "mem":
			message_str= 'Total Memory :' + str(mem_use.total) \
			+' bytes\nAvailable    :' + str(mem_use.available) \
			+' bytes\nPercent      :' + str(mem_use.percent) + '%' \
			+' \nUsed Memory  :' + str(mem_use.used) \
			+' bytes\nFree Memory  :' + str(mem_use.free) +'bytes'
			c.send(message_str)

		c.close()

