CREATE DATABASE ecommerce;
USE ecommerce;

-- Count how many orders exist for each order_status. Sort by count highest first.
select order_status,count(order_id) as order_count from orders group by order_status order by order_count desc;
select customer_id ,min(order_purchase_timestamp) as first_order,max(order_purchase_timestamp) as last_order
 from orders where order_status = "delivered" group by customer_id ;
 
 -- LAG() to find gap between purchases
 
 with order_timeline as (
 select customer_id, order_purchase_timestamp,
 lag(order_purchase_timestamp) over(partition by customer_id order by order_purchase_timestamp) as previous_timestamp
 from orders where order_status = "delivered"
 )select customer_id,order_purchase_timestamp,previous_timestamp,DATEDIFF(order_purchase_timestamp,previous_timestamp)AS days_since_last_order
 from order_timeline; 
 
 --  Identify Churned Customers
 
 with churned_customer as (
 select customer_id,max(order_purchase_timestamp) as last_order from orders where order_status = "delivered" group  by customer_id
 )select customer_id , last_order ,case 
 when datediff((select max(order_purchase_timestamp) from orders where order_status = "delivered"),last_order)>90 then "churned"
 else "active"
 end as status from churned_customer;

with churned_customer as(
select customer_id,last_order, case when datediff((select max(order_purchase_timestamp) from orders where order_status = "delivered"),
last_order)>90 then "churned" else "active" end as status from
(select customer_id, max(order_purchase_timestamp) as last_order from orders where order_status ="delivered" group by customer_id
) base),
churn_summary as(
select count(*) as total_customer,
sum(case when status = "churned" then 1 else 0 end ) as churned_customer from churned_customer
)select total_customer,churned_customer,round(churned_customer *100/total_customer,2) as churn_rate from churn_summary;

-- Revenue Analysis (JOIN with payments)


select o.order_id,p.payment_value from orders o left join payments p on o.order_id=p.order_id limit 10;

with churned_customer as(
select customer_id, last_order,case 
when datediff((select max(order_purchase_timestamp) as last_order from orders where order_status = "delivered"),last_order)>90 then 
"churned" else "active"
end as status from 
(select customer_id,max(order_purchase_timestamp) as last_order from orders where order_status = "delivered" group by customer_id)base)
select c.status,
count(distinct o.customer_id) as total_customer,round(sum(p.payment_value)) as total_revnue from orders o left join payments p
 on o.order_id = p.order_id
 left join churned_customer c on o.customer_id = c.customer_id
where order_status = "delivered" group by c.status;

--  State wise churn using the customers table.
-- -------------writitng churned customer cte again and again to pratice ----------------
with churned_customer as(
select customer_id, last_order,
case when datediff((select max(order_purchase_timestamp) as last_order from orders where order_status = "delivered"),last_order)>90 then
"churned"   
end as status from (select customer_id, max(order_purchase_timestamp) as last_order from orders where order_status = "delivered" 
group by customer_id)base)
select cu.customer_state,count(*) as total_customer,count(case when cc.status = "churned" then 1 end) as churned_count,
round(count(case when cc.status="churned" then 1 end)*100/count(*),2) as churn_rate from churned_customer cc
left join customers cu on cc.customer_id = cu.customer_id group by customer_state order by churn_rate desc;

-- Which month had the most orders?
select date_format(order_purchase_timestamp,'%Y-%m') as months,count(order_id) as count_order from orders
 where order_status = "delivered" group by months order by months asc;
 
 -- Month over Month Growth % using LAG()
 with monthly_orders as(
 select date_format(order_purchase_timestamp,'%Y-%m')as months ,count(order_id) as count_order 
 from orders where order_status = "delivered" group by months order by months asc
 )select months,count_order,lag(count_order) over(order by months) as previous_month,
round((count_order-lag(count_order) over (order by months))*100/lag(count_order) over (order by months),2) as growth_pct
from monthly_orders;

-- Top 10 Cities by Revenue
select sum(p.payment_value) as revnue, c.customer_city from orders o left join payments p on o.order_id = p.order_id
left join customers c on o.customer_id = c.customer_id where order_status = "delivered" group by customer_city order by revnue desc limit 10  ;

-- Average order value per state
select round(avg(p.payment_value),2) as order_value,c.customer_state from orders o 
left join customers c on o.customer_id=c.customer_id 
left join payments p on o.order_id = p.order_id
where order_status ="delivered" group by customer_state ;

-- Payment type breakdown
select count(distinct o.order_id) as total_order, p.payment_type,sum(p.payment_value) as revnue,
round(sum(payment_value)*100/(select sum(payment_value) from payments),2) as percent_revnue from orders o left join payments p on o.order_id = p.order_id
group by payment_type