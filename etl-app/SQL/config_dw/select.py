import duckdb

# Kết nối với database
con = duckdb.connect(database='/home/anhcu/Final_ETL_App/etl-app/datawarehouse.duckdb')

con.sql("Select * from dim_companies;").show()
con.sql("Select count(*) from dim_companies;").show()
con.sql("Select * from dim_time;").show()
con.sql("Select count(*) from dim_time;").show()
con.sql("Select * from dim_news;").show()
con.sql("Select count(*) from dim_news;").show()
con.sql("Select * from dim_topics;").show()
con.sql("Select count(*) from dim_topics;").show()
con.sql("Select * from fact_candles;").show()
con.sql("Select count(*) from fact_candles;").show()
con.sql("Select * from fact_news_companies;").show()
con.sql("Select count(*) from fact_news_companies;").show()
con.sql("Select * from fact_news_topics;").show()
con.sql("Select count(*) from fact_news_topics;").show()