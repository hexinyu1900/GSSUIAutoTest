import os, random
from Config import Env_config


class SelectImage:
    @classmethod
    def select_image(cls, file_path):
        list1 = []
        for dirpath, dirnames, filenames in os.walk(file_path):
            for i in filenames:
                list1.append(os.path.join(dirpath, i))
                x = random.choice(list1)
        return x


if __name__ == '__main__':
    print(SelectImage.select_image(Env_config.image_path))
