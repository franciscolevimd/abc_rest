from fastapi import APIRouter, Response, status
from passlib.hash import sha256_crypt
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT
from ..config.db import conn
from ..schemas.user import user_entity, users_entity
from ..models.user import User

user = APIRouter()


@user.get('/users', response_model=list[User], tags=['users'])
def find_all_users():
	return users_entity(conn.abc_db.users.find())


@user.post('/users', response_model=User, tags=['users'])
def create_user(user:User):
	new_user = dict(user)
	new_user['password'] = sha256_crypt.encrypt(new_user['password'])
	del new_user['id']
	id = conn.abc_db.users.insert_one(new_user).inserted_id
	user = conn.abc_db.users.find_one({'_id': id})
	return user_entity(user)


@user.get('/users/{user_id}', response_model=User, tags=['users'])
def find_user(user_id:str):
	return user_entity(conn.abc_db.users.find_one({'_id': ObjectId(user_id)}))


@user.put('/users/{user_id}', response_model=User, tags=['users'])
def update_user(user_id:str, user: User):
	user = dict(user)
	user['password'] = sha256_crypt.encrypt(user['password'])
	conn.abc_db.users.find_one_and_update({'_id': ObjectId(user_id)}, {'$set': user})
	return user_entity(conn.abc_db.users.find_one({'_id': ObjectId(user_id)}))


@user.delete('/users/{user_id}', status_code=status.HTTP_204_NO_CONTENT, tags=['users'])
def delete_user(user_id:str):
	conn.abc_db.users.find_one_and_delete({'_id': ObjectId(user_id)})
	return Response(status_code=HTTP_204_NO_CONTENT)