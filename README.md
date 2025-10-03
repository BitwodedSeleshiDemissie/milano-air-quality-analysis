# 🌆 Milano Air Quality Analysis  

![Daily Average Pollutants](figures/daily_average.png)  
![Monthly Average Pollutants](figures/monthly_average.png)  

---

## 📊 Project Overview  
This project analyzes **air quality data from Milano** using open datasets from Regione Lombardia.  
We explore pollutant trends (PM10, NO2, O3), detect "bad air days", and build a simple forecast for PM10.  

The project combines **exploratory data analysis** with **time-series modeling** to extract insights that can support **public health and urban policy planning**.  

---

## 🧮 Methodology  

1. **Time-Series Aggregation**  
   - Compute **daily averages**:  
     \[
     \bar{x}_{d} = \frac{1}{n_d} \sum_{i=1}^{n_d} x_i
     \]  
   - Compute **monthly averages**:  
     \[
     \bar{x}_{m} = \frac{1}{n_m} \sum_{i=1}^{n_m} x_i
     \]  

2. **Threshold Detection (Bad Air Days)**  
   - Define “bad air day” for **PM10 > 50 µg/m³**:  
     \[
     \text{BadDay} =
     \begin{cases}
     1 & \text{if PM10} > 50 \\
     0 & \text{otherwise}
     \end{cases}
     \]  

3. **Distribution Analysis**  
   - Histograms approximate probability density:  
     \[
     p(x) \approx \frac{\text{count in bin}}{N \cdot \Delta x}
     \]  

4. **Forecasting (Autoregressive Modeling)**  
   - Use AR model for PM10 trends:  
     \[
     x_t = c + \phi_1 x_{t-1} + \phi_2 x_{t-2} + \dots + \phi_p x_{t-p} + \epsilon_t
     \]  

---

## 📂 Dataset  
- Source: [Regione Lombardia – Dati sensori aria](https://www.dati.lombardia.it/Ambiente/Dati-sensori-aria/nicp-bhqi/about_data)  
- File: `data/air_quality.csv` (not included in repo due to size, please download from the link above)  

---

## 🛠️ How to Run  

1. Create a virtual environment:  
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows
