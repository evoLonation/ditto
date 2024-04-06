import os
import json
from flearn.utils.model_utils import read_data

def main():
    train_path = os.path.join('data', 'fmnist', 'data', 'train')
    test_path = os.path.join('data', 'fmnist', 'data', 'test')
    dataset = read_data(train_path, test_path)
    users, _, train_data, test_data = dataset
    os.mkdir('splitted_dataset')
    for i, u in enumerate(users):
        with open(f'splitted_dataset/client_{i}.json', 'wt') as f:
            json.dump(test_data[u], f)
        
    
if __name__ == '__main__':
    main()