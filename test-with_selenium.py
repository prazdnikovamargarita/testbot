from test_variables import *

stor_dict = {}


class Stor:
    def __init__(self, stor):
        self.stor = stor

def error(message):
    markup_error_button =  types.ReplyKeyboardMarkup(resize_keyboard=True)
    error_button = types.KeyboardButton("/start")
    markup_error_button.row(error_button)
    bot.send_message(message.chat.id, "Have some errors.\nGo to start", reply_markup=markup_error_button)



@bot.message_handler(commands=['start'])
def start(message):
    try:
        user_id = message.from_user.id
        chat_id=message.chat.id
        user_id = message.from_user.id

        if (user_id == 308984767) or(user_id==458888496):
            bot.send_message(message.chat.id, "Choose acc", reply_markup=markup_choose_storage)
        else:
            msg = bot.send_message(message.chat.id, 'Введите пароль')
            bot.register_next_step_handler(msg, check_pass)
    except:
        markup_error_button =  types.ReplyKeyboardMarkup(resize_keyboard=True)
        error_button = types.KeyboardButton("/start")
        markup_error_button.row(error_button)
        bot.send_message(message.chat.id, "Go to start", reply_markup=markup_error_button)



       
def check_pass(message):
    chat_id=message.chat.id
    text = message.text
    username = message.from_user.username
    
    if (text.lower()=="cat"):

        print("test-bot")
        bot.send_message(message.chat.id, "Choose acc", reply_markup=markup_choose_storage)
        

    else:
        markup_error_button =  types.ReplyKeyboardMarkup(resize_keyboard=True)
        error_button = types.KeyboardButton("/start")
        markup_error_button.row(error_button)
        bot.send_message(message.chat.id, "Pass incorrect. Go to start", reply_markup=markup_error_button)





def show_acc(message):
    bot.send_message(message.chat.id, "Choose acc", reply_markup=markup_choose_storage)
test ="false"

@bot.message_handler(regexp='eanna9790@gmail.com')
@bot.message_handler(regexp='seoteamessay@gmail.com')
def choose_storage(message):
    try:

        global test
        global storage
        text = message.text
        chat_id = message.chat.id
        if text =="seoteamessay@gmail.com":
            test ="true"
            storage="authorizedcreds-second.dat"
        if text == "eanna9790@gmail.com":
            test = "true"
            storage = "authorizedcreds.dat"
        stor = Stor(storage)
        storage_file = file.Storage(storage)
        credentials = storage_file.get()
    
        # If authenticated credentials don't exist, open Browser to authenticate
        if credentials is None or credentials.invalid:

            CLIENT_ID = '124538964907-7n68c101qtdml0v8g3bgdacus0ju4bhf.apps.googleusercontent.com'
            CLIENT_SECRET = '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'

            # Check https://developers.google.com/webmaster-tools/v1/ for all available scopes
            OAUTH_SCOPE = 'https://www.googleapis.com/auth/webmasters.readonly'

            # Redirect URI for installed apps
            REDIRECT_URI = 'urn:ietf:wg:oauth:2.0:oob'

            # Run through the OAuth flow and retrieve credentials
            flow = OAuth2WebServerFlow(CLIENT_ID, CLIENT_SECRET, OAUTH_SCOPE, REDIRECT_URI)
            authorize_url = flow.step1_get_authorize_url()
            
            options = webdriver.ChromeOptions()
            options.add_argument('--allow-profiles-outside-user-dir')
            options.add_argument('--enable-profile-shortcut-manager')
            options.add_argument(r'user-data-dir=C:\\Users\\user\\Desktop\\new-bot\\User Data')
            options.add_argument('--profile-directory=Profile 2')




            options = webdriver.ChromeOptions()
            s=Service('chromedriver103.exe')
            chrome_driver_path = "chromedriver103.exe"
            options.add_argument("--allow-profiles-outside-user-dir")
            options.add_argument("--enable-profile-shortcut-manager")
            options.add_argument(r'user-data-dir=C:\Users\user\Desktop\new-bot\User Data')
            options.add_argument("--profile-directory=Profile 2")
            options.add_experimental_option('excludeSwitches', ['enable-logging'])
            with webdriver.Chrome(ChromeDriverManager().install(), options=options) as driver:
                #time.sleep(1)
                driver.get(authorize_url)
                #driver.implicitly_wait(100) 
                time.sleep(1)
                if text =="seoteamessay@gmail.com":
                    user_login = driver.find_element(By.XPATH, '//div[@data-identifier="seoteamessay@gmail.com"]')
                if text == "eanna9790@gmail.com":
                    user_login = driver.find_element(By.XPATH, '//div[@data-identifier="eanna9790@gmail.com"]')
                """user_login = driver.find_element(By.ID, 'identifierId')
                time.sleep(1)
                user_login.send_keys("seoteamessay@gmail.com")"""
                user_login.click()
                time.sleep(3)
                btn = driver.find_elements(By.XPATH, '//button')
                #print(btn)
                btn[2].click()
                time.sleep(3)
                btn = driver.find_elements(By.XPATH, '//button')
                btn[2].click()
                time.sleep(3)
                textbox = driver.find_element(By.TAG_NAME, 'textarea').text

                # print the contents of the textarea
                
                time.sleep(3)
                #user_pass = driver.find_element(By.XPATH, '//input[name="password"]')
            
                

            #msg = bot.send_message(message.chat.id, f'Go to the following link in your browser: {authorize_url}' )






            GA = Google_Authorizate(creds=creds, site_api=site_api, storage=stor.stor, code=textbox)
            webmasters_service = GA.authorize_creds(creds)
            
            bot.send_message(message.chat.id, "Choose period", reply_markup=markup_choose_period)
        else:          

            
            bot.send_message(message.chat.id, "Choose period", reply_markup=markup_choose_period)
        stor = Stor(storage)
        stor_dict[chat_id] = stor
        stor.stor = storage
    except:
        error(message)


def with_date_period(message, date):
    try:
        #print(choose_storage)
        chat_id = message.chat.id
        stor = stor_dict[chat_id] 
           # Get credentials to log in the api
        GAsec = Google_Authorizate_sec(creds=creds, site_api=site_api, storage=stor.stor)
        request={
        'quotaUser':'string',
        'fields':'string',
        'upload_protocol':'string',
        'alt':'',
        'access_token':'string',
        'callback':'string',
        '$.xgafv':'',
        'uploadType':'string',
        'prettyPrint':'true'

        }
        webmasters_service = GAsec.authorize_creds(creds)  
        response = GAsec.domains_founder(webmasters_service, site_api, request)
        print(f"Storage: {storage}")
        markup_go_to_start =  types.ReplyKeyboardMarkup(resize_keyboard=True)
        maxRows = 25000 # Maximum 25K per call 
        numRows = 0     # Start at Row Zero
        print(date)
        currentTimeDate = datetime.now()
        currentTime = currentTimeDate.strftime('%Y-%m-%d')
        request = {
                "dataState": "ALL",
                "startDate":  date,     # Get today's date (while loop)
                "endDate": str(currentTime) ,       # Get today's date (while loop)
                "dimensions": ['date','page','query'],  # Extract This information
                "rowLimit": maxRows,                    # Set number of rows to extract at once (max 25k)
                "startRow": numRows                     # Start at row 0, then row 25k, then row 50k... until with all.
            }
        i=0
        array_msg = []

        for val in response['siteEntry']:
            print(val['siteUrl'])
            try:
                if not (val['permissionLevel']=='siteUnverifiedUser'):
                    response_messege = GAsec.execute_request(webmasters_service,val['siteUrl'] , request)
                    j=0
                    for item in response_messege['rows']:
                        
                        i=i+int(item['clicks'])
                        j=j+int(item['clicks'])
                    msg_for_array = f"""{val['siteUrl']} - clicks: {j}"""
                    array_msg.append(msg_for_array)
                else:
                    pass
                    
            except:
                print("not")
        print("sum:")
        print(i)
        sum_traf=f"sum of clicks: {i}"
        array_msg.append(sum_traf)
        bot.send_message(message.chat.id, '\n'.join(array_msg),)
    except:
        error(message)
        os.remove(storage)



@bot.message_handler(regexp="for 3 days")
def for_three_days(message):
    try:

        print(test)
        date = datetime.now() - timedelta(days=3)
        date = str(date.strftime('%Y-%m-%d'))
        with_date_period(message, date)
        print(message.text)
        print(storage)
        bot.send_message(message.chat.id, "Choose acc", reply_markup=markup_choose_storage)
    except:
        error(message)

@bot.message_handler(regexp="for 1 week")
def for_three_days(message):
    try:
        date = datetime.now() - timedelta(days=7)
        date = str(date.strftime('%Y-%m-%d'))
        with_date_period(message, date)
        bot.send_message(message.chat.id, "Choose acc", reply_markup=markup_choose_storage)
    except:
        error(message)

@bot.message_handler(regexp="for 3 month")
def for_three_days(message):
    try:
        date = datetime.now() - timedelta(days=92)
        date = str(date.strftime('%Y-%m-%d'))
        with_date_period(message, date)
        bot.send_message(message.chat.id, "Choose acc", reply_markup=markup_choose_storage)
    except:
        error(message)

@bot.message_handler(regexp="for last 24 hours")
def for_three_days(message):
    try:
        date = datetime.now() - timedelta(days=1)
        date = str(date.strftime('%Y-%m-%d'))
        with_date_period(message, date)
        bot.send_message(message.chat.id, "Choose acc", reply_markup=markup_choose_storage)
    except:
        error(message)


    
@bot.message_handler(regexp="choose date")
def yout_choose(message):
    try:
        print("youre choose")
        bot.send_message(message.chat.id, f"Enter Date: year-month-day")
    except:
        error(message)


@bot.message_handler(regexp="\d\d\d\d-\d\d-\d\d")
def print_your_choose(message):
    try:
        chat_id = message.chat.id
        date = message.text
        with_date_period(message, date)
        bot.send_message(message.chat.id, "Choose acc", reply_markup=markup_choose_storage)
    except:
        error(message)


            
  
def schedule_checker():
    while True:
        schedule.run_pending()
        sleep(1)




def send_messadge():
    try:
        print("staart")
        storages={'authorizedcreds-second.dat', 'authorizedcreds.dat'}
        for storage_dat in storages:
            GA = Google_Authorizate(creds=creds, site_api=site_api, storage=storage_dat, code="code")
            webmasters_service = GA.authorize_creds(creds)     # Get credentials to log in the api
            request={
            'quotaUser':'string',
            'fields':'string',
            'upload_protocol':'string',
            'alt':'',
            'access_token':'string',
            'callback':'string',
            '$.xgafv':'',
            'uploadType':'string',
            'prettyPrint':'true'

            }
            response = GA.domains_founder(webmasters_service, site_api, request)
            print(f"Storage: {storage}")
            markup_go_to_start =  types.ReplyKeyboardMarkup(resize_keyboard=True)
            webmasters_service = GA.authorize_creds(creds)
            maxRows = 25000 # Maximum 25K per call 
            numRows = 0     # Start at Row Zero
            currentTimeDate = datetime.now()
            currentTime = currentTimeDate.strftime('%Y-%m-%d')
            date = datetime.now() - timedelta(days=1)
            date = str(date.strftime('%Y-%m-%d'))
            request = {
                    "dataState": "ALL",
                    "startDate":  date,     # Get today's date (while loop)
                    "endDate": str(currentTime) ,       # Get today's date (while loop)
                    "dimensions": ['date','page','query'],  # Extract This information
                    "rowLimit": maxRows,                    # Set number of rows to extract at once (max 25k)
                    "startRow": numRows                     # Start at row 0, then row 25k, then row 50k... until with all.
                }
            i=0
            array_msg = []

            for val in response['siteEntry']:
                print(val['siteUrl'])
                try:
                    if not (val['permissionLevel']=='siteUnverifiedUser'):
                        response_messege = GA.execute_request(webmasters_service,val['siteUrl'] , request)
                        j=0
                        for item in response_messege['rows']:
                            
                            i=i+int(item['clicks'])
                            j=j+int(item['clicks'])
                        msg_for_array = f"""{val['siteUrl']} - clicks: {j}"""
                        array_msg.append(msg_for_array)
                    else:
                        pass
                        
                except:
                    print("not")
            print("sum:")
            print(i)
            sum_traf=f"sum of clicks: {i}"
            array_msg.append(sum_traf)
            bot.send_message("308984767", '\n'.join(array_msg),)
            bot.send_message("458888496", '\n'.join(array_msg),)
    except:
        bot.send_message("308984767", 'Verification is needed')
        bot.send_message("458888496", 'Verification is needed')

if __name__ == '__main__':
    #send_messadge()
    #schedule.every(3).minutes.do(send_messadge)
    schedule.every().day.at("07:03").do(send_messadge)
    Thread(target=schedule_checker).start()
        
    bot.enable_save_next_step_handlers()

    bot.load_next_step_handlers()

    bot.polling(allowed_updates=True, none_stop = True)
        

    