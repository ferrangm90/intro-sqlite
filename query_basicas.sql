SELECT * FROM persona;

SELECT name,lastname,email FROM persona;
INSERT INTO persona(name,lastname,dni,email)  VALUES  ("Albert"," Rueda","77123098S","alberto@gmail.com");
UPDATE persona SET name="Ana", lastname="Gomez", dni="44323432P", email="ama@gmail.com" WHERE id=3;

SELECT * FROM persona WHERE name LIKE  "Ma%";

SELECT * FROM persona ORDER BY "id";

DELETE from persona where id="2";

