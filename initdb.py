import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()


cur.execute("INSERT INTO menu (id, item_name, image_url) VALUES (?, ?, ?)",
            (1, 'Biriyani', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ2kEC9i98kt_qqUEOyI6X_dj0LG1XkvL5kCQ&usqp=CAU')            
            )
            
cur.execute("INSERT INTO menu (id, item_name, image_url) VALUES (?, ?, ?)",
            (2, 'Chapati', 'https://images.unsplash.com/photo-1576846806147-8065a16f89b0?ixlib=rb-1.2.1&ixid=MXwxMjA3fDB8MHxzZWFyY2h8MXx8Y2hhcGF0aXxlbnwwfHwwfA%3D%3D&auto=format&fit=crop&w=900&q=60')                        
            )


cur.execute("INSERT INTO menu (id, item_name, image_url) VALUES (?, ?, ?)",
            (3, 'Rise', 'https://img.traveltriangle.com/blog/wp-content/tr:w-700,h-400/uploads/2017/10/Ela-Sadya.jpg')                        
            )            

cur.execute("INSERT INTO menu (id, item_name, image_url) VALUES (?, ?, ?)",
            (4, 'Porotta', 'https://i.redd.it/u9hfn7nn5c751.jpg')                        
            )



connection.commit()
connection.close()