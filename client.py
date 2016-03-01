import sys

#Perhaps make this self distributional
#Make it pull NTRU.py from a server 
#Make it pull aes.py from a server
#Make it pull poly.py from a server

from NTRU import *
from config import *
import aes
import base64
import socket

class Client(object):

  def __init__(self):
    self. n = NTRU()
    self.pub, self.params = self.checkIfExists()

  def log(self, info, msg):
    print "[%s]: %s" % (info, msg)

  def checkIfExists(self):
    if not exists:
      return self.genKeys()
    else:
      return self.loadKeys()

  def genKeys(self):
    pub, params = n.genereateNTRUKeys()
    pwd = raw_input('Enter a STRONG password:')
    if len(pwd) > 6:
      print "Password is good"
    else:
      print "Retard alert. This application is not for you"
      sys.exit(1)
    return pub, params

  def saveKeys(self, pub, params):
    #-Make this AES password encrypted-#
    f = open('keys/pub.key' , 'w+')
    f.write(pub)
    f.close()
    f = open('keys/priv.key' , 'w+')
    f.write(priv)
    f.close()

  def loadKeys(self):
    return pub, params
    pass

  def passToAesKey(self, password):
    pass

  def initiateLogin(self):
    print "Login to Zeinet" #Ceniax?
    username = raw_input("Enter username")
    password = self.passToAesKey(raw_input("Enter password"))
    self.auth(username, password)
    self.username = username
    self.password = password
    self.loop()

  def aesEncrypt(self, key, msg):
    return base64.b64encode(aes.encryptData(aeskey, msg))

  def aesDecrypt(self, key, msg):
    return aes.decryptData(key, base64.b64decode(msg))

  def auth(self, username, password):
    pass

  def loop(self):
    pass

  def sendMessage(self, msg):
    aesMsg = base64.b64encode(aes.encryptData(self.server_aeskey, msg))
    aesParts = n.splitNthChar(7, aesMsg)
    encryptedParts = n.encryptParts(params, pub, aesParts)
    print encryptedparts
    #Join these parts
    #Form packet
    #Send packet
    pass

  def handlePacket(self, packet);
    pass

c = Client()
c.initiateLogin()

""" Example Usage
n = NTRU()
pub, params = n.generateNTRUKeys()
msg = "Hello world! I am intangere!"
aeskey = str(uuid.uuid4().hex)
aesMsg = base64.b64encode(aes.encryptData(aeskey, msg))
aesParts = n.splitNthChar(7, aesMsg)
encryptedParts = n.encryptParts(params, pub, aesParts)
decryptedParts = n.decryptParts(params, encryptedParts)
print "Pubkey: %s" % pub
print "Params: %s" % params
print "Message: %s" % msg
print "Aes Message: %s" % aesMsg
print "Ntru Parts: %s" % encryptedParts
print "Decrypted Message: %s" % decryptedParts
print "Decrypted Aes Message: %s" % aes.decryptData(aeskey, base64.b64decode(decryptedParts))
"""

