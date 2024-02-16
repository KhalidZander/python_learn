from pyspark import SparkConf,SparkContext
import os
os.environ['PYSPARK_PYTHON']="E:/python/python.exe"


conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")

sc = SparkContext(conf=conf)


rdd = sc.parallelize([1,2,3,4,5])



sc.stop()