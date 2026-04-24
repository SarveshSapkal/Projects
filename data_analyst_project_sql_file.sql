-- Q.1. what is the total revenue genreated by male vs female customer
select gender, sum(purchase_amount) as total_spent from customer group by gender;

-- Q.2. which customers used a discount but still spent more than the avg purchase amount
select customer_id, purchase_amount from customer where discount_applied = 'Yes'
and purchase_amount >= (select avg(purchase_amount) from customer);

-- Q.3. which are the top 5 products with the highest avg review rating
select item_purchased, round(avg(review_rating),2) as review from customer
group by item_purchased 
order by review desc limit 5;

-- Q.4. compare the avg purchase amount between standerd and express shipping
select shipping_type, round(avg(purchase_amount),2) as 'avg apurchase amount' from customer
where shipping_type in ('standard','express') 
group by shipping_type;

-- Q.5. Do subscribed customer spend more ? compare avg spend and total revenue 
-- between subscribers and non subscribers
select subscription_status,count(customer_id) as 'total customer',
round(avg(purchase_amount),2) as 'average spend amount',
round(sum(purchase_amount),2) as 'total sales'
from customer 
group by subscription_status;

-- Q.6. which 5 products have the highest percentage of purchases with discount appliied ?
select item_purchased,
round(100*sum(case when discount_applied = 'Yes' then 1 else 0 end)/count(*),2) as discount_rate
from customer
group by item_purchased
order by discount_rate desc
limit 5;

-- Q.7. segment customers into new, returning, and loyal based on their total
-- number of previous purchases, and show the count of each segment

with customer_type as (
select customer_id, previous_purchases,
case 
when previous_purchases = 1 then 'New'
when previous_purchases between 2 and 10 then 'Returning'
else 'Loyal'
end as customer_segment
from customer)
select customer_segment, count(*) as 'Number of customers'
from customer_type
group by customer_segment;

-- Q.8. what are top 3 most purchased products within each category
with item_counts as(
select category,item_purchased,count(customer_id) as total_orders,
ROW_NUMBER() over(partition by category order by count(customer_id) DESC)
as item_rank from customer
group by category,item_purchased)

select item_rank, category, item_purchased,total_orders
from item_counts
where item_rank <=3;

-- Q.9. are customers who are repeat buyers (more than 5 previous purchases) also likely to subscribe ?
select subscription_status, count(customer_id) as repeat_buyers
 from customer 
 where previous_purchases > 5 
 group by subscription_status;

-- Q.10. what is the revenue contribution of each group
select age_group, sum(purchase_amount) as total_sales 
from customer 
group by age_group
order by total_sales desc; 

