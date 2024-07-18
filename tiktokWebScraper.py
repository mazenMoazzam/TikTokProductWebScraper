import requests
from bs4 import BeautifulSoup
import csv
import os

tiktokUrl = 'https://ads.tiktok.com/business/creativecenter/top-products/pc/en'

response = requests.get(tiktokUrl)
htmlContent = response.content

soup = BeautifulSoup(htmlContent, 'html.parser')

products = []

for productRow in soup.find_all('tr', class_='product row class'):  
    productName = productRow.find('td', class_='product name class').text.strip()  
    productCategory = productRow.find('td', class_='product category class').text.strip() 
    popularity = productRow.find('td', class_='product popularity class').text.strip()  
    popularityChange = productRow.find('td', class_='product popularity change class').text.strip()  
    ctr = productRow.find('td', class_='product ctr class').text.strip()  
    cvr = productRow.find('td', class_='product cvr class').text.strip() 
    cpa = productRow.find('td', class_='product cpa class').text.strip()  

    products.append([productName, productCategory, popularity, popularityChange, ctr, cvr, cpa])

print("Current directory:", os.getcwd()) #wrote this to see what directory the csv file is being written

outputPath = 'tiktokProducts.csv'
with open(outputPath, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Product Name', 'Category', 'Popularity', 'Popularity Change', 'CTR', 'CVR', 'CPA'])
    writer.writerows(products)

print(f"Data saved to {output_path}")
