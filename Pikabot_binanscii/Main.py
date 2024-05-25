import binascii
import os

# Pikabot'un özelliklerine karşılık gelen bayt desenleri
traits = [
    b'8d85????89b5????508d85??????50',
    b'558bec5151894d??56bec7260000578b',
    b'6a4068????????64a100000000506489',
]

def scan_file_for_pikabot(file_path):
    try:
        with open(file_path, 'rb') as file:
            content = file.read()

            for trait in traits:
                if binascii.hexlify(trait) in binascii.hexlify(content):
                    print(f"{file_path} matches Pikabot pattern.")
                    return True

            print(f"{file_path} does not match Pikabot pattern.")
            return False
    except Exception as e:
        print(f"Error scanning {file_path}: {str(e)}")
        return False

def scan_directory_for_pikabot(directory):
    try:
        for root, dirs, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                scan_file_for_pikabot(file_path)
    except Exception as e:
        print(f"Error scanning directory {directory}: {str(e)}")

def main():
    path_to_scan = r'C:\Users\MUSTAFA\Desktop\hafboa' #Buraya kendi yolunuzu vermeniz lazım
    scan_directory_for_pikabot(path_to_scan)

if __name__ == "__main__":
    main()
