
# Python code to illustrate Sending mail from  
# your Gmail account  
import smtplib 
  
# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587) 
  
# start TLS for security 
s.starttls() 
  
# Authentication 
s.login("aleenav1996@gmail.com", "secret-password") 
  
# message to be sent 
message = "Hello Aleena Hiiii"
  
# sending the mail 
s.sendmail("aleenav1996@gmail.com", "aleenav.sayone@gmail.com", message) 
  
# terminating the session 
s.quit() 
