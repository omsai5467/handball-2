import requests
import json
x = requests.get('http://handballindia.org/jsom')

j = json.loads(x.text)
i = json.loads(j["data"])
def loadall():
    x = open("total.csv","w")
    for k in i:
        # print(k["fields"]["firstname"])
        x.write(f"{k['pk']}*{k['fields']['playerid']}*{k['fields']['firstname']}*{k['fields']['lastname']}*{k['fields']['fathername']}*{k['fields']['address']}*{k['fields']['city']}*{k['fields']['phonenumber']}*{k['fields']['Email']}*{k['fields']['gender']}*{k['fields']['age']}*{k['fields']['dist']}*{k['fields']['city']}*{k['fields']['state']}*{k['fields']['photo']}*{k['fields']['adhar']}*{k['fields']['birth']}*{k['fields']['playerid']}\n")

x = open("photos.html","w")
for k in i:
    t = f"""
            <img src = "https://omsai.s3.amazonaws.com/{k['fields']['photo']}" width= '500px' height= '500px'/>

    """
    x.write(t)
x = open("total.json","w")
x.write(f"{i}")
if __name__ == '__main__':
    loadall()
