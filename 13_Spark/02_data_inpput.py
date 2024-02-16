from pyspark import SparkConf,SparkContext

conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")

sc = SparkContext(conf=conf)

rdd1 = sc.parallelize([1,2,3,4,5])
rdd2 = sc.parallelize((1,2,3,4,5))
rdd3 = sc.parallelize("abc") # 字符串拆分成char
rdd4 = sc.parallelize({1,2,3,4,5})
rdd5 = sc.parallelize({"key1":"value1"}) # 字典只保留key

print(rdd1.collect())
print(rdd2.collect())
print(rdd3.collect())
print(rdd4.collect())
print(rdd5.collect())

rdd6 = sc.textFile("./13_spark/02_hello.txt")
print(rdd6.collect())

sc.stop()