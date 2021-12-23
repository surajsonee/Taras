import requests
from bs4 import BeautifulSoup
import re
import time
import csv

#URL = ""
#page = requests.get(URL)
#print("started")
#soup = BeautifulSoup(page.content, "html.parser")
#results = soup.find(id="companyResults")
#print(results)

from selenium import webdriver
from selenium.webdriver.chrome import service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import InvalidSelectorException, NoSuchElementException

options = Options()
# options.headless = True
# options.add_argument("--window-size=1920,1200")
ser = Service("/Users/seema/Downloads/chromedriver")
driver = webdriver.Chrome(options=options, service=ser)
driver.get("https://www.dnb.com/business-directory/company-information.scenic_and_sightseeing_transportation_land.us.california.html?page=2")
#print(driver.page_source)
content = driver.page_source
soup = BeautifulSoup(content, features="html.parser")
companies = []
for element in soup.findAll('div', attrs={'id': 'companyResults'}):
    for author in element.findAll('a'):
        filter_link = "https://www.dnb.com"+author['href']
        companies.append(filter_link)

final_data = []

com_lis = ['https://www.dnb.com/business-directory/company-profiles.napa_valley_wine_train_llc.5ffcf97629af298e45b501853fb2f57d.html','https://www.dnb.com/business-directory/company-profiles.als_west_coast_logistics_inc.2cdffffb3ab88a9e30b763c5cbd07757.html']
for i in companies:  
    my_data = []
    driver = webdriver.Chrome(options=options, service=ser)
    print("Processing url: ", i)
    driver.get(i)
    content_ = driver.page_source
    time.sleep(4)
    soup_ = BeautifulSoup(content_, features="html.parser")
    c_data = []
    company_name = driver.find_element_by_xpath('//*[@id="content"]/div/div/div[3]/div/div[1]/div/div[2]/div/div[1]/div[1]/span/span')
    my_data.append(company_name.text)
    company_desc = driver.find_element_by_xpath('//*[@id="content"]/div/div/div[3]/div/div[1]/div/div[2]/div/div[1]/div[2]/span/span')
    my_data.append(company_desc.text)
    company_key_principal = driver.find_element_by_xpath('//*[@id="content"]/div/div/div[3]/div/div[1]/div/div[2]/div/div[1]/div[3]/span/span')
    my_data.append(company_key_principal.text)
    company_industries = driver.find_element_by_xpath('//*[@id="content"]/div/div/div[3]/div/div[1]/div/div[2]/div/div[1]/div[4]/span/span[1]')
    my_data.append(company_industries.text)
    try:
        company_address = driver.find_element_by_xpath('//*[@id="company_profile_snapshot"]/div[2]/div[2]/span/span')
        my_data.append(company_address.text)
    except NoSuchElementException as e:
        my_data.append("No Data")
    try:
        company_phone = driver.find_element_by_xpath('//*[@id="company_profile_snapshot"]/div[3]/div[2]/span/span')
        my_data.append(company_phone.text)
    except NoSuchElementException as e:
        my_data.append("No Data")
    try:
        company_website = driver.find_element_by_xpath('//*[@id="hero-company-link"]')
        my_data.append(company_website.text)
    except NoSuchElementException as e:
         my_data.append("No Data")
    try:
        company_employee_this_site = driver.find_element_by_xpath('//span[contains(@name, "employees_this_site")]/span')
        my_data.append(company_employee_this_site.text)
        print('company_employee_this_site', company_employee_this_site.text)
    except NoSuchElementException as e:
        my_data.append("No Data")

    try:
        company_employee_all_site = driver.find_element_by_xpath('//span[contains(@name, "employees_all_site")]/span')
        my_data.append(company_employee_all_site.text)
        print("company_employee_all_site",company_employee_all_site.text)
    except NoSuchElementException as e:
        my_data.append("No Data")
        print("company_employee_all_site", company_employee_all_site.text)

    try:
        company_revenue = driver.find_element_by_xpath('///span[contains(@name, "revenue_in_us_dollar")]/span')
        my_data.append(company_revenue.text)
        print("company_revenue", company_revenue.text)
    except NoSuchElementException as e:
        my_data.append('No Data')

    try:
        company_year_started = driver.find_element_by_xpath('//span[contains(@name, "year_started")]/span') 
        my_data.append(company_year_started.text)
    except NoSuchElementException as e:
        my_data.append("No Data")
        
    try:
        company_incorporated = driver.find_element_by_xpath('//span[contains(@name, "year_incorporated")]/span')
        my_data.append(company_incorporated.text)
    except NoSuchElementException as e:
        my_data.append("No Data")

    try:
        company_esg_ranking = driver.find_element_by_xpath('//span[contains(@name, "esgRank")]/span')
        my_data.append(company_esg_ranking.text)
    except NoSuchElementException as e:
        my_data.append("No Data")

    try:
        company_esg_industry_avg = driver.find_element_by_xpath('//span[contains(@name, "esgIndustryAverage")]/span')
        my_data.append(company_esg_ranking.text)
    except NoSuchElementException as e:
        my_data.append("No Data")

    final_data.append(my_data)
    driver.close()
    

#     for company_desc in soup_.findAll('div', attrs={'class': 'company-profile-overview-starting-margin'}):
#         for company_name in company_desc.findAll('span', attrs={'name': 'company_name'}):
#             for name in company_name.findAll('span'):
#                 c_name = re.sub('\s+',' ',name.text)
#                 c_data.append(c_name)

#         # for company description
#         for company_name in company_desc.findAll('span', attrs={'name': 'company_description'}):
#             for com_desc in company_name.findAll('span'):
#                 c_desc = re.sub('\s+',' ',com_desc.text)
#                 c_data.append(c_desc)

#         # for key principal
#         for company_name in company_desc.findAll('span', attrs={'name': 'key_principal'}):
#             for com_desc in company_name.find('span'):
#                 c_keyprincipal = re.sub('\s+',' ',com_desc.text).replace(',', ' ')
#                 c_data.append(c_keyprincipal)
#                 #print('Key principal', c_keyprincipal)

#         # for industry links
#         for company_name in company_desc.findAll('span', attrs={'name': 'industry_links'}):
#             for a in company_name.findAll('a', attrs={'class': 'company_profile_overview_underline_links'}):
#                 c_indus = re.sub('\s+',' ',a.text).replace(',', ' ')
#                 c_data.append(c_indus)
#                 #print('Industry', c_indus)

#     for element_ in soup_.findAll('div', attrs={'id': 'company_profile_snapshot'}):
#         for address in element_.findAll('span', attrs={'name': 'company_address'}):
#             for span in address.find('span'):
#                 new_data = re.sub('\s+',' ',span.text)
#                 c_data.append(new_data)

#         # Get company phone
#         for address in element_.findAll('span', attrs={'name': 'company_phone'}):
#             for span in address.find('span'):
#                 new_data = re.sub('\s+',' ',span.text)
#                 c_data.append(new_data)

#         # Get company website
#         for address in element_.findAll('span', attrs={'name': 'company_website'}):
#             for span in address.findAll('span'):
#                 for a in span.findAll('a', attrs={'id': 'hero-company-link'}):
#                     c_data.append(a['href'])

#         # Get company employees_this_site
#         for address in element_.findAll('span', attrs={'name': 'employees_this_site'}):
#             for span in address.find('span'):
#                 new_data = re.sub('\s+',' ',span.text)
#                 c_data.append(new_data)
        
#         # Get company employees_all_site
#         for address in element_.findAll('span', attrs={'name': 'employees_all_site'}):
#             for span in address.find('span'):
#                 new_data = re.sub('\s+',' ',span.text)
#                 c_data.append(new_data)

#         # Get company revenue
#         for address in element_.findAll('span', attrs={'name': 'revenue_in_us_dollar'}):
#             for span in address.find('span'):
#                 new_data = re.sub('\s+',' ',span.text)
#                 c_data.append(new_data)
        
#         # Get company year_started
#         for address in element_.findAll('span', attrs={'name': 'year_started'}):
#             for span in address.find('span'):
#                 new_data = re.sub('\s+',' ',span.text)
#                 c_data.append(new_data)

#         # Get company year_incorporated
#         for address in element_.findAll('span', attrs={'name': 'year_incorporated'}):
#             if address == '':
#                 print("Yes found!")
#             for span in address.find('span'):
#                 new_data = re.sub('\s+',' ',span.text)
#                 if new_data is None and new_data == '':
#                     c_data.append(new_data)

#         # Get company esgRank
#         for address in element_.findAll('span', attrs={'name': 'esgRank'}):
#             for span in address.find('span'):
#                 new_data = re.sub('\s+',' ',span.text)
#                 c_data.append(new_data)

#         # Get company esgIndustryAverage
#         for address in element_.findAll('span', attrs={'name': 'esgIndustryAverage'}):
#             for span in address.find('span'):
#                 new_data = re.sub('\s+',' ',span.text)
#                 c_data.append(new_data)

#     final_data.append(c_data)

# str_list = [list(filter(None, lst)) for lst in final_data]
# print(str_list)


with open('/Users/seema/Documents/Myprojects/output.csv','a') as f:
    writer = csv.writer(f)
    writer.writerow(['Company_Name', 'Company_Description', 'Key_Principal', 'Industry', 'Address', 'Phone', 'website', 'Employee(This site)', 'Employee(All site)', 'Revenue', 'Year started', 'Incorporated', 'ESG ranking', 'ESG industry average'])
    writer.writerows(final_data)






