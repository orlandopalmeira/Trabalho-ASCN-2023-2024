import json
import os

def merge_files(destination_file, *source_files):
    with open(destination_file, 'a') as dest_file:
        for source_file in source_files:
            with open(source_file, 'r') as src_file:
                # Skip the first line and copy the rest to the destination file
                next(src_file)  # Skip the first line
                dest_file.write(src_file.read())

def copy_file(source_file, destination_file):
    with open(source_file, 'r') as source:
        content = source.read()
    
    with open(destination_file, 'w') as destination:
        destination.write(content)

directory_path = 'results'
file_names_old = os.listdir(directory_path)

file_names = []
for f in file_names_old:
    if f.startswith('statistics'):
        res_f = directory_path + '/' + f
        file_names.append(res_f)

# Initialize an empty dictionary to store the merged data
merged_data = {"Total": {
    "transaction": "Total",
    "sampleCount": 0,
    "errorCount": 0,
    "meanResTime": 0.0,
    "minResTime": float('inf'),
    "maxResTime": 0.0,
    "throughput": 0.0
}}


# Loop through each file
for file_name in file_names:
    with open(file_name, 'r') as file:
        data = json.load(file)
        # Sum the sampleCount and errorCount, accumulate other values
        merged_data["Total"]["sampleCount"] += data["Total"]["sampleCount"]
        merged_data["Total"]["errorCount"] += data["Total"]["errorCount"]
        merged_data["Total"]["meanResTime"] += data["Total"]["meanResTime"]
        merged_data["Total"]["minResTime"] = min(merged_data["Total"]["minResTime"], data["Total"]["minResTime"])
        merged_data["Total"]["maxResTime"] = max(merged_data["Total"]["maxResTime"], data["Total"]["maxResTime"])
        merged_data["Total"]["throughput"] += data["Total"]["throughput"]

# Calculate averages
total_count = len(file_names)
merged_data["Total"]["meanResTime"] /= total_count
# merged_data["Total"]["throughput"] /= total_count

# Write the merged data to a new JSON file
with open(directory_path+"/merged_file.json", 'w') as merged_file:
    json.dump(merged_data, merged_file, indent=2)

print("Statistics have been saved to 'merged_file.json'")

####! Merging result_vm.jtl files
file_names = []
for f in file_names_old:
    if f.startswith('results_vm'):
        res_f = directory_path + '/' + f
        file_names.append(res_f)

copy_file(file_names[0], directory_path+'/merged_results.jtl')
merge_files(directory_path+'/merged_results.jtl', *(file_names[1:]))

print("Result logs been saved to 'merged_results.json'")
