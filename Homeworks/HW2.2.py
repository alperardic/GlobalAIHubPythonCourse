KullaniciIDPassWord = {"AlperArdic" : "PythonEgitimi"}

print("Hoşgeldiniz! Giriş yapmak için kullanıcı adı ve parolanızı girmelisiniz.")
kullanici = input("Kullanıcı adını giriniz :  \n")
sifre = input("Şifreyi giriniz : \n")

if kullanici in KullaniciIDPassWord:
    if KullaniciIDPassWord["AlperArdic"] == sifre:
        print("Başarıyla giriş yaptınız!")
    else:
        print("Kullanıcı adınız veya şifreniz hatalıdır. \nGiriş işlemi başarısız!")
else:
    print("Kullanıcı adınız veya şifreniz hatalıdır. \nGiriş işlemi başarısız!")