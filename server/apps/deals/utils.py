import csv
import io

from django.contrib.postgres.aggregates import ArrayAgg
from django.db.models import Sum

from .constants import DealsTopCustomers
from .models import Deal


def object_for_response(queryset):
    customers_by_spent_money = queryset.values('customer').annotate(
        spent_money=Sum('total'),
        gems=ArrayAgg('item', distinct=True),
    ).order_by('-spent_money')[:DealsTopCustomers.TOP_CUSTOMERS]

    for row in customers_by_spent_money:
        current_customer_gems = row['gems']
        other_customers_gems = sum(
            [obj.get('gems') for obj in customers_by_spent_money
             if not (obj.get('customer') == row['customer'])], []
        )
        intersection_gems = list(
            set(current_customer_gems) & set(other_customers_gems)
        )
        row['gems'] = intersection_gems

    return {'response': customers_by_spent_money}


def parse_csv(file):
    deals_list = []

    decoded_file = file.read().decode()
    io_string = io.StringIO(decoded_file)
    reader = csv.reader(io_string)
    next(reader)

    for row in reader:
        deals_list.append(
            Deal(
                customer=row[0],
                item=row[1],
                total=row[2],
                quantity=row[3],
                date=row[4],
            )
        )

    return deals_list
