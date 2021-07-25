//db = db.getSiblingDB('admin')
// move to the admin db - always created in Mongo.
db.auth('root', 'root1234')
// log as root admin if you decided to authenticate in your docker-compose file.
db = db.getSiblingDB('abc_db');
// create and move to your new database
db.createUser({
	user: 'abcUser',
	pwd: 'R4na123K',
	roles: [
	{
      role: 'dbOwner',
      db: 'abc_db',
    },
  ],
});
// user created
db.createCollection('users');
// add new collection
