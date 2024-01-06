import requests
import os


def download_file(url, filename):
    """
    Download a file from the given URL and save it to the destination folder.

    Parameters:
        - url (str): The URL of the file to download.
        - destination_folder (str): The folder where the file should be saved. Default is the current directory.
    """
    response = requests.get(url)

    if response.status_code == 200:
        # Extracting the filename from the URL
        destination_path = os.path.join("./Data", filename) # Probleme : creer dir data !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

        with open(destination_path, "wb") as file:
            file.write(response.content)

        print(f"File '{filename}' downloaded successfully.")
    else:
        print(f"Failed to download the file. Status Code: {response.status_code}")


if __name__ == "__main__":
    # Data nombres licenciés
    download_file(
        "https://www.data.gouv.fr/fr/datasets/r/b62c05d2-6b45-44e0-80a4-6e10e3f14ec6",
        "lic-data-2021.csv",
    )
    download_file(
        "https://www.data.gouv.fr/fr/datasets/r/1eb1e7c9-27c4-4834-b8b6-cf63b45ee74b",
        "lic-data-2020.csv",
    )
    download_file(
        "https://www.data.gouv.fr/fr/datasets/r/9b002e32-0ec9-40fc-9292-cddeae4416c6",
        "lic-data-2019.csv",
    )

    # Data géolocalisation
    download_file(
        "https://www.data.gouv.fr/fr/datasets/r/dbe8a621-a9c4-4bc3-9cae-be1699c5ff25",
        "geolocalisation.csv",
    )
