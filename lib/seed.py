from models.hotel import Hotel
from models.customer import Customer
from models.review import Review

from models.__init__ import CONN, CURSOR

Hotel.create_table()
Customer.create_table()
Review.create_table()

CURSOR.execute("DELETE FROM hotels")
CURSOR.execute("DELETE FROM customers")
CURSOR.execute("DELETE FROM reviews")
CONN.commit()

Hotel.create("Marriott")
Hotel.create("Hampton Inn")
Hotel.create("Flatiron Resort")

Customer.create("Alice", "Baker")
Customer.create("Bruce", "Wayne")
Customer.create("Chris", "Jordan")

Review.create(5, "Best hotel ever!", 1, 1)
Review.create(4, "Pretty good hotel!", 1, 2)
Review.create(5, "Flatiron Resort is the best resort!", 3, 3)
Review.create(3, "Not as good as the last time.", 1, 1)