ontime = spark.read.format('csv').options(
	header='true', inferschema='true').load("/mnt/on_time/*.csv")
	
ontime.write.mode("append").parquet("/mnt/on_time/parquet/flights")
print("Done")
