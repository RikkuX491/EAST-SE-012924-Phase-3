.mode column

SELECT customers.id, customers.first_name, customers.last_name
FROM customers
INNER JOIN reviews
ON customers.id = reviews.customer_id
INNER JOIN hotels
ON hotels.id = reviews.hotel_id
WHERE hotels.id = 1
GROUP BY customers.id;