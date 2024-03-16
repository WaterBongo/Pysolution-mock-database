import requests
import os







def dump_all_solutions(isbn,bin):
    sols = []
    headers = {
        'DNT': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        'authorization': 'wixcode-pub.410face28c390b732bd4c7c20f7ed583d9818567.eyJpbnN0YW5jZUlkIjoiMDUzZDZjZjgtYzM1Yi00MWI3LTk4ZDItNTkwMWQ4YjM0NmI5IiwiaHRtbFNpdGVJZCI6ImM2ZThlNTM2LWY4NDEtNGYwMi05NWNhLTgyNmRjYzczNzA3MCIsInVpZCI6bnVsbCwicGVybWlzc2lvbnMiOm51bGwsImlzVGVtcGxhdGUiOmZhbHNlLCJzaWduRGF0ZSI6MTcwOTY5NjgxOTYwMSwiYWlkIjoiODQzNjhjNjYtM2IxNy00ZmVhLTgyYWUtOGFkYjI1MGE5OWM5IiwiYXBwRGVmSWQiOiJDbG91ZFNpdGVFeHRlbnNpb24iLCJpc0FkbWluIjpmYWxzZSwibWV0YVNpdGVJZCI6IjNkYjk3OTJmLTliYWYtNDg0Ny05ZGIxLWI2ZDVjYzc5YWIwZiIsImNhY2hlIjpudWxsLCJleHBpcmF0aW9uRGF0ZSI6bnVsbCwicHJlbWl1bUFzc2V0cyI6IlNob3dXaXhXaGlsZUxvYWRpbmcsQWRzRnJlZSxIYXNEb21haW4iLCJ0ZW5hbnQiOm51bGwsInNpdGVPd25lcklkIjoiNzNkZmY5YmMtZDRjNy00YjQ2LTg1OTEtNTM0YzBkNmFlYjE1IiwiaW5zdGFuY2VUeXBlIjoicHViIiwic2l0ZU1lbWJlcklkIjpudWxsLCJwZXJtaXNzaW9uU2NvcGUiOm51bGwsImxvZ2luQWNjb3VudElkIjpudWxsLCJpc0xvZ2luQWNjb3VudE93bmVyIjpudWxsfQ==',
        # Already added when you pass json=
        # 'Content-Type': 'application/json',
        'Accept': 'application/json, text/plain, */*',
        'Referer': 'https://www.litsolutions.org/_partials/wix-thunderbolt/dist/clientWorker.647591a4.bundle.min.js',
        'commonConfig': '%7B%22brand%22%3A%22wix%22%2C%22host%22%3A%22VIEWER%22%2C%22BSI%22%3A%22f2d71a20-314c-4936-8112-252eb148a84d%7C2%22%7D',
        'x-wix-brand': 'wix',
        'X-Wix-Client-Artifact-Id': 'wix-thunderbolt',
    }

    json_data = {
        'collectionName': 'dsd32',
        'dataQuery': {
            'filter': {
                'isbn_c_p': {
                    '$contains': f'{isbn}_{bin}',
                },
            },
            'sort': [
                {
                    'fieldName': 'timeStamp',
                    'order': 'ASC',
                },
            ],
            'paging': {
                'offset': 0,
                'limit': 1000,
            },
            'fields': [],
        },
        'options': {},
        'includeReferencedItems': [],
        'segment': 'LIVE',
        'appId': 'b5f31e06-ca73-4184-b3ee-0c26227e9fd1',
    }

    response = requests.post('https://www.litsolutions.org/_api/cloud-data/v1/wix-data/collections/query', headers=headers, json=json_data)
    print(response.json())
    reqjson = response.json()
    print(reqjson['items'])
    for itm in reqjson['items']:
        sols.append(f"{itm['fileName']} - {itm['link']}")
    return sols



def save_dump(isbn, unit, solution):
        directory = f"./solutions/{isbn}"
        if not os.path.exists(directory):
            os.makedirs(directory)
        file_path = f"{directory}/{unit}.txt"
        with open(file_path, "a") as file:
            file.write(solution+"\n")
