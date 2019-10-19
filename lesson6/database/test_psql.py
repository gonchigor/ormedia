import psycopg2

if __name__ == '__main__':
    conn = psycopg2.connect(dbname='shop', user='python',
                            password='python12345', host='localhost')
    cursor = conn.cursor()
    print("connect")
    cursor.execute('''select customers.name,
        customers.email,
        sale.date_sale,
        sum (p.price * ms.quantity) as cost
        from sale
        join customers on sale.id_customer = customers.id_customer
        join magazine_sales as ms on sale.id_sale = ms.id_sale
        join prices p on p.id_product = ms.id_product 
        AND p.date_price_change = (select max(date_price_change) 
            from prices p_max where
            p_max.id_product=p.id_product 
            and p_max.date_price_change <=  sale.date_sale) 
        group by customers.name,
        customers.email,
        sale.date_sale;''')
    for row in cursor:
        print(*row)
    cursor.close()
    conn.close()
