import md5
import time
print('''
___  / / /___    |__  ___/___  / / /       ___  //_/____  _/___  / ___  / ___  ____/___  __ \
__  /_/ / __  /| |_____ \ __  /_/ /        __  ,<    __  /  __  /  __  /  __  __/   __  /_/ /     https://github.com/vkp100/
_  __  /  _  ___ |____/ / _  __  /         _  /| |  __/ /   _  /____  /____  /___   _  _, _/ 
/_/ /_/   /_/  |_|/____/  /_/ /_/          /_/ |_|  /___/   /_____//_____//_____/   /_/ |_|  
                                                                                             
 
''')
counter = 1
 
md5_hash = raw_input(" Enter your md5 Hash: ")
pwdfile = raw_input(" enter your wordlist path: ")
 
 
try:
    pwdfile = open(pwdfile,"r")
except:
    print "\nFile not found"
    quit()
 
for password in pwdfile:
    filemd5 = md5.new(password.strip()).hexdigest()
    start = time.time()
    print "Trying password %d: %s" % (counter, password.strip())
 
    counter += 1
    end = time.time()
    t_time = end - start
 
    if md5_hash == filemd5:
        print "\nPassword Found. \nPassword is : %s" % password
        print "Total Run time was: ", t_time, "second"
        time.sleep(10)
        break
 
 
else:
    print "\nPassword not Found."
