from configuracoes.configs import color
import random, os, smtplib, random, string, sys, subprocess, time, threading
from threading import Thread
from wifi import Cell


class NetworkScanner(object):
    ips_online=[]
    threads=[]

    def scannear_rede(self, ip_inicial, ip_final):
        ip_base=subprocess.getoutput("echo %s 2> /dev/null | egrep -o \"([0-9]{1,3}\.){3}\"" % ip_inicial)
        ip_inicial=int(subprocess.getoutput("echo %s 2> /dev/null | egrep -o \"([0-9]{1,3})$\"" % ip_inicial))
        ip_final=int(ip_final)
    
        while(ip_inicial <= ip_final):
            ip=ip_base+str(ip_inicial)
            self.threads.append(threading.Thread(target=self.ping, args=(ip,)).start())
            ip_inicial += 1
    
    def ping(self, ip):
        time.sleep(0.2)
        ping = os.system('ping -c 1 %s > /dev/null 2> /dev/null' % ip)
        
        if(ping==0):
            mac_adress=subprocess.getoutput("arp -a %s 2> /dev/null | egrep -o \"([a-Z,0-9]{2}\:){5}[a-Z,0-9]{2}\"" % ip)
            self.ips_online.append((ip,mac_adress,))
        while(len(self.threads)==0):
            time.sleep(0.5)
        self.threads.pop()
        
        print("\n\n*****************\nTHREADS EXISTENTES >> %s\n*****************\n" % len(self.threads))
        
        return 
      
   