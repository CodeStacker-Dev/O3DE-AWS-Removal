import os

# Keywords to search for
AMAZON_KEYWORDS = [
    "Amazon",
    "AWS",
    "GameLift",
    "AWSCore",
    "AWSMetrics",
    "AWSGameLift",
    "AWSClientAuth",
    "AWSNativeSDK",
    "GridMate",  # Amazon's networking system
    "AWS_",  # Macros and settings
    "AZAWS",  # AZ AWS integration
    "AmazonWebServices",
]

# File extensions to scan
VALID_EXTENSIONS = [".cpp", ".h", ".cs", ".json", ".xml", ".cmake", ".cfg", ".py", ".sh"]

# Function to search for Amazon-related keywords
def scan_files(base_path, keywords):
    found_files = []

    for root, _, files in os.walk(base_path):
        for file in files:
            # Only scan valid file types
            if not any(file.endswith(ext) for ext in VALID_EXTENSIONS):
                continue

            file_path = os.path.join(root, file)
            try:
                with open(file_path, "r", errors="ignore") as f:
                    content = f.readlines()

                # Check for keywords in the file
                matches = [line.strip() for line in content if any(keyword in line for keyword in keywords)]
                
                if matches:
                    found_files.append(file_path)
                    print(f"\n🚨 Found Amazon-related code in: {file_path}")
                    for match in matches[:5]:  # Show first 5 matches per file
                        print(f"   ↳ {match}")
                    if len(matches) > 5:
                        print("   ... (more matches hidden)")

            except:
                continue  # Ignore unreadable files (binaries, etc.)

    return found_files

# Main function
def main():
    base_path = os.getcwd()  # Assume script runs from O3DE root directory
    print("\n=== Scanning O3DE for Amazon-related code ===\n")

    found_files = scan_files(base_path, AMAZON_KEYWORDS)

    if found_files:
        print("\n=== Summary: Amazon-related files found ===")
        for file in found_files:
            print(f"📌 {file}")
        print("\nReview and remove these files manually if necessary.")
    else:
        print("\n✅ No Amazon-related files found!")

if __name__ == "__main__":
    main()
