user,account  are entities that define the schema of the database. they connect through foreigh keys. The user owns all the information of the users who they are and what id they posses. 

Transaction I think belongs to its own entity. Transaction has a foreign key account_id that references Account's id. Transaction has amounts. category it's also its own entity to be able to edit easily.

we take advantages of the keys. so transaction has a foreigh key referencing to account (id) that connects with the user.

Category also has its own table with a foreigh key referencing to the user (user_id)
transaction has also a foreigh key refeneing to the category_id

user entry should hold the following:
- name not null
- last name not null
- email not null and unique
- id not null primary key crated by supabase

password are created by the user and supabase stores not us

Account entry hols the following:
- account_id not null primary key not null unique uuid
- user_id foreign key references to user table not null uuid
- type enum either checking or saving,credit card not null
- balance (calcualted from transactions) this is not a column
- alias default checking-1 text unique for user

Category entry holds the following:
-category_id uuid not nutll primary key unique
- user_id foreign key uuid not null
- name text not null unique per user

Transaction entry holds the following:
- account_id not null not null uuid foreign key referencing account entry
- transaction_id not null uuid primary key
- description text optional
- amount decimal not null  money going out will be negative and coming in will be positive
- date date required
- category_id foreigh key referencing to category entry uuid, nullable, on delete set null 