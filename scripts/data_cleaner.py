import pandas as pd
import os

def clean_and_consolidate(input_dir, output_path):
    all_data = []
    for file in os.listdir(input_dir):
        if file.endswith('.xlsx') or file.endswith('.xls'):
            file_path = os.path.join(input_dir, file)
            df = pd.read_excel(file_path)
            df = df.dropna(how='all')
            df.columns = [c.strip().lower().replace(' ', '_') for c in df.columns]
            all_data.append(df)
    
    if all_data:
        master_df = pd.concat(all_data, ignore_index=True)
        master_df.to_excel(output_path, index=False)
        print(f"Consolidated data saved to {output_path}")

if __name__ == "__main__":
    clean_and_consolidate("data/raw/", "data/processed/master_output.xlsx")
