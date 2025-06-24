create database WedWise;
use Wedwise;

CREATE TABLE venues_data (
    venue_name VARCHAR(255),
    venue_type VARCHAR(100),
    ratings DECIMAL(2, 1),
    reviews INT,
    menu_price decimal,
    rooms INT,
    pax_min INT,
    pax_max INT,
    destination VARCHAR(100),
    amenities INT
);


select * from venues_data;


SET GLOBAL local_infile = 1;
SHOW GLOBAL VARIABLES LIKE 'local_infile';
SHOW VARIABLES LIKE 'secure_file_priv';

LOAD DATA INFILE "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Venues_data.csv"
INTO TABLE venues_data
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(venue_name, venue_type, ratings, reviews, menu_price, rooms, pax_min, pax_max, destination,amenities);


select count(*) from venues_data;



# 1. Top Rated Venues In Each City

SELECT venue_name, destination,ratings
FROM venues_data v
WHERE ratings = (
    SELECT MAX(ratings)
    FROM venues_data
    WHERE destination = v.destination
);


# 2. Venues with Above-Average Price

SELECT venue_name, venue_type, menu_price
FROM venues_data v
WHERE menu_price > (
    SELECT AVG(menu_price)
    FROM venues_data
    WHERE destination = v.destination
);

# 3.Venue types that have more than 10 venues with a rating above 4.5 (i.e., premium) across all cities
SELECT venue_type, COUNT(*) AS premium_count,ratings
FROM venues_data
WHERE ratings > 4.5
GROUP BY venue_type,ratings
HAVING COUNT(*) > 10;

# 4.Venue with Maximum Capacity in Each State
SELECT venue_name, destination,rooms, pax_max
FROM venues_data v
WHERE rooms = (
    SELECT MAX(rooms)
    FROM venues_data
    WHERE destination = v.destination
);

# 5. 2nd Most Expensive Venue per City
SELECT destination, venue_name, menu_price
FROM (
    SELECT *,
           DENSE_RANK() OVER (PARTITION BY destination ORDER BY menu_price DESC) as price_rank
    FROM venues_data
) ranked
WHERE price_rank = 2;


# 6. Find the top 10 most expensive venues (based on menu_price) across all destinations. Show their venue name, destination, and price.
SELECT venue_name, destination, menu_price
FROM venues_data
ORDER BY menu_price DESC
LIMIT 10;


# 7. Unique Venue Count per City (Window Function)
SELECT DISTINCT destination, total_venues
FROM (
    SELECT 
        destination,
        COUNT(*) OVER (PARTITION BY destination) AS total_venues
    FROM venues_data
) sub;



# 8. Top 3 Most Reviewed Venues in Each State
SELECT venue_name, reviews, destination
FROM (
    SELECT *,
           ROW_NUMBER() OVER (PARTITION BY destination ORDER BY reviews DESC) AS rn
    FROM venues_data
) ranked
WHERE rn <= 3;


# 9. Find the top 2 most expensive venues in each destination based on menu price.
SELECT venue_name, destination, menu_price, price_rank
FROM (
    SELECT *,
           RANK() OVER (PARTITION BY destination ORDER BY menu_price DESC) AS price_rank
    FROM venues_data
) ranked
WHERE price_rank <= 2;



