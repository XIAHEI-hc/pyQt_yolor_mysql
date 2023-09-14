import numpy as np
import pymysql
import matplotlib.pyplot as plt
import datetime

# Step 1: Generate sin waveform
x = np.linspace(0, 2 * np.pi, 10000)
y = np.sin(x)

# Generate timestamps
start_time = datetime.datetime.now()
timestamps = [(start_time + datetime.timedelta(seconds=i*0.1)) for i in range(10000)]

conn = pymysql.connect(host='111.230.38.189', user='root', password='@y1a4n7g8ok0')
cursor = conn.cursor()

# 创建数据库（如果不存在的话）
cursor.execute("CREATE DATABASE IF NOT EXISTS timedata CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")

# 选择数据库
cursor.execute("USE timedata")

# Create a table to store waveform with timestamp
cursor.execute("CREATE TABLE IF NOT EXISTS sin_wave_with_time (timestamp DATETIME, x DOUBLE, y DOUBLE)")

# Insert waveform data into the database
values = [(t, xi, yi) for t, xi, yi in zip(timestamps, x, y)]
cursor.executemany("INSERT INTO sin_wave_with_time (timestamp, x, y) VALUES (%s, %s, %s)", values)

conn.commit()
cursor.close()
conn.close()
