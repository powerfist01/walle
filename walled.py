import os
import string
import random
import requests

class Walle:

    IMAGES_FOLDER_PATH = f'{os.getcwd()}/images'

    def __init__(self) -> None:
        '''
        Initialize
        '''
        os.makedirs(self.IMAGES_FOLDER_PATH, exist_ok=True)
        self.remove_previous_wallpapers()

    def set_wallpaper_by_file_path(self, image_filepath):
        '''
        Set wallpaper by file path
        '''

        if(not os.path.exists(image_filepath)):
            raise Exception('File not found')

        os.system(f"/usr/bin/gsettings set org.gnome.desktop.background picture-uri {image_filepath}")

    def remove_previous_wallpapers(self):
        '''
        Remove previous wallpapers
        '''

        for filename in os.listdir(self.IMAGES_FOLDER_PATH):
            file_path = os.path.join(self.IMAGES_FOLDER_PATH, filename)
            try:
                if(os.path.isfile(file_path)):
                    os.unlink(file_path)
            except Exception as e:
                print(e)

    def fetch_image_from_picsum(self):
        '''
        Fetch image from picsum
        '''

        url = 'https://picsum.photos/3840/2160?random=1'

        response = requests.get(url)

        if(response.status_code != 200):
            raise Exception('Error fetching image')

        return response.content

    def generate_random_filename(self):
        '''
        Generate random filename
        '''
        filename = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        return filename


    def write_image_to_file(self, image_metadata):
        '''
        Write image to file
        '''

        if(not image_metadata):
            raise Exception('Image metadata not found')
        
        image_filepath = self.IMAGES_FOLDER_PATH + '/' + self.generate_random_filename() + '.jpg'
        with open(image_filepath, 'wb') as file:
            file.write(image_metadata)

        return image_filepath


if __name__ == '__main__':

    walle = Walle()
    image_metadata = walle.fetch_image_from_picsum()
    image_filepath = walle.write_image_to_file(image_metadata)
    walle.set_wallpaper_by_file_path(image_filepath)