# -*- coding: utf-8 -*-

from itemCatalog.models import Category, Item, User, Role


def populateDB(dbObject):

    role1 = Role(name = "admin", description = "The Admin role")
    role2 = Role(name = "user", description = "The Common User role")
    dbObject.session.add(role1)
    dbObject.session.add(role2)
    dbObject.session.commit()

    user1 = User("admin@admin.com", "pwadmin@admin.com")
    user1.roles.append(role1)
    
    user2 = User("u@u.com", "pwu@u.com")
    user2.roles.append(role2)

    dbObject.session.add(user1)
    dbObject.session.add(user2)
    dbObject.session.commit()


    cat1 = Category("Beach",
                   "Best places to surf, dive swim and get a natural tan.")
    cat2 = Category("Museum",
                   "Pieces of history and culture that will amaze you.")
    cat3 = Category("LandMark",
                   "Places you must see before die.")
    cat4 = Category("Amusement Parks",
                   "Description of Amusement Parks.")
    cat5 = Category("Island Resort",
                   "Description of Island Resort.")
    cat6 = Category("Zoo",
                   "Description of Zoo.")
    dbObject.session.add(cat1)
    dbObject.session.add(cat2)
    dbObject.session.add(cat3)
    dbObject.session.add(cat4)
    dbObject.session.add(cat5)
    dbObject.session.add(cat6)
    dbObject.session.commit()

    item = Item(name = "La Concha Beach",
                country = "Spain",
                image = u"La-Concha.jpg",
                description = """Lorem ipsum dolor sit amet, consectetur
                adipiscing elit. Nullam porta scelerisque neque, vitae
                efficitur felis elementum nec. Duis venenatis nibh id cursus
                eleifend. Vivamus enim nulla, aliquet viverra varius a,
                faucibus sed velit. Aenean convallis dui nunc, eleifend
                interdum nibh lobortis ut. Praesent finibus nisi in felis
                gravida rutrum quis ac enim. Donec aliquet nisi mi, tincidunt
                ornare purus imperdiet et. Duis ullamcorper iaculis viverra.
                Lorem ipsum dolor sit amet, consectetur adipiscing elit.
                Donec eu magna ut tortor ullamcorper mattis sit amet vitae
                justo. Orci varius natoque penatibus et magnis dis parturient
                montes, nascetur ridiculus mus. In elementum, sapien vitae
                dignissim semper, justo magna efficitur nisl, a finibus metus
                lectus eu erat. Vestibulum ornare ultrices mattis. Quisque a
                tellus nisi. Phasellus ipsum urna, ullamcorper quis lacus
                quis, ultrices consectetur tortor. Nulla facilisi. Sed mattis,
                lectus eu varius efficitur, leo turpis euismod quam, eu
                bibendum sapien tellus ut libero.
                Integer molestie, tellus sit amet elementum fringilla, enim
                ex varius mi, vitae venenatis felis velit vitae lectus. Mauris
                eu dictum turpis. Ut ornare neque neque, quis rhoncus odio
                interdum mollis. Curabitur fermentum fringilla ante ut mattis.
                Sed at diam in purus dapibus posuere. Sed blandit enim sit
                amet ex pellentesque, eu suscipit urna ultricies. Praesent
                eget lectus eget sapien suscipit commodo in eu mauris. Donec
                eget maximus tortor. Fusce neque orci, egestas eu interdum
                molestie, finibus finibus sapien. Phasellus porttitor
                malesuada nibh, ac tincidunt diam tempus et. Quisque
                consequat purus lobortis, mollis eros ac, rutrum ipsum.
                Praesent nulla sapien, gravida ut quam id, tristique maximus
                magna. Fusce efficitur justo non dolor consequat, feugiat
                aliquet arcu aliquam. Nunc ac pharetra mi. In hac habitasse
                platea dictumst. """)
    item.location = u"San Sebastián"
    item.category_id = cat1.id
    item.user = user2
    dbObject.session.add(item)
    dbObject.session.commit()
    

    item = Item(name = "Bondi Beach",
                country = "Australia",
                image = u"Bondi-beach.jpg",
                description = """Integer molestie, tellus sit amet
                elementum fringilla, enim ex varius mi, vitae venenatis felis
                velit vitae lectus. Mauris eu dictum turpis. Ut ornare neque
                neque, quis rhoncus odio interdum mollis. Curabitur fermentum
                fringilla ante ut mattis. Sed at diam in purus dapibus
                posuere. Sed blandit enim sit amet ex pellentesque, eu
                suscipit urna ultricies. Praesent eget lectus eget sapien
                suscipit commodo in eu mauris. Donec eget maximus tortor.
                Fusce neque orci, egestas eu interdum molestie, finibus
                finibus sapien. Phasellus porttitor malesuada nibh, ac
                tincidunt diam tempus et. Quisque consequat purus lobortis,
                mollis eros ac, rutrum ipsum. Praesent nulla sapien, gravida
                ut quam id, tristique maximus magna. Fusce efficitur justo
                non dolor consequat, feugiat aliquet arcu aliquam. Nunc ac
                pharetra mi. In hac habitasse platea dictumst.
                Proin lacinia porta lorem, eu hendrerit turpis varius ac.
                Proin eget dignissim ante. Mauris convallis lacinia leo,
                efficitur rutrum enim dictum nec. Nam cursus volutpat enim
                vitae vehicula. Donec vestibulum consequat cursus. In laoreet
                sit amet nulla sed tincidunt. Vestibulum accumsan mattis ante
                ut commodo. Curabitur sollicitudin, ante in auctor pulvinar,
                odio sapien lobortis libero, a varius est velit id risus.
                Curabitur sed tellus in odio aliquet porta ac quis lectus.
                Quisque est magna, consequat sit amet semper quis, tempus
                non metus.""")
    item.location = "Sydney, New South Wales"
    item.category_id = cat1.id
    item.user = user2
    dbObject.session.add(item)
    dbObject.session.commit()
    


    item = Item(name = "Playa del Amor",
                country = "Mexico",
                image = u"playa-del-mayor-hidden-beach.jpg",
                description = """Nam a mattis dolor, at dignissim ante. Duis
                efficitur nunc condimentum felis dignissim, in congue lacus
                blandit. Etiam consequat lacus vel venenatis volutpat. Etiam
                a orci quis felis laoreet imperdiet. Donec dignissim turpis
                lorem, in ultrices nisi dignissim eget. Etiam porttitor,
                mauris maximus fringilla tincidunt, diam nisi sollicitudin
                nunc, sed aliquam lacus lacus nec magna. Morbi molestie elit
                non lacus tristique, id accumsan eros tincidunt. Morbi
                maximus, enim eget porta sollicitudin, lectus neque auctor
                arcu, at varius dolor dui et dui. Nam sit amet dolor mollis,
                porttitor nibh a, tincidunt lorem. Phasellus ut arcu a neque
                viverra tempus eleifend vel enim. Ut et elit ornare, luctus
                nulla in, bibendum purus. Nunc ligula velit, consectetur nec
                lacus quis, porta aliquet sem. Vestibulum vel vulputate
                sapien. Nam luctus ex ut pulvinar lobortis.""")
    item.location = "Marietas Islands"
    item.category_id = cat1.id
    item.user = user2
    dbObject.session.add(item)
    dbObject.session.commit()


    item = Item(name = "Cathedrals Beach",
                country = "Spain",
                image = "Cathedrals Beach.jpg",
                description = """Integer molestie, tellus sit amet elementum
                fringilla, enim ex varius mi, vitae venenatis felis velit
                vitae lectus. Mauris eu dictum turpis. Ut ornare neque neque,
                quis rhoncus odio interdum mollis. Curabitur fermentum
                fringilla ante ut mattis. Sed at diam in purus dapibus
                posuere. Sed blandit enim sit amet ex pellentesque, eu
                suscipit urna ultricies. Praesent eget lectus eget sapien
                suscipit commodo in eu mauris. Donec eget maximus tortor.
                Fusce neque orci, egestas eu interdum molestie, finibus
                finibus sapien. Phasellus porttitor malesuada nibh, ac
                tincidunt diam tempus et. Quisque consequat purus lobortis,
                mollis eros ac, rutrum ipsum. Praesent nulla sapien, gravida
                ut quam id, tristique maximus magna. Fusce efficitur justo
                non dolor consequat, feugiat aliquet arcu aliquam. Nunc ac
                pharetra mi. In hac habitasse platea dictumst.
                Proin lacinia porta lorem, eu hendrerit turpis varius ac.
                Proin eget dignissim ante. Mauris convallis lacinia leo,
                efficitur rutrum enim dictum nec. Nam cursus volutpat enim
                vitae vehicula. Donec vestibulum consequat cursus. In laoreet
                sit amet nulla sed tincidunt. Vestibulum accumsan mattis
                ante ut commodo. Curabitur sollicitudin, ante in auctor
                pulvinar, odio sapien lobortis libero, a varius est velit
                id risus. Curabitur sed tellus in odio aliquet porta ac
                quis lectus. Quisque est magna, consequat sit amet semper
                quis, tempus non metus.""")
    item.location = "Ribadeo"
    item.category_id = cat1.id
    item.user = user2
    dbObject.session.add(item)
    dbObject.session.commit()


    item = Item(name = "Bowman's Beach",
                country = "United States",
                image = u"Bowman_s_Beach.jpg",
                description = """Lorem ipsum dolor sit amet, consectetur
                adipiscing elit. Nullam porta scelerisque neque, vitae
                efficitur felis elementum nec. Duis venenatis nibh id cursus
                eleifend. Vivamus enim nulla, aliquet viverra varius a,
                faucibus sed velit. Aenean convallis dui nunc, eleifend
                interdum nibh lobortis ut. Praesent finibus nisi in felis
                gravida rutrum quis ac enim. Donec aliquet nisi mi, tincidunt
                ornare purus imperdiet et. Duis ullamcorper iaculis viverra.
                Lorem ipsum dolor sit amet, consectetur adipiscing elit.
                Donec eu magna ut tortor ullamcorper mattis sit amet vitae
                justo. Orci varius natoque penatibus et magnis dis parturient
                montes, nascetur ridiculus mus. In elementum, sapien vitae
                dignissim semper, justo magna efficitur nisl, a finibus metus
                lectus eu erat. Vestibulum ornare ultrices mattis. Quisque a
                tellus nisi. Phasellus ipsum urna, ullamcorper quis lacus
                quis, ultrices consectetur tortor. Nulla facilisi. Sed
                mattis, lectus eu varius efficitur, leo turpis euismod
                quam, eu bibendum sapien tellus ut libero.""")
    item.location = "Sanibel Island, Florida"
    item.category_id = cat1.id
    item.user = user2
    dbObject.session.add(item)
    dbObject.session.commit()



    item = Item(name = u"The Mosque–Cathedral of Córdoba",
                country = "Spain",
                image = u"Mezquita_de_Córdoba_desde_el_aire.jpg",
                description = """Lorem ipsum dolor sit amet, consectetur
                adipiscing elit. Nullam porta scelerisque neque, vitae
                efficitur felis elementum nec. Duis venenatis nibh id cursus
                eleifend. Vivamus enim nulla, aliquet viverra varius a,
                faucibus sed velit. Aenean convallis dui nunc, eleifend
                interdum nibh lobortis ut. Praesent finibus nisi in felis
                gravida rutrum quis ac enim. Donec aliquet nisi mi, tincidunt
                ornare purus imperdiet et. Duis ullamcorper iaculis viverra.
                Lorem ipsum dolor sit amet, consectetur adipiscing elit.
                Donec eu magna ut tortor ullamcorper mattis sit amet vitae
                justo. Orci varius natoque penatibus et magnis dis parturient
                montes, nascetur ridiculus mus. In elementum, sapien vitae
                dignissim semper, justo magna efficitur nisl, a finibus metus
                lectus eu erat. Vestibulum ornare ultrices mattis. Quisque a
                tellus nisi. Phasellus ipsum urna, ullamcorper quis lacus
                quis, ultrices consectetur tortor. Nulla facilisi. Sed
                mattis, lectus eu varius efficitur, leo turpis euismod
                quam, eu bibendum sapien tellus ut libero.""")
    item.location = u"Córdoba"
    item.category = cat3
    item.user = user2
    dbObject.session.add(item)
    dbObject.session.commit()



    item = Item(name = "Basilica of the Sagrada Familia",
                country = "Spain",
                image = u"Sagrada_Familia.jpg",
                description = """Integer molestie, tellus sit amet elementum
                fringilla, enim ex varius mi, vitae venenatis felis velit
                vitae lectus. Mauris eu dictum turpis. Ut ornare neque neque,
                quis rhoncus odio interdum mollis. Curabitur fermentum
                fringilla ante ut mattis. Sed at diam in purus dapibus
                posuere. Sed blandit enim sit amet ex pellentesque, eu
                suscipit urna ultricies. Praesent eget lectus eget sapien
                suscipit commodo in eu mauris. Donec eget maximus tortor.
                Fusce neque orci, egestas eu interdum molestie, finibus
                finibus sapien. Phasellus porttitor malesuada nibh, ac
                tincidunt diam tempus et. Quisque consequat purus lobortis,
                mollis eros ac, rutrum ipsum. Praesent nulla sapien, gravida
                ut quam id, tristique maximus magna. Fusce efficitur justo
                non dolor consequat, feugiat aliquet arcu aliquam. Nunc ac
                pharetra mi. In hac habitasse platea dictumst.
                Proin lacinia porta lorem, eu hendrerit turpis varius ac.
                Proin eget dignissim ante. Mauris convallis lacinia leo,
                efficitur rutrum enim dictum nec. Nam cursus volutpat enim
                vitae vehicula. Donec vestibulum consequat cursus. In laoreet
                sit amet nulla sed tincidunt. Vestibulum accumsan mattis
                ante ut commodo. Curabitur sollicitudin, ante in auctor
                pulvinar, odio sapien lobortis libero, a varius est velit
                id risus. Curabitur sed tellus in odio aliquet porta ac
                quis lectus. Quisque est magna, consequat sit amet semper
                quis, tempus non metus.""")
    item.location = "Barcelona"
    item.category_id = cat3.id
    item.user = user2
    dbObject.session.add(item)
    dbObject.session.commit()



    item = Item(name = "The Acropolis of Athens",
                country = "Greece",
                image = u"View_of_the_Acropolis_Athens.jpg",
                description = """Nam a mattis dolor, at dignissim ante. Duis
                efficitur nunc condimentum felis dignissim, in congue lacus
                blandit. Etiam consequat lacus vel venenatis volutpat. Etiam
                a orci quis felis laoreet imperdiet. Donec dignissim turpis
                lorem, in ultrices nisi dignissim eget. Etiam porttitor,
                mauris maximus fringilla tincidunt, diam nisi sollicitudin
                nunc, sed aliquam lacus lacus nec magna. Morbi molestie elit
                non lacus tristique, id accumsan eros tincidunt. Morbi
                maximus, enim eget porta sollicitudin, lectus neque auctor
                arcu, at varius dolor dui et dui. Nam sit amet dolor mollis,
                porttitor nibh a, tincidunt lorem. Phasellus ut arcu a neque
                viverra tempus eleifend vel enim. Ut et elit ornare, luctus
                nulla in, bibendum purus. Nunc ligula velit, consectetur nec
                lacus quis, porta aliquet sem. Vestibulum vel vulputate
                sapien. Nam luctus ex ut pulvinar lobortis.""")
    item.location = "Athens"
    item.category_id = cat3.id
    item.user = user2
    dbObject.session.add(item)
    dbObject.session.commit()



    item = Item(name = "Alcatraz Island",
                country = "United States",
                image = u"Alcatraz_Island_photo_D_Ramey_Logan.jpg",
                description = """Lorem ipsum dolor sit amet, consectetur
                adipiscing elit. Nullam porta scelerisque neque, vitae
                efficitur felis elementum nec. Duis venenatis nibh id cursus
                eleifend. Vivamus enim nulla, aliquet viverra varius a,
                faucibus sed velit. Aenean convallis dui nunc, eleifend
                interdum nibh lobortis ut. Praesent finibus nisi in felis
                gravida rutrum quis ac enim. Donec aliquet nisi mi, tincidunt
                ornare purus imperdiet et. Duis ullamcorper iaculis viverra.
                Lorem ipsum dolor sit amet, consectetur adipiscing elit.
                Donec eu magna ut tortor ullamcorper mattis sit amet vitae
                justo. Orci varius natoque penatibus et magnis dis parturient
                montes, nascetur ridiculus mus. In elementum, sapien vitae
                dignissim semper, justo magna efficitur nisl, a finibus metus
                lectus eu erat. Vestibulum ornare ultrices mattis. Quisque a
                tellus nisi. Phasellus ipsum urna, ullamcorper quis lacus
                quis, ultrices consectetur tortor. Nulla facilisi. Sed mattis,
                lectus eu varius efficitur, leo turpis euismod quam, eu
                bibendum sapien tellus ut libero.
                Integer molestie, tellus sit amet elementum fringilla, enim
                ex varius mi, vitae venenatis felis velit vitae lectus. Mauris
                eu dictum turpis. Ut ornare neque neque, quis rhoncus odio
                interdum mollis. Curabitur fermentum fringilla ante ut mattis.
                Sed at diam in purus dapibus posuere. Sed blandit enim sit
                amet ex pellentesque, eu suscipit urna ultricies. Praesent
                eget lectus eget sapien suscipit commodo in eu mauris. Donec
                eget maximus tortor. Fusce neque orci, egestas eu interdum
                molestie, finibus finibus sapien. Phasellus porttitor
                malesuada nibh, ac tincidunt diam tempus et. Quisque
                consequat purus lobortis, mollis eros ac, rutrum ipsum.
                Praesent nulla sapien, gravida ut quam id, tristique maximus
                magna. Fusce efficitur justo non dolor consequat, feugiat
                aliquet arcu aliquam. Nunc ac pharetra mi. In hac habitasse
                platea dictumst. """)
    item.location = "San Francisco, California"
    item.category = cat3
    item.user = user2
    dbObject.session.add(item)
    dbObject.session.commit()


    item = Item(name = "Petra",
                country = "Jordan",
                image = u"Petra_Jordan.jpg",
                description = """Nam a mattis dolor, at dignissim ante. Duis
                efficitur nunc condimentum felis dignissim, in congue lacus
                blandit. Etiam consequat lacus vel venenatis volutpat. Etiam
                a orci quis felis laoreet imperdiet. Donec dignissim turpis
                lorem, in ultrices nisi dignissim eget. Etiam porttitor,
                mauris maximus fringilla tincidunt, diam nisi sollicitudin
                nunc, sed aliquam lacus lacus nec magna. Morbi molestie elit
                non lacus tristique, id accumsan eros tincidunt. Morbi
                maximus, enim eget porta sollicitudin, lectus neque auctor
                arcu, at varius dolor dui et dui. Nam sit amet dolor mollis,
                porttitor nibh a, tincidunt lorem. Phasellus ut arcu a neque
                viverra tempus eleifend vel enim. Ut et elit ornare, luctus
                nulla in, bibendum purus. Nunc ligula velit, consectetur nec
                lacus quis, porta aliquet sem. Vestibulum vel vulputate
                sapien. Nam luctus ex ut pulvinar lobortis.""")
    item.category_id = cat3.id
    item.user = user2
    dbObject.session.add(item)
    dbObject.session.commit()



    item = Item(name = "The Louvre",
                country = "France",
                image = u"Le_Louvre_-_Aile_Richelieu.jpg",
                description = """Integer molestie, tellus sit amet elementum
                fringilla, enim ex varius mi, vitae venenatis felis velit
                vitae lectus. Mauris eu dictum turpis. Ut ornare neque neque,
                quis rhoncus odio interdum mollis. Curabitur fermentum
                fringilla ante ut mattis. Sed at diam in purus dapibus
                posuere. Sed blandit enim sit amet ex pellentesque, eu
                suscipit urna ultricies. Praesent eget lectus eget sapien
                suscipit commodo in eu mauris. Donec eget maximus tortor.
                Fusce neque orci, egestas eu interdum molestie, finibus
                finibus sapien. Phasellus porttitor malesuada nibh, ac
                tincidunt diam tempus et. Quisque consequat purus lobortis,
                mollis eros ac, rutrum ipsum. Praesent nulla sapien, gravida
                ut quam id, tristique maximus magna. Fusce efficitur justo
                non dolor consequat, feugiat aliquet arcu aliquam. Nunc ac
                pharetra mi. In hac habitasse platea dictumst.
                Proin lacinia porta lorem, eu hendrerit turpis varius ac.
                Proin eget dignissim ante. Mauris convallis lacinia leo,
                efficitur rutrum enim dictum nec. Nam cursus volutpat enim
                vitae vehicula. Donec vestibulum consequat cursus. In laoreet
                sit amet nulla sed tincidunt. Vestibulum accumsan mattis
                ante ut commodo. Curabitur sollicitudin, ante in auctor
                pulvinar, odio sapien lobortis libero, a varius est velit
                id risus. Curabitur sed tellus in odio aliquet porta ac
                quis lectus. Quisque est magna, consequat sit amet semper
                quis, tempus non metus.""")
    item.location = "Paris"
    item.category_id = cat2.id
    item.user = user2
    dbObject.session.add(item)
    dbObject.session.commit()



    item = Item(name = "The American Museum of Natural History",
                country = "United States",
                image = u"USA-NYC-American_Museum_of_Natural_History.jpg",
                description = """Nam a mattis dolor, at dignissim ante. Duis
                efficitur nunc condimentum felis dignissim, in congue lacus
                blandit. Etiam consequat lacus vel venenatis volutpat. Etiam
                a orci quis felis laoreet imperdiet. Donec dignissim turpis
                lorem, in ultrices nisi dignissim eget. Etiam porttitor,
                mauris maximus fringilla tincidunt, diam nisi sollicitudin
                nunc, sed aliquam lacus lacus nec magna. Morbi molestie elit
                non lacus tristique, id accumsan eros tincidunt. Morbi
                maximus, enim eget porta sollicitudin, lectus neque auctor
                arcu, at varius dolor dui et dui. Nam sit amet dolor mollis,
                porttitor nibh a, tincidunt lorem. Phasellus ut arcu a neque
                viverra tempus eleifend vel enim. Ut et elit ornare, luctus
                nulla in, bibendum purus. Nunc ligula velit, consectetur nec
                lacus quis, porta aliquet sem. Vestibulum vel vulputate
                sapien. Nam luctus ex ut pulvinar lobortis.""")
    item.location = "New York"
    item.category_id = cat2.id
    item.user = user2
    dbObject.session.add(item)
    dbObject.session.commit()



    item = Item(name = "Museum of Modern Art",
                country = "United States",
                image = u"MoMa_NY_USA.jpg",
                description = """Integer molestie, tellus sit amet
                elementum fringilla, enim ex varius mi, vitae venenatis felis
                velit vitae lectus. Mauris eu dictum turpis. Ut ornare neque
                neque, quis rhoncus odio interdum mollis. Curabitur fermentum
                fringilla ante ut mattis. Sed at diam in purus dapibus
                posuere. Sed blandit enim sit amet ex pellentesque, eu
                suscipit urna ultricies. Praesent eget lectus eget sapien
                suscipit commodo in eu mauris. Donec eget maximus tortor.
                Fusce neque orci, egestas eu interdum molestie, finibus
                finibus sapien. Phasellus porttitor malesuada nibh, ac
                tincidunt diam tempus et. Quisque consequat purus lobortis,
                mollis eros ac, rutrum ipsum. Praesent nulla sapien, gravida
                ut quam id, tristique maximus magna. Fusce efficitur justo
                non dolor consequat, feugiat aliquet arcu aliquam. Nunc ac
                pharetra mi. In hac habitasse platea dictumst.
                Proin lacinia porta lorem, eu hendrerit turpis varius ac.
                Proin eget dignissim ante. Mauris convallis lacinia leo,
                efficitur rutrum enim dictum nec. Nam cursus volutpat enim
                vitae vehicula. Donec vestibulum consequat cursus. In laoreet
                sit amet nulla sed tincidunt. Vestibulum accumsan mattis ante
                ut commodo. Curabitur sollicitudin, ante in auctor pulvinar,
                odio sapien lobortis libero, a varius est velit id risus.
                Curabitur sed tellus in odio aliquet porta ac quis lectus.
                Quisque est magna, consequat sit amet semper quis, tempus
                non metus.""")
    item.location = "New York"
    item.category_id = cat2.id
    item.user = user2
    dbObject.session.add(item)
    dbObject.session.commit()



    item = Item(name = "Egyptian Museum or Museum of Cairo",
                country = "Egypt",
                image = u"The_Egyptian_Museum.jpg",
                description = """Nam a mattis dolor, at dignissim ante. Duis
                efficitur nunc condimentum felis dignissim, in congue lacus
                blandit. Etiam consequat lacus vel venenatis volutpat. Etiam
                a orci quis felis laoreet imperdiet. Donec dignissim turpis
                lorem, in ultrices nisi dignissim eget. Etiam porttitor,
                mauris maximus fringilla tincidunt, diam nisi sollicitudin
                nunc, sed aliquam lacus lacus nec magna. Morbi molestie elit
                non lacus tristique, id accumsan eros tincidunt. Morbi
                maximus, enim eget porta sollicitudin, lectus neque auctor
                arcu, at varius dolor dui et dui. Nam sit amet dolor mollis,
                porttitor nibh a, tincidunt lorem. Phasellus ut arcu a neque
                viverra tempus eleifend vel enim. Ut et elit ornare, luctus
                nulla in, bibendum purus. Nunc ligula velit, consectetur nec
                lacus quis, porta aliquet sem. Vestibulum vel vulputate
                sapien. Nam luctus ex ut pulvinar lobortis.""")
    item.location = "Cairo"
    item.category_id = cat2.id
    item.user = user2
    dbObject.session.add(item)
    dbObject.session.commit()

    

    item = Item(name = "Tate Modern",
                country = "UK",
                image = u"Tate_Modern_viewed_from_Thames.jpg",
                description = """Integer molestie, tellus sit amet
                elementum fringilla, enim ex varius mi, vitae venenatis felis
                velit vitae lectus. Mauris eu dictum turpis. Ut ornare neque
                neque, quis rhoncus odio interdum mollis. Curabitur fermentum
                fringilla ante ut mattis. Sed at diam in purus dapibus
                posuere. Sed blandit enim sit amet ex pellentesque, eu
                suscipit urna ultricies. Praesent eget lectus eget sapien
                suscipit commodo in eu mauris. Donec eget maximus tortor.
                Fusce neque orci, egestas eu interdum molestie, finibus
                finibus sapien. Phasellus porttitor malesuada nibh, ac
                tincidunt diam tempus et. Quisque consequat purus lobortis,
                mollis eros ac, rutrum ipsum. Praesent nulla sapien, gravida
                ut quam id, tristique maximus magna. Fusce efficitur justo
                non dolor consequat, feugiat aliquet arcu aliquam. Nunc ac
                pharetra mi. In hac habitasse platea dictumst.
                Proin lacinia porta lorem, eu hendrerit turpis varius ac.
                Proin eget dignissim ante. Mauris convallis lacinia leo,
                efficitur rutrum enim dictum nec. Nam cursus volutpat enim
                vitae vehicula. Donec vestibulum consequat cursus. In laoreet
                sit amet nulla sed tincidunt. Vestibulum accumsan mattis ante
                ut commodo. Curabitur sollicitudin, ante in auctor pulvinar,
                odio sapien lobortis libero, a varius est velit id risus.
                Curabitur sed tellus in odio aliquet porta ac quis lectus.
                Quisque est magna, consequat sit amet semper quis, tempus
                non metus.""")
    item.location = "London"
    item.category_id = cat2.id
    item.user = user2
    dbObject.session.add(item)
    dbObject.session.commit()



    item = Item(name = "The National Zoological Gardens of South Africa",
                country = "South Africa",
                image = "The National Zoological Gardens of South Africa.jpg",
                description = """Lorem ipsum dolor sit amet, consectetur
                adipiscing elit. Nullam porta scelerisque neque, vitae
                efficitur felis elementum nec. Duis venenatis nibh id cursus
                eleifend. Vivamus enim nulla, aliquet viverra varius a,
                faucibus sed velit. Aenean convallis dui nunc, eleifend
                interdum nibh lobortis ut. Praesent finibus nisi in felis
                gravida rutrum quis ac enim. Donec aliquet nisi mi, tincidunt
                ornare purus imperdiet et. Duis ullamcorper iaculis viverra.
                Lorem ipsum dolor sit amet, consectetur adipiscing elit.
                Donec eu magna ut tortor ullamcorper mattis sit amet vitae
                justo. Orci varius natoque penatibus et magnis dis parturient
                montes, nascetur ridiculus mus. In elementum, sapien vitae
                dignissim semper, justo magna efficitur nisl, a finibus metus
                lectus eu erat. Vestibulum ornare ultrices mattis. Quisque a
                tellus nisi. Phasellus ipsum urna, ullamcorper quis lacus
                quis, ultrices consectetur tortor. Nulla facilisi. Sed mattis,
                lectus eu varius efficitur, leo turpis euismod quam, eu
                bibendum sapien tellus ut libero.
                Integer molestie, tellus sit amet elementum fringilla, enim
                ex varius mi, vitae venenatis felis velit vitae lectus. Mauris
                eu dictum turpis. Ut ornare neque neque, quis rhoncus odio
                interdum mollis. Curabitur fermentum fringilla ante ut mattis.
                Sed at diam in purus dapibus posuere. Sed blandit enim sit
                amet ex pellentesque, eu suscipit urna ultricies. Praesent
                eget lectus eget sapien suscipit commodo in eu mauris. Donec
                eget maximus tortor. Fusce neque orci, egestas eu interdum
                molestie, finibus finibus sapien. Phasellus porttitor
                malesuada nibh, ac tincidunt diam tempus et. Quisque
                consequat purus lobortis, mollis eros ac, rutrum ipsum.
                Praesent nulla sapien, gravida ut quam id, tristique maximus
                magna. Fusce efficitur justo non dolor consequat, feugiat
                aliquet arcu aliquam. Nunc ac pharetra mi. In hac habitasse
                platea dictumst. """)
    item.location = "Pretoria"
    item.category_id = cat6.id
    item.user = user2
    dbObject.session.add(item)
    dbObject.session.commit()
