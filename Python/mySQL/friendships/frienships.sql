INSERT INTO users (first_name, last_name)
VALUES ('Ana', 'Kola'),
('Ledina', 'Vojka'),
('Sonila', 'Mertiri'),
('Gersi', 'Tollja'),
('Klejsi', 'Decka'),
('Paola', 'Kanani');
SELECT * FROM users;
INSERT INTO friendships (user_id, friend_id)
VALUES
(1,2), (1,4), (1,6);
INSERT INTO friendships (user_id, friend_id)
VALUES
(2,1), (2,3), (2,5);
INSERT INTO friendships (user_id, friend_id)
VALUES
(3,2), (3,5);
INSERT INTO friendships (user_id, friend_id)
VALUES
(4,3);
INSERT INTO friendships (user_id, friend_id)
VALUES
(5,1), (5,6);
INSERT INTO friendships (user_id, friend_id)
VALUES
(6,2), (6,3);
-- display all the users and their friends
SELECT * FROM users 
JOIN friendships ON users.id = friendships.user_id
LEFT JOIN users as user2 ON friendships.friend_id = user2.id;
-- display the first three users and their friends
SELECT users.first_name, users.last_name, user2.first_name, user2.last_name
FROM users 
JOIN friendships ON users.id = friendships.user_id
LEFT JOIN users as user2 ON friendships.friend_id = user2.id 
WHERE users.id IN (1,2,3);
-- NINJA Query: Return all users who are friends with the first user, make sure their names are displayed in results.
SELECT users.id, users.first_name AS my_name, user2.first_name AS friend_name, user2.last_name AS friend_last_name
FROM users
JOIN friendships ON users.id = friendships.user_id
LEFT JOIN users as user2 ON friendships.friend_id = user2.id
WHERE users.id = 1;

-- NINJA Query: Return the count of all friendships
-- SELECT * FROM friendships;
SELECT COUNT(*) AS num_of_friendships
FROM friendships;
--  GROUP BY user_id;

-- NINJA Query: Find out who has the most friends and return the count of their friends.
SELECT users.first_name, user_id, COUNT(*) AS my_friends
FROM users
JOIN friendships ON users.id = friendships.user_id
LEFT JOIN users as user2 ON friendships.friend_id = user2.id
GROUP BY user_id
ORDER BY my_friends DESC
LIMIT 2;
-- NINJA Query: Return the friends of the third user in alphabetical order
SELECT users.id, users.first_name AS user_name, user2.first_name AS alphabetic_friend_names
FROM users
JOIN friendships ON users.id = friendships.user_id
LEFT JOIN users as user2 ON friendships.friend_id = user2.id
WHERE users.id = 3
ORDER BY user2.first_name;