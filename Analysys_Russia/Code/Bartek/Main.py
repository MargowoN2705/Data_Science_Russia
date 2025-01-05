import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


russian_data = pd.read_csv("../../Russia_22_data_updated (1).csv")
consumptuon_data = pd.read_csv('../../Alkohol_Consumption.csv')
russian_data = russian_data.drop(columns=['Mapped_Region'])