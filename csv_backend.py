import csv

class CSVBackend:
    def __init__(self):
        pass

    def export_to_csv(self, table_name, rows):
        file_name = f"{table_name}_data.csv"
        with open(file_name, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            # Define headers based on table name
            if table_name == "Patient":
                writer.writerow(["ID", "Name", "Age", "Gender", "Contact", "Health Issue"])
            elif table_name == "Doctor":
                writer.writerow(["ID", "Name", "Age", "Gender", "Contact", "Specialization", "Timing"])
            elif table_name == "Nurse":
                writer.writerow(["ID", "Name", "Age", "Gender", "Contact", "Floor", "Shift"])
            elif table_name == "Staff":
                writer.writerow(["ID", "Name", "Age", "Gender", "Contact", "Post", "Shift"])

            for row in rows:
                writer.writerow(row)

        print(f"Data exported to {file_name}")
