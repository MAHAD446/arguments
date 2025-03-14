def total_calc(bill_amount,tip_perc):
#define function to calculate the tip on the bill
  total = bill_amount*(1 + 0.01*tip_perc)
  total = round(total,2)
  print(f"please pay ${total}")

  # spesify only bill_amount
  # default value to tip percentage is 
 
   
total_calc(150,20)
