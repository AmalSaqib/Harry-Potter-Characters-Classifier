import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
import tensorflow_datasets as tfds

from tensorflow.keras import layers


import os

input_dir = "./dataset/train"

for folders in os.listdir(input_dir):
    folder = os.path.join(input_dir, folders)
    for files in os.listdir(folder):
        