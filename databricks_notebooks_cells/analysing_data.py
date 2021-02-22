flightTable = spark.read.parquet('/mnt/on_time/parquet/flights')
flightTable.createOrReplaceTempView('flightTable')

out1 = spark.sql("select * from flightTable where Month=0 and Year= 2018")
out2 = spark.sql("select * from flightTable where Month=2 and Year= 2018")
total = out1.count()+out2.count()
print(total)
