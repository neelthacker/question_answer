# question_answer

# question_answer
This project is used to add, update question and user can write the answer for the particular questions and search the particular questions by referance of the tags or user name with the help of apis

API for authentication token
Method:- POST
url:- http://{ip-address}/api/auth_token/
Body:- 
	key:- username, password

Authentication:-
	Type:- API Key:-
		Key:- Authorization
		Value:- Token {received authentication token}

API for create question
url:- http://{ip-address}/api/create_questions/
Method:- POST
Authentication:- describe above
Body:-
	Key:-title, body, tags

API to get questions based on tags
URL:- http://{ip-address}/api/create_questions/
Method:- GET
Authentication:- describe above
Params:-
	Key:-tag

API to update question
url:- http://127.0.0.1:8000/api/create_questions/
Method:- PUT
Authentication:- describe above
Body:-
	Key:-question_id, title, body, tags

API to add answer for a particular question
url:- http://127.0.0.1:8000/api/answer_questions/{question id}/
Method:- POST
Authentication:- describe above
Body:-
	Key:-answer

API to get all questions with there answers
url:- http://127.0.0.1:8000/api/questions_and_answers/
Method:- GET
Authentication:- describe above

API to get questions based on particular user
url:- http://127.0.0.1:8000/api/create_questions/
Method:- GET
Authentication:- describe above
Params:-
	Key:-user
	value:- user id

API to update status of the answer by default is true and write value in true or false
url:- http://127.0.0.1:8000/api/answer_questions/{question id}/
Method:- PUT
Authentication:- describe above
Body:-
	Key:-status, answer_id
