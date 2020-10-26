from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import pandas as pd

class ApplyBot:
    def __init__(self):
        self.bot = webdriver.Firefox()
        """
        with open('/Users/tashakim/Desktop/Tasha_Kim_Resume.pdf', 'rb') as f:
            self.resume = f.read()
        """
        

    def openPage(self, url):
        bot = self.bot 
        bot.get(url)
        time.sleep(1)

    """
    def uploadResume(self):
        resume = self.bot.find_element_by_name('resume')
        resume.sendKeys(self.resume)
    """
    def fillText(self):
        bot = self.bot
        current_company = bot.find_element_by_name('org')
        linkedin = bot.find_element_by_name('urls[LinkedIn]')
        github = bot.find_element_by_name('urls[GitHub]')
        major = bot.find_element_by_name('cards[0bb396d1-c0f6-46c8-a3c5-79444ccc65b5][field6]')
        
        current_company.clear()
        linkedin.clear()
        github.clear()
        major.clear()

        current_company.send_keys('Brown University')
        linkedin.send_keys('https://www.linkedin.com/in/tasha-jae-young-kim/')
        github.send_keys('https://github.com/tashakim')
        major.send_keys('Mathematics - Computer Science')
        
        print("text fields filled")
        time.sleep(1)


    def pullDown(self):
        bot = self.bot
        actions = ActionChains(bot)
        
        graduation_season = bot.find_element_by_name('cards[0bb396d1-c0f6-46c8-a3c5-79444ccc65b5][field0]')  
        graduation_season.send_keys(Keys.RETURN)
        graduation_season.send_keys('Spring 2021')
        graduation_season.send_keys(Keys.RETURN)

        work_permit = bot.find_element_by_name('cards[0bb396d1-c0f6-46c8-a3c5-79444ccc65b5][field1]')
        work_permit.send_keys(Keys.RETURN)
        work_permit.send_keys('No')
        work_permit.send_keys(Keys.RETURN)

        """
        university = bot.find_element_by_class_name('select2-selection__placeholder')
        university.send_keys(Keys.RETURN)
        university.send_keys('Brown University')
        university.send_keys(Keys.RETURN)
        """
        degree = bot.find_element_by_name('cards[0bb396d1-c0f6-46c8-a3c5-79444ccc65b5][field3]')
        degree.send_keys(Keys.RETURN)
        degree.send_keys('B')
        degree.send_keys(Keys.RETURN)

        major = bot.find_element_by_name('cards[0bb396d1-c0f6-46c8-a3c5-79444ccc65b5][field5]')
        major.send_keys(Keys.RETURN)
        major.send_keys('Other')
        major.send_keys(Keys.RETURN)

        location = bot.find_element_by_name('cards[0bb396d1-c0f6-46c8-a3c5-79444ccc65b5][field7]')
        location.send_keys(Keys.RETURN)
        location.send_keys('U', Keys.ARROW_DOWN, Keys.RETURN)     
        time.sleep(2)
        print("Selected location")

        """
        demographic = bot.find_element_by_name('candidate-location')
        demographic.send_keys(Keys.RETURN)
        demographic.send_keys('U')
        demographic.send_keys(Keys.DOWN)
        demographic.send_keys(Keys.DOWN) 
        demographic.send_keys(Keys.RETURN)
        """

        consent = bot.find_element_by_name('consent[marketing]')
        actions = ActionChains(bot)
        actions.move_to_element(consent)
        actions.click()
        actions.perform()

        print("consented!")



if __name__ == "__main__":
    tasha = ApplyBot()
    urls = ['https://jobs.lever.co/spotify/233d0c5d-5ec9-4284-8cf8-49c928d06994/apply',
    'https://jobs.lever.co/spotify/5ecdb89c-ac6c-4fe6-891f-b9265ac56d61/apply',
    'https://jobs.lever.co/spotify/e1545f57-eff1-413f-8eca-4c57c3c035e7/apply',
    'https://jobs.lever.co/spotify/88b48be8-b604-4f60-bb32-b03f5d8c957f/apply',
    'https://jobs.lever.co/spotify/2f46bc1b-9605-489a-a06d-e051d3efaef0/apply',
    'https://jobs.lever.co/spotify/5e4b0eda-03e7-411f-b2bf-846de3b8f04a/apply',
    'https://jobs.lever.co/spotify/51150991-18b7-4e24-ad9c-111829df3d30/apply',
    'https://jobs.lever.co/spotify/1de8a240-3881-4a61-bc4a-29ab5f725860/apply',
    'https://jobs.lever.co/spotify/b03f5357-7e72-4d4a-b772-14afbe009946/apply',
    'https://jobs.lever.co/spotify/b0e069e6-d195-4277-afa3-ed8f4e274dbc/apply',
    'https://jobs.lever.co/spotify/d726c929-92fa-4b42-a43c-b9d7c951a230/apply',
    'https://jobs.lever.co/spotify/8649a266-054a-450f-b032-6d37f77fba97/apply',
    'https://jobs.lever.co/spotify/707e2a3a-9f3d-466c-a6e5-57a44e7eec74/apply',
    'https://jobs.lever.co/spotify/fe639d54-d0e6-4ed0-8a60-cea8e9d8fba8/apply']

            
    for url in urls:
        tasha.openPage(url) 
        #tasha.uploadResume()
        tasha.fillText()
        tasha.pullDown()