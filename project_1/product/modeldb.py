from django.db import connection


class Brand:
    def all(self):

        with connection.cursor() as cursor:
            cursor.execute('select * from brand;')
            datas = cursor.fetchall()
        return datas
class Category:
    def all(self):
        with connection.cursor() as cursor:
            cursor.execute('select * from category;')
            datas = cursor.fetchall()
        return datas
class Product:
    def column(self):
        with connection.cursor() as cursor:
            cursor.execute('show columns from product;')
            columns = cursor.fetchall()
        return columns

    def create(self,productinfo):
        
        with connection.cursor() as cursor:
            sql = """
                INSERT INTO product(productname,brandid,rating,catergoryid,productprice,productimg,productdescription)
                VALUES (%s,%s,%s,%s,%s,%s,%s)
            """
            cursor.execute(sql,productinfo)
    def all(self):
        with connection.cursor() as cursor:
            cursor.execute("""select product.productid, 
                            product.productname,categoryname,brand.brandname,

                            product.rating,
                            product.productprice,product.productdescription,product.productimg

                            from product left join brand on product.brandid = brand.brandid 
                            left join category on product.catergoryid = category.categoryid """)
            datas = cursor.fetchall()
        return datas
    def selectdata(self,id):
        with connection.cursor() as cursor:
            sql = 'select * from product where productid=%s;'
            cursor.execute(sql,str(id))
            datas = cursor.fetchone()
            
        return datas
    def update(self,product):
        with connection.cursor() as cursor:
            sql = '''UPDATE product SET productname=%s,brandid=%s,rating=%s,catergoryid=%s,
                        productprice=%s,productimg=%s,productdescription=%s where productid=%s;'''
            cursor.execute(sql,product)
    def delete(self,did):
        with connection.cursor() as cursor:
            sql = '''DELETE FROM product where productid=%s;'''
            cursor.execute(sql,str(did))
            
            