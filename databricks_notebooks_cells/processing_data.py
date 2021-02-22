ontime_data = spark.read.format('csv').options(
  header='true', infraschema='true').load("/mnt/on_time/On_Time_Marketing_Carrier_On_Time_Performance_(Beginning_January_2018)_2018_1.csv")

ontime_data.write.parquet('/mnt/on_time/parquet/data_5')

flightDF = spark.read.format('parquet').options(header='true',infraschema='true').load("/mnt/on_time/parquet/flights")

ontime_data.printSchema()
flightDF.printSchema()

print("NUmber of Flight: ",flightDF.count())

ontime_data.show(100, False)
flightDF.show(20, False)

display(flightDF)
