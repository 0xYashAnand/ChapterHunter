import array as manga
import requests, openpyxl
from bs4 import BeautifulSoup


excel = openpyxl.Workbook()

#print(excel.sheetnames)                                     # printing how many sheets we have in our excel file                  
sheet = excel.active                                         # activating the sheets for our use
sheet.title = 'Latest Manga Realeasd'                        # renaming the sheet name
print(excel.sheetnames)                                      # printing the sheet name
sheet.append(['Manga Name'  , 'Chapter' , 'Release Time'])   # creating three rows 



# creating array as manga
manga = [ 
    "https://manhuaus.com/manga/100000-levels-of-body-refining-all-the-dogs-i-raise-are-the-emperor/",
    "https://manhuaus.com/manga/99-ways-to-become-heroes-by-beauty-masters/",
    "https://manhuaus.com/manga/againts-the-sky-supreme/",
    "https://manhuaus.com/manga/am-i-invincible/",
    "https://manhuaus.com/manga/banished-disciples-counterattack/",
    "https://manhuaus.com/manga/chronicles-of-the-martial-gods-return/",
    "https://manhuaus.com/manga/coming-out-of-seclusion-after-a-hundred-thousand-years/",
    "https://manhuaus.com/manga/cultivating-the-supreme-dantian/",
    "https://1stkissmanga.me/manga/hey-boss-i-am-your-new-wife/",
    "https://1stkissmanga.me/manga/im-the-great-immortal/"
]

x = len(manga)

# code for scrapping the website
for x in manga:
        #req for reading all the info of the website
        req = requests.get(x)                                            
        soup = BeautifulSoup(req.content , "html.parser")

        #creating object then using find to identify the html tag with class 
        MangaName = soup.find('div'  , class_="post-title").h1.text             
        Chapter = soup.find('li' , class_="wp-manga-chapter").a.text
        Date = soup.find('li' , class_="wp-manga-chapter").span.text
        print(MangaName, Chapter , Date)

        #storing data in excel sheet 
        sheet.append([MangaName, Chapter , Date])                           
        

excel.save('Chapter Update Info.xlsx')