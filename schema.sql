DROP TABLE IF EXISTS menu;
DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS user_selection;

CREATE TABLE menu (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    item_name TEXT NOT NULL,
    image_url TEXT NOT NULL
);

CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    phone INTEGER NOT NULL UNIQUE
);


CREATE TABLE user_selection (
    user_id INTEGER NOT NULL UNIQUE,
    menu_id  INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES user (id),
    FOREIGN KEY (menu_id) REFERENCES menu (id),
    primary key (user_id, menu_id)
);