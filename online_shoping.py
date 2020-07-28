from Online_shop.Shop import Shop
from Online_shop.Customers import Customers
from Online_shop.Discount import Discount
from Online_shop.Repository import Rep
from Online_shop.Order import Order
from Online_shop.Good import Good


class Main:
    shop = Shop('online shop')
    while True:
        rule = input()
        if rule == 'add':
            entry = input().lower()
            if entry == 'customer':
                customer_id = int(input())
                customer_name = input()
                customer = Customers(customer_name, customer_id)
                shop.addcustomers(customer)
                # print(shop.customerslist)

            elif entry == 'good':
                good_id = int(input())
                good_name = input()
                good_price = int(input())
                good_amount = int(input())
                good = Good(good_name, good_id, good_price)
                shop.setgood(good)
                shop.increamentGood(good, good_amount)
                # print(shop.goods)

            elif entry == 'repository':
                rep_id = int(input())
                rep_capacity = int(input())
                rep = Rep(rep_id, rep_capacity)
                shop.addrep(rep)
                # print(shop.reps)

            elif entry == 'order':
                order_id = int(input())
                order_customer_id = int(input())
                order = Order(order_id, order_customer_id)
                for j in range(len(shop.customerslist)):
                    if order_customer_id == shop.customerslist[j].id:
                        shop.customerslist[j].addorder(order)
                        # print(shop.customerslist[j].orderslist[0].id, 'order check')

            elif entry == 'balance':
                balance_customer_id = int(input())
                balance_settle = int(input())
                for j in range(len(shop.customerslist)):
                    if balance_customer_id == shop.customerslist[j].id:
                        shop.customerslist[j].setbalance(balance_settle)
                        # print(shop.customerslist[j].balance, 'check balance')

            elif entry == 'item':
                item_order_id = int(input())
                item_id = int(input())
                item_amount = int(input())
                for i in range(len(shop.customerslist)):
                    for j in range(len(shop.customerslist[i].orderslist)):
                        if item_order_id == shop.customerslist[i].orderslist[j].id:
                            for k in range(len(shop.goods)):
                                if item_id == shop.goods[k].id:
                                    shop.customerslist[i].orderslist[j].additem(shop.goods[k], item_amount)

            elif entry == 'discount':
                descount_id = int(input())
                descount_precentage = int(input())
                discont = Discount(descount_id, descount_precentage)
                shop.addDiscount(discont)

        elif rule == 'report':
            report_entry = input().lower()
            if report_entry == 'customers':
                for i in range(len(shop.customerslist)):
                    print(shop.customerslist[i].id, ',', shop.customerslist[i].name, ',', shop.customerslist[
                        i].balance, ','
                          , len(shop.customerslist[i].saved), ',', len(shop.customerslist[i].orderslist), "\n")

            elif report_entry == 'repositories':
                for i in range(len(shop.reps)):
                    print(shop.reps[i].id, ',', shop.reps[i].capacity, ',', shop.reps[i].getfreecap, '\n')

            elif report_entry == 'income':
                print(shop.income)

        elif rule == 'remove'.lower():
            if input() == 'item':
                orderid = int(input())
                itemid = int(input())
                for i in range(len(shop.customerslist)):
                    for j in range(len(shop.customerslist[i].orderslist)):
                        if orderid == shop.customerslist[i].orderslist[j]:
                            for k in range(len(shop.goods)):
                                if itemid == shop.goods[k]:
                                    shop.customerslist[i].orderslist[j].removeitem(shop.goods[k])

        elif rule == 'submit':
            submit_entry = input().lower()
            if submit_entry == 'order':
                submit_id = int(input())
                for i in range(len(shop.customerslist)):
                    for j in range(len(shop.customerslist[i].orderslist)):
                        if submit_id == shop.customerslist[i].orderslist[j]:
                            if shop.customerslist[i].balance >= shop.customerslist[i].orderslist[j].price:
                                for l in range(len(shop.customerslist[i].orderslist[j].orders)):
                                    for t in range(len(shop.reps)):
                                        for s in range(len(shop.reps.goods)):
                                            if shop.reps.goods[s].id == shop.customerslist[i].orderslist[j].orders[
                                                l].id:
                                                if shop.customerslist[i].orderslist[j].orders[l].value <= \
                                                        shop.reps.goods[s].value:
                                                    shop.customerslist[i].submitorder(
                                                        shop.customerslist[i].orderslist[j])
                                                    shop.reps[t].removegood(shop.reps.goods[s],
                                                                            shop.customerslist[i].orderslist[j].orders[
                                                                                l].value)
                                                    shop.customerslist[i].balance -= \
                                                        shop.customerslist[i].orderslist[j].orders[l].calculateprice
                                                    shop.income += shop.customerslist[i].orderslist[j].orders[
                                                        l].calculateprice

            elif submit_entry == 'discount':
                ord_id = int(input())
                discont_id = int(input())
                for i in range(len(shop.customerslist)):
                    for j in range(len(shop.customerslist[i].orderslist)):
                        if ord_id == shop.customerslist[i].orderslist[j].id:
                            for k in range(len(shop.discount)):
                                if shop.discount[k].id == discont_id:
                                    if not shop.customerslist[i].discounted:
                                        shop.customerslist[i].orderslist[j].adddiscount(shop.discount[k])
                                        shop.addDiscount(shop.discount[k])
                                        shop.customerslist[i].discounted = True

        elif rule == 'terminate':
            break
