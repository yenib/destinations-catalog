
CREATE TABLE "user" (
	id SERIAL, 
	name VARCHAR(120), 
	last_name VARCHAR(120), 
	email VARCHAR(120) NOT NULL, 
	password VARCHAR(255) NOT NULL, 
	picture VARCHAR(255), 
	active BOOLEAN DEFAULT FALSE, 
	PRIMARY KEY (id), 
	UNIQUE (email)
);


CREATE TABLE role (
	id SERIAL, 
	name VARCHAR(80), 
	description VARCHAR(255), 
	PRIMARY KEY (id), 
	UNIQUE (name)
);


CREATE TABLE role_users (
	user_id INTEGER NOT NULL, 
	role_id INTEGER NOT NULL, 
	PRIMARY KEY (user_id, role_id), 
	FOREIGN KEY(user_id) REFERENCES "user" (id), 
	FOREIGN KEY(role_id) REFERENCES role (id)
);


CREATE TABLE category (
	id SERIAL, 
	name VARCHAR(80) NOT NULL, 
	description TEXT, 
	PRIMARY KEY (id), 
	UNIQUE (name)
);


CREATE TABLE item (
	id SERIAL, 
	name VARCHAR(120), 
	description TEXT, 
	image VARCHAR(255), 
	image_alt VARCHAR(150), 
	country VARCHAR(80) NOT NULL, 
	location VARCHAR(150), 
	category_id INTEGER NOT NULL, 
	user_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(category_id) REFERENCES category (id), 
	FOREIGN KEY(user_id) REFERENCES "user" (id)
);


-- Database Initial Data

INSERT INTO role (name, description) VALUES ('admin', 'The Admin role');
INSERT INTO "user" (email, password) VALUES ('admin@admin.com', 'pwadmin@admin.com');
INSERT INTO role_users (user_id, role_id) VALUES ((SELECT max(id) FROM "user"), (SELECT max(id) FROM role));

INSERT INTO role (name, description) VALUES ('user', 'The Common User role');
INSERT INTO "user" (email, password) VALUES ('u@u.com', 'pwu@u.com');
INSERT INTO role_users (user_id, role_id) VALUES ((SELECT max(id) FROM "user"), (SELECT max(id) FROM role));


INSERT INTO category (name, description) VALUES
    ('Beach', 'Best places to surf, dive swim and get a natural tan.'),
    ('Museum', 'Pieces of history and culture that will amaze you.'),
    ('LandMark', 'Places you must see before die.'),
    ('Amusement Parks', 'Description of Amusement Parks.'),
    ('Island Resort', 'Description of Island Resort.'),
    ('Zoo', 'Description of Zoo.');



INSERT INTO item (name, country, image, description, location, category_id, user_id) VALUES
    ('La Concha Beach', 'Spain', 'La-Concha.jpg', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam porta scelerisque neque, vitae efficitur felis elementum nec. Duis venenatis nibh id cursus eleifend. Vivamus enim nulla, aliquet viverra varius a, faucibus sed velit. Aenean convallis dui nunc, eleifend interdum nibh lobortis ut. Praesent finibus nisi in felis gravida rutrum quis ac enim. Donec aliquet nisi mi, tincidunt ornare purus imperdiet et. Duis ullamcorper iaculis viverra.
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec eu magna ut tortor ullamcorper mattis sit amet vitae justo. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. In elementum, sapien vitae dignissim semper, justo magna efficitur nisl, a finibus metus lectus eu erat. Vestibulum ornare ultrices mattis. Quisque a tellus nisi. Phasellus ipsum urna, ullamcorper quis lacus quis, ultrices consectetur tortor. Nulla facilisi. Sed mattis, lectus eu varius efficitur, leo turpis euismod quam, eu bibendum sapien tellus ut libero.
Integer molestie, tellus sit amet elementum fringilla, enim ex varius mi, vitae venenatis felis velit vitae lectus. Mauris eu dictum turpis. Ut ornare neque neque, quis rhoncus odio interdum mollis. Curabitur fermentum fringilla ante ut mattis. Sed at diam in purus dapibus posuere. Sed blandit enim sit amet ex pellentesque, eu suscipit urna ultricies. Praesent eget lectus eget sapien suscipit commodo in eu mauris. Donec eget maximus tortor. Fusce neque orci, egestas eu interdum molestie, finibus finibus sapien. Phasellus porttitor malesuada nibh, ac tincidunt diam tempus et. Quisque consequat purus lobortis, mollis eros ac, rutrum ipsum. Praesent nulla sapien, gravida ut quam id, tristique maximus magna. Fusce efficitur justo non dolor consequat, feugiat aliquet arcu aliquam. Nunc ac pharetra mi. In hac habitasse platea dictumst.', 'San Sebastián', (SELECT id FROM category WHERE name='Beach'), (SELECT id FROM "user" WHERE email='u@u.com')),

    ('Bondi Beach', 'Australia', 'Bondi-beach.jpg', 'Integer molestie, tellus sit amet elementum fringilla, enim ex varius mi, vitae venenatis felis velit vitae lectus. Mauris eu dictum turpis. Ut ornare neque neque, quis rhoncus odio interdum mollis. Curabitur fermentum fringilla ante ut mattis. Sed at diam in purus dapibus  posuere. Sed blandit enim sit amet ex pellentesque, eu suscipit urna ultricies. Praesent eget lectus eget sapien suscipit commodo in eu mauris. Donec eget maximus tortor.
Fusce neque orci, egestas eu interdum molestie, finibus finibus sapien. Phasellus porttitor malesuada nibh, ac tincidunt diam tempus et. Quisque consequat purus lobortis, mollis eros ac, rutrum ipsum. Praesent nulla sapien, gravida ut quam id, tristique maximus magna. Fusce efficitur justo non dolor consequat, feugiat aliquet arcu aliquam. Nunc ac pharetra mi. In hac habitasse platea dictumst. Proin lacinia porta lorem, eu hendrerit turpis varius ac. Proin eget dignissim ante. Mauris convallis lacinia leo, efficitur rutrum enim dictum nec. Nam cursus volutpat enim vitae vehicula. Donec vestibulum consequat cursus. In laoreet sit amet nulla sed tincidunt. Vestibulum accumsan mattis ante ut commodo. Curabitur sollicitudin, ante in auctor pulvinar, odio sapien lobortis libero, a varius est velit id risus. Curabitur sed tellus in odio aliquet porta ac quis lectus. Quisque est magna, consequat sit amet semper quis, tempus non metus.', 'Sydney, New South Wales', (SELECT id FROM category WHERE name='Beach'), (SELECT id FROM "user" WHERE email='u@u.com')),
        
    ('Playa del Amor', 'Mexico', 'playa-del-mayor-hidden-beach.jpg', 'Nam a mattis dolor, at dignissim ante. Duis efficitur nunc condimentum felis dignissim, in congue lacus blandit. Etiam consequat lacus vel venenatis volutpat. Etiam a orci quis felis laoreet imperdiet. Donec dignissim turpis lorem, in ultrices nisi dignissim eget. Etiam porttitor, mauris maximus fringilla tincidunt, diam nisi sollicitudin nunc, sed aliquam lacus lacus nec magna. Morbi molestie elit non lacus tristique, id accumsan eros tincidunt. Morbi maximus, enim eget porta sollicitudin, lectus neque auctor arcu, at varius dolor dui et dui. Nam sit amet dolor mollis,  porttitor nibh a, tincidunt lorem. Phasellus ut arcu a neque viverra tempus eleifend vel enim. Ut et elit ornare, luctus nulla in, bibendum purus. Nunc ligula velit, consectetur nec lacus quis, porta aliquet sem. Vestibulum vel vulputate sapien. Nam luctus ex ut pulvinar lobortis.', 'Marietas Islands', (SELECT id FROM category WHERE name='Beach'), (SELECT id FROM "user" WHERE email='u@u.com')),

    ('Cathedrals Beach', 'Spain', 'Cathedrals Beach.jpg', 'Integer molestie, tellus sit amet elementum fringilla, enim ex varius mi, vitae venenatis felis velit vitae lectus. Mauris eu dictum turpis. Ut ornare neque neque, quis rhoncus odio interdum mollis. Curabitur fermentum fringilla ante ut mattis. Sed at diam in purus dapibus  posuere. Sed blandit enim sit amet ex pellentesque, eu suscipit urna ultricies. Praesent eget lectus eget sapien suscipit commodo in eu mauris. Donec eget maximus tortor.
Fusce neque orci, egestas eu interdum molestie, finibus finibus sapien. Phasellus porttitor malesuada nibh, ac tincidunt diam tempus et. Quisque consequat purus lobortis, mollis eros ac, rutrum ipsum. Praesent nulla sapien, gravida ut quam id, tristique maximus magna. Fusce efficitur justo non dolor consequat, feugiat aliquet arcu aliquam. Nunc ac pharetra mi. In hac habitasse platea dictumst. Proin lacinia porta lorem, eu hendrerit turpis varius ac. Proin eget dignissim ante. Mauris convallis lacinia leo, efficitur rutrum enim dictum nec. Nam cursus volutpat enim vitae vehicula. Donec vestibulum consequat cursus. In laoreet sit amet nulla sed tincidunt. Vestibulum accumsan mattis ante ut commodo. Curabitur sollicitudin, ante in auctor pulvinar, odio sapien lobortis libero, a varius est velit id risus. Curabitur sed tellus in odio aliquet porta ac quis lectus. Quisque est magna, consequat sit amet semper quis, tempus non metus.', 'Ribadeo', (SELECT id FROM category WHERE name='Beach'), (SELECT id FROM "user" WHERE email='u@u.com')),

    ('Bowman''s Beach', 'United States', 'Bowman_s_Beach.jpg', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam porta scelerisque neque, vitae efficitur felis elementum nec. Duis venenatis nibh id cursus eleifend. Vivamus enim nulla, aliquet viverra varius a, faucibus sed velit. Aenean convallis dui nunc, eleifend interdum nibh lobortis ut. Praesent finibus nisi in felis gravida rutrum quis ac enim. Donec aliquet nisi mi, tincidunt ornare purus imperdiet et. Duis ullamcorper iaculis viverra.
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec eu magna ut tortor ullamcorper mattis sit amet vitae justo. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. In elementum, sapien vitae dignissim semper, justo magna efficitur nisl, a finibus metus lectus eu erat. Vestibulum ornare ultrices mattis. Quisque a tellus nisi. Phasellus ipsum urna, ullamcorper quis lacus quis, ultrices consectetur tortor. Nulla facilisi. Sed mattis, lectus eu varius efficitur, leo turpis euismod quam, eu bibendum sapien tellus ut libero.', 'Sanibel Island, Florida', (SELECT id FROM category WHERE name='Beach'), (SELECT id FROM "user" WHERE email='u@u.com')),

   ('The Mosque–Cathedral of Córdoba', 'Spain', 'Mezquita_de_Córdoba_desde_el_aire.jpg', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam porta scelerisque neque, vitae efficitur felis elementum nec. Duis venenatis nibh id cursus eleifend. Vivamus enim nulla, aliquet viverra varius a, faucibus sed velit. Aenean convallis dui nunc, eleifend interdum nibh lobortis ut. Praesent finibus nisi in felis gravida rutrum quis ac enim. Donec aliquet nisi mi, tincidunt ornare purus imperdiet et. Duis ullamcorper iaculis viverra.
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec eu magna ut tortor ullamcorper mattis sit amet vitae justo. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. In elementum, sapien vitae dignissim semper, justo magna efficitur nisl, a finibus metus lectus eu erat. Vestibulum ornare ultrices mattis. Quisque a tellus nisi. Phasellus ipsum urna, ullamcorper quis lacus quis, ultrices consectetur tortor. Nulla facilisi. Sed mattis, lectus eu varius efficitur, leo turpis euismod quam, eu bibendum sapien tellus ut libero.', 'Córdoba', (SELECT id FROM category WHERE name='LandMark'), (SELECT id FROM "user" WHERE email='u@u.com')),

    ('Basilica of the Sagrada Familia', 'Spain', 'Sagrada_Familia.jpg', 'Integer molestie, tellus sit amet elementum fringilla, enim ex varius mi, vitae venenatis felis velit vitae lectus. Mauris eu dictum turpis. Ut ornare neque neque, quis rhoncus odio interdum mollis. Curabitur fermentum fringilla ante ut mattis. Sed at diam in purus dapibus  posuere. Sed blandit enim sit amet ex pellentesque, eu suscipit urna ultricies. Praesent eget lectus eget sapien suscipit commodo in eu mauris. Donec eget maximus tortor.
Fusce neque orci, egestas eu interdum molestie, finibus finibus sapien. Phasellus porttitor malesuada nibh, ac tincidunt diam tempus et. Quisque consequat purus lobortis, mollis eros ac, rutrum ipsum. Praesent nulla sapien, gravida ut quam id, tristique maximus magna. Fusce efficitur justo non dolor consequat, feugiat aliquet arcu aliquam. Nunc ac pharetra mi. In hac habitasse platea dictumst. Proin lacinia porta lorem, eu hendrerit turpis varius ac. Proin eget dignissim ante. Mauris convallis lacinia leo, efficitur rutrum enim dictum nec. Nam cursus volutpat enim vitae vehicula. Donec vestibulum consequat cursus. In laoreet sit amet nulla sed tincidunt. Vestibulum accumsan mattis ante ut commodo. Curabitur sollicitudin, ante in auctor pulvinar, odio sapien lobortis libero, a varius est velit id risus. Curabitur sed tellus in odio aliquet porta ac quis lectus. Quisque est magna, consequat sit amet semper quis, tempus non metus.', 'Barcelona', (SELECT id FROM category WHERE name='LandMark'), (SELECT id FROM "user" WHERE email='u@u.com')),
    
    ('The Acropolis of Athens', 'Greece', 'View_of_the_Acropolis_Athens.jpg', 'Nam a mattis dolor, at dignissim ante. Duis efficitur nunc condimentum felis dignissim, in congue lacus blandit. Etiam consequat lacus vel venenatis volutpat. Etiam a orci quis felis laoreet imperdiet. Donec dignissim turpis lorem, in ultrices nisi dignissim eget. Etiam porttitor, mauris maximus fringilla tincidunt, diam nisi sollicitudin nunc, sed aliquam lacus lacus nec magna. Morbi molestie elit non lacus tristique, id accumsan eros tincidunt. 
Morbi maximus, enim eget porta sollicitudin, lectus neque auctor arcu, at varius dolor dui et dui. Nam sit amet dolor mollis, porttitor nibh a, tincidunt lorem. Phasellus ut arcu a neque viverra tempus eleifend vel enim. Ut et elit ornare, luctus nulla in, bibendum purus. Nunc ligula velit, consectetur nec lacus quis, porta aliquet sem. Vestibulum vel vulputate sapien. Nam luctus ex ut pulvinar lobortis.', 'Athens', (SELECT id FROM category WHERE name='LandMark'), (SELECT id FROM "user" WHERE email='u@u.com')),

    ('Alcatraz Island', 'United States', 'Alcatraz_Island_photo_D_Ramey_Logan.jpg', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam porta scelerisque neque, vitae efficitur felis elementum nec. Duis venenatis nibh id cursus eleifend. Vivamus enim nulla, aliquet viverra varius a, faucibus sed velit. Aenean convallis dui nunc, eleifend interdum nibh lobortis ut. Praesent finibus nisi in felis gravida rutrum quis ac enim. Donec aliquet nisi mi, tincidunt ornare purus imperdiet et. Duis ullamcorper iaculis viverra.
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec eu magna ut tortor ullamcorper mattis sit amet vitae justo. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. In elementum, sapien vitae dignissim semper, justo magna efficitur nisl, a finibus metus lectus eu erat. Vestibulum ornare ultrices mattis. Quisque a tellus nisi. Phasellus ipsum urna, ullamcorper quis lacus quis, ultrices consectetur tortor. Nulla facilisi. Sed mattis, lectus eu varius efficitur, leo turpis euismod quam, eu bibendum sapien tellus ut libero.', 'San Francisco, California', (SELECT id FROM category WHERE name='LandMark'), (SELECT id FROM "user" WHERE email='u@u.com')),

    ('Petra', 'Jordan', 'Petra_Jordan.jpg', 'Nam a mattis dolor, at dignissim ante. Duis efficitur nunc condimentum felis dignissim, in congue lacus blandit. Etiam consequat lacus vel venenatis volutpat. Etiam a orci quis felis laoreet imperdiet. Donec dignissim turpis lorem, in ultrices nisi dignissim eget. Etiam porttitor,  mauris maximus fringilla tincidunt, diam nisi sollicitudin nunc, sed aliquam lacus lacus nec magna. 
Morbi molestie elit non lacus tristique, id accumsan eros tincidunt. Morbi maximus, enim eget porta sollicitudin, lectus neque auctor arcu, at varius dolor dui et dui. Nam sit amet dolor mollis, porttitor nibh a, tincidunt lorem. Phasellus ut arcu a neque viverra tempus eleifend vel enim. Ut et elit ornare, luctus nulla in, bibendum purus. Nunc ligula velit, consectetur nec lacus quis, porta aliquet sem. Vestibulum vel vulputate sapien. Nam luctus ex ut pulvinar lobortis.', '', (SELECT id FROM category WHERE name='LandMark'), (SELECT id FROM "user" WHERE email='u@u.com')),

    ('The Louvre', 'France', 'Le_Louvre_-_Aile_Richelieu.jpg', 'Integer molestie, tellus sit amet elementum fringilla, enim ex varius mi, vitae venenatis felis velit vitae lectus. Mauris eu dictum turpis. Ut ornare neque neque, quis rhoncus odio interdum mollis. Curabitur fermentum fringilla ante ut mattis. Sed at diam in purus dapibus  posuere. Sed blandit enim sit amet ex pellentesque, eu suscipit urna ultricies. Praesent eget lectus eget sapien suscipit commodo in eu mauris. Donec eget maximus tortor.
Fusce neque orci, egestas eu interdum molestie, finibus finibus sapien. Phasellus porttitor malesuada nibh, ac tincidunt diam tempus et. Quisque consequat purus lobortis, mollis eros ac, rutrum ipsum. Praesent nulla sapien, gravida ut quam id, tristique maximus magna. Fusce efficitur justo non dolor consequat, feugiat aliquet arcu aliquam. Nunc ac pharetra mi. In hac habitasse platea dictumst. Proin lacinia porta lorem, eu hendrerit turpis varius ac. Proin eget dignissim ante. Mauris convallis lacinia leo, efficitur rutrum enim dictum nec. Nam cursus volutpat enim vitae vehicula. Donec vestibulum consequat cursus. In laoreet sit amet nulla sed tincidunt. Vestibulum accumsan mattis ante ut commodo. Curabitur sollicitudin, ante in auctor pulvinar, odio sapien lobortis libero, a varius est velit id risus. Curabitur sed tellus in odio aliquet porta ac quis lectus. Quisque est magna, consequat sit amet semper quis, tempus non metus.', 'Paris', (SELECT id FROM category WHERE name='Museum'), (SELECT id FROM "user" WHERE email='u@u.com')),

    ('The American Museum of Natural History', 'United States', 'USA-NYC-American_Museum_of_Natural_History.jpg', 'Nam a mattis dolor, at dignissim ante. Duis efficitur nunc condimentum felis dignissim, in congue lacus blandit. Etiam consequat lacus vel venenatis volutpat. Etiam a orci quis felis laoreet imperdiet. Donec dignissim turpis lorem, in ultrices nisi dignissim eget. Etiam porttitor,  mauris maximus fringilla tincidunt, diam nisi sollicitudin nunc, sed aliquam lacus lacus nec magna. 
Morbi molestie elit non lacus tristique, id accumsan eros tincidunt. Morbi maximus, enim eget porta sollicitudin, lectus neque auctor arcu, at varius dolor dui et dui. Nam sit amet dolor mollis, porttitor nibh a, tincidunt lorem. Phasellus ut arcu a neque viverra tempus eleifend vel enim. Ut et elit ornare, luctus nulla in, bibendum purus. Nunc ligula velit, consectetur nec lacus quis, porta aliquet sem. Vestibulum vel vulputate sapien. Nam luctus ex ut pulvinar lobortis.', 'New York', (SELECT id FROM category WHERE name='Museum'), (SELECT id FROM "user" WHERE email='u@u.com')),
    
    ('Museum of Modern Art', 'United States', 'MoMa_NY_USA.jpg', 'Integer molestie, tellus sit amet elementum fringilla, enim ex varius mi, vitae venenatis felis velit vitae lectus. Mauris eu dictum turpis. Ut ornare neque neque, quis rhoncus odio interdum mollis. Curabitur fermentum fringilla ante ut mattis. Sed at diam in purus dapibus  posuere. Sed blandit enim sit amet ex pellentesque, eu suscipit urna ultricies. Praesent eget lectus eget sapien suscipit commodo in eu mauris. Donec eget maximus tortor.
Fusce neque orci, egestas eu interdum molestie, finibus finibus sapien. Phasellus porttitor malesuada nibh, ac tincidunt diam tempus et. Quisque consequat purus lobortis, mollis eros ac, rutrum ipsum. Praesent nulla sapien, gravida ut quam id, tristique maximus magna. Fusce efficitur justo non dolor consequat, feugiat aliquet arcu aliquam. Nunc ac pharetra mi. In hac habitasse platea dictumst. Proin lacinia porta lorem, eu hendrerit turpis varius ac. Proin eget dignissim ante. Mauris convallis lacinia leo, efficitur rutrum enim dictum nec. Nam cursus volutpat enim vitae vehicula. Donec vestibulum consequat cursus. In laoreet sit amet nulla sed tincidunt. Vestibulum accumsan mattis ante ut commodo. Curabitur sollicitudin, ante in auctor pulvinar, odio sapien lobortis libero, a varius est velit id risus. Curabitur sed tellus in odio aliquet porta ac quis lectus. Quisque est magna, consequat sit amet semper quis, tempus non metus.', 'New York', (SELECT id FROM category WHERE name='Museum'), (SELECT id FROM "user" WHERE email='u@u.com')),

    ('Egyptian Museum or Museum of Cairo', 'Egypt', 'The_Egyptian_Museum.jpg', 'Nam a mattis dolor, at dignissim ante. Duis efficitur nunc condimentum felis dignissim, in congue lacus blandit. Etiam consequat lacus vel venenatis volutpat. Etiam a orci quis felis laoreet imperdiet. Donec dignissim turpis lorem, in ultrices nisi dignissim eget. Etiam porttitor,  mauris maximus fringilla tincidunt, diam nisi sollicitudin nunc, sed aliquam lacus lacus nec magna. 
Morbi molestie elit non lacus tristique, id accumsan eros tincidunt. Morbi maximus, enim eget porta sollicitudin, lectus neque auctor arcu, at varius dolor dui et dui. Nam sit amet dolor mollis, porttitor nibh a, tincidunt lorem. Phasellus ut arcu a neque viverra tempus eleifend vel enim. Ut et elit ornare, luctus nulla in, bibendum purus. Nunc ligula velit, consectetur nec lacus quis, porta aliquet sem. Vestibulum vel vulputate sapien. Nam luctus ex ut pulvinar lobortis.', 'Cairo', (SELECT id FROM category WHERE name='Museum'), (SELECT id FROM "user" WHERE email='u@u.com')), 
 
    ('Tate Modern', 'UK', 'Tate_Modern_viewed_from_Thames.jpg', 'Integer molestie, tellus sit amet elementum fringilla, enim ex varius mi, vitae venenatis felis velit vitae lectus. Mauris eu dictum turpis. Ut ornare neque neque, quis rhoncus odio interdum mollis. Curabitur fermentum fringilla ante ut mattis. Sed at diam in purus dapibus  posuere. Sed blandit enim sit amet ex pellentesque, eu suscipit urna ultricies. Praesent eget lectus eget sapien suscipit commodo in eu mauris. Donec eget maximus tortor.
Fusce neque orci, egestas eu interdum molestie, finibus finibus sapien. Phasellus porttitor malesuada nibh, ac tincidunt diam tempus et. Quisque consequat purus lobortis, mollis eros ac, rutrum ipsum. Praesent nulla sapien, gravida ut quam id, tristique maximus magna. Fusce efficitur justo non dolor consequat, feugiat aliquet arcu aliquam. Nunc ac pharetra mi. In hac habitasse platea dictumst. Proin lacinia porta lorem, eu hendrerit turpis varius ac. Proin eget dignissim ante. Mauris convallis lacinia leo, efficitur rutrum enim dictum nec. Nam cursus volutpat enim vitae vehicula. Donec vestibulum consequat cursus. In laoreet sit amet nulla sed tincidunt. Vestibulum accumsan mattis ante ut commodo. Curabitur sollicitudin, ante in auctor pulvinar, odio sapien lobortis libero, a varius est velit id risus. Curabitur sed tellus in odio aliquet porta ac quis lectus. Quisque est magna, consequat sit amet semper quis, tempus non metus.', 'London', (SELECT id FROM category WHERE name='Museum'), (SELECT id FROM "user" WHERE email='u@u.com')),

    ('The National Zoological Gardens of South Africa', 'South Africa', 'The National Zoological Gardens of South Africa.jpg', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam porta scelerisque neque, vitae efficitur felis elementum nec. Duis venenatis nibh id cursus eleifend. Vivamus enim nulla, aliquet viverra varius a, faucibus sed velit. Aenean convallis dui nunc, eleifend interdum nibh lobortis ut. Praesent finibus nisi in felis gravida rutrum quis ac enim. Donec aliquet nisi mi, tincidunt ornare purus imperdiet et. Duis ullamcorper iaculis viverra.
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec eu magna ut tortor ullamcorper mattis sit amet vitae justo. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. In elementum, sapien vitae dignissim semper, justo magna efficitur nisl, a finibus metus lectus eu erat. Vestibulum ornare ultrices mattis. Quisque a tellus nisi. Phasellus ipsum urna, ullamcorper quis lacus quis, ultrices consectetur tortor. Nulla facilisi. Sed mattis, lectus eu varius efficitur, leo turpis euismod quam, eu bibendum sapien tellus ut libero.
Integer molestie, tellus sit amet elementum fringilla, enim ex varius mi, vitae venenatis felis velit vitae lectus. Mauris eu dictum turpis. Ut ornare neque neque, quis rhoncus odio interdum mollis. Curabitur fermentum fringilla ante ut mattis. Sed at diam in purus dapibus posuere. Sed blandit enim sit amet ex pellentesque, eu suscipit urna ultricies. Praesent eget lectus eget sapien suscipit commodo in eu mauris. Donec eget maximus tortor. Fusce neque orci, egestas eu interdum molestie, finibus finibus sapien. Phasellus porttitor malesuada nibh, ac tincidunt diam tempus et. Quisque consequat purus lobortis, mollis eros ac, rutrum ipsum. Praesent nulla sapien, gravida ut quam id, tristique maximus magna. Fusce efficitur justo non dolor consequat, feugiat aliquet arcu aliquam. Nunc ac pharetra mi. In hac habitasse platea dictumst.', 'Pretoria', (SELECT id FROM category WHERE name='Zoo'), (SELECT id FROM "user" WHERE email='u@u.com'));




