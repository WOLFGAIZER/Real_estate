from email_sender import *
from tkinter import messagebox
from datetime import datetime
password = "" #Enter your password for SQL in the localhost
def establish_connection(host = '127.0.0.1', user = 'root', passwd = password, database= 'matrix_real_estate'):
    '''Establishes connection with local database, throws exception(not error) if connection not established'''
    import mysql.connector as cntr
    from mysql.connector import Error
    connection = None
    try:
        connection = cntr.connect(
                host=host,
                user=user,
                passwd=passwd,
                database=database
            )

        return connection

    except Error as e:
        return f'An error occured : {e}'
    
def login_agent(username, password):
    '''Function used to login the agent into the GUI'''

    connection = establish_connection()
    curr = connection.cursor()

    curr.execute(f"select * from agents where username = '{username}'")
    agent_info = curr.fetchall()
    connection.commit()

    if len(agent_info)==0:
        return 1, "Invalid Username!", agent_info
    else:
        agent_info = agent_info[0]
        if agent_info[6] != password:
            return 1, "Invalid Password!", agent_info
    global agentid, agent_inf
    agent_inf = agent_info
    agentid = agent_info[0]

    return 0, None, agent_info

def register_user(user_type, name, mobile, email, aadhar, username, password, operating_area):
    '''Function Used for Registration of Agent/Buyer/Seller'''
    flag, message = 0, ""
    connection = establish_connection()
    curr = connection.cursor()
    
    try:
        curr.execute(f"Insert into {user_type} (name, phone_number, mail_id, unique_id, username, password, operating_area) values('{name}', {mobile}, '{email}', {aadhar}, '{username}', '{password}', '{operating_area}')" if user_type=='agents'
                    else f"Insert into {user_type} values({aadhar}, '{name}', {mobile}, '{email}')")
        curr.execute(f"Select * from {user_type} where unique_id = {aadhar}" if user_type=="agents"
                     else f"Select * from {user_type} where {user_type.rstrip('s')}_uid = {aadhar}")
        user_info = curr.fetchall()[0]
        try:
            if user_type=="agents":
                email_new_registration(user_type, email, user_info)
            else:
                email_new_registration(user_type, email, user_info, agent_assigned=agent_inf)
            connection.commit()
        except:
            messagebox.showerror("Error Sending Mail", "There has been a error in sending a confirmation mail.\n Make sure your internet connection is running.")
            return 4, ""
        if user_type=="agents":
            return 0, None
        else:
            return assign_customer(user_type, aadhar, name, mobile, email)
    except:
        if user_type=="agents":
            curr.execute(f"Select * from {user_type} where username = '{username}'")
            result = curr.fetchall()
            if len(result)!=0:
                flag, message = 1, "Username"
            curr.execute(f"Select * from {user_type} where operating_area = '{operating_area}'")
            result = curr.fetchall()
            if len(result)!=0:
                flag, message = 1, "Operating Area"
        else:
            flag, message = assign_customer(user_type, aadhar, name, mobile, email, new=False)

        if flag==1 and message == "":
            curr.execute(f"Select * from {user_type} where unique_id = {aadhar}" if user_type=="agents" 
                     else f"Select * from {user_type} where {user_type.rstrip('s')}_uid = {aadhar}")
            result = curr.fetchall()
            if len(result)!=0:
                flag, message = 1, "Aadhar Number"
    
            curr.execute(f"Select * from {user_type} where phone_number = {mobile}")
            result = curr.fetchall()
            if len(result)!=0:
                flag, message = 1, "Phone Number"
            
            curr.execute(f"Select * from {user_type} where mail_id = '{email}'")
            result = curr.fetchall()
            if len(result)!=0:
                flag, message = 1, "E-Mail ID"
        
        connection.commit()
    return flag, message

def assign_customer(user_type, aadhar, name, mobile, email, new=True):
    '''Used to assign a new/existing customer with the logged in agent.'''
    connection = establish_connection()
    curr = connection.cursor()
    
    ## Check if it is assigned.
    curr.execute(f"Select * from {user_type} where {user_type.rstrip('s')}_uid = {aadhar} and name = '{name}' and phone_number = {mobile} and mail_id = '{email}'")
    result = curr.fetchall()

    if len(result)!=0:
        curr.execute(f"Select * from {user_type.rstrip('s')}_assigned where {user_type.rstrip('s')}_uid = {aadhar}")
        result = curr.fetchall()
        if len(result)!=0:
            return 3, f"Username is already assigned to Agent_ID {result[0][0]}"
        ##Otherwise assign it to agent (Global Variable)
        else:
            curr.execute(f"Insert into {user_type.rstrip('s')}_assigned (agent_id, {user_type.rstrip('s')}_uid) values({agentid}, {aadhar})")
            email_assigned_customer(user_type, email, agent_inf[3], (aadhar, name, mobile, email), agent_inf, new= new)
            connection.commit()
            if new==False:
                return 2, f"{user_type.rstrip('s')} is already registered. He/She has been assigned to you.\nAn Email has been sent for confirmation."
            else:
                return 0, None
    else:
        return 1, ""
    
def list_assigned_customers(customer_type, agent_id=-1):
    '''Returns all the assigned customers with the mentioned agent id'''

    connection = establish_connection()
    curr = connection.cursor()
    if agent_id==-1:
        curr.execute(f"Select x.{customer_type.rstrip('s')}_uid, name from {customer_type} x join {customer_type.rstrip('s')}_assigned y on x.{customer_type.rstrip('s')}_uid = y.{customer_type.rstrip('s')}_uid where agent_id = {agentid}")
    else:
        curr.execute(f"Select x.{customer_type.rstrip('s')}_uid, name from {customer_type} x join {customer_type.rstrip('s')}_assigned y on x.{customer_type.rstrip('s')}_uid = y.{customer_type.rstrip('s')}_uid where agent_id = {agent_id}")
    
    assigned_customers = curr.fetchall()
    for i in range(len(assigned_customers)):
        assigned_customers[i] = f"{assigned_customers[i][1]}, {assigned_customers[i][0]}"
    
    return assigned_customers

def unassign_customer(customer_type, customer_uid):
    '''Unassigns a buyer/seller from the logged in agent'''

    connection = establish_connection()
    curr = connection.cursor()

    ##Removing available properties of sellers.
    if customer_type=="sellers":
        curr.execute(f"select DISTINCT amount_per_month from availability where (house_number, pincode) in (Select house_number, pincode from owns where seller_uid = {customer_uid}) and amount_per_month is NOT NULL")
        rent_costs = curr.fetchall()
        curr.execute(f"select DISTINCT selling_price from availability where (house_number, pincode) in (Select house_number, pincode from owns where seller_uid = {customer_uid}) and selling_price is NOT NULL")
        sale_costs = curr.fetchall()
        
        try:
            curr.execute(f"Delete from availability where (house_number, pincode) in (Select house_number, pincode from owns where seller_uid = {customer_uid})")
        except:
            messagebox.showerror("Error Unassigning", "There has been some error with unassigning the customer from the database.\nIt might be due to error in connection with the database.\nPlease try again later")   
            return 1
        
        ##Checking if there are no houses left with the prices of removed houses, If so then remove those prices as the table represents a weak entity..
           
        if len(rent_costs)!=0:
            for i in rent_costs:
                curr.execute(f"select * from availability where amount_per_month = {i[0]}")
                result = curr.fetchall()
                if len(result)==0:
                    curr.execute(f"Delete from rent_cost where amount_per_month = {i[0]}")
        
        if len(sale_costs)!=0:
            for i in sale_costs:
                curr.execute(f"select * from availability where selling_price = {i[0]}")
                result = curr.fetchall()
                if len(result)==0:
                    curr.execute(f"Delete from sale_cost where selling_price = {i[0]}")

    ##Removing from buyer/seller_assigned
    try:
        curr.execute(f"Delete from {customer_type.rstrip('s')}_assigned where {customer_type.rstrip('s')}_uid = {customer_uid}")
    except:
        messagebox.showerror("Error Unassigning", "There has been some error with unassigning the customer from the database.\nIt might be due to error in connection with the database.\nPlease try again later")
        return 1
    
    curr.execute(f"Select * from {customer_type} where {customer_type.rstrip('s')}_uid = {customer_uid}")

    email_unassigned_customer(customer_type, curr.fetchone(), agent_inf)
    curr.fetchall()
    connection.commit()
    return 0

def remove_available_property(house_number, pincode):
    '''This removes the mentioned property from the available table'''

    connection = establish_connection()
    curr = connection.cursor()

    curr.execute(f"select DISTINCT amount_per_month from availability where (house_number, pincode) = ('{house_number}', {pincode}) and amount_per_month IS NOT NULL")
    rent_costs = curr.fetchall()
    curr.execute(f"select DISTINCT selling_price from availability where (house_number, pincode) = ('{house_number}', {pincode}) and selling_price IS NOT NULL")
    sale_costs = curr.fetchall()

    try:
        curr.execute(f"Delete from availability where (house_number, pincode) = ('{house_number}', {pincode})")
        curr.execute(f"Update seller_assigned set Number_of_properties=Number_of_properties-1 where seller_uid = (Select seller_uid from sellers where seller_uid = (select seller_uid from owns where (house_number, pincode) = ('{house_number}', {pincode})))")
    except:
        messagebox.showerror("Error Unassigning", "There has been some error with unassigning the customer from the database.\nIt might be due to error in connection with the database.\nPlease try again later")   
        return 1
    
    ##Checking if there are no houses left with the prices of removed houses, If so then remove those prices as the table represents a weak entity..
           
    if len(rent_costs)!=0:
        for i in rent_costs:
            curr.execute(f"select * from availability where amount_per_month = {i[0]}")
            result = curr.fetchall()
            if len(result)==0:
                curr.execute(f"Delete from rent_cost where amount_per_month = {i[0]}")
        
    if len(sale_costs)!=0:
        for i in sale_costs:
            curr.execute(f"select * from availability where selling_price = {i[0]}")
            result = curr.fetchall()
            if len(result)==0:
                curr.execute(f"Delete from sale_cost where selling_price = {i[0]}")
    
    curr.execute(f"Select * from sellers where seller_uid = (select seller_uid from owns where (house_number, pincode) = ('{house_number}', {pincode}))")
    email_property_removed_to_owner(house_number, pincode, curr.fetchone())
    curr.fetchall()
    connection.commit()
    return 0

def get_available_properties(agent_id = -1):
    '''This function returns all the available properties under the mention agent_id'''

    connection = establish_connection()
    curr = connection.cursor()

    curr.execute(f"select house_number, pincode from availability where (house_number, pincode) in (Select house_number, pincode from owns where seller_uid in (Select seller_uid from seller_assigned where agent_id = {agentid if agent_id==-1 else agent_id}))")
    properties = curr.fetchall()

    for i in range(len(properties)):
        properties[i] = f"{properties[i][0]}, {properties[i][1]}"
    
    connection.commit()
    return properties


def add_property(house_number, street, city, locality, pincode, area, bedrooms, year_of_construction, seller_uid, sale_price, rent_price, sale_type):
    '''This function adds the property to available whether new/old'''

    connection = establish_connection()
    curr = connection.cursor()

    curr.execute(f"Select * from property where (house_number, pincode) = ('{house_number}', {pincode})")
    house = curr.fetchall()
    
    if len(house)==0:
        return add_new_property(house_number, street, city, locality, pincode, area, bedrooms, year_of_construction, seller_uid, sale_price, rent_price, sale_type)
    else:
        messagebox.showinfo("Property already Exists", "The entered property details already exists in the database\nWe will try to update the information.")
        return add_existing_property(house_number, street, city, locality, pincode, area, bedrooms, year_of_construction, sale_price, rent_price, sale_type)

def add_new_property(house_number, street, city, locality, pincode, area, bedrooms, year_of_construction, seller_uid, sale_price, rent_price, sale_type):
    '''This is a part of add_property that adds properties which do not belong to the property table'''

    connection = establish_connection()
    curr = connection.cursor()
    date_today = datetime.today().strftime('%Y-%m-%d')
    try:
        curr.execute(f"Insert into property values('{house_number}', '{street}', '{city}', '{locality}', {pincode}, {area}, {bedrooms}, {year_of_construction})")
        curr.execute(f"Insert into owns values({seller_uid}, '{house_number}', {pincode})")
        curr.execute(f"Update seller_assigned set Number_of_properties = Number_of_properties + 1 where (agent_id, seller_uid) = ({agentid}, {seller_uid})")
        curr.execute(f"Insert into availability values('{house_number}', {pincode}, 'yes', 'yes', {rent_price}, {sale_price}, '{date_today}')" if sale_type=="Both"
                    else f"Insert into availability values('{house_number}', {pincode}, 'yes', 'no', NULL, {sale_price}, '{date_today}')" if sale_type=="Sale"
                    else f"Insert into availability values('{house_number}', {pincode}, 'no', 'yes', {rent_price}, NULL, '{date_today}')")
            
        if rent_price!="":
            curr.execute(f"Select * from rent_cost where amount_per_month = {rent_price}")
            if len(curr.fetchall())==0:
                curr.execute(f"Insert into rent_cost values({rent_price})")

        if sale_price!="":
            curr.execute(f"Select * from sale_cost where selling_price = {sale_price}")
            if len(curr.fetchall())==0:
                curr.execute(f"Insert into sale_cost values({sale_price})")
        
        curr.execute(f"select * from sellers where seller_uid = {seller_uid}")
        email_added_property(curr.fetchone(), (house_number, street, city, locality, pincode, area, bedrooms, year_of_construction))
        curr.fetchall()
        connection.commit()
        return 0
    except:
        messagebox.showerror("Error Adding Property", "There has been some error with adding the property to the database.\nIt might be due to error in connection with the database.\nPlease try again later")   
        return 1  

def add_existing_property(house_number, street, city, locality, pincode, area, bedrooms, year_of_construction, seller_uid, sale_price, rent_price, sale_type):
    '''This modifies and adds the existing property into the property table'''

    connection = establish_connection()
    curr = connection.cursor()

    date_today = datetime.today().strftime('%Y-%m-%d')
    try:
        curr.execute(f"Update property set street='{street}', city='{city}', locality='{locality}', area={area}, bedrooms={bedrooms}, year_of_construction={year_of_construction} where (house_number, pincode) = ('{house_number}', {pincode})")
        curr.execute(f"Select * from availability where (house_number, pincode) = ('{house_number}', {pincode})")
        result = curr.fetchall()
        if len(result)!=0:
            curr.execute(f"Update availability set sale='yes', rent='yes', amount_per_month={rent_price}, selling_price = {sale_price} where (house_number, pincode) = ('{house_number}', {pincode})" if sale_type=="Both"
                         else f"Update availability set sale='yes', rent='no', amount_per_month=NULL, selling_price = {sale_price} where (house_number, pincode) = ('{house_number}', {pincode})" if sale_type=="Sale"
                         else f"Update availability set sale='no', rent='yes', amount_per_month={rent_price}, selling_price = NULL where (house_number, pincode) = ('{house_number}', {pincode})")
        else:
            curr.execute(f"Insert into availability values('{house_number}', {pincode}, 'yes', 'yes', {rent_price}, {sale_price}, '{date_today}')" if sale_type=="Both"
                     else f"Insert into availability values('{house_number}', {pincode}, 'yes', 'no', NULL, {sale_price}, '{date_today}')" if sale_type=="Sale"
                     else f"Insert into availability values('{house_number}', {pincode}, 'no', 'yes', {rent_price}, NULL, '{date_today}')")
        

        if rent_price!="":
            curr.execute(f"Select * from rent_cost where amount_per_month = {rent_price}")
            if len(curr.fetchall())==0:
                curr.execute(f"Insert into rent_cost values({rent_price})")

        if sale_price!="":
            curr.execute(f"Select * from sale_cost where selling_price = {sale_price}")
            if len(curr.fetchall())==0:
                curr.execute(f"Insert into sale_cost values({sale_price})")

        curr.execute(f"select * from sellers where seller_uid = {seller_uid}")
        email_added_property(curr.fetchone(), (house_number, street, city, locality, pincode, area, bedrooms, year_of_construction))
        curr.fetchall()
        connection.commit()
        return 0
    except:
        messagebox.showerror("Error Adding Property", "There has been some error with adding the property to the database.\nIt might be due to error in connection with the database.\nPlease try again later")   
        return 1

def get_agent_ids():
    '''This function returns all the agent_ids'''

    connection = establish_connection()
    curr = connection.cursor()

    curr.execute(f"select agent_id, name from agents")
    agents = curr.fetchall()

    for i in range(len(agents)):
        agents[i] = f"{agents[i][0]}, {agents[i][1]}"

    connection.commit()
    return agents

def get_sale_report(agent_id = "-1, 0"):
    '''This function returns the details of property sold by given agent_id'''
    agent_id = agent_id.split(", ")
    agent_id = int(agent_id[0])
    connection = establish_connection()
    curr = connection.cursor()

    curr.execute(f"select house_number,street,locality,city,price,transaction_date from real_estate_transactions natural join property where type='SOLD' and agent_id={agent_id if agent_id==-1 else agent_id }")
    agents = curr.fetchall()

    connection.commit()
    return agents

def get_rent_report(agent_id = "-1, 0"):
    '''This function returns the details of property rented by given agent_id'''

    agent_id = agent_id.split(", ")
    agent_id = int(agent_id[0])
    connection = establish_connection()
    curr = connection.cursor()

    curr.execute(f"select house_number,street,locality,city,price,transaction_date from real_estate_transactions natural join property where type='RENT' and agent_id={agent_id if agent_id==-1 else agent_id }")
    agents = curr.fetchall()

    connection.commit()
    return agents

def perform_transaction(buyer_id, seller_id, house_number, pincode, transaction_date, price, transaction_type):
    '''This function performs the transaction for a property being sold/rented.'''

    connection = establish_connection()
    curr = connection.cursor()
    #print(buyer_id, seller_id, house_number, pincode, transaction_date, price, transaction_type)
    ##Check if seller owns the property id
    curr.execute(f"Select * from owns where seller_uid = {seller_id} and house_number = '{house_number}' and pincode = {pincode}")
    result = curr.fetchall()
    if len(result)==0:
        messagebox.showerror("Invalid Entry", "Seller does not own the house\nPlease enter valid details")
        return 1
    
    try:
        curr.execute(f"Select DATEDIFF('{transaction_date}', date_since_available) from availability where (house_number, pincode) = ('{house_number}', {pincode})")
        time_on_market = curr.fetchone()
        if int(time_on_market[0])<0:
            messagebox.showerror("Date error", "The entered transaction date must be after the date since available")
            return 1
        
        curr.execute(f"Select Sale, Rent from availability where (house_number, pincode) = ('{house_number}', {pincode})")
        result = curr.fetchone()
        if transaction_type=='SOLD':
            if result[0]=='no':
                messagebox.showerror("Property not available", "The property is not available for sale.")
                return 1
        elif transaction_type=='RENT':
            if result[1]=='no':
                messagebox.showerror("Property not available", "The property is not available for rent.")
                return 1
            
        time_on_market = time_on_market[0]
        curr.execute(f"Insert into real_estate_transactions values({agentid}, {buyer_id}, {seller_id}, '{house_number}', {pincode}, {price}, '{transaction_type}', {time_on_market},'{transaction_date}')")
        
        flag = remove_available_property(house_number, pincode)
        if flag==0:
            curr.execute(f"delete from seller_assigned where Number_of_properties=0")
            #num = curr.fetchone()
            #print(num)
            #if(curr.fetchone()[0]=="0"):
            #    flag = unassign_customer("sellers", seller_id)
            #    print("Seller Unassigned")
        if flag==0:
            flag = unassign_customer("buyers", buyer_id)
        if flag==0:
            curr.execute(f"Delete from owns where (seller_uid, house_number, Pincode) = ({seller_id}, '{house_number}', {pincode})")
    
        curr.execute(f"select * from sellers where seller_uid = {seller_id}")
        seller_info = curr.fetchone()
        curr.execute(f"Select * from buyers where buyer_uid = {buyer_id}")
        buyer_info = curr.fetchone()
        curr.execute(f"Select * from property where (house_number, pincode) = ('{house_number}', {pincode})")
        house_details = curr.fetchone()

        email_complete_transaction(seller_info, buyer_info, agent_inf, house_details, price, transaction_type, transaction_date)
        connection.commit()
        return 0
    except:
        messagebox.showerror("Error Adding Property", "There has been some error with adding the property to the database.\nIt might be due to error in connection with the database.\nPlease try again later")   
        return 1
