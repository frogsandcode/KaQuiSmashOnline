from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import KahootSmashForm
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import threading
import platform
import time



@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')


@app.route('/kahoot', methods=['GET', 'POST'])
def slam_kahoot():
    form = KahootSmashForm()

    def bot(pin, name):
        if platform.system() == 'Windows':
            driver = webdriver.Chrome(executable_path='webDrivers\chromedriver.exe')
        elif platform.system() == 'Darwin':
            driver = webdriver.Chrome(executable_path='webDrivers/chromedrivermac')

        driver.get('http://www.kahoot.it')

        driver.implicitly_wait(2)

        driver.find_element_by_id('inputSession').send_keys(pin)
        driver.find_element_by_xpath("//button[@type='submit']").click()

        driver.implicitly_wait(2)

        driver.find_element_by_id('username').send_keys(name)
        driver.find_element_by_id('username').send_keys(Keys.RETURN)

        time.sleep(30)

        driver.quit()

    # once form submitted
    if form.validate_on_submit():
        flash('Slam requested on Kahoot game at ' + form.pin.data + '. Bots will remain in game for 30 seconds and then'
                                                                    ' leave. If you have called a large slam, be '
                                                                    'patient! If your bots do not appear after a few '
                                                                    'minutes, make sure you entered the correct pin. '
                                                                    'Do not spam slam requests.')

        for x in range(form.numBots.data):
            name = form.baseName.data + str(x)
            threading.Thread(target=bot, args=(form.pin.data, name)).start()

        return redirect(url_for('home'))

    return render_template('kahoot.html', title='Slam a Kahoot', form=form)
