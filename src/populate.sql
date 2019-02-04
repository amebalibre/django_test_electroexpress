-- PRODUCTS
INSERT INTO ecommerce_product(name, price, type, stock, inclusion_date) VALUES('Sambusng Galaxy Tab A 10.1 2016 32GB', 179, 'T', 0, '2016-02-02');
INSERT INTO ecommerce_product(name, price, type, stock, inclusion_date) VALUES('Bq Aquaris M 10 10.1 16GB HD Blanca', 155, 'T', 13, '2018-12-12');
INSERT INTO ecommerce_product(name, price, type, stock, inclusion_date) VALUES('Xiaomi Redmi Note 6 Pro 4/64Gb Negro Libre', 219, 'M', 3, '2017-01-13');
INSERT INTO ecommerce_product(name, price, type, stock, inclusion_date, discontinued_date) VALUES('Aple iPhone 5S 16GB REWARE Refurbished Gris Espacial Libre', 139, 'M', 2, '2015-11-30', '2019-01-20');

-- PROMOS
INSERT INTO ecommerce_promo(code, type, value, active) VALUES('TEN10', 'P', 10, true);
INSERT INTO ecommerce_promo(code, type, value, active) VALUES('MISEUROS', 'C', 5, true);
