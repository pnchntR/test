from fastapi import FastAPI

app =FastAPI()

@app.get('/verify')
def function(id:str='0000000000000'):
    
    verify = 'T'

    return {'verify':verify}

