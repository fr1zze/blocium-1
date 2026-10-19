# Blogicum

Учебный Django-проект с лентой публикаций, страницами публикаций,
категорий, описанием проекта и правилами сообщества.

Все команды выполняются из корня репозитория в PowerShell:

```powershell
python -m venv venv
.\venv\Scripts\python.exe -m pip install -r requirements.txt
.\venv\Scripts\python.exe blogicum/manage.py migrate
.\venv\Scripts\python.exe blogicum/manage.py runserver
```

Сайт доступен по адресу http://127.0.0.1:8000/.

Проверки проекта:
```powershell
.\venv\Scripts\python.exe -m pytest
.\venv\Scripts\python.exe blogicum/manage.py check
```

Приложения `blog` и `pages` находятся в `blogicum/`, настройки проекта —
в `blogicum/blogicum/`, общие шаблоны — в `blogicum/templates/`,
статика — в `blogicum/static/`. Каталог `html/` содержит исходную вёрстку;
Django использует шаблоны из `blogicum/templates/`.
