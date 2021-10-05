import serial 
import struct
import time

serial_port = serial.Serial('/dev/ttyS0', 115200, serial.EIGHTBITS, serial.PARITY_NONE, serial.STOPBITS_ONE) # inicijalizacija serijskog porta na racunaru 
'''
koristimo serijski port ttyS0, baudrate komunikacije setujemo na 115200
'''

#####################################################
'''                  Za slanje                    '''
##################################################### 
def send(message):
 
    message = list(message.split(' ')) # poruka se splituje po zarezu i konvertuje iz string-a u listu
    sendString = b'' # previks za bajt se dodaje poruci
    
    for elem in message:
        
        elem = int(elem) # elementi liste se konvertuju u integer
        sendString += struct.pack('!B', elem) # formatiranje poruka iz liste   
    
    try:
    
        serial_port.write(sendString) # slanje komande na serijski port
        
        print(f"Message: {sendString} successfully sent to serial port.") # povratna informacija o slanju poruke, ispisana u konzoli      
    
    except KeyboardInterrupt:
            
        print("Process terminated via keyboard.") # povratna informacija o primanju poruke, ispisana u konzoli
        serial_port.close() # zatvaranje serisjkog porta
    
    except:

        print("Error while sending message to serial port, check if serial port is connected.") # povratna informacija o prekidu, ispisana u konzoli
        serial_port.close() # zatvaranje serisjkog porta

#####################################################
'''                 Za primanje                   '''
#####################################################
def receive():

    receive = [] # lista za cuvanje primljenih poruka
    count = 0 # brojac

    while True:

        count += 1 # inkrementovanje brojaca
        
        try:
        
            if serial_port.is_open: # provera da li je serijski port "otvoren"
            
                receive.append(serial_port.read()) # primljene poruke se dodaju listi za cuvanje
                
                print(f"Message: {receive} successfully received on serial port.") # povratna informacija o primanju poruke, ispisana u konzoli
                print(f"Counter at: {counter}") # povratna informacija o stanju brojaca      
        
        except KeyboardInterrupt:
            
            print("Process terminated via keyboard.") # povratna informacija o prekidu od strane korisnika, ispisana u konzoli
            serial_port.close() # zatvaranje serisjkog porta

        except:

            print("Error while reading serial port, check if serial port is connected.")  # povratna informacija o prekidu, ispisana u konzoli
            serial_port.close() # zatvaranje serisjkog porta

#####################################################
'''                     Test                      '''
#####################################################

def main():

    send("1 2 5")
    time.sleep(5)

    #receive()
    #time.sleep(5)
    
if __name__ == "__main__":

    main()
