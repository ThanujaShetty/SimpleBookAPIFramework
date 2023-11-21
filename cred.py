import random


def get_creds(custom_input_name):
    custom_input_name = str(custom_input_name).lower()
    num = random.randint(1000, 3000)
    cust_mail = custom_input_name+str(num) +"@gmail.com"
    return {"customer_name" : custom_input_name,
            "customer_email" : cust_mail}

def order_details(Book_id,cust_name):
    Book_id =int(Book_id)
    cust_name=str(cust_name).upper()
    return {
  "bookId": Book_id,
  "customerName": cust_name
}




if __name__ == "__main__":
    print(get_creds("KRUSHNA"))
    print(order_details(1,"chetan2"))