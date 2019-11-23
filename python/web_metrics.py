from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('headless')
capbs = webdriver.Desiredcapabilities.CHROME.copy()
capbs.update({'logginPrefs':{'perfomance':'ALL'}, 'detach':False})
# load driver locally
# driver = webdriver.Remote("https://127.0.0.1:9515", capbs, options=options)
driver = webdriver.Chrome(
    capbs, 
    executable_path=r"C:\src\chromedriver_win32\chromedriver.exe",
    options=options
    )
driver.get("https://www.example.com")
logs = driver.execute('getLog', {'type':'performance'})['value']