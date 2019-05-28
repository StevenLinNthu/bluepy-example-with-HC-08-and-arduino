from bluepy.btle import Scanner, DefaultDelegate, Peripheral
import threading

class ScanDelegate(DefaultDelegate): 
    def __init__(self): 
        DefaultDelegate.__init__(self)

    def handleDiscovery(self, dev, isNewDev, isNewData): 
        if isNewDev: 
            None
            #print ("Discovered device" + dev.addr) 
        elif isNewData: 
            print ("Received new data from"+ dev.addr)
            
    def handleNotification(self, cHandle, data):
        string = "Receive: " + bytes.decode(data)
        print(string)
        
        
def blue_scan():
    device_msg = [0,0]
    for dev in devices:
        for (adtype, desc, value) in dev.getScanData():
            res = value.find("HC-08") #your device
            if res < 0:
                None
            else:
                device_msg[1] = dev.addrType
                device_msg[0] = dev.addr
                print("%s %s %s" % (device_msg[0], value, device_msg[1]))
                break
    return device_msg
  
#scan for your device    
scanner = Scanner().withDelegate(ScanDelegate()) 
devices = scanner.scan(3.0)
remote = blue_scan()

#connect your device
print(remote) 
p = Peripheral(remote[0]) #remote[0]
p.setDelegate(ScanDelegate())

s = p.getServiceByUUID("0000ffe0-0000-1000-8000-00805f9b34fb")
c = s.getCharacteristics()[0]
 

def notification_thread():
    while True:
        if p.waitForNotifications(2.0):
            # handleNotification() was called
            continue
def send_thread():
    while True:
        cmd = input()
        tmp = c.write(bytes(cmd, "utf-8"), True)
        if tmp :
            print("Send: " +  cmd)
        
        
if __name__ == "__main__":
    t1 = threading.Thread(target = notification_thread)
    t2 = threading.Thread(target = send_thread)
    t1.start()
    t2.start()
