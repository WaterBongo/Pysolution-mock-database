import botasaurus,requests
from botasaurus import *

from botasaurus import *

@browser()
def get_image_link(driver: AntiDetectDriver, data):
    driver.google_get(data)
    heading_element = driver.get_elements_or_none_by_xpath('//*[@id="app"]/div/div/div/div[1]/div[1]/img')
    if heading_element:
        heading_src = heading_element[0].get_attribute("src")
        print(heading_src)
    
    return heading_src

def download_image(link,name):
    response = requests.get(link)
    with open(f"./wrk/{name}", "wb") as file:
        file.write(response.content)
if __name__ == "__main__":
    yandex_link="https://yadi.sk/i/vuxpMFxeEtiZeA"
    imagelink = get_image_link(yandex_link)
    download_image(imagelink)

    