from warnings import filterwarnings
from selenium import webdriver
import time
import utils as utils

filterwarnings("ignore")
utils.startBanner()
lista_credentials = ''
listaConturi = list()
utils.readTheList("lista_ig.txt", listaConturi)

lista_credentials = utils.enterCredentials()
driver = webdriver.Firefox(executable_path = 'geckodriver.exe')#deprecated method, todo: pass a service object
driver.get("https://www.instagram.com/accounts/login/")
time.sleep(5)   
utils.loginPage(lista_credentials[0], lista_credentials[1], driver)
utils.repeatComments(driver,listaConturi)
utils.closeTheBot(driver)