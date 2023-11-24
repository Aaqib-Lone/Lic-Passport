# import pytesseract
# import cv2
# import json
# import re

# # Configure Tesseract executable path (update with your Tesseract installation path)
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
# def DL(image_path, extracted_info):
#     # Load the image of the driving license
#     # image_path = img
#     img = cv2.imread(image_path)
#     # Resize and convert to grayscale
#     img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
#     img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#     # Perform OCR to extract text
#     text = pytesseract.image_to_string(img)
#     lines = text.split("\n")

#     # Define regular expression patterns for name, DOB, and license number
#     # name_pattern = r"(Name|name|N|Na|Nam|me|Full Name)\s*:\s*([A-Z][A-Z\s]+)"
#     # Additional name patterns
#     name_patterns = [
#         # r"Name[:\s]*([A-Z][A-Z\s]+)",
#         r"ame[:\s]*([A-Z][A-Z\s]+)",
#         # r"[:\s]*([A-Z][A-Z\s]+)",
#         # r"N[:\s]*([A-Z][A-Z\s]+)",
#         # r"Na[:\s]*([A-Z][A-Z\s]+)",
#         r"Name[:\s]*([\w\s']+)"
#         r"Name[\s]*([\w\s']+)"
#         r":\s*([A-Z\s]+)$"
#         r"Nam[:\s]*([A-Z][A-Z\s]+)",
#         r"name[:\s]*([A-Z][A-Z\s]+)",
#         r"nam[:\s]*([A-Z][A-Z\s]+)",
#         r"na[:\s]*([A-Z][A-Z\s]+)",
#     ]

#     # # Define a pattern to match a date of birth (DOB) in the format MM/DD/YYYY
#     # dob_pattern = r"DOB:\s*(\d{2}/\d{2}/\d{4})"

#     # # Search for the DOB using the pattern
#     # dob_match = re.search(dob_pattern, text)

#     # # Extract and format the DOB if found
#     # if dob_match:
#     #     dob = dob_match.group(1).strip()


#     # dob_pattern = r"DOB[:\s]*([\d/]+|\d{1,2}[-/]\d{1,2}[-/]\d{2,4}|\d{4}[-/]\d{1,2}[-/]\d{1,2})"
#     # Additional DOB patterns
#     dob_pattern = [
#         r"DOB[:\s]*([\d/]+|\d{1,2}[-/]\d{1,2}[-/]\d{2,4}|\d{4}[-/]\d{1,2}[-/]\d{1,2})",
#         r"Date of Birth[:\s]*([\d/]+|\d{1,2}[-/]\d{1,2}[-/]\d{2,4}|\d{4}[-/]\d{1,2}[-/]\d{1,2})",
#         r"Birthday[:\s]*([\d/]+|\d{1,2}[-/]\d{1,2}[-/]\d{2,4}|\d{4}[-/]\d{1,2}[-/]\d{1,2})",
#         r"Birth Date[:\s]*([\d/]+|\d{1,2}[-/]\d{1,2}[-/]\d{2,4}|\d{4}[-/]\d{1,2}[-/]\d{1,2})",
#         r"DOB[:\s]*([\d/]+|\d{1,2}[-/]\d{1,2}[-/]\d{2,4}|\d{4}[-/]\d{1,2}[-/]\d{1,2})",
#         r"Date of Birth[ :\s]*([\d/]+|\d{1,2}[-/]\d{1,2}[-/]\d{2,4}|\d{4}[-/]\d{1,2}[-/]\d{1,2})",
#         r"Birth Date[ :\s]*([\d/]+|\d{1,2}[-/]\d{1,2}[-/]\d{2,4}|\d{4}[-/]\d{1,2}[-/]\d{1,2})",
#         r"Birthday[ :\s]*([\d/]+|\d{1,2}[-/]\d{1,2}[-/]\d{2,4}|\d{4}[-/]\d{1,2}[-/]\d{1,2})",
#         r"DO[ :\s]*([\d/]+|\d{1,2}[-/]\d{1,2}[-/]\d{2,4}|\d{4}[-/]\d{1,2}[-/]\d{1,2})",
#         r"dob[ :\s]*([\d/]+|\d{1,2}[-/]\d{1,2}[-/]\d{2,4}|\d{4}[-/]\d{1,2}[-/]\d{1,2})",
#         r"DOB\s*:\s*(\d{2}-\d{2}-\d{4})",
#     ]

#     license_number_pattern = (
#         r"[A-Z]{2}-[0-9A-Z-]+|[A-Z]{2}[0-9]{2} [0-9A-Z-]+|No\.mHos\s*(\d+)"
#     )
#     # pattern1 = r"[A-Z]{2}-[0-9A-Z-]+"
#     # pattern2 = r"[A-Z]{2}[0-9]{2} [0-9A-Z-]+"

#     # Initialize variables to store extracted information
#     name = None
#     date_of_birth = None
#     license_number = None

#     # Print Extracted text
#     print(text)

#     # Define a pattern to match a name
#     name_pattern = r":\s*([A-Z\s]+)$"

#     # Search for the name using the pattern
#     name_match = re.search(name_pattern, text, re.MULTILINE)


#     # Extract and format the name if found
#     if name_match:
#         name = name_match.group(1).strip()

#     # Extract name
#     for line in lines:
#         if not name:
#             for pattern in name_patterns:
#                 name_match = re.search(pattern, line)
#                 if name_match:
#                     name = name_match.group(1).strip()
#                     break  # Stop searching if a match is found

#         if not date_of_birth:
#             for pattern in dob_pattern:
#                 dob_match = re.search(pattern, line)
#                 if dob_match:
#                     date_of_birth = dob_match.group(1).strip()
#                     break  # Stop searching if a match is found

#         if not license_number and re.search(license_number_pattern, line):
#             license_number_match = re.search(license_number_pattern, line)
#             if license_number_match:
#                 license_number = license_number_match.group().strip()

#     # Define regular expression patterns for address (similar to your previous code)
#     address_patterns = [
#         r"Address[:\s]*([\w\s\d,/.'-]+)",
#         r"Add[:\s]*([\w\s\d,/.'-]+)",
#         r"Addres[:\s]*([\w\s\d,/.'-]+)",
#         r"dd[:\s]*([\w\s\d,/.'-]+)",
#         r"add[:\s]*([\w\s\d,/.'-]+)",
#         r"dd[ :\s]*([\w\s\d,/.'-]+)",
#     ]

#     # Initialize address variable
#     address = None

#     # Try each address pattern
#     for pattern in address_patterns:
#         address_match = re.search(pattern, text)
#         if address_match:
#             address = address_match.group(1).strip()
#             break  # Stop searching if a match is found
    
#     # Create a dictionary to store the extracted information
#     extracted_info["Document_type"]= "DRIVING LICENSE"
#     extracted_info["name"]= name
#     extracted_info["dob"]= date_of_birth,
#     extracted_info["DocNo"]= license_number,
#     extracted_info["address"]= address
#         # Add more fields here as needed

#     # Print the extracted information
#     for key, value in extracted_info.items():
#         print(f"{key}: {value}")

#     # Optionally, you can save the extracted information to a JSON file
#     with open("extracted_info.json", "w", encoding="utf-8") as json_file:
#         json.dump(extracted_info, json_file, ensure_ascii=False, indent=4)

#     with open("extracted_text.json", "w", encoding="utf-8") as json_file:
#         json.dump(text, json_file, ensure_ascii=False, indent=4)

#     # Display the processed image (optional)
#     # cv2.imshow("Processed Image", img_gray)
#     # cv2.waitKey(10000)
#     # cv2.imshow("Processed Image", cv2.resize(img_gray, (0, 0), fx=0.5, fy=0.5))

#     # cv2.waitKey(10000)
#     # cv2.destroyAllWindows()

# # obj={}
# # DL("driv_lic.jpg", obj)




import pytesseract
import cv2
import json
import re
import numpy as np

# Configure Tesseract executable path (update with your Tesseract installation path)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def DL(image_path, extracted_info):
# Load the image of the driving license
    img = cv2.imread(image_path)
    # Resize and convert to grayscale
    img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Sharpen the image using a kernel
    sharpening_kernel = np.array([[-1, -1, -1],
                                [-1, 9, -1],
                                [-1, -1, -1]])
    sharpened_img = cv2.filter2D(img_gray, -1, sharpening_kernel)

    # Perform OCR to extract text
    text = pytesseract.image_to_string(img)
    lines = text.split("\n")

    # Define regular expression patterns for name, DOB, and license number
    name_patterns = [
        r"Name\s*([\w\s']+)",
        r"Name\s*:(.*)",
        r"Name\s+([A-Z][A-Z\s']+)",
        r"Name[:\s]*([A-Z][A-Z\s]+)",
        r"Name[:;]\s*([A-Za-z\s\.]+),",
        r"ame[:\s]*([A-Z][A-Z\s]+)",
        r"Name[:\s]*([\w\s']+)",
        r"Name[\s]*([\w\s']+)",
        r":\s*([A-Z\s]+)$",
        r"Nam[:\s]*([A-Z][A-Z\s]+)",
        r"name[:\s]*([A-Z][A-Z\s]+)",
        r"nam[:\s]*([A-Z][A-Z\s]+)",
        r"na[:\s]*([A-Z][A-Z\s]+)",
        r"Full Name[:\s]*([A-Z][A-Z\s]+)",
        r"User Name[:\s]*([A-Z][A-Z\s]+)",
        r"Customer Name[:\s]*([\w\s']+)"
    ]

    dob_pattern = [
        r"D\.O\.B\.\s*:\s*(\d{1,2}[/.]\d{1,2}[/.]\d{4})"
        r"DOB[:\s]*([\d/]+|\d{1,2}[-/]\d{1,2}[-/]\d{2,4}|\d{4}[-/]\d{1,2}[-/]\d{1,2})|(\d{2}-\d{2} \d{4})",
        r"Date of Birth[:\s]*([\d/]+|\d{1,2}[-/]\d{1,2}[-/]\d{2,4}|\d{4}[-/]\d{1,2}[-/]\d{1,2})",
        r"Birthday[:\s]*([\d/]+|\d{1,2}[-/]\d{1,2}[-/]\d{2,4}|\d{4}[-/]\d{1,2}[-/]\d{1,2})",
        r"Birth Date[:\s]*([\d/]+|\d{1,2}[-/]\d{1,2}[-/]\d{2,4}|\d{4}[-/]\d{1,2}[-/]\d{1,2})",
        r"DO[ :\s]*([\d/]+|\d{1,2}[-/]\d{1,2}[-/]\d{2,4}|\d{4}[-/]\d{1,2}[-/]\d{1,2})",
        r"dob[ :\s]*([\d/]+|\d{1,2}[-/]\d{1,2}[-/]\d{2,4}|\d{4}[-/]\d{1,2}[-/]\d{1,2})",
        r"DOB\s*:\s*(\d{2}-\d{2}-\d{4})|(\d{2}-\d{2} \d{4})",
        # r"D\.O\.B\.?\s*:\s*(\d{1,2}/\d{1}/\d{4})"
        r"Date Of Bitch\s*:\s*(\d{2}-\d{2}-\d{4})|(\d{2}-\d{2} \d{4})",
        r"Date Of Bitch (\d{2}-\d{2}-\d{4})",
        r"Date of Birth\s*©\s*--\s*(\d{2}/\d{2}/\d{4})"
    ]

    license_number_pattern = r"[A-Z]{2}-[0-9A-Z-]+|[A-Z]{2}[0-9]{2} [0-9A-Z-]+|No\.mHos\s*(\d+)|M\d{2} (\d+)|OROF (\d+)|D\.L\.No\s*:\s*([A-Z/0-9-¥/0-9]+)|(\d{1,}/\d{1,}/\d{4})"

    # Initialize variables to store extracted information
    name = None
    date_of_birth = None
    license_number = None

    # Define a dictionary to map state codes to state names
    state_codes_to_names = {
        "AN": "Andaman and Nicobar Islands",
        "AP": "Andhra Pradesh",
        "AR": "Arunachal Pradesh",
        "AS": "Assam",
        "BR": "Bihar",
        "CG": "Chhattisgarh",
        "CH": "Chandigarh",
        "DD": "Daman and Diu",
        "DL": "Delhi",
        "DN": "Dadra and Nagar Haveli",
        "GA": "Goa",
        "GJ": "Gujarat",
        "HP": "Himachal Pradesh",
        "HR": "Haryana",
        "JH": "Jharkhand",
        "JK": "Jammu and Kashmir",
        "KA": "Karnataka",
        "KL": "Kerala",
        "LD": "Lakshadweep",
        "MH": "Maharashtra",
        "ML": "Meghalaya",
        "MN": "Manipur",
        "MP": "Madhya Pradesh",
        "MZ": "Mizoram",
        "NL": "Nagaland",
        "OD": "Odisha",
        "PB": "Punjab",
        "PY": "Puducherry",
        "RJ": "Rajasthan",
        "SK": "Sikkim",
        "TN": "Tamil Nadu",
        "TR": "Tripura",
        "TS": "Telangana",
        "UK": "Uttarakhand",
        "UP": "Uttar Pradesh",
        "WB": "West Bengal",
    }


    # Print Extracted text
    print(text)

    # Define a pattern to match a name
    name_pattern = r":\s*([A-Z\s]+)$"

    # Search for the name using the pattern
    name_match = re.search(name_pattern, text, re.MULTILINE)

    # Extract and format the name if found
    if name_match:
        name = name_match.group(1).strip()

    # Extract name
    for line in lines:
        if not name:
            for pattern in name_patterns:
                name_match = re.search(pattern, line)
                if name_match:
                    name = name_match.group(1).strip()
                    break  # Stop searching if a match is found

        if not date_of_birth:
            for pattern in dob_pattern:
                dob_match = re.search(pattern, line)
                if dob_match:
                    date_of_birth = dob_match.group(1).strip()
                    break  # Stop searching if a match is found

        if not license_number and re.search(license_number_pattern, line):
            license_number_match = re.search(license_number_pattern, line)
            if license_number_match:
                license_number = license_number_match.group().strip()
    # Regular expression patterns for address (continued from the previous code)
    address_patterns = [
        r"Address[:\s]*([\w\s\d,/.'-]+)",
        r"Address:(.*?)(?:D\.O\.B\.|D\.L\.No|$)",
        r"Addres[:\s]*([\w\s\d,/.'-]+)",
        r"Addres\s*:\s*([\w\s\d,/.'-]+)",
        r"dd[:\s]*([\w\s\d,/.'-]+)",
        r"add[:\s]*([\w\s\d,/.'-]+)",
        r"dd[ :\s]*([\w\s\d,/.'-]+)",
        r"Addresa \+(.*?)\n",
        r"Addresa\s*:(.*)",
        r"Permanent Acdress[ :\s]*([\w\s\d,/.'-]+)",
    ]

    # Initialize the address variable
    address = None

    # Try each address pattern
    for pattern in address_patterns:
        address_match = re.search(pattern, text)
        if address_match:
            address = address_match.group(1).strip()
            break  # Stop searching if a match is found

    # Initialize the state variable
    state = ''
    # for abbreviation in abbreviations:
    #     if abbreviation in license_number:
    #         index = abbreviations.index(abbreviation)
    #         state = states[index]

    if license_number:
        # Split the license number by '-' or ' ' and get the first part
        license_parts = re.split(r'[-\s]', license_number)
        if license_parts:
            license_prefix = license_parts[0]
            # Check if the license prefix is in the dictionary
            if license_prefix in state_codes_to_names:
                state = state_codes_to_names[license_prefix]

    # Add the "State" field to the extracted information dictionary
    # extracted_info["State"] = state

    # Create a dictionary to store the extracted information
    # extracted_info = {
    #     "Name": name,
    #     "Date of Birth": date_of_birth,
    #     "License Number": license_number,
    #     "State": state,  # Add the "State" field
    #     # Add more fields here as needed
    # }

    # Print the extracted information
    for key, value in extracted_info.items():
        print(f"{key}: {value}")

    # Print the state information
    # if state:
    #     print(f"State: {state}")
    # else:
    #     print("State information not found in the license number")

    extracted_info["Document_type"]= "DRIVING LICENSE"
    extracted_info["name"]= name
    extracted_info["view"]= "FRONT"
    extracted_info["dob"]= date_of_birth,
    extracted_info["State"]= state,
    extracted_info["DocNo"]= license_number,
    extracted_info["address"]= address
    print(extracted_info)
    # Optionally, you can save the updated extracted information to a JSON file
    with open("extracted_info.json", "w", encoding="utf-8") as json_file:
        json.dump(extracted_info, json_file, ensure_ascii=False, indent=4)

    # Create a dictionary to store the extracted information
    # extracted_info = {
    #     "Name": name,
    #     "Date of Birth": date_of_birth,
    #     "License Number": license_number,
    #     "Address": address,
    #     "State" : state
    #     # Add more fields here as needed
    # }
    # if state:
    #     print(f"State: {state}")
    # else:
    #     print("State information not found in the license number")

    # Print the extracted information
    # for key, value in extracted_info.items():
    #     print(f"{key}: {value}")

    # Optionally, you can save the extracted information to a JSON file
    with open("extracted_info.json", "w", encoding="utf-8") as json_file:
        json.dump(extracted_info, json_file, ensure_ascii=False, indent=4)

    with open("extracted_text.json", "w", encoding="utf-8") as json_file:
        json.dump(text, json_file, ensure_ascii=False, indent=4)

    # Display the processed image (optional)
    # cv2.imshow("Processed Image", img_gray)
    # cv2.waitKey(10000)
    # cv2.imshow("sharpened_img", cv2.resize(img_gray, (0, 0), fx=0.5, fy=0.5))

    # cv2.waitKey(10000)
# ext={}
# DL("drlic.jpg", ext)