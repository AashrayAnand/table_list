# Table List

## Simple webapp for viewing library room bookings

Webscrapes the University of Washington LibCal website for all bookings in **Odegaard Undergraduate Library** reserved by our fraternity.

Runs a _case-insensitive_ check for all rooms booked under the name "paphi" and populates a **SQLite** database.

Using **React**, **Redux**, and **AJAX**, neatly displays all matches on a remotely hosted **DigitalOcean** server.

![table_list](./table_list.png)