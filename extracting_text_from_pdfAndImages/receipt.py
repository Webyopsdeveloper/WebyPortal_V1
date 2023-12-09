import json
import requests
import pandas as pd

def data_from_receipt(image):
    url = "https://ocr.asprise.com/api/v1/receipt"

    data = {
        'api_key': 'TEST',
        'recognizer': 'auto',
        'ref_no': 'oct_python_123'
    }

    files = {
        'file': open(image, 'rb')
    }

    try:
        res = requests.post(url, data=data, files=files)
        res.raise_for_status()  
        response_data = res.json()

        with open("response1.json", "w") as f:
            json.dump(response_data, f)

    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)


def create_receipt_info_dataframe():
    with open("response1.json", "r") as f:
        data = json.load(f)

        if 'receipts' not in data:
            print("No receipts found.")
            return None

        receipt_data = []
        for idx, receipt in enumerate(data['receipts'], 1):
            receipt_info = {
                'Serial No.': idx,
                'Date of Purchase': receipt.get('date', 'N/A'),
                'Place of Purchase': receipt.get('merchant_name', 'N/A'),
                'Receipt No.': receipt.get('receipt_number', 'N/A')
            }
            receipt_data.append(receipt_info)

        return pd.DataFrame(receipt_data)


def print_item_details():
    with open("response1.json", "r") as f:
        data = json.load(f)

        if 'receipts' not in data:
            print("No receipts found.")
            return

        print("\nDetailed Item Information:")
        print("Serial No.\tItem Description\tItem Amount")
        print("-" * 70)

        for idx, receipt in enumerate(data['receipts'], 1):
            items = receipt['items']
            for item_idx, item in enumerate(items, 1):  
                item_description = item.get('description', 'N/A')
                item_amount = f"{receipt.get('currency', 'N/A')} {item.get('amount', 'N/A')}"
                print(f"{idx}\t\t{item_description}\t\t{item_amount}")


image = "images/sample1.jpg"
data_from_receipt(image)

receipt_info_df = create_receipt_info_dataframe()
if receipt_info_df is not None:
    print("Basic Receipt Information:")
    print(receipt_info_df.to_string(index=False))
    print()

print_item_details()
