from instabot import Bot

# تابع برای ریپورت کردن کاربر با شناسه دلخواه

def report_user(bot, user_id, num_reports):
    for i in range(num_reports):
        bot.report(user_id)
        print(f'Report {i+1} completed.')


# your_username, your_password
your_username = 'your_username'
your_password = 'your_password'

# user_to_report ID

user_to_report = 'user_to_report'
num_reports = 10  # تعدا ریپورت های مورد نظر

bot = Bot()
bot.login(username=your_username, password=your_password)

report_user(bot, user_to_report, num_reports)