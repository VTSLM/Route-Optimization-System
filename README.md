# Intelligent Route Optimization System

An AI-powered logistics optimization platform that combines graph algorithms, machine learning, traffic-aware routing, and fleet optimization techniques to solve both single-vehicle and multi-vehicle routing problems.

---

# Project Overview

This project consists of two major modules:

## 1. Single Vehicle Route Optimization

Given a start location and destination, the system:

- Builds a road network using OSMnx
- Computes shortest paths using Dijkstra and A*
- Simulates traffic conditions
- Generates traffic-aware routes
- Predicts ETA using Machine Learning
- Compares shortest-distance and traffic-aware routes
- Visualizes routes on an interactive map

### Technologies Used

- OSMnx
- NetworkX
- Dijkstra Algorithm
- A* Search Algorithm
- FastAPI
- Streamlit
- Folium
- Scikit-Learn

---

## 2. Multi-Vehicle Fleet Routing

Given multiple delivery locations, the system:

- Generates delivery points
- Groups deliveries using K-Means Clustering
- Assigns deliveries to vehicles
- Optimizes each vehicle's route using TSP
- Calculates route statistics
- Estimates ETA and fuel consumption
- Visualizes fleet routes on a map

### Technologies Used

- K-Means Clustering
- Traveling Salesman Problem (TSP)
- Fleet Management
- Streamlit
- Folium

---

# Features

## Single Vehicle Routing

- Dijkstra Shortest Path
- A* Search
- Traffic-Aware Routing
- Dynamic Traffic Simulation
- Road Closure Simulation
- Accident Zone Simulation
- ETA Prediction
- Route Comparison Dashboard
- Interactive Map Visualization

## Multi Vehicle Routing

- Delivery Generation
- Vehicle Assignment
- K-Means Clustering
- TSP Route Optimization
- Fleet Analytics
- Fuel Consumption Estimation
- Fleet Dashboard
- Multi-Route Visualization

---

# Project Structure

```text
Route_Optimization_System/

│
├── algorithms/
│   ├── astar.py
│   ├── dijkstra.py
│   ├── tsp.py
│   ├── vehicle_clustering.py
│   └── route_optimizer.py
│
├── api/
│   ├── app.py
│   └── route_api.py
│
├── frontend/
│   ├── dashboard.py
│   └── fleet_dashboard.py
│
├── ml/
│   ├── dataset_generator.py
│   ├── traffic_model.py
│   └── traffic_dataset.csv
│
├── simulation/
│   ├── delivery_generator.py
│   ├── fleet_manager.py
│   ├── traffic_simulation.py
│   └── vehicle.py
│
├── utils/
│   ├── helpers.py
│   ├── fleet_metrics.py
│   └── fleet_analytics.py
│
├── visualization/
│   ├── fleet_visualization.py
│   ├── map_visualization.py
│   └── route_plot.py
│
├── main.py
├── main_fleet.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# System Architecture

## Single Vehicle Route Optimization

```text
Start Location
       ↓
Road Network (OSMnx)
       ↓
Traffic Simulation
       ↓
Traffic-Aware Graph
       ↓
Dijkstra / A*
       ↓
ETA Prediction
       ↓
Interactive Dashboard
```

---

## Multi Vehicle Fleet Routing

```text
Delivery Locations
        ↓
K-Means Clustering
        ↓
Vehicle Assignment
        ↓
TSP Optimization
        ↓
Fleet Analytics
        ↓
Fleet Dashboard
```

---

# Installation

## Step 1: Clone Repository

```bash
git clone https://github.com/VTSLM/Route-Optimization-System.git

cd Route-Optimization-System
```

---

## Step 2: Create Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Running the Project

---

## A. Train ETA Prediction Model

If the model has not been trained yet:

```bash
python ml/traffic_model.py
```

This generates and trains the ETA prediction model.

---

## B. Run Backend API

Open a terminal in the project root:

```bash
uvicorn api.app:app --reload
```

Backend starts at:

```text
http://127.0.0.1:8000
```

API documentation:

```text
http://127.0.0.1:8000/docs
```

---

## C. Run Single Vehicle Dashboard

Open a second terminal:

```bash
streamlit run frontend/dashboard.py
```

Dashboard opens at:

```text
http://localhost:8501
```

### Features Available

- Route Comparison
- Shortest Route
- Traffic-Aware Route
- ETA Prediction
- Distance Comparison
- Interactive Map

---

## D. Run Fleet Dashboard

Open another terminal:

```bash
streamlit run frontend/fleet_dashboard.py
```

### Features Available

- Delivery Generation
- Vehicle Assignment
- K-Means Clustering
- TSP Optimization
- Fleet Statistics
- Fleet Distance
- ETA Estimation
- Fuel Consumption
- Fleet Map Visualization

---

# Example Workflow

## Single Vehicle Routing

1. Enter source coordinates.
2. Enter destination coordinates.
3. Click "Compute Route".
4. Compare:
   - Shortest Route
   - Traffic-Aware Route
5. View:
   - Distance
   - ETA
   - Traffic Level
   - Route Visualization

---

## Fleet Routing

1. Select number of vehicles.
2. Select number of deliveries.
3. System automatically:
   - Generates deliveries
   - Clusters deliveries
   - Assigns vehicles
   - Optimizes routes
4. View:
   - Fleet Distance
   - ETA
   - Fuel Usage
   - Route Statistics
   - Fleet Map

---

# Machine Learning Module

The ETA prediction model is trained using:

### Features

- Distance
- Hour of Day
- Traffic Level
- Weather Condition

### Target

- ETA (Estimated Time of Arrival)

The model predicts travel time for routes under varying traffic conditions.

---

# Algorithms Implemented

## Graph Algorithms

- Dijkstra Algorithm
- A* Search Algorithm

## Optimization Algorithms

- Traveling Salesman Problem (Nearest Neighbor)
- K-Means Clustering

## Machine Learning

- ETA Prediction Model

---

# Future Improvements

- Real-world ETA dataset
- Real traffic APIs
- Weather API integration
- Vehicle Routing Problem (VRP)
- Traffic-aware fleet routing
- Dynamic rerouting
- Live GPS integration
- Fleet-wide optimization

---


## Route Comparison Dashboard

![Enter Coordinates](<Screenshot 2026-06-06 153341.png>)
![Route Statistics](<Screenshot 2026-06-06 153354.png>)
![Comparision](<Screenshot 2026-06-06 153412.png>)
## Fleet Dashboard
![Select number of vehicles and points](<Screenshot 2026-06-06 153646.png>)
![Route](<Screenshot 2026-06-06 153711.png>)


---

# Author

**Vatsal Mori**


Interests:
- Data Structures & Algorithms
- Artificial Intelligence
- Machine Learning
- Optimization
- Software Development

---
