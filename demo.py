from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import time

chrome_options = Options()
chrome_options.add_argument("--auto-open-devtools-for-tabs")

driver = webdriver.Chrome(options=chrome_options)

url_login = "https://www.facebook.com/login"
home_page = "https://www.facebook.com/home.php"
i_url = ".facebook.com/settings/account/?settings_tracking=mbasic_footer_link%3Asettings_3_0_pecs&eav=AfbfMcDWzb0-dLPsk0Pg4PAzzOKYtWSacEgpO6FW6hKxpORrtl5Kd_fPicI_7UfCQljY&paipv=0&_rdr"

driver.get(url_login)

time.sleep(1)

script_code = '''
var email = "";
var spinR = require(["SiteData"]).__spin_r;
var spinB = require(["SiteData"]).__spin_b;
var spinT = require(["SiteData"]).__spin_t;
var jazoest = require(["SprinkleConfig"]).jazoest;
var fbdtsg = require(["DTSGInitData"]).token;
var userId = require(["CurrentUserInitialData"]).USER_ID;
var hsi = require(["SiteData"]).hsi;
var url = "https://www.facebook.com/add_contactpoint/dialog/submit/";
var data = "jazoest=" + jazoest + "&fb_dtsg=" + fbdtsg + "&next=&contactpoint=" + email + "&__user=" + userId + "&__a=1&__dyn=&__req=1&__be=1&__pc=PHASED%3ADEFAULT&dpr=1&__rev=&__s=&__hsi=" + hsi + "&__spin_r=" + spinR + "&__spin_b=" + spinB + "&__spin_t=" + spinT;
fetch(url, {
    method: 'POST',
    body: data,
    headers: {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
}).then(function(response) {
    return response.text();
}).then(function(data) {
    console.log(data);
});
'''

if driver.current_url == home_page:
    time.sleep(1)
    driver.get("https://www" + i_url)

    time.sleep(2)

    contentt = script_code

    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])

    driver.execute_script(contentt)

    driver.close()

    driver.switch_to.window(driver.window_handles[0])

    ActionChains(driver).send_keys(Keys.ENTER).perform()

    time.sleep(4)

    driver.execute_script("window.close();")

    time.sleep(2)

    driver.get("https://mbasic" + i_url)

new_window = driver.window_handles[1]

driver.switch_to.window(new_window)

driver.switch_to.window(driver.window_handles[0])
