#Functions
#1. Customer file

    def add_cust():
        cust_id = input("Enter the customer ID: ")
        cust_name = input("Enter the customer name: ")
        cust_phone = int(input("Enter the phone number: "))
        location = input("Enter the location: ")
        
        plan_id = input("Enter the Plan ID: ")
    
        table_cust = open('C:\\Users\\imaja\\OneDrive\\Desktop\\MBA 2022 -2024\\T3\\Python\\CIA2\\customer.csv','a')
        table_cust.write(f"{cust_id},{cust_name},{cust_phone},{location},{plan_id}\n")
        
        print("Customer Added Successfully")
        table_cust.close()
    
    def display_cust():
        print("CUSTOMERS\n----------------")
        table_cust = open('C:\\Users\\imaja\\OneDrive\\Desktop\\MBA 2022 -2024\\T3\\Python\\CIA2\\customer.csv','r')
        print(table_cust.read())
        table_cust.close()
    
    def update_cust():
        cust_id = input("Enter the Customer ID to update: ")
        found = False
    
        with open('C:\\Users\\imaja\\OneDrive\\Desktop\\MBA 2022 -2024\\T3\\Python\\CIA2\\customer.csv', 'r+') as table_cust:
            lines = table_cust.readlines()
            table_cust.seek(0)
            for i, line in enumerate(lines):
                if line.startswith(cust_id + ','):
                    found = True
                    existing_cust = line.strip().split(',')
                    
                    cust_id = input(f"Enter the new ID for {existing_cust[0]}: ")
                    cust_name = input(f"Enter the new name for {existing_cust[1]}: ")
                    cust_phone = input(f"Enter the new phone number for {existing_cust[2]}: ")
                    location = input(f"Enter the new location for {existing_cust[3]}: ")
                    
                    display_plans()
                    plan_id = input(f"Enter the new plan ID for {existing_cust[4]}: ")
                    
                    new_line = f"{cust_id},{cust_name},{cust_phone},{location},{plan_id}\n"
                    lines[i] = new_line
                    break
            
            if not found:
                print("Customer not found!")
                return
            
            table_cust.writelines(lines)
            table_cust.truncate()
        
        print("Customer details updated successfully!")
        
    def delete_cust():
        cust_id = input("Enter the Customer ID to delete: ")
        found = False
    
        with open('C:\\Users\\imaja\\OneDrive\\Desktop\\MBA 2022 -2024\\T3\\Python\\CIA2\\customer.csv', 'r+') as table_cust:
            lines = table_cust.readlines()
            table_cust.seek(0)
            for line in lines:
                if not line.startswith(cust_id + ','):
                    table_cust.write(line)
                else:
                    found = True
            table_cust.truncate()
        
        if found:
            print("Customer deleted successfully!")
        else:
            print("Customer not found!")

    def view_profile(cust_id):
    print("Your Account😎\n----------------")
    found = False

    with open('C:\\Users\\imaja\\OneDrive\\Desktop\\MBA 2022 -2024\\T3\\Python\\CIA2\\customer.csv', 'r') as table_cust:
        for line in table_cust:
            if line.startswith(cust_id + ','):
                cust_details = line.strip().split(',')
                print(f"ID: {cust_details[0]}")
                print(f"Name: {cust_details[1]}")
                print(f"Phone: {cust_details[2]}")
                print(f"Location: {cust_details[3]}")
                print(f"Plan ID: {cust_details[4]}")
                found = True
                break

    if not found:
        print("Customer not found!")
        



#2. Service file

    def add_service():
        service_id = input("Enter the Service ID: ")
        service_name = input("Enter the Service name: ")
        price = int(input("Enter the Price: "))
        availability = input("Enter the Avalability(LIVE/CLOSED): ")
        display_plans()
        plan_id = input("Enter the Plan ID: ")
    
        table_services = open('C:\\Users\\imaja\\OneDrive\\Desktop\\MBA 2022 -2024\\T3\\Python\\CIA2\\services.csv','a')
        table_services.write(f"{service_id},{service_name},{price},{availability},{plan_id}\n")
        
        print("Service Added Successfully")
        table_services.close()

    def display_services():
    
        print("Services we offer😮\n---------------------")
        table_services = open('C:\\Users\\imaja\\OneDrive\\Desktop\\MBA 2022 -2024\\T3\\Python\\CIA2\\services.csv','r')
        print(table_services.read())
        table_services.close()



#3. Plans file

    def display_plans():
        print("Choose the best plan for you😍\n-----------------------")
        table_plans = open('C:\\Users\\imaja\\OneDrive\\Desktop\\MBA 2022 -2024\\T3\\Python\\CIA2\\plans.csv','r')
        print(table_plans.read())
        table_plans.close()
        
    
#4. Permissions file    

    def display_permissions():
        print("PERMISSIONS\n----------------")
        table_permissions = open('C:\\Users\\imaja\\OneDrive\\Desktop\\MBA 2022 -2024\\T3\\Python\\CIA2\\permissions.csv','r')
        print(table_permissions.read())
        table_permissions.close()
        
#5. Payment file  

    def add_payment(cust_id):
        import random
        
        pmt_id = random.randint(222222,999999)
        pmt_date = input("Enter the payment date(DD/MM/YYY): ")
        pmt_amount = int(input("Enter the payment amount: "))
        pmt_method = input("Enter the payment method: ")
        pmt_status = "SUCCESS"
        
    
        table_pmt = open('C:\\Users\\imaja\\OneDrive\\Desktop\\MBA 2022 -2024\\T3\\Python\\CIA2\\payment.csv','a')
        table_pmt.write(f"{cust_id},{pmt_id},{pmt_date},{pmt_amount},{pmt_method},{pmt_status}\n")
        
        print("Payment Successful")
        table_pmt.close()

    def display_payment():
        print("PAYMENT\n----------------")
        table_pmt = open('C:\\Users\\imaja\\OneDrive\\Desktop\\MBA 2022 -2024\\T3\\Python\\CIA2\\payment.csv','r')
        print(table_pmt.read())
        table_pmt.close()



#6. Customer Support file  


    def display_tickets():
        print("SUPPORT TICKETS\n----------------")
        table_support = open('C:\\Users\\imaja\\OneDrive\\Desktop\\MBA 2022 -2024\\T3\\Python\\CIA2\\support.csv','r')
        print(table_support.read())
        table_support.close()

    def support_request(cust_id):
        import random
       
        emp_id = random.randint(20,30)
        ticket_id = random.randint(1,1000)
        issue_description = input("Enter your issue: ")
        ticket_status = "OPEN"
        
    
        table_support = open('C:\\Users\\imaja\\OneDrive\\Desktop\\MBA 2022 -2024\\T3\\Python\\CIA2\\support.csv','a')
        table_support.write(f"{ticket_id},{cust_id},{emp_id},{issue_description},{ticket_status}\n")
        
        print("\nTicket Raised Successfully")
        table_support.close()

    def update_ticket():
        ticket_id = input("Enter the ticket ID to update: ")
        found = False
    
        with open('C:\\Users\\imaja\\OneDrive\\Desktop\\MBA 2022 -2024\\T3\\Python\\CIA2\\support.csv', 'r+') as table_support:
            lines = table_support.readlines()
            table_support.seek(0)
            for i, line in enumerate(lines):
                if line.startswith(ticket_id + ','):
                    found = True
                    existing_ticket = line.strip().split(',')
                    
                    ticket_status = input(f"Update the new status [ Currently: {existing_ticket[4]} ]")
                
                    
                    new_line = f"{existing_ticket[0]},{existing_ticket[1]},{existing_ticket[2]},{existing_ticket[3]},{ticket_status}\n"
                    lines[i] = new_line
                    break
            
            if not found:
                print("Ticket not found!")
                return
            
            table_support.writelines(lines)
            table_support.truncate()
        
        print("Ticket updated successfully!")
        
        
        
        
#7. Leads file  
    
    def display_leads():
        print("LEADS\n----------------")
        table_leads = open('C:\\Users\\imaja\\OneDrive\\Desktop\\MBA 2022 -2024\\T3\\Python\\CIA2\\leads.csv','r')
        print(table_leads.read())
        table_leads.close()
        
        
    def add_lead():
        import random
        
        lead_id = random.randint(600,999)
        lead_name = input("Enter the lead name: ")
        lead_phone = random.randint(9000000000,10000000000)
        lead_source = input("Enter the lead source: ")
        emp_id = random.randint(31,40)
        
        print('''\n STATUSES \n---------------
        \n1. Contacted: The lead has been contacted by a sales representative.
        \n2. Follow-up: A follow-up call or email is required to move the lead further in the sales process.
        \n3. Qualified: The lead has met certain criteria and has been deemed a qualified prospect.
        \n4. Not Interested: The lead has expressed disinterest in the product or service being offered.
        \n5. No Response: The lead has not responded to any attempts at contact.
        \n6. Demo/Meeting Scheduled: The lead has agreed to a demonstration or meeting to discuss the product or service further.''')
        
        lead_status = input("Enter the lead status: ")
        
    
        table_leads = open('C:\\Users\\imaja\\OneDrive\\Desktop\\MBA 2022 -2024\\T3\\Python\\CIA2\\leads.csv','a')
        table_leads.write(f"{lead_id},{lead_name},{lead_phone},{lead_source},{emp_id},{lead_status}\n")
        
        print("\nLead Added Successfully")
        table_leads.close()

    def update_lead():
        lead_id = input("Enter the lead ID to update: ")
        found = False
    
        with open('C:\\Users\\imaja\\OneDrive\\Desktop\\MBA 2022 -2024\\T3\\Python\\CIA2\\leads.csv', 'r+') as table_leads:
            lines = table_leads.readlines()
            table_leads.seek(0)
            for i, line in enumerate(lines):
                if line.startswith(lead_id + ','):
                    found = True
                    existing_ticket = line.strip().split(',')
                    
                    print('''\n STATUSES \n---------------
        \n1. Contacted: The lead has been contacted by a sales representative.
        \n2. Follow-up: A follow-up call or email is required to move the lead further in the sales process.
        \n3. Qualified: The lead has met certain criteria and has been deemed a qualified prospect.
        \n4. Not Interested: The lead has expressed disinterest in the product or service being offered.
        \n5. No Response: The lead has not responded to any attempts at contact.
        \n6. Demo/Meeting Scheduled: The lead has agreed to a demonstration or meeting to discuss the product or service further.''')
                    
                    lead_status = input(f"Update the new status [ Currently: {existing_ticket[5]} ]")
                
                    
                    new_line = f"{existing_ticket[0]},{existing_ticket[1]},{existing_ticket[2]},{existing_ticket[3]},{existing_ticket[4]},{lead_status}\n"
                    lines[i] = new_line
                    break
            
            if not found:
                print("Lead not found!")
                return
            
            table_leads.writelines(lines)
            table_leads.truncate()
        
        print("Lead updated successfully!")
        
        
        
        
#8. Employee file 

    def display_employees():
        print("EMPLOYEES\n----------------")
        table_emp = open('C:\\Users\\imaja\\OneDrive\\Desktop\\MBA 2022 -2024\\T3\\Python\\CIA2\\employee.csv','r')
        print(table_emp.read())
        table_emp.close()

