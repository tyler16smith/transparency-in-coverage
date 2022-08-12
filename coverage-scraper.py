import gzip
import json
import shutil
import time
from selenium import webdriver

urls = {
    "uhc": "https://transparency-in-coverage.uhc.com/",
    "kaiser": "https://healthy.kaiserpermanente.org/front-door/machine-readable",
    "anthem": "https://www.anthem.com/machine-readable-file/search/",
    "centene": "https://www.centene.com/price-transparency-files.html",
    "cigna": "https://www.cigna.com/legal/compliance/machine-readable-files",
    "humana": "https://developers.humana.com/Cost-Transparency",
}

# chromedriver
path = "C:/Program Files (x86)/Google/chromedriver.exe"
driver = webdriver.Chrome(path)
driver.get(urls["uhc"])
time.sleep(10)

# loop through first 10 records
for i in range(10):
    file_xpath = f'//*[@data-testid="list-item-{i}"]/div/div[2]/a'

    file_name = driver.find_element_by_xpath(file_xpath).text
    driver.find_element_by_xpath(file_xpath).click()
    time.sleep(3)
    file_loc = f"C:/Users/tyler/Downloads/{file_name}"

    if file_name[-2:] == "gz":
        with gzip.open(file_loc, "r") as f:
            data = f.read()
            j = json.loads(data.decode('utf-8'))
            print(type(j))
            print(j)
    else:
        file = open(file_loc)
        data = json.load(file)
        print(type(data))
        print(data)
