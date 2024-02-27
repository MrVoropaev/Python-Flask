from fastapi import FastAPI, Request
import logging
from typing import Optional
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

FORMAT = '{levelname:<8} - {asctime} - >>> {msg}'
logging.basicConfig(format=FORMAT, style='{', level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()
templates = Jinja2Templates(directory="HW5/templates")

class Task(BaseModel):
    title: str
    description: Optional[str] = None
    status: Optional[bool] = False

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    logger.info('Отработал GET запрос(Главная страница).')
    return templates.TemplateResponse("item.html", {"request": request})

@app.get('/tasks/', response_model=list[Task])
async def all_tasks():
    logger.info('Отработал GET запрос(прочитал БД и вывел все задачи).')
    return [{'title': 'Задача 1', 'description': 'Описание задачи 1', 'status': True},
            {'title': 'Задача 2', 'description': 'Описание задачи 2', 'status': False}]


@app.get('/tasks/{id_}', response_model=Task)
async def returns_task(id_: int):
    logger.info(f'Отработал GET запрос(вернул задачу с id = {id_}).')
    return {'title': f'Задача {id_}', 'description': f'Описание задачи {id_}', 'status': False}


@app.post("/tasks/", response_model=Task)
async def create_task(task: Task):
    logger.info('Отработал POST запрос(добавил новую задачу).')
    return task


@app.put("/tasks/{task_id}", response_model=Task)
async def update_task(task_id: int, task: Task):
    logger.info(f'Отработал PUT запрос(обновил задачу с id = {task_id}).')
    return task


@app.delete('/tasks/{task_id}')
async def delete_item(task_id: int):
    logger.info(f'Отработал DELETE запрос (удалил задачу с id = {task_id}).')
    return {'DELETE_task_id': task_id}


@app.exception_handler(Exception)
async def error_handler(request: Request, exc: Exception):
    logger.error(f'Произошла ошибка: {exc}')
    return templates.TemplateResponse("error.html", {"request": request, "error_message": str(exc)})