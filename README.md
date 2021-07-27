#TODO APP CREATED WITH DJANGO REST FRAMEWORK

# ENDPOINTS:
 api/register - Регистрация пользователя через электронную почту, пароль, имя и фамилию_
 api/this_ip_users/ - Список пользователей которые зарегестрировались под текущим IP_
 api/token - Получить токен для авторизации (через почту и пароль) использувалась библиотека drf_simple_jwt_
 
todo/ todo-list/ [name='todo-list'] - Список туду карточек текущего пользователя_
todo/ todo-done/ [name='todo-list'] - Список выполненых карточек_
todo/ todo-detail/<str:pk>/ [name='todo-detail'] - 1 карточка, достаеться по id_
todo/ todo-create/ [name='todo-create'] - Создать карточку_
todo/ todo-update/<str:pk>/ [name='todo-update'] - Обновить карточку (поставить ее в статус выполнено)_
todo/ todo-delete/<str:pk>/ [name='todo-delete'] - Удалить карточку_
