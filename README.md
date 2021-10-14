# Серијска комуникација

## Серијски порт
Серијски порт је врста рачунарског порта који се раније често користио за повезивање разних уређаја са рачунарима. Најчешће је кориштен за повезивање рачунарских мишева, рачунарских терминала и раних штампача али и других уређаја који данас углавном користе USB порт. Серијски порт користи RS-232 стандард за комуникацију, па се понекад назива и RS-232 порт. Такође постоје RS-422 и RS-485 стандарди.

Порт се може користити и за контролу уређаја и комуникацију са разним микроконтролерским развојним системима.

Раније је коришћен и за пренос фајлова између рачунара путем посебног серијског кабла. 

### Сигнали серијског порта

Стандардни серијски порт користи напонски ниво од -12 V за логичку јединицу а +12 V за логичку нулу, што је обрнуто од нормалне конвенције.

Ради лакше комуникације, пренесени битови нису само битови податка, већ постоје и СТАРТ, СТОП и ПАРИТЕТ (PARITY) битови.

Брзина рада се може подешавати са врло великим бројем бпс (бит по секунди) стања, неке од могућих брзина су:

    110, 300, 600, 1200, 2400, 4800, 9600, 14400, 19200, 28800, 38400, 57600 битова у секунди. 
    Неки серијски портови подржавају и брзине од 115200, 128000, и 256000 бпс. 
    Све брзине нису подржане од свих врста хардвера. Мање брзине омогућавају рад са већим дужинама серијског кабла.

Број битова података је 7 или 8, број старт битова 1, а стоп битова 0 до 2. Паритет може бити паран, непаран или непостојећи.

Број битова података је најчешће 8. Старт бит сигнализира уређају да се припреми за пријем података, пошто обара серијску линију са +12 на -12 волти. Стоп бит означава крај низа битова података, а паритет бит се користи за контролу исправности података. Оба се често изостављају. 

### Распоред пинова

Распоред пинова серијског порта се може видети у табели испод, за 9-пинске и 25-пинске конекторе. 
9-пински конектор је уведен на АТ (286) рачунарима током 1980-их година, као допуна тадашњем стандардном 25-пинском конектору, да омогући монтажу 2 серијска конектора на металну плочицу на картици.

Ознака | TxD | RxD | RTS | CTS | DSR | GND | DCD | DTR | RI 
--- | --- | --- | --- |--- |--- |--- |--- |--- |--- 
9-пински конектор | 3 | 2 | 7 | 8 | 6 | 5 | 1 | 4 | 9 
25-пински конектор | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 20 | 22 

### Објашњење пинова

- Излаз TxD (Transmit Data) Слање података
- Улаз RxD (Receive Data) Пријем података
- Излаз RTS (Request To Send) Захтев за слање
- Улаз CTS (Clear To Send) Спремност за слање
- Улаз DSR (Data Set Ready) Подаци спремни
- -GND (Ground) Минус сигнала
- Улаз DCD (Data Carrier Detector) Детектор носиоца података
- Излаз DTR (Data Terminal Ready) Уређај спреман
- Улаз RI (Ring Indicator) Индикатор звона

Приказ стандарног ДБ-9 конектора.

![Конектор](конектор.jpeg)


Модерне матичне плоче најчешће имају интегрисан један девет-пински серијски порт. У случају да плоча нема серијски порт, могуће је купити додатне картице са серијским портовима. 

## Коришћење серијског порта на рачунару (Linux)

У Linux оперативном систему, ознака првог порта је ttyS0, другог ttyS1 и тако даље. Популаран програм за коришћење порта у улози терминал емулатора је Minicom.
Приступ порту је могућ из већине програмских језика, као C, Python и других.

У програмском језику Python, контрола порта је једноставна уз помоћ pyserial библиотеке. Инсталација ове библиотеке се врши командама:

```bash
Инсталација за Python 3
pip3 install pyserial

Инсталација за Python 2
pip install pyserial
```
### Иницијализација серисјког порта 

На почетку је потребно импортовати библиотеке pyserial, struct и time.

```python
import serial 
import struct
import time
```
Затим се иницијализује серијски порт

```python
serial_port = serial.Serial('/dev/ttyS0', 115200, serial.EIGHTBITS, serial.PARITY_NONE, serial.STOPBITS_ONE)
```

### Приказ функције за слање поруке

```python
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
```
### Приказ функције за примање поруке

```python
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
```
