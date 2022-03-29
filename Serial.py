import serial 
import time

'''
koristimo serijski port ttyS0, baudrate komunikacije setujemo na 115200
'''

serial_port = serial.Serial('/dev/ttyS0', 115200, serial.EIGHTBITS, serial.PARITY_NONE, serial.STOPBITS_ONE) # инцијализација серијског порта на рачунару

#####################################################
'''                   За слање                    '''
##################################################### 
def send(message):
 
    if type(message) is str: # уколико је порука типа стринг, енкодује се у низ бајтова
        message = message.encode()
 
    try:
        
        serial_port.write(message) # слање поруке на дефинисани КОМ порт
        
        print(f"Message: {message} successfully sent to serial port.") # потврдна информација о послатој поруци      
    
    except KeyboardInterrupt:
            
        print("Process terminated via keyboard.") 
        serial_port.close() # затварање серијског порта
    
    except:

        print("Error while sending message to serial port, check if serial port is connected.")
        serial_port.close() # затварање серијског порта

#####################################################
'''                 За примање                    '''
#####################################################
def receive():

    receive = [] # листа за чување примљених порука

    while True:
        
        try:
        
            if serial_port.is_open: # провера да ли је порт отворен
            
                receive.append(serial_port.read()) # читање порука и смештање у листу
                
                print(f"Message: {receive} successfully received on serial port.")   
        
        except KeyboardInterrupt:
            
            print("Process terminated via keyboard.") 
            serial_port.close() # затварање серијског порта

        except:

            print("Error while reading serial port, check if serial port is connected.")  # povratna informacija o prekidu, ispisana u konzoli
            serial_port.close() # затварање серијског порта

#####################################################
'''                     Тест                      '''
#####################################################

def main():

    send("String")
    #send(20)
    time.sleep(5)

    #receive()
    #time.sleep(5)
    
if __name__ == "__main__":

    main()
