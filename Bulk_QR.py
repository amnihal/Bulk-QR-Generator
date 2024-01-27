import os
import qrcode
import zipfile


# Function to generate bulk QR codes and save them to a zip file
def generate_bulk_qr_codes(data_list, output_folder, zip_filename):
  with zipfile.ZipFile(zip_filename, 'w') as zip_file:
    for data in data_list:
      qr = qrcode.QRCode(
          version=1,
          error_correction=qrcode.constants.ERROR_CORRECT_L,
          box_size=10,
          border=4,
      )
      qr.add_data(data)
      qr.make(fit=True)

      img = qr.make_image(fill_color="black", back_color="white")

      # Save the QR code image
      filename = os.path.join(output_folder, f"{data}.png")
      img.save(filename)
      zip_file.write(filename, os.path.basename(filename))
      print(f"QR code for {data} saved")


if __name__ == "__main__":
  # Prompt the user to enter a comma-separated list of strings
  input_string = input("Enter a comma-separated list of strings: ")

  # Split the input string into a list
  data_list = [s.strip() for s in input_string.split(',')]

  # Output folder for saving QR code images
  output_folder = "qr_codes"

  # Create the output folder if it doesn't exist
  if not os.path.exists(output_folder):
    os.makedirs(output_folder)

  # Output zip file
  zip_filename = "qr_codes.zip"

  # Generate bulk QR codes and save to zip file
  generate_bulk_qr_codes(data_list, output_folder, zip_filename)

  print(f"All QR codes saved to {zip_filename}")
