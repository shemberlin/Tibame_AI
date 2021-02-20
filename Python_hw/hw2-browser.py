import webbrowser as web
url=input()
if len(url)==0:
    print("請輸入網址!")
web.open_new_tab(url)
