# 🚗 Vehicle Sales Data Analysis App

This Streamlit web application provides an interactive platform to explore and visualize a dataset of vehicle sales listings. It allows users to quickly preview the raw data and generate various plots with simple button clicks and checkbox selections.

---

## ✨ Features

* **Dataset Preview:** View the first 10 rows of the cleaned vehicle data.
* **Interactive Histograms:**
    * Distribution of vehicle **prices**.
    * Distribution of **odometer** readings.
* **Stacked Bar Chart:** Visualize the **count of vehicles by manufacturer**, with a breakdown by individual **model**.
* **Scatter Plot:** Explore the relationship between **price and model year**, colored by **vehicle condition**.
* **Box Plot:** Analyze **price distribution across different vehicle types**.

---

## 🚀 How to Run the App

Follow these steps to get the Vehicle Sales Data Analysis App up and running on your local machine.

### Prerequisites

Before you start, make sure you have:

* **Python 3.8+** installed.
* **pip** (Python package installer) installed.
* **Git** (optional, if cloning the repository).

### Setup Instructions

1.  **Clone the Repository (if applicable) or Download the Project:**
    If your project is hosted on GitHub, use Git to clone it:
    ```bash
    git clone <your-repository-url>
    cd vehicles_us
    ```
    Otherwise, ensure you have the `vehicles_us` folder containing `app.py` and the `notebooks` folder (with `vehicles_us.csv` inside it). Navigate to your `vehicles_us` directory:
    ```bash
    cd /path/to/your/vehicles_us
    ```

2.  **Create a Virtual Environment (Recommended):**
    It's best practice to use a virtual environment to manage dependencies and avoid conflicts with other Python projects.
    ```bash
    python -m venv .venv
    ```

3.  **Activate the Virtual Environment:**

    * **On Windows (PowerShell):**
        ```powershell
        .\.venv\Scripts\Activate.ps1
        ```
    * **On Windows (Command Prompt):**
        ```cmd
        .venv\Scripts\activate.bat
        ```
    * **On macOS/Linux:**
        ```bash
        source .venv/bin/activate
        ```
    You'll know it's active when `(.venv)` appears at the beginning of your terminal prompt.

4.  **Install Dependencies:**
    With your virtual environment active, install the required libraries:
    ```bash
    pip install pandas plotly streamlit
    ```

5.  **Run the Streamlit App:**
    Once all dependencies are installed, you can launch the application:
    ```bash
    streamlit run app.py
    ```
    Your web browser should automatically open to the Streamlit app (usually at `http://localhost:8501`).

---

## 📊 Data Source

The application uses the `vehicles_us.csv` dataset, which is expected to be located in the `notebooks/` subdirectory relative to `app.py`.

* **Path:** `vehicles_us/notebooks/vehicles_us.csv`

---

## 🛠️ Technologies Used

* **Streamlit:** For building the interactive web application.
* **Pandas:** For data loading, cleaning, and manipulation.
* **Plotly Express:** For generating interactive and aesthetically pleasing data visualizations.

---

## ✍️ Author

[DonnieFV]

---