Insert into dojos (id, name, created_at, updated_at)
VALUES
(2, 'San Jose', NOW(), NOW()),
(3, 'Burbank', NOW(), NOW()),
(4, 'OC', NOW(), NOW()),
(5, 'Dallas', NOW(), NOW()),
(6, 'Boise', NOW(), NOW()),
(7, 'Chicago', NOW(), NOW()),
(8, 'DC', NOW(), NOW());

INSERT INTO ninjas (id, first_name, last_name, age, created_at, updated_at, dojos_id)
Values (1, 'Todd', 'Enders', 26, NOW(), NOW(), 1),
(2, 'Speros', 'Misirlakis', 28, NOW(), NOW(), 1),
(3, 'Donovan', 'An', 27, NOW(), NOW(), 1),
(4, 'Phil', 'Krull', 31, NOW(), NOW(), 1);
