from bs4 import BeautifulSoup as bs
from requests import get
import json

url = "https://www.melon.com/genre/song_list.htm?gnrCode=GN0100&orderBy=POP"
url2 = "https://www.melon.com/commonlike/getSongLike.json?contsIds=600287375%2C33241003%2C600299706%2C38733032%2C38429074%2C32061975%2C1121123%2C4446485%2C600359330%2C38104031%2C37228861%2C38123338%2C34752757%2C30962526%2C36699489%2C37390939%2C601273260%2C38635449%2C37145732%2C34657844%2C37375706%2C34061322%2C33496587%2C600493407%2C30877002%2C39051429%2C39430660%2C36382580%2C34451383%2C39721328%2C37023625%2C38583620%2C600668850%2C37069064%2C600906246%2C34360855%2C600035196%2C4352438%2C34908740%2C600791038%2C35008524%2C39765727%2C601379618%2C33411344%2C600447153%2C39765728%2C31742666%2C33855085%2C418168%2C601358454"
head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36'}
# app2와 달리 리스트 불러오는게 비동기라서 head부분을 추가로 요구함. 로봇이 아님을 선언하는 부분

res = get(url, headers=head)
res2 = get(url2, headers=head)
# 406 코드 = 비동기라서 아직 못 가져옴 => head 추가하기
# 200 = 정상코드

titles = []
images = []
likes = []
albums = []
cnts = []
ids = []

if res.status_code == 200:
    data = bs(res.text)
    # print(data.title.text)
    title = data.title.text
    trs = data.select('#frm tbody > tr')
    # `'#frm tbody > tr'`: ID가 frm인 것 중에 tbody의 직계 자식인 모든 tr태그 찾아옴
    # print(len(trs))

if res2.status_code == 200:
    jData = json.loads(res2.text)
    # print(jData)
    for row in jData["contsLike"]:
        cnts.append({"CONTSID":row["CONTSID"], "SUMMCNT":row["SUMMCNT"]})

for i in range(len(trs)):
    titles.append(trs[i].select("td")[4].select_one("div[class='ellipsis rank01']").text.replace("\n","").replace("\xa0"," ").strip())
    # strip(): () => 좌우의 공백, \n, \t 제거해줌 (특정문자) => 좌우의 특정 문자 제거
    images.append(trs[i].select("td")[2].select_one("img")["src"].strip())
    albums.append(trs[i].select("td")[5].select_one("div[class='ellipsis rank03']").text.replace("\n","").replace("\xa0"," ").strip())
    ids.append(int(trs[i].select('td')[0].select_one("input[type='checkbox']").get("value")))
    
for id in ids:
    for row in cnts:
        if id == row["CONTSID"]:
            likes.append(row["SUMMCNT"])

            
# print("제목: ",titles)
for title, album, image, like in zip(titles, albums, images, likes):
    print("제목: ",{title})
    print("앨범: ",{album})
    print("앨범사진: ",{image})
    print("좋아요: ",{like})    
    print("-"*50)


# print("제목: ",titles)
# print("앨범: ",albums)
# print("앨범사진: ",images)
# print("좋아요: ",likes)
# print(arr[9])