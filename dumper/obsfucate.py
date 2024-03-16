import os
import base64
import shutil
import math,random
# Define the source and destination directories
source_dir = './solutions/9781337516853'
destination_dir = './solutions_obsfuated/9781337516853/'

# Create the destination directory if it doesn't exist
if not os.path.exists(destination_dir):
    os.makedirs(destination_dir)

# Iterate over all files in the source directory
for root, dirs, files in os.walk(source_dir):
    for file in files:
        # Check if the file is a text file
        if file.endswith('.txt'):
            # Read the contents of the text file
            file_path = os.path.join(root, file)
            with open(file_path, 'r') as f:
                text = f.read()

            # Encode the text as base64
            for i in range(random.randint(1, 10)):
                text = base64.b64encode(text.encode()).decode()


            # Create the corresponding file in the destination directory
            destination_file_path = os.path.join(destination_dir, file)
            with open(destination_file_path, 'w') as f:
                f.write(text)

# Print a message to indicate the process is complete
print('Text files have been obfuscated and saved in the "solutions_obsfuated" folder.')