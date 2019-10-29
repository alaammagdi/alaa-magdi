from selenium import webdriver

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(executable_path='/Users/alaamagdi/PycharmProjects/Facebook/chromedriver', options=options)
driver.maximize_window()
email='alaa123456@gmail.com'
existingemail='alaa.mmagdi@hotmail.com'
nonemail='atest12345678@gmail.com'
password="Alaa1@34"
wrongPass="alaa123"
emptyEmail=''
emptyPass=''
FName='Alaa'
LName= 'Moh'
shortName='A'
mobileNumber='01014537864'
sillyPass='123'
url="https://www.facebook.com/"