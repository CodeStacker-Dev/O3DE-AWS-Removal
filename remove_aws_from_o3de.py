import os
import shutil

# List of AWS-related directories to remove
]

# List of AWS-related CMake files to modify
CMAKE_FILES = [
    "CMakeLists.txt",
    "Code/CMakeLists.txt",
    "Scripts/bootstrap.cfg",
]

# AWS-related CMake and config keywords to remove
]

# Function to remove directories
def remove_directories(base_path, directories):
    for directory in directories:
        full_path = os.path.join(base_path, directory)
        if os.path.exists(full_path):
            print(f"Removing directory: {full_path}")
            shutil.rmtree(full_path, ignore_errors=True)
        else:
            print(f"Skipping (not found): {full_path}")

# Function to clean CMake files
def clean_cmake_files(base_path, cmake_files, keywords):
    for cmake_file in cmake_files:
        full_path = os.path.join(base_path, cmake_file)
        if os.path.exists(full_path):
            with open(full_path, "r") as f:
                lines = f.readlines()
            
            # Remove lines containing AWS-related keywords
            new_lines = [line for line in lines if not any(keyword in line for keyword in keywords)]
            
            # Rewrite the file if changes were made
            if len(new_lines) != len(lines):
                with open(full_path, "w") as f:
                    f.writelines(new_lines)
                print(f"Cleaned: {full_path}")
            else:
                print(f"No AWS references found in: {full_path}")
        else:
            print(f"Skipping (not found): {full_path}")

# Function to search and remove AWS references in all files
def remove_aws_references(base_path, keywords):
    for root, _, files in os.walk(base_path):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                with open(file_path, "r") as f:
                    content = f.readlines()
                
                new_content = [line for line in content if not any(keyword in line for keyword in keywords)]
                
                if len(new_content) != len(content):
                    with open(file_path, "w") as f:
                        f.writelines(new_content)
                    print(f"Removed AWS references in: {file_path}")
            except:
                continue  # Ignore files that cannot be read (e.g., binaries)

# Main execution function
def main():
    base_path = os.getcwd()  # Assume script runs from O3DE root directory

    print("=== Removing AWS dependencies from O3DE ===")
    
    # Remove AWS directories
    
    # Clean CMake files

    # Remove AWS references from all source files

    print("=== AWS removal process completed ===")
    print("Now rebuild O3DE using CMake and Ninja.")

if __name__ == "__main__":
    main()
