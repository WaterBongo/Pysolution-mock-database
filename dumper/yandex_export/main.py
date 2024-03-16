import requests

from bs4 import BeautifulSoup
import json
he = ''

#
sesh = requests.Session()
cookies = {
    'yandexuid': '4477297161707092377',
    'spravka': 'dD0xNzA5NDk4NzIxO2k9MTQ2Ljc0Ljk0LjExNjtEPUFBOERDRkVBMUU1MUREQ0I2NUY3NzVCRkE3N0FBQTJDQzY1Mzg2OUVDNUNGNDk0RDJFODQ5ODVCRjE0NzlENTZDRkE4QTVGMUQ0MzU2RTI3NEQxQTgyNjhGRkFBMEFEN0RENzIwQzQzRkVBNDYyNkQzQjcxQjdGQjY4OUE2RTRFMDVDNzUyQkE2QjAxRDFCRDE5M0NGNkM3QjI5MTE0MDlDQkQ3M0ZCOUFCODMxNzU2QzMyMjdENkU1RDlEO3U9MTcwOTQ5ODcyMTU2NzgzOTI5OTtoPWU2NTE0MmFmNDVjZDBhNGUzNWNmOTE1NDg5NWU4MTE0',
    'is_gdpr': '0',
    'is_gdpr_b': 'CLKxMRD47gE=',
    'i': 'OvN1u3AXCsI1MJvQELeBNOV2tnG1p2Tlqk+UnxLq8bDaUW2+j+UcA/Zl04ZT7yApdlCnY2AkB6MSl3dAEMb2h77/Vjs=',
    'yashr': '3711696501709701205',
    'receive-cookie-deprecation': '1',
    'yp': '1710306008.szm.2:1440x900:1222x855',
    '_yasc': '/Cp84jEUB9T6ILsMI1CiTRUGNSIaJ2TiiN/FC5Xm7AF3gq2whdfLa3vPMz0mWofDq6hUBk3eHooEznyv',
    'bltsr': '1',
    'KIykI': '1',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'yandexuid=4477297161707092377; spravka=dD0xNzA5NDk4NzIxO2k9MTQ2Ljc0Ljk0LjExNjtEPUFBOERDRkVBMUU1MUREQ0I2NUY3NzVCRkE3N0FBQTJDQzY1Mzg2OUVDNUNGNDk0RDJFODQ5ODVCRjE0NzlENTZDRkE4QTVGMUQ0MzU2RTI3NEQxQTgyNjhGRkFBMEFEN0RENzIwQzQzRkVBNDYyNkQzQjcxQjdGQjY4OUE2RTRFMDVDNzUyQkE2QjAxRDFCRDE5M0NGNkM3QjI5MTE0MDlDQkQ3M0ZCOUFCODMxNzU2QzMyMjdENkU1RDlEO3U9MTcwOTQ5ODcyMTU2NzgzOTI5OTtoPWU2NTE0MmFmNDVjZDBhNGUzNWNmOTE1NDg5NWU4MTE0; is_gdpr=0; is_gdpr_b=CLKxMRD47gE=; i=OvN1u3AXCsI1MJvQELeBNOV2tnG1p2Tlqk+UnxLq8bDaUW2+j+UcA/Zl04ZT7yApdlCnY2AkB6MSl3dAEMb2h77/Vjs=; yashr=3711696501709701205; receive-cookie-deprecation=1; yp=1710306008.szm.2:1440x900:1222x855; _yasc=/Cp84jEUB9T6ILsMI1CiTRUGNSIaJ2TiiN/FC5Xm7AF3gq2whdfLa3vPMz0mWofDq6hUBk3eHooEznyv; bltsr=1; KIykI=1',
    'DNT': '1',
    'If-None-Match': 'W/"820a-P2/BowU5my1pDV70OroZtOME8Sg"',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not(A:Brand";v="24", "Chromium";v="122"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
}

response = sesh.get('https://yadi.sk/i/Lc7sl9fNjk8prg', cookies=cookies, headers=headers)
print(response.text)
soup = BeautifulSoup(response.text, 'html.parser')
# Now you can use BeautifulSoup methods to parse and extract data from the website
# For example, you can find all the links on the page using the find_all method
meta_tags = soup.find_all('meta')
for tag in meta_tags:
    if 'property' in tag.attrs and tag.attrs['property'] == 'og:image':
        content = tag.attrs['content']
        print(content)
        lin = content.replace("&amp;","&")
        print(lin)


import requests

cookies = {
    'yandexuid': '4477297161707092377',
    'spravka': 'dD0xNzA5NDk4NzIxO2k9MTQ2Ljc0Ljk0LjExNjtEPUFBOERDRkVBMUU1MUREQ0I2NUY3NzVCRkE3N0FBQTJDQzY1Mzg2OUVDNUNGNDk0RDJFODQ5ODVCRjE0NzlENTZDRkE4QTVGMUQ0MzU2RTI3NEQxQTgyNjhGRkFBMEFEN0RENzIwQzQzRkVBNDYyNkQzQjcxQjdGQjY4OUE2RTRFMDVDNzUyQkE2QjAxRDFCRDE5M0NGNkM3QjI5MTE0MDlDQkQ3M0ZCOUFCODMxNzU2QzMyMjdENkU1RDlEO3U9MTcwOTQ5ODcyMTU2NzgzOTI5OTtoPWU2NTE0MmFmNDVjZDBhNGUzNWNmOTE1NDg5NWU4MTE0',
    'is_gdpr': '0',
    'is_gdpr_b': 'CLKxMRD47gE=',
    'i': 'OvN1u3AXCsI1MJvQELeBNOV2tnG1p2Tlqk+UnxLq8bDaUW2+j+UcA/Zl04ZT7yApdlCnY2AkB6MSl3dAEMb2h77/Vjs=',
    'yashr': '3711696501709701205',
    'receive-cookie-deprecation': '1',
    'yp': '1710306008.szm.2:1440x900:1222x855',
    '_yasc': '/Cp84jEUB9T6ILsMI1CiTRUGNSIaJ2TiiN/FC5Xm7AF3gq2whdfLa3vPMz0mWofDq6hUBk3eHooEznyv',
    'bltsr': '1',
    'KIykI': '1',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'text/plain',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'yandexuid=4477297161707092377; spravka=dD0xNzA5NDk4NzIxO2k9MTQ2Ljc0Ljk0LjExNjtEPUFBOERDRkVBMUU1MUREQ0I2NUY3NzVCRkE3N0FBQTJDQzY1Mzg2OUVDNUNGNDk0RDJFODQ5ODVCRjE0NzlENTZDRkE4QTVGMUQ0MzU2RTI3NEQxQTgyNjhGRkFBMEFEN0RENzIwQzQzRkVBNDYyNkQzQjcxQjdGQjY4OUE2RTRFMDVDNzUyQkE2QjAxRDFCRDE5M0NGNkM3QjI5MTE0MDlDQkQ3M0ZCOUFCODMxNzU2QzMyMjdENkU1RDlEO3U9MTcwOTQ5ODcyMTU2NzgzOTI5OTtoPWU2NTE0MmFmNDVjZDBhNGUzNWNmOTE1NDg5NWU4MTE0; is_gdpr=0; is_gdpr_b=CLKxMRD47gE=; i=OvN1u3AXCsI1MJvQELeBNOV2tnG1p2Tlqk+UnxLq8bDaUW2+j+UcA/Zl04ZT7yApdlCnY2AkB6MSl3dAEMb2h77/Vjs=; yashr=3711696501709701205; receive-cookie-deprecation=1; yp=1710306008.szm.2:1440x900:1222x855; _yasc=/Cp84jEUB9T6ILsMI1CiTRUGNSIaJ2TiiN/FC5Xm7AF3gq2whdfLa3vPMz0mWofDq6hUBk3eHooEznyv; bltsr=1; KIykI=1',
    'DNT': '1',
    'Origin': 'https://disk.yandex.com',
    'Referer': 'https://disk.yandex.com/i/SV3K2gjvRDs-hQ',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'X-Retpath-Y': 'https://disk.yandex.com/i/SV3K2gjvRDs-hQ',
    'sec-ch-ua': '"Not(A:Brand";v="24", "Chromium";v="122"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
}

# data = he
# response = requests.post('https://disk.yandex.com/public/api/download-url', cookies=cookies, headers=headers, data=data)
# print(response.text)