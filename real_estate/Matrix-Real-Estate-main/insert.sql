-- Active: 1674189764067@@127.0.0.1@3306@matrix_real_estate

Delete from agents;
delete from buyers;
delete from sellers;
delete from property;
delete from rent_cost;
delete from sale_cost;
ALTER TABLE agents auto_increment=0;
INSERT INTO agents (name, phone_number, mail_id, unique_id, username, password, operating_area) VALUES
('Amit Sharma', 9087654321, 'amit.sharma@gmail.com', 123456782312, 'amit.sharma', 'Password1', 'Park Street, Kolkata'),
('Riya Chakraborty', 9898765432, 'riya.c@gmail.com', 234567890123, 'riya.chakraborty', 'Chakraborty1', 'Gariahat, Kolkata'),
('Rakesh Singh', 8976543210, 'rakesh.singh@gmail.com', 345678901234, 'rakesh.singh', 'Singh1234', 'Malviya Nagar, Delhi'),
('Priya Singh', 9876543590, 'priya.singh@gmail.com', 456789012345, 'priya.singh', 'Singh9876', 'Lajpat Nagar, Delhi'),
('Rajeev Sharma', 8765432109, 'rajeev.sharma@gmail.com', 567890123456, 'rajeev.sharma', 'Sharma@123', 'Kamla Nagar, Delhi'),
('Anjali Mishra', 7654321098, 'anjali.mishra@gmail.com', 678901234567, 'anjali.mishra', 'Mishra_123', 'Paltan Bazar, Guwahati'),
('Vikram Das', 6543210987, 'vikram.das@gmail.com', 789012345678, 'vikram.das', 'DasVikram1', 'Dispur, Guwahati'),
('Shubham Singh', 5432109876, 'shubham.singh@gmail.com', 890123456789, 'shubham.singh', 'S1nghS', 'Jadavpur, Kolkata'),
('Sneha Chatterjee', 4321098765, 'sneha.c@gmail.com', 901234567890, 'sneha.chatterjee', 'Ch@tterjee', 'Tollygunge, Kolkata'),
('Rohan Sen', 3210987654, 'rohan.sen@gmail.com', 123456789012, 'rohan.sen', 'sen_rohan1', 'Ballygunge, Kolkata'),
('Avik Ghosh', 2109876543, 'avik.ghosh@gmail.com', 234567734123, 'avik.ghosh', 'Ghosh_Avik1', 'Sundarpur, Guwahati'),
('Aarav Kumar', 1098765432, 'aarav.kumar@gmail.com', 345683101234, 'aarav.kumar', 'kum@rAarav', 'Rajarhat, Kolkata'),
('Rahul Singh', 9876541210, 'rahul.singh@gmail.com', 883789012345, 'rahul.singh', 'singh_rahul1', 'Anna Nagar, Chennai'),
('Sanjana Gupta', 8115432109, 'sanjana.gupta@gmail.com', 641890123456, 'sanjana.gupta', 'Gupta@sanjana', 'South Delhi, Delhi');

INSERT INTO buyers (buyer_uid, name, phone_number, mail_id)
VALUES
(101234567890, 'Rajesh Kumar', 8989898989, 'rajesh.kumar@example.com'),
(102345678901, 'Vikram Singh', 8899889988, 'vikram.singh@example.com'),
(103456789012, 'Anjali Patel', 9876543210, 'anjali.patel@example.com'),
(104567890123, 'Rahul Sharma', 9123456789, 'rahul.sharma@example.com'),
(105678901234, 'Riya Gupta', 9898989898, 'riya.gupta@example.com'),
(106789012345, 'Prashant Singh', 9988776655, 'prashant.singh@example.com'),
(107890123456, 'Deepak Kumar', 9123123123, 'deepak.kumar@example.com'),
(108901234567, 'Amita Sharma', 9888888888, 'amita.sharma@example.com'),
(109012345678, 'Sanjay Gupta', 9777777777, 'sanjay.gupta@example.com'),
(111223344556, 'Neha Patel', 8999899989, 'neha.patel@example.com'),
(112334455667, 'Rahul Sharma', 8999999999, 'rahul.sharma2@example.com'),
(113445566778, 'Gaurav Singh', 8888888888, 'gaurav.singh@example.com'),
(114556677889, 'Vidya Patel', 8989898988, 'vidya.patel@example.com'),
(115667788990, 'Ankit Gupta', 8998989898, 'ankit.gupta@example.com'),
(116778899001, 'Priya Singh', 8999898989, 'priya.singh2@example.com'),
(117889900112, 'Rohit Kumar', 8888999999, 'rohit.kumar@example.com'),
(118990011223, 'Kavita Gupta', 8998989899, 'kavita.gupta@example.com'),
(119001122334, 'Rohit Patel', 9888888988, 'rohit.patel@example.com'),
(120112233445, 'Shweta Sharma', 9888999999, 'shweta.sharma@example.com'),
(121234567890, 'Rajat Singh', 8999899999, 'rajat.singh@example.com'),
(122345678901, 'Neetu Gupta', 8989898987, 'neetu.gupta@example.com'),
(123456789012, 'Suresh Kumar', 9888888887, 'suresh.kumar@example.com'),
(124567890123, 'Jaya Patel', 9876543211, 'jaya.patel@example.com'),
(125678901234, 'Praveen Singh', 9898989899, 'praveen.singh@example.com'),
(126789012345, 'Neha Gupta', 9123456788, 'neha.gupta2@example.com');

INSERT INTO sellers (seller_uid, name, phone_number, mail_id)
VALUES
(912345678901, 'Ankit Sharma', 9123456789, 'ankit.sharma@example.com'),
(923456789012, 'Rahul Gupta', 9234567890, 'rahul.gupta@example.com'),
(934567890123, 'Priya Singh', 9345678901, 'priya.singh@example.com'),
(945678901234, 'Rajiv Kumar', 9456789012, 'rajiv.kumar@example.com'),
(956789012345, 'Amit Mishra', 9567890123, 'amit.mishra@example.com'),
(967890123456, 'Neha Gupta', 9678901234, 'neha.gupta@example.com'),
(978901234567, 'Karan Patel', 9789012345, 'karan.patel@example.com'),
(989012345678, 'Sneha Singh', 9890123456, 'sneha.singh@example.com'),
(900123456789, 'Abhishek Kumar', 9001234567, 'abhishek.kumar@example.com'),
(811223344556, 'Swati Sharma', 8112233445, 'swati.sharma@example.com'),
(822334455667, 'Rohit Gupta', 8223344556, 'rohit.gupta@example.com'),
(833445566778, 'Vikas Singh', 8334455667, 'vikas.singh@example.com'),
(844556677889, 'Nisha Patel', 8445566778, 'nisha.patel@example.com'),
(855667788990, 'Saurabh Sharma', 8556677889, 'saurabh.sharma@example.com'),
(866778899001, 'Pooja Singh', 8667788990, 'pooja.singh@example.com'),
(877889900112, 'Alok Kumar', 8778899001, 'alok.kumar@example.com'),
(888990011223, 'Mukesh Gupta', 8889900112, 'mukesh.gupta@example.com'),
(899001122334, 'Ritu Patel', 8990011223, 'ritu.patel@example.com'),
(910112233445, 'Aarav Sharma', 9101122334, 'aarav.sharma@example.com'),
(821234567890, 'Anjali Gupta', 8212345678, 'anjali.gupta@example.com');

INSERT INTO property (house_number, Street, City, Locality, Pincode, Area, Bedrooms, year_of_construction)
VALUES('C-101', 'Nehru Road', 'Delhi', 'Lajpat Nagar', 110024, 1200, 2, 2019),
('D-402', 'Rajdanga Main Road', 'Kolkata', 'Tollygunge', 700107, 1400, 3, 2016),
('A-2', 'Vikaspuri Road', 'South Delhi', 'South Delhi', 110018, 1000, 1, 2021),
('B-701', 'G.S. Road', 'Guwahati', 'Paltan Bazar', 781001, 1800, 4, 2017),
('C-203', 'Sukanta Sarani', 'Kolkata', 'Jadavpur', 700032, 950, 2, 2022),
('B-601', 'Rani Laxmi Bai Marg', 'Delhi', 'Malviya Nagar', 110017, 1300, 3, 2018),
('D-304', 'Kamla Nagar Road', 'Delhi', 'Kamla Nagar', 110007, 1100, 2, 2020),
('A-15', 'Gariahat Road', 'Kolkata', 'Gariahat', 700029, 1000, 2, 2015),
('B-501', 'Dispur Road', 'Guwahati', 'Dispur', 781005, 1600, 3, 2016),
('C-401', 'Park Street', 'Kolkata', 'Park Street', 700016, 1200, 2, 2019),
('A-7', 'Sundarpur Main Road', 'Guwahati', 'Sundarpur', 781005, 900, 1, 2023),
('B-902', 'Golpark Road', 'Kolkata', 'Ballygunge', 700019, 1700, 4, 2020),
('D-205', 'Sahapur Main Road', 'Kolkata', 'Tollygunge', 700053, 1150, 2, 2017),
('C-702', 'Hauz Khas Road', 'South Delhi', 'South Delhi', 110016, 1500, 3, 2022),
('A-3', 'Ballygunge Circular Road', 'Kolkata', 'Ballygunge', 700019, 950, 2, 2021),
('B-303', 'Kolathur Road', 'Chennai', 'Anna Nagar', 600040, 1000, 2, 2015),
('C-401', 'Paltan Bazar Road', 'Guwahati', 'Paltan Bazar', 781008, 1200, 3, 2018),
('D-102', 'Kavi Subhash Road', 'Kolkata', 'Tollygunge', 700041, 800, 1, 2023),
('Q-17', 'Shillong Road', 'Guwahati', 'Dispur', 781005, 1000, 2, 2019),
('E-5', 'Ganesh Chandra Avenue', 'Kolkata', 'Malviya Nagar', 700029, 1600, 3, 2016),
('A-12', 'Rajendra Place', 'Delhi', 'Lajpat Nagar', 110024, 1500, 2, 2019),
('4/5', 'Prince Anwar Shah Road', 'Kolkata', 'Tollygunge', 700033, 1200, 3, 2018),
('B-32', 'Bhaskar Nagar Road', 'Guwahati', 'Paltan Bazar', 781008, 800, 1, 2021),
('77', 'Safdarjung Enclave', 'Delhi', 'Park Street', 110029, 2000, 4, 2017),
('10', 'VIP Road', 'Kolkata', 'Tollygunge', 700045, 900, 2, 2022);

insert into real_estate_transactions 
values(4, 122345678901, 912345678901, 'A-12', 110024, 18000000, 'SOLD', 1361, '2023-01-15'),
(9, 123456789012, 989012345678, '10', 700045, 9000000, 'SOLD', 134, '2022-10-21'),
(9, 124567890123, 899001122334, '4/5', 700033, 35000, 'RENT', 579, '2020-02-14'),
(6, 125678901234, 888990011223, 'B-32', 781008, 11500, 'RENT', 398, '2023-01-31'),
(1, 126789012345, 912345678901, '77', 110029, 35000000, 'SOLD', 568, '2019-07-04');

insert into buyer_assigned values(13, 101234567890),
(5, 102345678901),
(8, 103456789012),
(8, 104567890123),
(3, 105678901234),
(3, 106789012345),
(7, 107890123456),
(3, 108901234567),
(6, 109012345678),
(14, 111223344556),
(5, 112334455667),
(9, 113445566778),
(11, 114556677889),
(1, 115667788990),
(4, 116778899001),
(10, 117889900112),
(2, 118990011223),
(3, 119001122334),
(14, 120112233445),
(13, 121234567890);

INSERT INTO seller_assigned (agent_id, seller_uid, Number_of_properties)
VALUES 
  (4,912345678901, 1),
  (9,923456789012, 1),
  (14,934567890123, 1),
  (6,945678901234, 1),
  (8,956789012345, 1),
  (3,967890123456, 1),
  (5,978901234567, 1),
  (2,989012345678, 1),
  (7,900123456789, 1),
  (1,811223344556, 1),
  (11,822334455667, 1),
  (10,833445566778, 1),
  (9,844556677889, 1),
  (14,855667788990, 1),
  (10,866778899001, 1),
  (13,877889900112, 1),
  (6,888990011223, 1),
  (9,899001122334, 1),
  (7,910112233445, 1),
  (3,821234567890, 1);

  INSERT INTO owns (seller_uid, house_number, Pincode)
VALUES 
  (912345678901, 'C-101', 110024),
  (923456789012, 'D-402', 700107),
  (934567890123, 'A-2', 110018),
  (945678901234, 'B-701', 781001),
  (956789012345, 'C-203', 700032),
  (967890123456, 'B-601', 110017),
  (978901234567, 'D-304', 110007),
  (989012345678, 'A-15', 700029),
  (900123456789, 'B-501', 781005),
  (811223344556, 'C-401', 700016),
  (822334455667, 'A-7', 781005),
  (833445566778, 'B-902', 700019),
  (844556677889, 'D-205', 700053),
  (855667788990, 'C-702', 110016),
  (866778899001, 'A-3', 700019),
  (877889900112, 'B-303', 600040),
  (888990011223, 'C-401', 781008),
  (899001122334, 'D-102', 700041),
  (910112233445, 'Q-17', 781005),
  (821234567890, 'E-5', 700029);

  INSERT INTO availability (house_number, Pincode, Sale, Rent, amount_per_month, selling_price, date_since_available)
VALUES
('C-101', 110024, 'yes', 'no', null, 15000000, '2022-01-01'),
('D-402', 700107, 'yes', 'yes', 20000, 20000000, '2021-05-01'),
('A-2', 110018, 'yes', 'no', null, 10000000, '2021-12-01'),
('B-701', 781001, 'no', 'yes', 25000, null, '2022-03-01'),
('C-203', 700032, 'yes', 'yes', 15000, 18000000, '2022-02-01'),
('B-601', 110017, 'yes', 'yes', 25000, 25000000, '2021-08-01'),
('D-304', 110007, 'no', 'yes', 18000, null, '2022-01-01'),
('A-15', 700029, 'no', 'yes', 15000, null, '2021-04-01'),
('B-501', 781005, 'yes', 'no', null, 12000000, '2022-02-01'),
('C-401', 700016, 'no', 'yes', 20000, null, '2021-10-01'),
('A-7', 781005, 'yes', 'no', null, 8000000, '2023-01-01'),
('B-902', 700019, 'yes', 'yes', 30000, 30000000, '2021-09-01'),
('D-205', 700053, 'yes', 'no', null, 11000000, '2022-04-01'),
('C-702', 110016, 'no', 'yes', 28000, null, '2021-07-01'),
('A-3', 700019, 'yes', 'yes', 17000, 20000000, '2022-03-01'),
('B-303', 600040, 'yes', 'no', null, 9000000, '2021-01-01'),
('C-401', 781008, 'yes', 'yes', 22000, 25000000, '2021-12-01'),
('D-102', 700041, 'no', 'yes', 16000, null, '2022-02-01'),
('Q-17', 781005, 'yes', 'no', null, 12000000, '2021-11-01'),
('E-5', 700029, 'yes', 'yes', 25000, 30000000, '2022-06-01');

INSERT INTO rent_cost(amount_per_month)
SELECT DISTINCT amount_per_month
FROM availability where amount_per_month is not null;

INSERT INTO sale_cost(selling_price)
SELECT DISTINCT selling_price
FROM availability where selling_price is not null;
