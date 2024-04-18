import time
import random
import selenium
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def startBanner():
    print("*************************************************")
    print("|                                               |")
    print("|                Made by AkabJack               |")
    print("|                                               |")
    print("*************************************************")

def enterCredentials():
    credentials_list = list()
    print("What is your username?")
    credentials_list.append(input())
    print("What is your password?")
    credentials_list.append(input())
    print("Thanks, I'm going to work now!")
    return credentials_list
    
def loginPage(username, password, driver):
    counter = 0
    while counter < 15:
        try:
            cookie_button = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[1]')#hardcoded
            username_element = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[1]/div/label/input')
            password_element = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[2]/div/label/input')
            login_button = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[3]')
            break
        except:
            time.sleep(1)#wait 1 second
            counter += 1
            print(15 - counter, "seconds left")
        finally:
            if(counter == 15):
                print("something happend (╥﹏╥) ")
                driver.quit()#driver.close() inchide tabul
                #inchidem cum trebuie instanta
                exit()
    print("Found the cookie element, I'm gonna press it!")
    cookie_button.click()
    time.sleep(2)
    print("Writing credentials")
    username_element.send_keys(username)
    time.sleep(1)
    password_element.send_keys(password)
    time.sleep(1)
    print("Ready to login ٩( ^ᗜ^  ) و")
    login_button.click()
    time.sleep(7)

def readTheList(path, followers_list):
    file = ''
    x = ''
    try:
        file = open(path, "r")
    except:
        print("File has not been found!")
        exit()
    finally:
        for x in file:
            followers_list.append(x.strip("\n"))

def repeatComments(driver, lista):
    repeat = 'y'
    while repeat == 'y':
        post = ""
        nr_of_people = ""
        delay_time = ""
        commentmode = ""
        print("The link to the post:")
        post = input()
        print("The number of people who can be tagged to the post?:")
        nr_of_people = int(input())
        print("The delay time between each tag?")
        delay_time = int(input())
        print('Do you want multiple persons tagged in a single comment? Answer with "y" if you want, else answer with "n"')
        commentmode = input()
        if commentmode == 'y':
            makeMultipleComments(driver, post, nr_of_people, lista, delay_time)
        else:
            makeComments(driver, post, nr_of_people, lista, delay_time)
        print('Do you want to repeat with another post? Answer with "y" if you want, else answer with "n"')
        repeat = input()
    print("Ok, Goodbye!")
    
def makeMultipleComments(driver, post, nr_of_people, lista, delay_time):
    print("How many people in a comment? (Multiple of number of people)")
    numberOfPeopleOnCom = int(input())
    driver.get(post)
    time.sleep(3)
    list_lenght = len(lista)
    selected_people_int = list()
    selected_people = list()
    elementsOfPage = list()
    def searchElements():
        inside_list = list()
        counter = 0
        while counter < 10:
            try:
                comment_Text_box_ins = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div[1]/div/div[2]/section/div/form/div/textarea')
                comment_box_button_ins = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div[1]/div/div[2]/section/div/form/div/div[2]')
                inside_list.append(comment_Text_box_ins)
                inside_list.append(comment_box_button_ins)
                counter = 10
            except:
                time.sleep(1)
                counter += 1
                print(10 - counter, "seconds left till the post opens")
        return inside_list
    elementsOfPage = searchElements()
    counter = 0
    x = random.randint(0, list_lenght)
    while counter < nr_of_people:
        if x in selected_people_int:
            x = random.randint(0, list_lenght)
        else:
            counter += 1
            selected_people_int.append(x)
            selected_people.append(lista[x])

    restPeople = nr_of_people%numberOfPeopleOnCom
    if restPeople != 0:
        wildcard = 1
    else:
        wildcard = 0
    #todo finish
    for i in range(int(nr_of_people/numberOfPeopleOnCom)+wildcard):#nr_of_people este cate persoane etichetam
        com = ""
        if i == int(nr_of_people/numberOfPeopleOnCom):
            for d in range(restPeople):
                com += selected_people[d+(i*numberOfPeopleOnCom)] + " "
        else:
            for z in range(numberOfPeopleOnCom):
                com += selected_people[z+(i*numberOfPeopleOnCom)] + " "
        elementsOfPage = searchElements()
        elementsOfPage[0].send_keys(com)
        time.sleep(1)
        print("Tagged: ", com)
        elementsOfPage[1].click()
        time.sleep(delay_time)
        

def makeComments(driver, post, nr_of_people, lista, delay_time):
    # driver.execute_script("window.open('about:blank','secondtab');")
    # driver.switch_to.window("secondtab")
    driver.get(post)
    time.sleep(3)
    counter = 0
    list_lenght = len(lista)
    selected_people_int = list()
    selected_people = list()
    
    while counter < 10:
        try:
            comment_Text_box = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div[1]/div[1]/article/div/div[2]/div/div[2]/section[3]/div/form/div/textarea')#tre sa caudam iframe-ul
            comment_box_button = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div[1]/div[1]/article/div/div[2]/div/div[2]/section[3]/div/form/div/div[2]')
            counter = 10
        except:
            time.sleep(1)
            counter += 1
            print(10 - counter, "seconds left till the post opens")

    counter = 0
    x = random.randint(0, list_lenght)
    while counter < nr_of_people:
        if x in selected_people:
            x = random.randint(0, list_lenght)
        else:
            counter += 1
            selected_people_int.append(x)
            selected_people.append(lista[x])

    for i in range(nr_of_people):#nr_of_people este cate persoane etichetam
        comment_Text_box.send_keys(lista[selected_people[i]])
        time.sleep(1)
        print("Tagged: ", lista[selected_people[i]])
        comment_box_button.click()
        time.sleep(delay_time)
        
def closeTheBot(driver):
    os.system('tskill plugin-container')
    driver.quit()
    print("Goodbye")
