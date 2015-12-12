#####################
#Copyright Intangere#
#####################

from ntru import *
import random
from random import randint
import aes, base64
import uuid
import string
import re

class NTRU(object):

	def __init__(self):
		self.ranPol=[-1,-1,1,1]
		self.d = randint(3,6)
		self.d1 = self.d+1
		self.f = self.randfArray(randint(6,20))
		self.g = self.randgArray(randint(7,20))
		self.idxs = {x:i for i,x in enumerate(string.printable)}
		self.ridxs = {i:x for i,x in enumerate(string.printable)}

	def randfArray(self, l):
		f = []
		for x in range(0,self.d1):
			f.append(1)
		for x in range(0,self.d):
			f.append(-1)
		while len(f) < l:
			f.append(0)
		random.shuffle(f)
		print f
		print self.d
		return f				

	def randgArray(self, l):
		g = []
		for x in range(0,self.d):
			g.append(1)
		for x in range(0,self.d):
			g.append(-1)
		while len(g) < l:
			g.append(0)
		random.shuffle(g)
		return g			

	def RandomPrime(self, min, max):
  		while True:
    			n = random.randint(min, max)
			if n % 2 == 0:
      				continue;
	    		prime = True;
			for x in range(3, int(n**0.5 + 1), 2):
				if n % x == 0:
				        prime = False;        	
					break; 
    			if prime: 
				return n

	def generateNTRUKeys(self):
		while True:
			params = [7, self.RandomPrime(10, 99), self.RandomPrime(100000, 999999)]
			ntruObj = Ntru(params[0], params[1], params[2])
			ntruObj.genPublicKey(self.f,self.g,self.d)
			msg = [1,10,50,60,70]
			encMsg = self.encryptUsingPubKey(params, ntruObj.getPublicKey(), msg) 
			if msg == self.decryptUsingPrivKey(params, encMsg):
				return ntruObj.getPublicKey(), params
				break

	def encryptUsingPubKey(self, params, pub, msg):
		ntruObj = Ntru(params[0], params[1],params[2])
		ntruObj.setPublicKey(pub)
		encryptedMsg = ntruObj.encrypt(msg, self.ranPol)
		return encryptedMsg

	def decryptUsingPrivKey(self, params, msg):
		ntruObj = Ntru(params[0], params[1],params[2])
		ntruObj.genPublicKey(self.f,self.g,self.d)
		decryptedMsg = ntruObj.decrypt(msg)
		return decryptedMsg

	def splitNthChar(self, nth, msg):
		split = re.findall(''.join('.' for x in range(0, nth)), msg)
		split.append(msg[-1])
		return split

	def encryptParts(self, params, pub, parts):
		encryptedParts = []
		for part in parts:
			partIdxs = [self.idxs[x] for x in part]
			encryptedParts.append(self.encryptUsingPubKey(params, pub, partIdxs))
		return encryptedParts

	def decryptParts(self, params, parts):
		decryptedParts = []
		message = ""
		for part in parts:
			decryptedParts.append(self.decryptUsingPrivKey(params, part))
		for decryptedPart in decryptedParts:
			for x in decryptedPart:
				message = ''.join([message, self.ridxs[x]]) 
		return message

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
