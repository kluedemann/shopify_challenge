SELECT * FROM shopify WHERE order_amount > 2000;

SELECT total_items, order_amount, COUNT(*) FROM shopify WHERE order_amount > 2000 GROUP BY total_items, order_amount;

SELECT created_at FROM shopify WHERE order_amount = 704000;