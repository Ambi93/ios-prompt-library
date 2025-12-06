import csv
import json
import glob
import os

def convert_csv_to_json(csv_file_path):
    data = {}
    with open(csv_file_path, 'r', encoding='utf-8') as csvf:
        csv_reader = csv.DictReader(csvf)
        for row in csv_reader:
            category = row.get('category')
            if category:
                if category not in data:
                    data[category] = []
                data[category].append({
                    'title': row.get('title', ''),
                    'text': row.get('text', '')
                })
    return data

def main():
    import sys
    if len(sys.argv) < 2:
        print("Usage: python csv_to_json.py <path_to_csv_files>")
        sys.exit(1)

    csv_pattern = sys.argv[1]
    csv_files = glob.glob(csv_pattern)

    for csv_file in csv_files:
        json_data = convert_csv_to_json(csv_file)
        
        # Construct output JSON filename
        base_name = os.path.splitext(os.path.basename(csv_file))[0]
        json_file_name = f"{base_name} Prompt Library.json"
        
        # Ensure the output directory exists
        output_dir = os.path.dirname(csv_file)
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        json_output_path = os.path.join(output_dir, json_file_name)

        with open(json_output_path, 'w', encoding='utf-8') as jsonf:
            json.dump(json_data, jsonf, indent=4, ensure_ascii=False)
        print(f"Converted {csv_file} to {json_output_path}")

if __name__ == '__main__':
    main()
