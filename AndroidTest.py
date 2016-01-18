
import sys
import os, fnmatch
import subprocess

class AndroidDebugBridge:

        package = ""
        activity = ""
        root_dir='B:/Web/Application'

        def __init__(self,pcapPath,pcapName):
                print('__init__')
                if not self.Test_Android_Application():
                        return
                self.pcapPath=pcapPath
                self.pcapName=pcapName
                #print(self.pcapPath)
                #print(self.pcapName)
                self.driverFunction();
                

        def call_adb(self,command):
                command_result = ''
                command_text = 'adb %s' % command
                results = os.popen(command_text, "r")
                while 1:
                    line = results.readline()
                    if not line: break
                    command_result += line
                return command_result

        def check_devices(self):
                result =  self.call_adb("devices")
                devices = result.partition('\n')[2].replace('\n', '').split('\tdevice')
                if not devices[0]:
                        return False
                else:
                        return [device for device in devices if len(device) > 2]
               

        def Test_Android_Application(self):
                #check if device connected                
                if not self.check_devices():
                        print("NO DEVICE CONNECTED !! ")
                        return False
                else:
                        print(self.check_devices())
                        return True


        def setActivity_Package(self,apk_address):
                command = "aapt dump badging %s" %apk_address
                print(command)
                aapt_result = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True).communicate()[0]
                lines = aapt_result.split("\n")
                myDic = {}
                for line in lines:
                        splitedline=line.split(":")
                        if len(splitedline)==2:
                                myKey,myValue=line.split(":")
                                myDic[myKey]=myValue
                AndroidDebugBridge.package = myDic['package'].split("'")[1]
                AndroidDebugBridge.activity = myDic['launchable-activity'].split("'")[1]
                print(AndroidDebugBridge.package)
                argument2 = self.root_dir+'\\AndroidTest.bat ' +AndroidDebugBridge.package+"/"+AndroidDebugBridge.activity +" " +AndroidDebugBridge.package+ " " + apk_address+" " + apk_address.replace("/","\\") +" "+self.pcapPath+" "+self.pcapName
                print(argument2)                                                                                                                                                                                        
                p = subprocess.Popen(argument2, shell=True).communicate()
                
        

        def driverFunction(self):
                for file in os.listdir(self.root_dir):
                        if file.endswith(".apk"):
                                print(self.root_dir+'/\"' + file+'\"')
                                self.setActivity_Package('\"'+self.root_dir+'/' + file+'\"')

                                               
                    
                 
def main():
        if len(sys.argv)!= 3:
                print ('usage: python AndroidTest.py --pcapfilePath --pcapfileName')
                sys.exit(1)
        else:
                obj=AndroidDebugBridge(sys.argv[1],sys.argv[2])
    
    


# Standard boilerplate to call the main() function.
if __name__ == '__main__':
  main()




