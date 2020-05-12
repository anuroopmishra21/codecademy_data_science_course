import codecademylib
import pandas as pd
visits = pd.read_csv('visits.csv',
                     parse_dates=[1])
cart = pd.read_csv('cart.csv',
                   parse_dates=[1])
checkout = pd.read_csv('checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('purchase.csv',
                       parse_dates=[1])
print(visits.head())
print(cart.head())
print(checkout.head())
print(purchase.head())
visits_cart = pd.merge(visits,cart,how='left')
null_cart_time = visits_cart[visits_cart.cart_time.isnull()]
percentage_v_to_c = float(len(null_cart_time))/len(visits_cart)
print(percentage_v_to_c)
cart_checkout = pd.merge(cart,checkout,how='left')
percentage_c_to_co = float(len(cart_checkout[cart_checkout.checkout_time.isnull()]))/len(cart_checkout)
print(percentage_c_to_co)
all_data = visits.merge(cart,how='left').merge(checkout,how='left').merge(purchase,how='left')
print(all_data.head())
checkout_purchase = pd.merge(checkout,purchase,how='left')
percentage_co_to_p = float(len(checkout_purchase[checkout_purchase.purchase_time.isnull()]))/len(checkout_purchase)
print(percentage_co_to_p)
all_data['time_to_purchase'] = all_data.purchase_time - all_data.visit_time
print(all_data.time_to_purchase)
average_time_to_purchase = all_data.time_to_purchase.mean()
print(average_time_to_purchase)
