def Image():
  print("          _____                    _____                    _____                _____     ")     
  print("         /\    \                  /\    \                  /\    \              |\    \    ")     
  print("        /::\    \                /::\____\                /::\    \             |:\____\   ")     
  print("       /::::\    \              /:::/    /               /::::\    \            |::|   |    ")    
  print("      /::::::\    \            /:::/    /               /::::::\    \           |::|   |    ")    
  print("     /:::/\:::\    \          /:::/    /               /:::/\:::\    \          |::|   |    ")    
  print("    /:::/__\:::\    \        /:::/    /               /:::/__\:::\    \         |::|   |     ")   
  print("   /::::\   \:::\    \      /:::/    /               /::::\   \:::\    \        |::|   |      ")  
  print("  /::::::\   \:::\    \    /:::/    /      _____    /::::::\   \:::\    \       |::|___|______ ") 
  print(" /:::/\:::\   \:::\____\  /:::/____/      /\    \  /:::/\:::\   \:::\ ___\      /::::::::\    \ ")
  print("/:::/  \:::\   \:::|    ||:::|    /      /::\____\/:::/__\:::\   \:::|    |    /::::::::::\____\ ")
  print("\::/   |::::\  /:::|____||:::|____\     /:::/    /\:::\   \:::\  /:::|____|   /:::/~~~~/~~      ")
  print(" \/____|:::::\/:::/    /  \:::\    \   /:::/    /  \:::\   \:::\/:::/    /   /:::/    /      ")   
  print("       |:::::::::/    /    \:::\    \ /:::/    /    \:::\   \::::::/    /   /:::/    /    ")      
  print("       |::|\::::/    /      \:::\    /:::/    /      \:::\   \::::/    /   /:::/    /   ")        
  print("       |::| \::/____/        \:::\__/:::/    /        \:::\  /:::/    /    \::/    /  ")          
  print("       |::|  ~|               \::::::::/    /          \:::\/:::/    /      \/____/ ")            
  print("       |::|   |                \::::::/    /            \::::::/    / ")                          
  print("       \::|   |                 \::::/    /              \::::/    / ")                           
  print("        \:|   |                  \::/____/                \::/____/ ")                            
  print("         \|___|                   ~~                       ~~      ") 
pass

def core():
  import wolframalpha  
  client = wolframalpha.Client("2EW32G-X4HL6ALHW5")       
  import wikipedia
  while True:
    s = "ruby@Answer:"
    x = str(input("A@Quest:"))
    if x == "/exit":
      print("Ruby:Simple mode off")
      Run()
    else:
      try:
        wiki = wikipedia.summary(x, sentences=1)
        wolfram = next(client.query(x).results).text
        print (s+"Wolfram Result: ","\033[0;32;48m"+wolfram, "Wikipedia Result: ","\033[0;32;48m"+wiki, "\033[0;37;48m")
      except StopIteration:
        wiki = wikipedia.summary(x, sentences=1)
        print (s+"Wikipedia Result: ", "\033[0;32;48m"+wiki, "\033[0;37;48m")
      except wikipedia.exceptions.PageError:
        wolfram = next(client.query(x).results).text
        print (s+"Wolfram Result: ","\033[0;32;48m"+wolfram, "\033[0;37;48m")
      except wikipedia.exceptions.DisambiguationError:
        wolfram = next(client.query(x).results).text
        print(s+"\033[0;32;48m"+wolfram, "\033[0;37;48m")
      except:
        wiki = wikipedia.summary(x, sentences=2)
        print(s+"\033[0;32;48m"+wiki, "\033[0;37;48m")
  return
pass




def Run(): 
 while True:
    s = "Ruby:" 
    y = str(input("A:"))
    if y == "/Simple":
       print(s+"Simple Mode is On")
       core()
    elif y == "up up down down left right left right B A":
      import shame   
    elif y == "/add": 
      print(s+"soon")
    elif y == "/exit":
      close()
    elif y == "clear":
      cl()
    elif y == "/work":
      Work_Station()
    elif y == "/Developer Mode":
      Command_editor()
    elif y == "work":
        work()
    else: 
      print("The command not prepartis")
pass

def cl():
  print("\n"*50)
  Image()
  print("\n"*10)

def Work_Station():
  import Play
  Run()
pass

def Command_editor():
    import os 
    os.system("gnome-terminal -e 'bash -c \"cd && cd Documents/Python && sudo python3.8 Command_editor.py && sudo python3.8 Ruby.py; exec bash\"'")
    close()
pass

def close():
    print("Good bye")
    import os
    import signal
    os.kill(os.getppid(), signal.SIGHUP)
pass

def work():
   print("Fuyk yee")
pass









