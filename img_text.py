#%%
import numpy as np
from skimage import transform
import pandas as pd
import cv2

data = pd.read_csv("comma_delimited_stock_prices.csv")
data.info()
data.describe()
data.head()
print(data)

# %%
import csv

with open("comma_delimited_stock_prices.csv", "r") as file:
    reader = csv.reader(file, delimiter=",")

for row in reader:
    print(row)

# %%
single_image = cv2.imread("img.jpg")

print(type(single_image))
print(single_image.shape)

single_image = cv2.resize(single_image,(150,150))
print(single_image.shape)

gray_image = cv2.cvtColor(single_image, cv2.COLOR_RGB2GRAY)
print(gray_image.shape)

flipped_image = np.fliplr(gray_image)

rotated_image = transform.rotate(single_image, angle=45)
cv2.imshow('image', flipped_image)
cv2.waitKey(0)
# %%