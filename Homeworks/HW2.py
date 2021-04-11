userName = "AlperArdic"
passWord = "PythonEgitimi"

print("Hoşgeldiniz! Giriş yapmak için kullanıcı adı ve parolanızı girmelisiniz.")
kullanici = input("Kullanıcı adını giriniz :  \n")
sifre = input("Şifreyi giriniz : \n")

if kullanici != userName or sifre != passWord:
    print("Kullanıcı adınız veya şifreniz hatalıdır. \nGiriş işlemi başarısız!")
else:
    print("Başarıyla giriş yaptınız!")
