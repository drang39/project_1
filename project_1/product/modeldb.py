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
                INSERT INTO product(productname,brand_id_id,rating,category_id_id,price,productimg,description)
                VALUES (%s,%s,%s,%s,%s,%s,%s)
            """
            cursor.execute(sql,productinfo)
    def all(self):
        with connection.cursor() as cursor:
            cursor.execute("""select product.id, 
                            product.productname,categoryname,brand.brandname,

                            product.rating,
                            product.price,product.productimg

                            from product left join brand on product.brand_id_id = brand.id 
                            left join category on product.category_id_id = category.id """)
            datas = cursor.fetchall()
        return datas
    def selectdata(self,id):
        with connection.cursor() as cursor:
            sql = 'select * from product where id=%s;'
            cursor.execute(sql,str(id))
            datas = cursor.fetchone()
            
        return datas
    def update(self,product):
        with connection.cursor() as cursor:
            sql = '''UPDATE product SET productname=%s,brand_id_id=%s,rating=%s,category_id_id=%s,
                        price=%s,productimg=%s,description=%s where id=%s;'''
            cursor.execute(sql,product)
    def delete(self,did):
        with connection.cursor() as cursor:
            sql = '''DELETE FROM product where id=%s;'''
            cursor.execute(sql,str(did))
            
            