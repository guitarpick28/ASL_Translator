import os
import shutil
import random

#Make sub folders with labels of the letters and numbers within the train, test, and validation
def create_sub_folders(labels: list , data_directory: str, subset:str="train"):
    for label in labels:
        label_folder=os.path.join(data_directory, subset, label)
        if not os.path.exists(label_folder):
            os.makedirs(label_folder)
def write_labels_text(labels: list , data_directory: str):
    file_path=os.path.join(data_directory, "labels.txt")
    with open(file_path, 'wt') as file:
        for label in labels:
            file.write(label+"\n")

def get_labels(data_directory:str="Data/asl_dataset")->list:
    items=os.listdir(data_directory)
    items=list(sorted(set(items)))
    labels=[]
    for item in items:
        if os.path.isdir(os.path.join(data_directory,item)):
            labels.append(item)
    return labels
def randomize_images(label, images_folder, output_folder, test=.1,val=.1):
    train=1-test-val
    images=[]
    for image_name in os.listdir(images_folder):
        if os.path.isfile(os.path.join(images_folder,image_name)):
            images.append(image_name)
    test_count=int(len(images)*test)
    val_count=int(len(images)*val)
    random.shuffle(images)
    for i in range(test_count):
        image_name=images.pop()
        source_image=os.path.join(images_folder,image_name)
        destination_image=os.path.join(output_folder, "test", label, image_name)
        shutil.copy(source_image, destination_image)
    for i in range(val_count):
        image_name=images.pop()
        source_image=os.path.join(images_folder,image_name)
        destination_image=os.path.join(output_folder, "val", label, image_name)
        shutil.copy(source_image, destination_image)
    for image_name in images:
        source_image=os.path.join(images_folder,image_name)
        destination_image=os.path.join(output_folder, "train", label, image_name)
        shutil.copy(source_image, destination_image)
def main():
    unsorted_data_dir="Data/asl_dataset"
    labels=get_labels(unsorted_data_dir)
    output_dir="Data/asl_dataset_sorted"
    shutil.rmtree(output_dir)
    for subset in ["train", "val", "test"]:
        create_sub_folders(labels, output_dir, subset=subset)
    write_labels_text(labels, output_dir)
    for label in labels:
        images_folder=os.path.join(unsorted_data_dir, label)
        randomize_images(label, images_folder, output_dir)

if __name__ == "__main__":
    main()