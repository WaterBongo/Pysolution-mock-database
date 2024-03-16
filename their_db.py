import requests,scrapeimage,threading
quests = []
unit ="10.5"
while True:
    herm = input("Question")
    if herm.isdigit():
        quests.append(int(herm))
    elif "-" in herm:
        herm = herm.split('-')
        for num in range(int(herm[0]),int(herm[1])+1):
            quests.append(num)
    if herm == "odd":
        oddq = input("Odd Questions: ")
        #sample would be like 8-16
        oddq=oddq.split('-')
        for num in range(int(oddq[0])-1,int(oddq[1])+1):
            if int(num) % 2 != 0:
                quests.append(num)
    elif herm == "even":
        evenq = input("Even Questions: ")
        evenq=evenq.split('-')
        for num in range(int(evenq[0])-1,int(evenq[1])+1):
            if int(num) % 2 == 0:
                quests.append(num)
    elif herm == "eoo":
        eooq = input("Every Other Odd Questions: ")
        eooq = eooq.split('-')
        temp_list = []
        for num in range(int(eooq[0])-1,int(eooq[1])+1):
            if int(num) % 2 != 0:
                temp_list.append(num)
        for num in range(len(temp_list)):
            if num % 2 == 0:
                quests.append(temp_list[num])
    elif herm == "mulp":
        multiple = int(input("Enter the multiple: "))
        mulpq = input("Range for multiples: ")
        mulpq = mulpq.split('-')
        for num in range(int(mulpq[0]), int(mulpq[1])+1):
            if num % multiple == 0:
                quests.append(num)
    elif herm =="break":
        break
    print(quests)



def get_img(val):

    headers = {
        'DNT': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
        'authorization': 'wixcode-pub.26fb95dc4d808536e2e1d64dd5cfd1e16dc45fb7.eyJpbnN0YW5jZUlkIjoiMDUzZDZjZjgtYzM1Yi00MWI3LTk4ZDItNTkwMWQ4YjM0NmI5IiwiaHRtbFNpdGVJZCI6ImM2ZThlNTM2LWY4NDEtNGYwMi05NWNhLTgyNmRjYzczNzA3MCIsInVpZCI6bnVsbCwicGVybWlzc2lvbnMiOm51bGwsImlzVGVtcGxhdGUiOmZhbHNlLCJzaWduRGF0ZSI6MTcwNzQxOTg1MDMwOSwiYWlkIjoiODQzNjhjNjYtM2IxNy00ZmVhLTgyYWUtOGFkYjI1MGE5OWM5IiwiYXBwRGVmSWQiOiJDbG91ZFNpdGVFeHRlbnNpb24iLCJpc0FkbWluIjpmYWxzZSwibWV0YVNpdGVJZCI6IjNkYjk3OTJmLTliYWYtNDg0Ny05ZGIxLWI2ZDVjYzc5YWIwZiIsImNhY2hlIjpudWxsLCJleHBpcmF0aW9uRGF0ZSI6bnVsbCwicHJlbWl1bUFzc2V0cyI6IlNob3dXaXhXaGlsZUxvYWRpbmcsSGFzRG9tYWluLEFkc0ZyZWUiLCJ0ZW5hbnQiOm51bGwsInNpdGVPd25lcklkIjoiNzNkZmY5YmMtZDRjNy00YjQ2LTg1OTEtNTM0YzBkNmFlYjE1IiwiaW5zdGFuY2VUeXBlIjoicHViIiwic2l0ZU1lbWJlcklkIjpudWxsLCJwZXJtaXNzaW9uU2NvcGUiOm51bGwsImxvZ2luQWNjb3VudElkIjpudWxsLCJpc0xvZ2luQWNjb3VudE93bmVyIjpudWxsfQ==',

        'Accept': 'application/json, text/plain, */*',
        'Referer': 'https://www.litsolutions.org/_partials/wix-thunderbolt/dist/clientWorker.14ac12b3.bundle.min.js',
        'commonConfig': '%7B%22brand%22%3A%22wix%22%2C%22host%22%3A%22VIEWER%22%2C%22BSI%22%3A%22be392483-54cd-4a9b-9eb8-194d1fb8504c%7C1%22%7D',
        'x-wix-brand': 'wix',
        'X-Wix-Client-Artifact-Id': 'wix-thunderbolt',
    }
    json_data = {
            'collectionName': 'dsd32',
            'dataQuery': {
                'filter': {
                    'fileName': {
                        '$contains': f'9781337516853, Chapter {unit}, Problem {val }E.png',
                    },
                },
                'paging': {
                    'offset': 0,
                },
                'fields': [],
            },
            'options': {},
            'includeReferencedItems': [],
            'segment': 'LIVE',
            'appId': '4a5d6d14-5386-4dd7-ab71-ee3148e20c5f',
        }

    response = requests.post('https://www.litsolutions.org/_api/cloud-data/v1/wix-data/collections/query', headers=headers, json=json_data)
    print(f"{response.json()['items'][0]['link']} | {val}")

    

headers = {
    'DNT': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    'authorization': 'wixcode-pub.26fb95dc4d808536e2e1d64dd5cfd1e16dc45fb7.eyJpbnN0YW5jZUlkIjoiMDUzZDZjZjgtYzM1Yi00MWI3LTk4ZDItNTkwMWQ4YjM0NmI5IiwiaHRtbFNpdGVJZCI6ImM2ZThlNTM2LWY4NDEtNGYwMi05NWNhLTgyNmRjYzczNzA3MCIsInVpZCI6bnVsbCwicGVybWlzc2lvbnMiOm51bGwsImlzVGVtcGxhdGUiOmZhbHNlLCJzaWduRGF0ZSI6MTcwNzQxOTg1MDMwOSwiYWlkIjoiODQzNjhjNjYtM2IxNy00ZmVhLTgyYWUtOGFkYjI1MGE5OWM5IiwiYXBwRGVmSWQiOiJDbG91ZFNpdGVFeHRlbnNpb24iLCJpc0FkbWluIjpmYWxzZSwibWV0YVNpdGVJZCI6IjNkYjk3OTJmLTliYWYtNDg0Ny05ZGIxLWI2ZDVjYzc5YWIwZiIsImNhY2hlIjpudWxsLCJleHBpcmF0aW9uRGF0ZSI6bnVsbCwicHJlbWl1bUFzc2V0cyI6IlNob3dXaXhXaGlsZUxvYWRpbmcsSGFzRG9tYWluLEFkc0ZyZWUiLCJ0ZW5hbnQiOm51bGwsInNpdGVPd25lcklkIjoiNzNkZmY5YmMtZDRjNy00YjQ2LTg1OTEtNTM0YzBkNmFlYjE1IiwiaW5zdGFuY2VUeXBlIjoicHViIiwic2l0ZU1lbWJlcklkIjpudWxsLCJwZXJtaXNzaW9uU2NvcGUiOm51bGwsImxvZ2luQWNjb3VudElkIjpudWxsLCJpc0xvZ2luQWNjb3VudE93bmVyIjpudWxsfQ==',

    'Accept': 'application/json, text/plain, */*',
    'Referer': 'https://www.litsolutions.org/_partials/wix-thunderbolt/dist/clientWorker.14ac12b3.bundle.min.js',
    'commonConfig': '%7B%22brand%22%3A%22wix%22%2C%22host%22%3A%22VIEWER%22%2C%22BSI%22%3A%22be392483-54cd-4a9b-9eb8-194d1fb8504c%7C1%22%7D',
    'x-wix-brand': 'wix',
    'X-Wix-Client-Artifact-Id': 'wix-thunderbolt',
}
for val in quests:
    json_data = {
        'collectionName': 'dsd32',
        'dataQuery': {
            'filter': {
                'fileName': {
                    '$contains': f'9781337516853, Chapter {unit}, Problem {val }E.png',
                },
            },
            'paging': {
                'offset': 0,
            },
            'fields': [],
        },
        'options': {},
        'includeReferencedItems': [],
        'segment': 'LIVE',
        'appId': '4a5d6d14-5386-4dd7-ab71-ee3148e20c5f',
    }
    
    response = requests.post('https://www.litsolutions.org/_api/cloud-data/v1/wix-data/collections/query', headers=headers, json=json_data)
    print(response.json()['items'][0]['link'])
    # img_link = scrapeimage.get_image_link(response.json()['items'][0]['link'])
    # scrapeimage.download_image(img_link, f"Chapter {unit}, Problem {val}E.png")
