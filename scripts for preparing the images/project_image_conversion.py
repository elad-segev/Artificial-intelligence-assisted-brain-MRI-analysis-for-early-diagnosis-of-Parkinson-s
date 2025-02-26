from PIL import Image
import os


def upscale_image(input_image_path, output_resolution, output_image_path=None):

    try:
        # Load the input image
        with Image.open(input_image_path) as img:
            # Upscale the image to the target resolution
            upscaled_img = img.resize(output_resolution, Image.Resampling.LANCZOS)

            # Save the upscaled image if a path is provided
            if output_image_path:
                upscaled_img.save(output_image_path)
                return "success"
            else:
                return upscaled_img

    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def main():
    patient_folders_path = r"C:\Users\elads\Desktop\‏‏תיקיה חדשה\מחקרים לבינה\pic\מקור התמונות\תמונות נוספות להערכה ראשונית של המודל\PD\pd_sum"
    output_path = r"C:\Users\elads\Desktop\‏‏תיקיה חדשה\מחקרים לבינה\pic\output\הערכה ראשונית\PD"
    output_res = (250, 250)
    valid_extensions = (".png", ".jpg", ".jpeg")

    # Get user-defined prefix
    #user_prefix = "PD_patient(30)"

    # Ensure the output folder exists
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    # Initialize a counter for the images (start at 1)
    count_of_iter = 1

    # Iterate over files in the input folder
    for file_name in os.listdir(patient_folders_path):
        file_path = os.path.join(patient_folders_path, file_name)

        # Process only valid image files
        if file_path.lower().endswith(valid_extensions):
            # Generate a new name for the output file with user-defined prefix and image count
            #file_extension = os.path.splitext(file_name)[-1]  # Get the original file extension
            #new_file_name = f"{user_prefix}_{count_of_iter}{file_extension}"
            #output_file_path = os.path.join(output_path, new_file_name)
            output_file_path = os.path.join(output_path, file_name)

            # Upscale the image
            result = upscale_image(file_path, output_res, output_file_path)

            if result == "success":
                #print(f"The operation was successful for {file_name} -> {new_file_name}")
                print(f"The operation was successful for {file_name}")
                count_of_iter += 1

    print(f"Total number of images processed: {count_of_iter - 1}")


main()
