import pytesseract
import cv2
import json
import re

# Configure Tesseract executable path (update with your Tesseract installation path)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
def Passport_data(image_path, ext_data):
    # Load the image of the driving license
    # image_path = "pass.jpg"
    img = cv2.imread(image_path)
    # Resize and convert to grayscale
    img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Perform OCR to extract text
    text = pytesseract.image_to_string(img)
    lines = text.split("\n")


    # Additional name patterns
    name_patterns = [
        # r"Name[:\s]*([A-Z][A-Z\s]+)",
        r"ame[:\s]*([A-Z][A-Z\s]+)",
        # r"[:\s]*([A-Z][A-Z\s]+)",
        # r"N[:\s]*([A-Z][A-Z\s]+)",
        # r"Na[:\s]*([A-Z][A-Z\s]+)",
        r"Name[:\s]*([\w\s']+)"
        r"Name[\s]*([\w\s']+)"
        r":\s*([A-Z\s]+)$"
        r"Nam[:\s]*([A-Z][A-Z\s]+)",
        r"name[:\s]*([A-Z][A-Z\s]+)",
        r"nam[:\s]*([A-Z][A-Z\s]+)",
        r"na[:\s]*([A-Z][A-Z\s]+)",
    ]


    dob_pattern = r"Date of Birth[^\d]*(\d{2}/\d{2}/\d{4})"

    # Search for the DOB using the pattern
    dob_match = re.search(dob_pattern, text)

    # Extract and format the DOB if found
    if dob_match:
        dob = dob_match.group(1)
        print("Date of Birth:", dob)
    else:
        print("Date of Birth not found")

    # Initialize variables to store extracted information
    name = None
    date_of_birth = None
    license_number = None

    #Print Extracted text
    print(text)

    # Find the index of "P<"
    start_index = text.find("P<")

    # Extract text from "P<" to the end of the string
    if start_index != -1:
        text = text[start_index:]
        print("Extracted Text:")
        print(text)
    else:
        print("Pattern 'P<' not found in the text.")

    # Define a pattern to match a name
    name_pattern = r":\s*([A-Z\s]+)$"

    # Search for the name using the pattern
    name_match = re.search(name_pattern, text, re.MULTILINE)


    # Extract and format the name if found
    if name_match:
        name = name_match.group(1).strip()

    lines = text.split('\n')

    # Initialize variables to store extracted information
    account_holder_name = ""
    nominee_name = ""
    passport_number = ""


    name_pattern = r"P<([^<]+)<<([A-Z\s<]+)<<"
    name_match = re.search(name_pattern, text)
    name = name_match.group(1).strip().replace("IND", "") + " " + name_match.group(2).strip() if name_match else "Name not found"
    name=name.replace("<", "")
    print("Full Name:", name)
    ext_data['name']=name
    # Define a regular expression pattern for extracting name based on arrows (case-insensitive)
    name_pattern = r'(?i)[A-Z ]+(?:<+|>+)[A-Z ]+'

    # Find all name matches in the text
    name_matches = re.findall(name_pattern, text)

    # Process the name matches
    for name in name_matches:
        # Split the name based on the arrows
        parts = re.split('<+|>+', name)
        if len(parts) >= 2:
            first_name = parts[0].strip()
            last_name = parts[1].strip()

    # Define regular expressions for first name, last name, and passport number
    name_pattern = r'<(.*?)<<'  # Matches text between '<' and '<<'
    # passport_pattern = r'J(\d+<)'  # Matches 'J' followed by digits and '<'

    # Define a regular expression pattern for the name
    name_pattern = r'Full Name:\s+(.*?)\n'



    # Define a regular expression pattern for the passport number
    passport_pattern = r'[A-Z]\d+'  # Matches an alphabet letter followed by one or more digits

    # Use regular expressions to extract the passport number
    passport_matches = re.findall(passport_pattern, text)

    if passport_matches:
        passport_number = passport_matches[0]
    else:
        passport_number = "Passport Number Not Found"


    # Initialize first name and last name
    first_name = ""
    last_name = ""

    # Define a regular expression pattern to capture the name
    name_pattern = r'(?<=<<)([^<]+)(?=<)'

    # Use regular expressions to extract the name
    name_matches = re.findall(name_pattern, text)

    if name_matches:
        first_name, last_name = name_matches[-2], name_matches[-1]
    else:
        first_name = "First Name Not Found"
        last_name = "Last Name Not Found"


    # Remove "IND" from the first name
    first_name = first_name.replace("IND", "")

    # print("Full Name:", full_name)
    print("Passport Number:", passport_number)
    print("First Name:", first_name)
    print("Last Name:", last_name)
    # print("Passport Number:", passport_number)
    ext_data['DocNo']=f"{passport_number}"
    ext_data['Document_type']="Passport"
    # Optionally, you can save the extracted information to a JSON file
    # with open("extracted_info.json", "w", encoding="utf-8") as json_file:
    #     json.dump(extracted_info, json_file, ensure_ascii=False, indent=4)

    with open("text.json", "w", encoding="utf-8") as json_file:
        json.dump(text, json_file, ensure_ascii=False, indent=4)

    # cv2.imshow("Processed Image", cv2.resize(img_gray, (0, 0), fx=0.5, fy=0.5))
    print(ext_data)
    # cv2.waitKey(10000)
    # cv2.destroyAllWindows()
# ext_data={}
# Passport_data("pass.jpg", ext_data)