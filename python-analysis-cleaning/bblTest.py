import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys


## open acris with selenium
driver = webdriver.Chrome()
driver.get("https://a836-acris.nyc.gov/CP/LookUp/Index")
assert "Automated" in driver.title

## open CSV
completedDF = pd.read_csv('LL24Completed.csv')

## add empty BBL Column
bbl = ""
completedDF['BBL'] = bbl

## iterate over each row and find BBL number with address
for index, row in completedDF.iterrows():
    dfBorough = row['Borough']
    dfAddress = row['Address']
  
    if isinstance(dfBorough, str):
        print(dfBorough)

        if isinstance(dfAddress, str):
            splitAddress = dfAddress.split()
            dfStreetNum = splitAddress[0]
            dfStreetName = dfAddress.replace(dfStreetNum, '')
            print(dfStreetNum)
            print(dfStreetName)
   
            ## input borough
            borough = driver.find_element_by_name("select_borough")
            borough.send_keys(dfBorough[0])
            borough.send_keys(Keys.RETURN)
            
            ## input street Num
            streetNum = driver.find_element_by_name("text_street_number")
            streetNum.clear()
            streetNum.send_keys(dfStreetNum)
            
            ## input street Name
            streetName = driver.find_element_by_name("text_street_name")
            streetName.clear()
            streetName.send_keys(dfStreetName)
            
            submit22 = driver.find_element_by_name("submit22")
            submit22.submit()
            
            time.sleep(1)
            
            block = driver.find_element_by_name("text_block")
            lot = driver.find_element_by_name("text_lot")
            
            blockNum = block.get_attribute("value")
            lotNum = lot.get_attribute("value")
            
            boroughNum = ''
            if dfBorough == 'Manhattan':
                boroughNum = '1'
            elif dfBorough == 'Bronx':
                boroughNum = '2'
            elif dfBorough == 'Brooklyn':
                boroughNum = '3'
            elif dfBorough == 'Queens':
                boroughNum = '4'
            elif dfBorough == 'Staten Island':
                boroughNum = '5'

            bblNum = ''
            bblNum = boroughNum + blockNum + lotNum
            print(bblNum)

            completedDF.loc[index, 'BBL'] = bblNum
            row['BBL'] = bblNum

completedDF.to_csv('LL24Completed_bbl.csv')

##driver.close()
