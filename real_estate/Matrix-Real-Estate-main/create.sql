-- Active: 1674189764067@@127.0.0.1@3306@matrix_real_estate
create database matrix_real_estate;

Create table agents (agent_id int auto_increment, name varchar(50) NOT NULL, phone_number numeric(10,0) NOT NULL, mail_id varchar(50) NOT NULL, unique_id numeric(12,0) NOT NULL, username varchar(50) NOT NULL, password varchar(50) NOT NULL, operating_area varchar(50) NOT NULL, primary key(agent_id), unique key(phone_number),unique key(mail_id),unique key(unique_id ),unique key(operating_area), unique key(username));

Create table sellers (seller_uid numeric(12,0), name varchar(50) NOT NULL, phone_number numeric(10,0) NOT NULL, mail_id varchar(50) NOT NULL,  primary key(seller_uid ), unique key(phone_number),unique key(mail_id));

Create table buyers (buyer_uid numeric(12,0), name varchar(50) NOT NULL, phone_number numeric(10,0) NOT NULL, mail_id varchar(50) NOT NULL,  primary key(buyer_uid ), unique key(phone_number),unique key(mail_id));

Create table rent_cost (amount_per_month int, primary key(amount_per_month));

Create table sale_cost (selling_price bigint, primary key(selling_price));

Create table property (house_number varchar(10), Street varchar(50) NOT NULL, City varchar(50) NOT NULL, Locality  varchar(50) NOT NULL, Pincode numeric(6,0) ,  Area int NOT NULL,Bedrooms int NOT NULL, year_of_construction numeric(4,0) NOT NULL,  primary key(house_number, Pincode));

Create table buyer_assigned (agent_id int NOT NULL, buyer_uid numeric(12,0), primary key(buyer_uid),FOREIGN KEY(agent_id) REFERENCES agents(agent_id) on delete cascade, FOREIGN KEY(buyer_uid) REFERENCES buyers(buyer_uid) on delete cascade);

Create table seller_assigned (agent_id int , seller_uid numeric(12,0), Number_of_properties int DEFAULT 0, primary key(seller_uid,agent_id), FOREIGN KEY(agent_id) REFERENCES agents(agent_id) on delete cascade, FOREIGN KEY(seller_uid) REFERENCES sellers(seller_uid) on delete cascade);

Create table availability (house_number varchar(10),  Pincode numeric(6,0), Sale varchar(3)  NOT NULL, Rent varchar(3)  NOT NULL, amount_per_month int, selling_price bigint, date_since_available date NOT NULL, primary key(house_number, Pincode),FOREIGN KEY(house_number, Pincode) REFERENCES property(house_number, Pincode) on delete cascade);

Create table owns (seller_uid numeric(12,0), house_number varchar(10),  Pincode numeric(6,0), primary key(house_number, Pincode), FOREIGN KEY(house_number, Pincode) REFERENCES property(house_number, Pincode) on delete cascade, FOREIGN KEY(seller_uid) REFERENCES sellers(seller_uid) on delete cascade);

Create table Real_Estate_Transactions (agent_id int , buyer_uid numeric(12,0) , seller_uid numeric(12,0) , house_number varchar(10),  Pincode numeric(6,0), price int NOT NULL, type varchar(4) NOT NULL, time_on_market int NOT NULL, transaction_date date, primary key(house_number, Pincode, transaction_date), FOREIGN KEY(house_number, Pincode) REFERENCES property(house_number, Pincode) on delete cascade, FOREIGN KEY(seller_uid) REFERENCES sellers(seller_uid) on delete cascade, FOREIGN KEY(agent_id) REFERENCES agents(agent_id) on delete cascade, FOREIGN KEY(buyer_uid) REFERENCES buyers(buyer_uid) on delete cascade);