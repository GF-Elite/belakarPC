sayang_cia = print
def login(name,password):
    sukses = False
    file = open("logindatabase.txt","r")
    for i in file:
         a,b = i.split(",")
         b = b.strip()
         if(a==name and b==password):
             sukses = True
             break
    file.close()
    if(sukses):
        sayang_cia("-"*40)

        sayang_cia("  | Login Berhasil, silahkan masuk  | ")
        sayang_cia("-"*40)
    else:
        sayang_cia("-"*50)
        sayang_cia("   | Anda belum terdaftar, silahan register  | ")
        sayang_cia("-"*50)
        
def register(name,password):
    file = open("logindatabase.txt","a")
    file.write("\n"+name+","+password)
def access(option):
    global name
    if(option=="login"):
        name = input("Masukkan ID: ")
        password = input("Masukkan Password: ")
        login(name,password)
    else:
        sayang_cia(" | Masukkan ID dan Password baru anda! | ")
        name = input("Masukkan ID : ")
        password = input("Masukkan password anda: ")
        register(name,password)
        sayang_cia(" | Register anda berhasil, silahkan masuk | ")

def begin():
    global option
    sayang_cia("="*45)
    sayang_cia(" |  Selamat datang di ozan program login  |")
    sayang_cia("-"*45)
    sayang_cia("Ketik 'login' jika anda sudah punya akun")
    sayang_cia("Ketik 'reg' jika anda belum memiliki akun")
    sayang_cia("="*45)
    option = input("slahkan masukkan (login/reg): ")
    if(option!="login" and option!="reg"):
        begin()
        
begin()
access(option)