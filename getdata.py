import requests

try:
    newapidata= []
    url = "https://api.worldbank.org/v2/country/ARG;BOL;BRA;CHL;COL;ECU;GUY;PRY;PER;SUR;URY;VEN/indicator/NY.GDP.MKTP.CD?format=json&page=1&per_page=50"
    response = requests.get(url)
    if(response.status_code==200):
        data = response.json()
        print(data[0]["pages"])
        pages=data[0]["pages"]
        for i in range(1, pages+1):
            url =f"https://api.worldbank.org/v2/country/ARG;BOL;BRA;CHL;COL;ECU;GUY;PRY;PER;SUR;URY;VEN/indicator/NY.GDP.MKTP.CD?format=json&page={i}&per_page=50"
            response = requests.get(url)
            if(response.status_code==200):
                data = response.json()
                newapidata.extend(data[1])
                #print(newapidata)

    else:
        print("Data fetching failed",response.status_code)
except Exception as e:
    print("Exception occurred",e)

else:
    print("Data fetched successfully")

