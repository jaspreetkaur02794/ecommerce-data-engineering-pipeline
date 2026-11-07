
import pandas as pd

def extract_sales_data(file_path):
    """
    Read raw e-commerce sales data from a CSV file.
    """
    try:
        df = pd.read_csv(file_path)

        print("Sales data extracted successfully!")
        print(f"Total records: {len(df)}")

        return df

    except FileNotFoundError:
        print("Error: Sales data file not found.")
        return None


if __name__ == "__main__":
    print("E-Commerce Data Pipeline Started")
