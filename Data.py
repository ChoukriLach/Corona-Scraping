from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ChromeOptions
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import os
from time import sleep



class Data :
    
    def __init__(self,url):
        self.url = url 
        self.data = self.get_data()
        

    def get_data(self) :
        options = ChromeOptions() 
        options.add_argument("headless")
        options.add_argument('--log-level=1')
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()) , options=options)
        driver.get(self.url)
        os.system('cls' if os.name == 'nt' else 'clear')
        sleep(2)
        totals = [ elem.text for elem in driver.find_elements(By.CSS_SELECTOR ,".maincounter-number")]  
        countries = [elem.text for elem in driver.find_elements(By.CSS_SELECTOR, 'a[href^="country"]')] 
        countries = [elem for elem in countries if elem]  
        countries.insert(207,"Diamond Princess")
        countries.insert(213,"Palau")
        countries.insert(217,"MS Zaandam")
        total_cases =  [elem.text for elem in driver.find_elements(By.CSS_SELECTOR , ".sorting_1")]  
        total_cases = [elem for elem in total_cases if elem]
        del total_cases[0]
        total_deaths = [elem.text for elem in driver.find_elements(By.CSS_SELECTOR , "td:nth-of-type(5)")] 
        total_deaths = total_deaths[4:232]
        del total_deaths[1]
        del total_deaths[6]
        del total_deaths[32]
        del total_deaths[207]
        total_recovered = [elem.text for elem in driver.find_elements(By.CSS_SELECTOR , "td:nth-of-type(7)")] 
        total_recovered = total_recovered[4:232]
        total_recovered = [ elem for elem in total_recovered if elem]
        countries.insert(0,'World')
        total_cases.insert(0,totals[0])
        total_deaths.insert(0,totals[1])
        total_recovered.insert(0,totals[2])
        data = {'Countries' : countries , 'Total Cases' : total_cases , 'Total Deaths' : total_deaths , 'Total Recovered' : total_recovered}

        return data


    def get_total_country_cases(self,country) : 

        for i in range(len(self.data['Countries'])) :
            if str(self.data['Countries'][i]).lower() == str(country).lower() :
                if str(self.data['Total Cases'][i]) == '' :
                    return 0 
                return self.data['Total Cases'][i]

    def get_total_country_death_cases(self,country) : 

        for i in range(len(self.data['Countries'])) :
            if str(self.data['Countries'][i]).lower() == str(country).lower() :
                if str(self.data['Total Deaths'][i]) == '' :
                    return 0 
                return self.data['Total Deaths'][i]

    def get_total_country_recovered_cases(self,country) : 

        for i in range(len(self.data['Countries'])) :
            if str(self.data['Countries'][i]).lower() == str(country).lower() :
                if str(self.data['Total Recovered'][i]) == '' :
                    return 0 
                if str(self.data['Total Recovered'][i]) == 'N/A' :
                    return 'Not Available'
                return self.data['Total Recovered'][i]





        

    