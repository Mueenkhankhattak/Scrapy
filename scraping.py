from bs4 import BeautifulSoup
import requests
url = 'https://www.skiresort.info/ski-resorts'
res = requests.get(url)
if res.status_code == 200:
    print(" Request successful!")
else:
    print(" Request failed!")


soup = BeautifulSoup(res.text, "lxml")

resorts =soup.find_all("div" , class_='resort-list-item')
resort_links = []
for resort in resorts:
    a_tag = resort.find("a" , class_="h3")
        
    if a_tag:
             
        resort_name  = a_tag.text.strip()
        href = a_tag.get("href")
        if href.startswith("http"):
            full_url = href
        else:
            full_url = f"https://www.skiresort.info{href}"

        resort_links.append(full_url)
        print(f'resort name : {resort_name}')
        print(f'urls : {full_url}')
        print('-' * 50)

        
for link in resort_links:
    try:
        res = requests.get(link)
        res.raise_for_status()
    except Exception as e:
        print(f"Failed to fetch {link} → {e}")
        continue

    
    soup = BeautifulSoup(res.text , 'lxml')
    detail_blocks = soup.find_all("div" , class_='detail-links')
    for main in detail_blocks:
        h5_label = main.find('div' , class_='label h5')
        if h5_label == 'Main link':
            description = main.find("div" , class_='description')
            if description:
                a_tag = description.find('a')
                if a_tag:
                    website_text = a_tag.text.strip()
                    website_url = a_tag['href']
                    print(f"Main Website: {website_text} → {website_url}")
                    print('-' * 50)
        
    
    


