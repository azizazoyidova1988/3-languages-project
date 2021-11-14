from django.db import connection
from contextlib import closing


def get_products(CODE):
    with closing(connection.cursor()) as cursor:
        cursor.execute(f"""select name_{CODE} as name,image from product """)
        posts = dict_fetchall(cursor)
        return posts


def get_testimonials(CODE):
    with closing(connection.cursor()) as cursor:
        cursor.execute(f"""select name_{CODE} as name, description_{CODE} as description,image from testimonial """)
        testimonials = dict_fetchall(cursor)
        return testimonials


def get_experts(CODE):
    with closing(connection.cursor()) as cursor:
        cursor.execute(f"""select name_{CODE} as name,image from expert """)
        commenter = dict_fetchall(cursor)
        return commenter



def dict_fetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def dict_fetchone(cursor):
    row = cursor.fetchone()
    if row is None:
        return False
    columns = [col[0] for col in cursor.description]
    return dict(zip(columns, row))
