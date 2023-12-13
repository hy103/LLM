few_shots = [{'Question': 'How many t-shirts do we have left for Nike in M size and white color?',
  'SQLQuery': "SELECT sum(stock_quantity) FROM t_shirts WHERE brand = 'Nike' AND color = 'White' AND size = 'M'",
  'SQLResult': 'Result of the SQL query',
  'Answer': '1'},
 {'Question': 'How much is the total price of the inventory for all S-size t-shirts?',
  'SQLQuery': "SELECT SUM(price*stock_quantity) FROM t_shirts WHERE size = 'S'",
  'SQLResult': 'Result of the SQL query',
  'Answer': '16894'},
 {'Question': 'If we have to sell all the Levi’s T-shirts today with discounts applied. How much revenue  our store will generate (post discounts)?',
  'SQLQuery': "select sum((t.t_shirts_price * (100.00 - d.pct_discount)/100)) as total_rev_post_discount from discounts d \n     left join (select (price*stock_quantity) as t_shirts_price, t_shirt_id from t_shirts where brand = 'Levi') t on d.t_shirt_id = t.t_shirt_id\n ",
  'SQLResult': 'Result of the SQL query',
  'Answer': '5571.50'},
 {'Question': 'If we have to sell all the Levi’s T-shirts today. How much revenue our store will generate without discount?',
  'SQLQuery': "SELECT SUM(price * stock_quantity) FROM t_shirts WHERE brand = 'Levi'",
  'SQLResult': 'Result of the SQL query',
  'Answer': '19249'},
 {'Question': "How many white color Levi's shirt I have?",
  'SQLQuery': "SELECT sum(stock_quantity) FROM t_shirts WHERE brand = 'Levi' AND color = 'White'",
  'SQLResult': 'Result of the SQL query',
  'Answer': '142'}]