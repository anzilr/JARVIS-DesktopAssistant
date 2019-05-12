from selenium import webdriver
import time
from config import *
from engine import *
from core import jarvis


def loopout():
    jarvis()


def fb():
        speak('opening facebook!')
        driver = webdriver.Chrome('chromedriver.exe')
        driver.get('https://www.facebook.com')

        email_input = driver.find_element_by_id('email')
        email_input.send_keys(FBEMAIL)

        psd_input = driver.find_element_by_id('pass')
        psd_input.send_keys(FBPASSWORD)

        # while loop causing bug here. now it's better.

        try:
            login_btn = driver.find_element_by_id(f'u_0_1')
            time.sleep(1)
            login_btn.click()
            speak('Logged in to facebook!')

        except Exception as e:
            try:
                login_btn = driver.find_element_by_id(f'u_0_2')
                time.sleep(1)
                login_btn.click()
                speak('Logged in to facebook!')

            except Exception as e:
                try:
                    login_btn = driver.find_element_by_id(f'u_0_3')
                    time.sleep(1)
                    login_btn.click()
                    speak('Logged in to facebook!')

                except Exception as e:
                    try:
                        login_btn = driver.find_element_by_id(f'u_0_4')
                        time.sleep(1)
                        login_btn.click()
                        speak('Logged in to facebook!')

                    except Exception as e:
                        try:
                            login_btn = driver.find_element_by_id(f'u_0_5')
                            time.sleep(1)
                            login_btn.click()
                            speak('Logged in to facebook!')

                        except Exception as e:
                            try:
                                login_btn = driver.find_element_by_id(f'u_0_6')
                                time.sleep(1)
                                login_btn.click()
                                speak('Logged in to facebook!')

                            except Exception as e:
                                try:
                                    login_btn = driver.find_element_by_id(f'u_0_7')
                                    time.sleep(1)
                                    login_btn.click()
                                    speak('Logged in to facebook!')

                                except Exception as e:
                                    try:
                                        login_btn = driver.find_element_by_id(f'u_0_8')
                                        time.sleep(1)
                                        login_btn.click()
                                        speak('Logged in to facebook!')

                                    except Exception as e:
                                        try:
                                            login_btn = driver.find_element_by_id(f'u_0_9')
                                            time.sleep(1)
                                            login_btn.click()
                                            speak('Logged in to facebook!')

                                        except Exception as e:
                                            print(e)
                                            speak('Sorry sir! an error occurred! unable to log in.')

        time.sleep(2)
        speak('Do you want to share a post?')

        # again loop problem. multiple nested while loop causing bugs. Now, tried with this, same problem.
        try:
            pinput = takeCommand().lower()
            if 'yes' in pinput:
                speak("ok! What should I post for you?")
                try:
                    pcont = takeCommand().lower()
                    speak("please confirm! Do you want to post this?")
                    print(pcont)

                    try:
                        postconf = takeCommand().lower()
                        if 'yes' in postconf or 's' in postconf:
                                try:
                                    status = driver.find_element_by_xpath("//textarea[@name='xhpc_message']")
                                    status.send_keys(pcont);
                                    postbutton = driver.find_element_by_css_selector(("button[class*='selected']"))
                                    # postbutton = driver.find_element_by_xpath("//button[contains(.,'selected')]")
                                    postbutton.click()
                                    print("post done")
                                    speak("Post created! Check your wall!")
                                    loopout()

                                except Exception as e:
                                    print('error')
                                    print(e)
                                    speak("sorry sir! an error occurred. Post creation failed!")
                                    loopout()
                        elif 'no' in postconf:
                            speak('ok sir!')
                            loopout()
                    except Exception as e:
                        speak("Sorry! I didn't get that! Say once again!")
                        return "None"
                except Exception as e:
                    speak("I didn't hear that! say once again")
                    return "None"

            elif 'no' in pinput or 'n' in pinput:
                speak("ok sir!")
                loopout()
        except Exception as e:
            speak("Sorry! I didn't get that! Say once again!")
            return "None"



time.sleep(30)
