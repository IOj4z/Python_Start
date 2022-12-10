import glob


# folder path
dir_path = r'/Users/godfather/Downloads/**/*.eps*'

# list to store files name
res = []
for file in glob.glob(dir_path, recursive=True):
    print(file)
# for path in os.scandir(dir_path):
#     if path.is_file():
#         if path.name == 'shutterstock_321823376.jpg':
#             print(path.name)
