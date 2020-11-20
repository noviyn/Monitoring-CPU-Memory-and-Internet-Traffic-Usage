import psutil as psu
from time import sleep
	
rx = psu.net_io_counters().bytes_sent
tx = psu.net_io_counters().bytes_recv
	
sleep(1)
	
rx_new = psu.net_io_counters().bytes_sent
tx_new = psu.net_io_counters().bytes_recv

sent_interval = rx_new - rx
rec_interval = tx_new - tx
	
print("Kelompok 6")
print("Monitoring Penggunaan CPU, Memory, dan Internet Traffic")
print(" ")
print("CPU Usage = {}%".format(psu.cpu_percent()))
print("Memory Usage = {}%".format(psu.virtual_memory()[2]))
print("Internet Traffic : ")
print("Tx  = {0:0.2f}Kbps ; Rx = {1:0.2f}Kbps".format(sent_interval/1024,rec_interval/1024, end='\r'))
print(" ")
print("Selesai")
