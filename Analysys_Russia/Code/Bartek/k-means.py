import os
os.environ['LOKY_MAX_CPU_COUNT'] = '4'

from Analysys_Russia.Code.Bartek.Main import russian_data, pd, np, sns, plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

print(russian_data.columns)

# --- First Clustering (Alcohol Consumption) ---
features = ['Vodka', 'Liqueurs', 'Beer',
            'Total alcohol consumption (in liters of pure alcohol per capita)']

data_selected = russian_data[features]
data_selected = data_selected.dropna()
russian_data_clean = russian_data.loc[data_selected.index]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(data_selected)

kmeans = KMeans(n_clusters=3, random_state=42)
russian_data_clean['Cluster'] = kmeans.fit_predict(X_scaled)

pca = PCA(n_components=2)
pca_result = pca.fit_transform(X_scaled)

plt.figure(figsize=(10, 7))
scatter = plt.scatter(pca_result[:, 0], pca_result[:, 1], c=russian_data_clean['Cluster'], cmap='coolwarm', alpha=1, edgecolors='black', s=100)
plt.xlabel('PC1 - Vodka, Liqueurs, Beer, Consumption', fontsize=14)
plt.ylabel('PC2 - Vodka, Liqueurs, Beer, Consumption', fontsize=14)
plt.title('KMeans Clustering – Alcohol Consumption in Russian Regions (Vodka, Liqueurs, Beer, Total Consumption)', fontsize=16)
plt.grid(True)
plt.show()

# --- Second Clustering (GRDP, Density, Population, Salary) ---
features = ['GRDP_per_capita', 'Salary','Density',"GRDP",'population ']

data_selected = russian_data[features]
data_selected = data_selected.dropna()
russian_data_clean = russian_data.loc[data_selected.index]

russian_data_clean = russian_data_clean[russian_data_clean['Density'] < 1500]
russian_data_clean = russian_data_clean[russian_data_clean['Salary'] < 125]

scaler = StandardScaler()
data_selected_clean = russian_data_clean[features]
X_scaled = scaler.fit_transform(data_selected_clean)

wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, random_state=10)
    kmeans.fit(X_scaled)
    wcss.append(kmeans.inertia_)

plt.plot(range(1, 11), wcss, marker='o', linestyle='-', color='b')
plt.xlabel('Number of Clusters', fontsize=14)
plt.ylabel('WCSS (Within-Cluster Sum of Squares)', fontsize=14)
plt.title('Elbow Method for Optimal Number of Clusters', fontsize=16)
plt.grid(True)
plt.show()

kmeans = KMeans(n_clusters=3, random_state=200)
russian_data_clean['Cluster'] = kmeans.fit_predict(X_scaled)

pca = PCA(n_components=2)
pca_result = pca.fit_transform(X_scaled)

plt.figure(figsize=(10, 7))
scatter = plt.scatter(pca_result[:, 0], pca_result[:, 1], c=russian_data_clean['Cluster'], cmap='coolwarm', alpha=1, edgecolors='black', s=100)
plt.xlabel('PC1 - (GRDP, Density, Population, Salary)', fontsize=14)
plt.ylabel('PC2 - (GRDP, Density, Population, Salary)', fontsize=14)
plt.title('KMeans Clustering – GRDP, Density, Population, Salary in Russian Regions', fontsize=16)
plt.grid(True)
plt.show()

# --- Third Clustering (Density, GRDP per capita) ---

features = ['Density', 'GRDP_per_capita']

data_selected = russian_data[features]
data_selected = data_selected.dropna()
russian_data_clean = russian_data.loc[data_selected.index]

russian_data_clean = russian_data_clean[russian_data_clean['Density'] < 1500]
russian_data_clean = russian_data_clean[russian_data_clean['Salary'] < 125]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(data_selected.loc[russian_data_clean.index])

kmeans = KMeans(n_clusters=3, random_state=42)
russian_data_clean['Cluster'] = kmeans.fit_predict(X_scaled)

pca = PCA(n_components=2)
pca_result = pca.fit_transform(X_scaled)

plt.figure(figsize=(10, 7))
scatter = plt.scatter(pca_result[:, 0], pca_result[:, 1], c=russian_data_clean['Cluster'], cmap='coolwarm', alpha=1, edgecolors='black', s=100)
plt.xlabel('PC1 - Density, GRDP per capita', fontsize=14)
plt.ylabel('PC2 - Density, GRDP per capita', fontsize=14)
plt.title('KMeans Clustering – Density and GRDP per capita in Russian Regions', fontsize=16)
plt.grid(True)
plt.show()
