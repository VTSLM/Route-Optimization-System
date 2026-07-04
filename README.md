# Intelligent Route Optimization System

An AI-powered logistics optimization platform that combines graph algorithms, machine learning, traffic-aware routing, and fleet optimization techniques to solve both single-vehicle and multi-vehicle routing problems on real-world road networks.

---

# Project Overview

The project consists of two major modules:

## 1. Single Vehicle Route Optimization

Given a source and destination, the system:

- Builds a real road network using OpenStreetMap
- Computes shortest and traffic-aware routes
- Simulates traffic conditions
- Predicts ETA using a Machine Learning model
- Compares multiple route metrics
- Displays the routes on an interactive map

### Technologies Used

- Python
- Streamlit
- OSMnx
- NetworkX
- Folium
- Scikit-Learn
- Pandas
- NumPy

---

## 2. Multi-Vehicle Route Optimization

Given multiple delivery locations, the system:

- Generates delivery points
- Groups deliveries using K-Means Clustering
- Assigns deliveries to vehicles
- Optimizes each vehicle's route using Traffic-Aware TSP
- Estimates ETA and fuel consumption
- Visualizes all vehicle routes on an interactive dashboard

### Technologies Used

- Python
- Streamlit
- OSMnx
- NetworkX
- K-Means Clustering
- Nearest Neighbor TSP
- Folium
- Scikit-Learn

---

# Features

## Single Vehicle Routing

- Real Road Network using OpenStreetMap
- Dijkstra Shortest Path
- Traffic-Aware Routing
- Traffic Simulation
- ETA Prediction using Machine Learning
- Route Comparison Dashboard
- Interactive Route Visualization

---

## Multi-Vehicle Routing

- Random Delivery Generation
- K-Means Delivery Clustering
- Vehicle Assignment
- Traffic-Aware Route Optimization
- ETA Prediction
- Fuel Consumption Estimation
- Fleet Statistics
- Interactive Fleet Dashboard
- Road-following Route Visualization

---

# Project Structure

```text
Route_Optimization_System/

│
├── algorithms/
│   ├── astar.py
│   ├── dijkstra.py
│   ├── route_optimizer.py
│   ├── traffic_route_cost.py
│   ├── tsp.py
│   └── vehicle_clustering.py
│
├── frontend/
│   ├── dashboard.py
│   └── fleet_dashboard.py
│
├── ml/
│   ├── train_real_eta_model.py
│   ├── real_eta_model.py
│   └── eta_model.pkl
│
├── simulation/
│   ├── delivery_generator.py
│   ├── fleet_manager.py
│   ├── rush_hour.py
│   ├── traffic_simulation.py
│   └── vehicle.py
│
├── utils/
│   ├── helpers.py
│   ├── route_service.py
│   ├── traffic_metrics.py
│   ├── fleet_metrics.py
│   ├── fleet_analytics.py
│   ├── fleet_analytics_summary.py
│   └── build_route_geometry.py
│
├── visualization/
│   ├── map_visualization.py
│   ├── route_plot.py
│   └── fleet_visualization.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# System Architecture

## Single Vehicle Route Optimization

```text
User Inputs Coordinates
          │
          ▼
Streamlit Dashboard
          │
          ▼
Route Service
          │
          ▼
OSMnx Road Network
          │
          ▼
Traffic Simulation
          │
          ▼
Shortest Route
Traffic-Aware Route
          │
          ▼
ETA Prediction Model
          │
          ▼
Interactive Map
```

---

## Multi Vehicle Route Optimization

```text
Generate Deliveries
        │
        ▼
K-Means Clustering
        │
        ▼
Vehicle Assignment
        │
        ▼
Traffic-Aware TSP
        │
        ▼
Road Geometry Generation
        │
        ▼
ETA & Fuel Estimation
        │
        ▼
Fleet Dashboard
```

---

# Installation

## 1. Clone the Repository

```bash
git clone https://github.com/VTSLM/Route-Optimization-System.git

cd Route-Optimization-System
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv myenv
```

Activate:

```bash
myenv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv myenv

source myenv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Running the Project

## Step 1 (Only Once): Train the ETA Model

If the trained model does not exist:

```bash
python ml/train_real_eta_model.py
```

---

## Step 2: Run Single Vehicle Dashboard

```bash
streamlit run frontend/dashboard.py
```

Features:

- Compare Shortest vs Traffic-Aware Route
- ETA Prediction
- Traffic Level
- Distance Comparison
- Interactive Map

---

## Step 3: Run Fleet Dashboard

```bash
streamlit run frontend/fleet_dashboard.py
```

Features:

- Delivery Generation
- Vehicle Assignment
- K-Means Clustering
- Traffic-Aware TSP
- ETA Prediction
- Fuel Consumption
- Fleet Statistics
- Fleet Route Visualization

---

# Example Workflow

## Single Vehicle Routing

1. Enter source coordinates.
2. Enter destination coordinates.
3. Click **Compute Route**.
4. Compare:
   - Shortest Route
   - Traffic-Aware Route
5. View:
   - Distance
   - ETA
   - Traffic Factor
   - Route Visualization

---

## Multi Vehicle Routing

1. Select number of vehicles.
2. Select number of deliveries.
3. Generate deliveries.
4. System automatically:
   - Clusters deliveries
   - Assigns deliveries to vehicles
   - Optimizes routes
   - Estimates ETA
   - Calculates fuel usage
5. View fleet statistics and interactive map.

---

# Machine Learning Module

The ETA Prediction model is trained using the NYC Taxi Trip Duration dataset.

### Features Used

- Route Distance
- Hour of Day
- Day of Week
- Traffic Factor

### Target

- Trip Duration (ETA)

Algorithm Used:

- Random Forest Regressor

The trained model predicts the estimated travel time for newly generated routes.

---

# Algorithms Used

## Graph Algorithms

- Dijkstra's Algorithm

## Optimization Algorithms

- K-Means Clustering
- Nearest Neighbor Traveling Salesman Problem (TSP)

## Machine Learning

- Random Forest Regression for ETA Prediction

---

# Tech Stack

| Category | Technologies |
|----------|--------------|
| Language | Python |
| Frontend | Streamlit |
| Maps | OSMnx, OpenStreetMap, Folium |
| Graph Processing | NetworkX |
| Machine Learning | Scikit-Learn |
| Data Processing | Pandas, NumPy |
| Model Storage | Joblib |
| Version Control | Git, GitHub |

---

# Future Improvements

- Integration with live traffic APIs
- Weather-aware route optimization
- Vehicle Routing Problem (VRP) solver
- Vehicle capacity constraints
- Time-window based deliveries
- Dynamic route re-optimization
- Live GPS tracking
- Reinforcement Learning based routing

---

# Screenshots

## Single Vehicle Dashboard

![Enter Coordinates](images/Screenshot%202026-06-06%20153341.png)

![Route Comparison](images/Screenshot%202026-06-06%20153354.png)

![Route Visualization](images/Screenshot%202026-06-06%20153412.png)

---

## Fleet Dashboard

![Fleet Dashboard](images/Screenshot%202026-06-06%20153646.png)

![Fleet Routes](images/Screenshot%202026-07-01%20164552.png)

---

# Developed By

**Vatsal Mori**
