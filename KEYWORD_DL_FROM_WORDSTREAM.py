from selenium import webdriver
from pathlib import Path
import time
import pandas as pd
option = webdriver.ChromeOptions()

option.add_argument("--user-data-dir=C:\\Users\\NEO\\AppData\\Local\\Google\\Chrome\\User Data\\")
option.add_argument("--profile-directory=Profile 1")
driver = webdriver.Chrome(executable_path=r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe', options=option)
driver.get('https://www.wordstream.com/popular-keywords')
link = driver.find_elements_by_partial_link_text('Keywords')
f = open('key.txt','w')
for i in range(len(link)):
    case =  (link[i].text.lower())
    f.write(case + '\n')
f.close()
# driver.close()
f = open('key.txt').readlines()
# DL CSV
for i in range(0, len(f)):
    link = "https://www.wordstream.com/popular-keywords/create/csv?tag_id="
    end_link = "-keywords"
    url = str(link)+str(f[i])+str(end_link)
    driver.get(url)
    time.sleep(3)       #Download csv file from wordstream
    # driver.close()
driver.quit()
# Change from CSV to TXT
for in_path in Path('PATH_TO_DL_FOLDER').glob('*.csv'):
     out_path = in_path.with_suffix('.txt')
     with in_path.open('r') as fin, out_path.open('w') as fout:
         reader = pd.read_csv(fin,index_col=False)
         writer = reader["Keyword"].tolist()
         # print(writer)
         raw = '\n'.join(writer)
         clear = fout.write(raw)
