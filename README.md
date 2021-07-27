#TODO APP CREATED WITH DJANGO REST FRAMEWORK

# ENDPOINTS:
 api/register - Регистрация пользователя через электронную почту, пароль, имя и фамилию
 api/this_ip_users/ - Список пользователей которые зарегестрировались под текущим IP
 api/token - Получить токен для авторизации (через почту и пароль) использувалась библиотека drf_simple_jwt
 
todo/ todo-list/ [name='todo-list'] - Список туду карточек текущего пользователя
todo/ todo-done/ [name='todo-list'] - Список выполненых карточек
todo/ todo-detail/<str:pk>/ [name='todo-detail'] - 1 карточка, достаеться по id
todo/ todo-create/ [name='todo-create'] - Создать карточку
todo/ todo-update/<str:pk>/ [name='todo-update'] - Обновить карточку (поставить ее в статус выполнено)
todo/ todo-delete/<str:pk>/ [name='todo-delete'] - Удалить карточку
