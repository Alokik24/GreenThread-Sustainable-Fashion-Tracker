# GreenThread: Sustainable Fashion Tracker

** Please go through the report for more details. I am currently working on deploying the project **

**GreenThread** is an open-source platform designed to empower consumers with transparent, data-driven insights into the environmental impact of fashion brands. It aggregates sustainability metrics, visualizes environmental footprints, and recommends eco-friendly alternatives.

---

## Problem Statement
The fashion industry is a major contributor to carbon emissions, excessive water usage, and waste production. Consumers lack accessible tools to compare and evaluate brands based on their environmental practices. **GreenThread** addresses this gap by providing a comprehensive, data-driven solution for responsible consumption and informed decision-making.

---

## Technical Features
- **Sustainable Brands Database**: A curated collection of ~5,000 brands with 25+ key environmental metrics (carbon footprint, water usage, waste production, sustainability scores).
- **Brand Name Generator**: A Python-based utility that generates culturally diverse, creative brand identifiers using multilingual word combinations.
- **Recommendation Engine**: Leverages KMeans clustering and Euclidean distance to suggest similar sustainable brands.
- **Impact Calculator**: Computes user-specific environmental impact (carbon, water, waste) based on purchase scenarios.
- **Data Visualizations**: Dynamic charts and graphs (Matplotlib, Seaborn) for trend analysis, brand comparisons, and impact insights.

---

## Architecture & Tech Stack
- **Backend**: Python, Flask
- **Database**: MongoDB (accessed via PyMongo)
- **Data Processing**: Pandas, NumPy, SciPy
- **Machine Learning**: scikit-learn (KMeans clustering)
- **Visualization**: Matplotlib, Seaborn
- **Frontend**: HTML, CSS, JavaScript, Bootstrap

---

## Database & Data Model
- **Collection**: `brands`
- **Key Fields**:
  - `brand_id` (String)  
  - `name` (String)  
  - `sustainability_score` (Float)  
  - `carbon_footprint` (Float)  
  - `water_usage` (Float)  
  - `waste_production` (Float)  
  - `certifications` (Array[String])  
  - `recycling_program` (Boolean)  
  - `material_types` (Array[String])  
  - `market_trends` (String)

---

## Machine Learning Model
- **Clustering Process**:
  1. Scale numeric sustainability metrics.  
  2. Apply KMeans to group brands with similar profiles.  
  3. Calculate Euclidean distances within clusters to identify nearest neighbors.  
- **Outcome**: A ranked list of alternative brands with comparable environmental footprints.

---

*This project is currently in development and not yet deployed.*
