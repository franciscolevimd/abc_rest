from fastapi import APIRouter


user = APIRouter()


@user.get('/users')
def find_all_users():
	return 'find_all_users'


@user.post('/users')
def create_user():
	return 'create_user'


@user.get('/users/{user_id}')
def find_user():
	return 'find_user'


@user.put('/users/{user_id}')
def update_user():
	return 'update_user'


@user.delete('/users/{user_id}')
def delete_user():
	return 'delete_user'