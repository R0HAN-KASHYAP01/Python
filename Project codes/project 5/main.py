import mysql.connector as sql

conn = sql.connect(host='localhost', user='root', passwd='#Shooting', database='grocery_shop')
if conn.is_connected():
    print('Successfully connected')
    c = conn.cursor()
    print('Grocery Shop Management System')
    print('1. Login')
    print('2. Exit')
    choice = int(input('Enter your choice:'))
    if choice == 1:
        user_name = input('Enter your user name:')
        password = input('Enter your password:')
        while user_name == 'akshat' and password == 'akshat982':
            print('Connected successfully')
            print('Grocery Shop')
            print('1. Customer Details')
            print('2. Product Details')
            print('3. Worker Details')
            print('4. See All Customer Details')
            print('5. See All Product Details')
            print('6. See All Worker Details')
            print('7. See One Customer Details')
            print('8. See One Product Details')
            print('9. See One Worker Details')
            print('10. Stocks')
            print('11. Pie Chart for Availability of Stock')
            choice = int(input('Enter the choice'))
            if choice == 1:
                cust_name = input('Enter your name=')
                phone_no = int(input('Enter your phone number='))
                cost = float(input('Enter your cost='))
                sql_insert = "insert into customer_details values (" + str(phone_no) + ", '" + cust_name + "', " + str(cost) + ")"
                c.execute(sql_insert)
                conn.commit()
                print('Data is updated')
            elif choice == 2:
                product_name = input('Enter product name=')
                product_cost = float(input('Enter the cost='))
                sql_insert = "insert into product_details values ('" + product_name + "', " + str(product_cost) + ")"
                c.execute(sql_insert)
                conn.commit()
                print('Data is updated')
            elif choice == 3:
                worker_name = input('Enter your name=')
                worker_work = input('Enter your work=')
                worker_age = int(input('Enter your age='))
                worker_salary = float(input('Enter your salary='))
                phone_no = int(input('Enter your phone number='))
                sql_insert = "insert into worker_details values ('" + worker_name + "','" + worker_work + "', " + str(worker_age) + ", " + str(worker_salary) + ", " + str(phone_no) + ")"
                c.execute(sql_insert)
                conn.commit()
                print('Data is updated')
            elif choice == 4:
                t = conn.cursor()
                t.execute('select * from customer_details')
                record = t.fetchall()
                for i in record:
                    print(i)
            # Add similar blocks for other choices... 
                    
            elif choice==5:
                t=conn.cursor()
                t.execute('select from product_details')
                record=t.fetchall()
                for i in record: 
                    print(i)
                    
            elif choice == 6:
                t-conn.cursor()
                t.execute('select from worker_details')
                record=t.fetchall()
                for i in record: print(i)
            elif choice==7:
                a=input('enter your name')
                t='select from customer_details where cust_name=("{}")'.format(a)
                c.execute(t)
                v=c.fetchall() 
                for i in v: 
                    print (v)
            elif choice ==8:
                a=input('enter your product_name')
                t='select from product_details where product_name=("{}") '.format(a)
                c.execute(t)
                v=c.fetchall()  
                for i in v:
                    print (i)
            elif choice==9:
                a-input('enter your name')
                t='select from worker details where worker_name=("{}")'.format(a)
                c.execute(t) 
                v=c.fetchall() 
                for i in v: 
                    print (v)
            elif choice==10:
                f=open('test.txt', 'r')
                data=f.read()
                print(data)
                f.close() 
            elif choice == 11:
                import matplotlib.pyplot as plt
                items = ('shoes', 'stationary', 'watch', 'house use', 'food items')
                availability = [156, 200, 103, 206, 196]
                colors = ['red', 'yellowgreen', 'blue', 'gold', 'lightcoral']
                plt.pie(availability, labels=items, colors=colors)
                plt.title('Availability of items in shop')
                plt.show()


            else:
                print('Wrong password, try again')
    elif choice == 2:
        exit()
