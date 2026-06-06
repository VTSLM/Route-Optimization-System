from sklearn.cluster import KMeans


def cluster_deliveries(deliveries, num_vehicles):

    kmeans = KMeans(n_clusters=num_vehicles, random_state=42)

    labels = kmeans.fit_predict(deliveries)

    clusters = {}

    for i in range(num_vehicles):
        clusters[i] = []

    for point, label in zip(deliveries, labels):
        clusters[label].append(point)

    return clusters
