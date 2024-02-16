from pyspark import SparkConf,SparkContext
import os
os.environ['PYSPARK_PYTHON']="E:/python/python.exe"


conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")

sc = SparkContext(conf=conf)


rdd = sc.parallelize([1,2,3,4,5])

def func(data):
    return data*10

rdd2=rdd.map(func)

print(rdd2.collect())

rdd3 = rdd2.map(lambda x: x*10)

print(rdd3.collect())

sc.stop()