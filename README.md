  ORM Backend Project (SQLAlchemy + SQLite) 

Описание :

  backend-система реализованную с использованием SQLAlchemy ORM и базы данных SQLite 
  Проект демонстрирует работу с основными типами связей в базе данных и CRUD-операции 

Используемые технологии :
	~ Python 3.14.3 
	~ SQLAlchemy ORM 
	~ SQLite 

Таблицы :
	User 
		~ id 
		~ username 
		~ email 
	Profile 
		~ id 
		~ full_name 
		~ bio 
		~ user_id 
	Course 
		~ id 
		~ title 
		~ description 
	Lesson 
		~ id 
		~ title 
		~ content 
		~ course_id 
	student_course 
		~ user_id 
		~ course_id 

Типы связей : 
	1:1 (One-to-One) 
	User - Profile 
	1:N (One-to-Many) 
	Course - Lessons 
	N:N (Many-to-Many) 
	User - Course 

Функциональность :
	CRUD операции :
		~ Create : создание пользователей и курсов 
		~ Read : получение данных по ID и полям 
		~ Update : обновление пользователя 
		~ Delete : удаление пользователя 
	Запросы :
		~ поиск пользователя по ID 
		~ поиск по username / title 
		~ получение связанных данных (курсы пользователя , уроки курса) 
		~ фильтрация через связи 
		~ JOIN-запросы 

Запуск проекта :

pip install sqlalchemy / pip install -r requirements.txt 
python main.py 
