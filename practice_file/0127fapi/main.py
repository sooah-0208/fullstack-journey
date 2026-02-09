from fastapi import FastAPI, Form  #Form 방식 쓰려면 import해와야함
from fastapi.responses import HTMLResponse

app = FastAPI()

arr = []

@app.get('/') #쿼리스트링 방식
def get_root(id: str="", pwd: str=""):
    return {'status':True, 'id': id, 'pwd': pwd}

@app.post('/') #path variable방식, 여러 form이 있을 때 매번 post함수를 만들어주기 번거로우니 var를 변수로 받아옴
def post_root(
    var: str,           #Path variable은 기본값 있으면 안 됨, {var}통해 받아와야함
    id: str = Form(''), #Form방식, 현재 html에서 form을 사용하고 있기때문에 Form방식 필요
    pwd: str = Form(''),
):
    return {'status':True, 'id': id, 'pwd': pwd, 'var': var}


@app.get('/v', response_class=HTMLResponse)
def view():
    return'''
<body>
    <form action="/" method='get'>
        <input type='text' name='id'/>
        <input type='password' name='pwd'/>
        <button type='submit'>요청</button>
    </form>
    <form action="/" method='post'>
        <input type='text' name='id'/>
        <input type='password' name='pwd'/>
        <button type='submit'>요청</button>
    </form>
</body>
'''

@app.get('/a', response_class=HTMLResponse)
def view():
    return '''
<body>
    <a href ='/http://127.0.0.1:8000/4'>돌아가기</a>
</body>
'''