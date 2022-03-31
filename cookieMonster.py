import pickle
import undetected_chromedriver as uc
import os



def Main():
    os.system("cls")
    print("Cookie monster ready. Please navigate to a website and log in to save cookies.")


    driver = uc.Chrome()
    name = input("Name for cookie package?\n$")
    name = "cookie_" + name
    input("Press enter to save all cookies and quit...")
    with open(name, 'wb') as filehandler:
        pickle.dump(driver.get_cookies(), filehandler)
    driver.quit()

Main()
