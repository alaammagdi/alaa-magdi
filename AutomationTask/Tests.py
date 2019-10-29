
from BaseTest import *
from attributes import *
from selenium.webdriver.support.select import Select




#Case 1 : Login - Failed Login in case of non existing email
preStart()
emailField=driver.find_element_by_id('email')
passwordField= driver.find_element_by_id('pass')
loginButton=driver.find_element_by_id('u_0_b')
emailField.send_keys(nonemail)
passwordField.send_keys(wrongPass)
loginButton.click()
driver.implicitly_wait(3)
facebookVal = driver.find_elements_by_partial_link_text('login/device-based/regular/login/?login_attempt')
validation =driver.find_elements_by_partial_link_text('login/device-based/regular/login/?login_attempt')
if (facebookVal == validation):
    print('Case 1 for empty credentials Passed')
else: print('Case 1 Failed')

#Case 2 : Login - Empty Credentials
preStart()
emailField=driver.find_element_by_id('email')
passwordField= driver.find_element_by_id('pass')
loginButton=driver.find_element_by_id('u_0_b')
emailField.send_keys(emptyEmail)
passwordField.send_keys(emptyPass)
loginButton.click()
driver.implicitly_wait(3)
facebookVal = driver.find_elements_by_partial_link_text('login/device-based/regular/login/?login_attempt')
validation =driver.find_elements_by_partial_link_text('login/device-based/regular/login/?login_attempt')
if (facebookVal == validation):
    print('Case 2 for empty credentials Passed')
else: print("Case 2 Failed")


#Case 3 : Login - Forget Account
preStart()
forgottenAccount=driver.find_element_by_xpath('//*[@id="login_form"]/table/tbody/tr[3]/td[2]/div/a')
forgottenAccount.click()
driver.implicitly_wait(3)
facebookVal = driver.find_element_by_id('identify_email')
validation =driver.find_element_by_id('identify_email')
if (facebookVal == validation):
    print('Case 3 for Forget Account Passed')
else: print("Case 3 Failed")

#Case 4 : Sign Up - All Empty Fields
preStart()
signUpButton = driver.find_element_by_id('u_0_15')
signUpButton.click()
driver.implicitly_wait(3)
facebookVal = driver.find_element_by_xpath('//*[@id="u_0_l"]/i[1]')
validation =driver.find_element_by_xpath('//*[@id="u_0_l"]/i[1]')
if (facebookVal == validation):
    print('Case 4 for Empty Sign up Form Passed')
else: print("Case 4 Failed")

#Case 5 : Sign Up - Invalid Password

preStart()
firstName=driver.find_element_by_id('u_0_m')
lastName=driver.find_element_by_id('u_0_o')
mobileOrEmail=driver.find_element_by_id('u_0_r')
newPassword=driver.find_element_by_id('u_0_y')
signUpButton = driver.find_element_by_id('u_0_15')
time.sleep(2)
firstName.send_keys(FName)
lastName.send_keys(LName)
mobileOrEmail.send_keys(mobileNumber)
newPassword.send_keys(sillyPass)
day= Select(driver.find_element_by_id('day'))
day.select_by_index(6);
month= Select(driver.find_element_by_id('month'))
month.select_by_index(6)
year= Select(driver.find_element_by_id('year'))
year.select_by_index(22)
gender=driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/form/div[1]/div[7]/span/span[1]/input')
gender.click()
signUpButton.click()
driver.implicitly_wait(10)
facebookVal = driver.find_element_by_id('reg_error_inner')
validation =driver.find_element_by_id('reg_error_inner')
if (facebookVal == validation):
    print('Case 5 for Invalid Password Passed')
else: print("Case 5 Failed")
time.sleep(3)


#Case 6: Sign Up - Existing User
preStart()
firstName=driver.find_element_by_id('u_0_m')
lastName=driver.find_element_by_id('u_0_o')
mobileOrEmail=driver.find_element_by_id('u_0_r')
newPassword=driver.find_element_by_id('u_0_y')
signUpButton = driver.find_element_by_id('u_0_15')
time.sleep(2)
firstName.send_keys(FName)
lastName.send_keys(LName)
mobileOrEmail.send_keys(existingemail)
driver.implicitly_wait(7)
reEnter=driver.find_element_by_id('u_0_u')
reEnter.send_keys(existingemail)
newPassword.send_keys(password)
day= Select(driver.find_element_by_id('day'))
day.select_by_index(6);
month= Select(driver.find_element_by_id('month'))
month.select_by_index(6)
year= Select(driver.find_element_by_id('year'))
year.select_by_index(22)
gender=driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/form/div[1]/div[7]/span/span[1]/input')
gender.click()
signUpButton.click()
driver.implicitly_wait(10)
facebookVal = driver.find_element_by_id('recovery_code_entry')
validation = driver.find_element_by_id('recovery_code_entry')
if (facebookVal == validation):
    print('Case 6 for Existing Email Passed')
else: print("Case 6 Failed")



#Case 7: Sign Up - Short Name Validation
preStart()
firstName=driver.find_element_by_id('u_0_m')
lastName=driver.find_element_by_id('u_0_o')
mobileOrEmail=driver.find_element_by_id('u_0_r')
newPassword=driver.find_element_by_id('u_0_y')
signUpButton = driver.find_element_by_id('u_0_15')
time.sleep(2)
firstName.send_keys(shortName)
lastName.send_keys(LName)
mobileOrEmail.send_keys(nonemail)
driver.implicitly_wait(7)
reEnter=driver.find_element_by_id('u_0_u')
reEnter.send_keys(nonemail)
newPassword.send_keys(password)
day= Select(driver.find_element_by_id('day'))
day.select_by_index(6);
month= Select(driver.find_element_by_id('month'))
month.select_by_index(6)
year= Select(driver.find_element_by_id('year'))
year.select_by_index(22)
gender=driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/form/div[1]/div[7]/span/span[1]/input')
gender.click()
signUpButton.click()
driver.implicitly_wait(10)
facebookVal = driver.find_element_by_id('reg_error_inner')
validation = driver.find_element_by_id('reg_error_inner')
if (facebookVal == validation):
    print('Case 7 for Short Name Passed')
else: print("Case 7 Failed")



#Case 8 : Successful Login
preStart()
emailField=driver.find_element_by_id('email')
passwordField= driver.find_element_by_id('pass')
loginButton=driver.find_element_by_id('u_0_4')
emailField.send_keys(email)
passwordField.send_keys(password)
loginButton.click()
time.sleep(3)
facebookVal = driver.find_element_by_id('navItem_4748854339')
validation = driver.find_element_by_id('navItem_4748854339')
if (facebookVal == validation):
    print('Case 8 for successful Login Passed')
else: print("Case 8 Failed")

postStop()







