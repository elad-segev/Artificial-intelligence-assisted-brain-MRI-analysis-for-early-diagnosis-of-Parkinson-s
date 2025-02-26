import os
import shutil
import pandas as pd


def copy_directory(src, dest, key=True):
    """
    Copy the folder and all its content, including the folder itself, from the source to the destination.

    Parameters:
    src (str): The source folder address.
    dest (str): The destination folder address.
    """
    # Check if the source folder exists
    if not os.path.exists(src):
        print(f"The source folder {src} does not exist.")
        return

    # Make sure the destination folder exists, create it if it doesn't
    if not os.path.exists(dest):
        os.makedirs(dest)

    # Copy the folder itself (not just its content) into the destination
    dest_folder = os.path.join(dest, os.path.basename(src))  # Add the folder name to the destination path

    # If the destination folder already exists, delete it before copying
    if os.path.exists(dest_folder):
        #print(f"The folder {dest_folder} already exists. Deleting it and copying the new folder.")
        #shutil.rmtree(dest_folder)
        return

    # Copy the entire folder (including the folder itself) to the destination
    if key:
        # Perform a copy operation
        shutil.copytree(src, dest_folder)
        print(f"The folder {src} has been successfully copied to {dest_folder}")
    else:
        # Perform a move operation
        shutil.copytree(src, dest_folder)  # Copy folder to destination
        shutil.rmtree(src)  # Delete the source folder
        print(f"The folder {src} has been moved to {dest_folder} and deleted from the source.")



def main():
    healthy_folder = r"D:\project\Control1"
    sick_folder = r"D:\project\PD1"
    prodromal_folder = r"D:\project\Prodromal1"
    patient_folders_path = r"C:\Users\elads\Desktop\‏‏תיקיה חדשה\מחקרים לבינה\מסד נתונים - MRI מוח אלעד\אוסף 2\PPMI"
    csv_path = r"C:\Users\elads\Desktop\‏‏תיקיה חדשה\מחקרים לבינה\מסד נתונים - MRI מוח אלעד\idaSearch_12_16_2024.csv"

    df = pd.read_csv(csv_path)

    dict_of_cycle = {}
    count_of_iter = 0
    # Check all patient folders in the given path
    for folder_name in os.listdir(patient_folders_path):
        folder_path = os.path.join(patient_folders_path, folder_name)
        if os.path.isdir(folder_path):  # If it's a directory
            # Check if the folder name appears in the CSV 'Subject ID' column
            if int(folder_name) in df['Subject ID'].values:
                # print(folder_name, "TRUE")

                # Find the value in the 'Research Group' column
                potential_research_group = df[df['Subject ID'] == int(folder_name)]["Research Group"]

                if len(potential_research_group) > 1:
                    dict_of_cycle[str(folder_name)] = len(potential_research_group)

                research_group = "".join(potential_research_group.values[0])

                # print(folder_name, research_group)

                # Decide where to copy the folder based on the 'Research Group' column value
                if research_group == 'PD':
                    target_folder = sick_folder
                elif research_group == 'Prodromal':
                    target_folder = prodromal_folder
                else:
                    target_folder = healthy_folder

                # Copy the folder to the target folder
                # print(folder_path)
                copy_directory(folder_path, target_folder)

            else:
                print(f"Folder {folder_name} not found in the CSV")

            count_of_iter += 1

    print(count_of_iter)
    print(dict_of_cycle)


if __name__ == "__main__":
    main()