#TODO APP CREATED WITH DJANGO REST FRAMEWORK

# ENDPOINTS:
 api/register - Регистрация пользователя через электронную почту, пароль, имя и фамилию <br />
 api/this_ip_users/ - Список пользователей которые зарегестрировались под текущим IP <br />
 api/token - Получить токен для авторизации (через почту и пароль) использувалась библиотека drf_simple_jwt <br />
 
todo/ todo-list/ [name='todo-list'] - Список туду карточек текущего пользователя <br />
todo/ todo-done/ [name='todo-list'] - Список выполненых карточек <br />
todo/ todo-detail/<str:pk>/ [name='todo-detail'] - 1 карточка, достаеться по id <br />
todo/ todo-create/ [name='todo-create'] - Создать карточку <br />
todo/ todo-update/<str:pk>/ [name='todo-update'] - Обновить карточку (поставить ее в статус выполнено) <br />
todo/ todo-delete/<str:pk>/ [name='todo-delete'] - Удалить карточку <br />
