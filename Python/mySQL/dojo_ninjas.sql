SELECT * FROM dojos;
INSERT INTO dojos (name) VALUES ('Endi'), ('Joana'), ('Endri');
SELECT * FROM dojos;
DELETE FROM dojos WHERE id IN (1,2,3,4,5,6);
SELECT * FROM dojos;
DELETE FROM dojos WHERE id IN (7,8,9);
SELECT * FROM dojos;
INSERT INTO dojos (name) VALUES ('Endi'), ('Joana'), ('Endri');
SELECT * FROM dojos;
INSERT INTO ninjas (first_name, last_name, age, dojo_id)
 VALUES ('Ninja1','Lastname1',21, 10),
 ('Ninja2','Lastname2',23, 10),
 ('Ninja3','Lastname3',25, 10);
 SELECT * FROM ninjas;
 INSERT INTO ninjas (first_name, last_name, age, dojo_id)
 VALUES ('Ninja4','Lastname4',21, 11),
 ('Ninja5','Lastname5',23, 11),
 ('Ninja6','Lastname6',25, 11);
 INSERT INTO ninjas (first_name, last_name, age, dojo_id)
 VALUES ('Ninja7','Lastname7',27, 12),
 ('Ninja8','Lastname8',23, 12),
 ('Ninja9','Lastname9',25, 12);
SELECT * FROM ninjas;
SELECT first_name, last_name
FROM ninjas
JOIN dojos ON ninjas.dojo_id = dojos.id
WHERE dojos.id= 10;
SELECT first_name, last_name
FROM ninjas
JOIN dojos ON ninjas.dojo_id = dojos.id
WHERE dojos.id= 12;
SELECT name 
FROM dojos
JOIN ninjas ON dojos.id= ninjas.dojo_id
ORDER BY ninjas.id DESC
LIMIT 1;
SELECT ninjas.id, ninjas.first_name, ninjas.last_name, dojos.id, dojos.name
FROM ninjas
JOIN dojos ON ninjas.dojo_id = dojos.id
WHERE ninjas.id = 6;
SELECT ninjas.*, dojos.*
FROM ninjas
JOIN dojos ON ninjas.dojo_id= dojos.id;