import requests
from parsel import Selector
base_url = 'https://www.skiresort.info'
main_url = f'{base_url}/ski-resorts/'
try:
    res = requests.get(main_url, timeout=10)
    print("connected successfuly")
    sel = Selector(text=res.text)
    links = sel.xpath("//div[@id ='resortList']//a[@class='h3']/@href").getall()
    names = sel.xpath("//div[@id ='resortList']//a[@class='h3']/text()").getall()

    for i, (name, link) in enumerate(zip(names[:50], links[:50]), start=1):
        resort_name = name.strip()
        if link.startswith('/'):
            resort_link = base_url + link
        else:
            resort_link = link
            print(f"\n{i}. {resort_name}: {resort_link}")
        
        try:
            resort_response = requests.get(resort_link ,timeout=10)
            resort_sel = Selector(text=resort_response.text)
            
            elevation_text = resort_sel.xpath('//div[@id="selAlti"]//text()').getall()
            if elevation_text:
                print(f'Elevation info : {elevation_text}')
            else:
                print(f'Elevation info Not Found!')
            
            
        except requests.exceptions.RequestException as e:
            print(f'connection Error : {e}')
            
            
        
except requests.exceptions.RequestException as e:
    print(f'Connection Error : {e}')

