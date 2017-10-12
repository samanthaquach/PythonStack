select * from users
left join friendships 
on users.idusers = friendships.users_id
left join users as users2
ON friendships.friend_id = users2.idusers

