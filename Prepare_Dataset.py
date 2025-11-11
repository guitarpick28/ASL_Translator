import os

#Make sub folders with labels of the letters and numbers within the train, test, and validation
def create_sub_folders(labels: list , data_directory: str, subset:str="train"):
    for label in labels:
        label_folder=os.path.join(data_directory, subset, label)
        if not os.path.exists(label_folder):
            os.makedirs(label_folder)


def get_labels(data_directory:str="Data/asl_dataset")->list:
    items=os.listdir(data_directory)
    items=list(sorted(set(items)))
    labels=[]
    for item in items:
        if os.path.isdir(os.path.join(data_directory,item)):
            labels.append(item)
    return labels

def main():
    labels=get_labels()
    output_dir="Data/asl_dataset_sorted"
    for subset in ["train", "val", "test"]:
        create_sub_folders(labels, output_dir, subset=subset)
if __name__ == "__main__":
    main()