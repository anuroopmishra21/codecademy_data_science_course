def gs_cost(weight):
  if weight<=2:
    return 1.50*weight+20.00
  elif weight>2 and weight<=6:
    return 3.00*weight+20.00
  elif weight>6 and weight<=10:
    return 4.00*weight+20.00
  else:
    return 4.75*weight+20.00
p=125.00
def drone_cost(weight):
  if weight<=2:
    return 4.50*weight
  elif weight>2 and weight<=6:
    return 9.00*weight
  elif weight>6 and weight<=10:
    return 12.00*weight
  else:
    return 14.25*weight
def cheapest(weight):
  g=gs_cost(weight)
  d=drone_cost(weight)
  if g<=p and g<=d:
    print("The ground shipping method will be cheapest with a cost of "+str(g))
  elif d<=p and d<=g:
    print("The drone shipping method will be cheapest with a cost of "+str(d))
  else:
    print("The premium ground shipping method will be cheapest with a cost of "+str(p))
cheapest(4.8)
cheapest(41.5)
