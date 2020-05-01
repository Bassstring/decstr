import numpy as np
import pickle
import matplotlib.pyplot as plt


def get_data():
    path_reachable_configs = '/home/flowers/Desktop/Scratch/sac_curriculum/language/data/possible_configs.pkl'
    path_config_transitions_reached = "/home/flowers/Desktop/Scratch/sac_curriculum/language/data/learned_configs.pkl"

    with open(path_reachable_configs, 'rb') as f:
        reachable_configs = pickle.load(f)

    with open(path_config_transitions_reached, 'rb') as f:
        reached_config_transitions = pickle.load(f)

    all_configs_transitions = []
    for i in range(reachable_configs.shape[0]):
        for j in range(reachable_configs.shape[0]):
            all_configs_transitions.append([reachable_configs[i], reachable_configs[j]])
    all_configs_transitions = np.array(all_configs_transitions)

    all_delta_configs = all_configs_transitions[:,1,:] - all_configs_transitions[:,0,:]
    unique_delta_configs = np.unique(all_delta_configs, axis=0)
    delta_magnitudes = np.sum(np.abs(unique_delta_configs), axis=1)
    unique, count = np.unique(delta_magnitudes, return_counts=True)
    plt.bar(unique, count, alpha=0.4)
    plt.xlabel('Magnitude of config differences')
    plt.ylabel('Counts')

    unique_reached_config_transitions = np.unique(reached_config_transitions.astype(np.int), axis=0)
    all_reached_delta_configs = unique_reached_config_transitions[:,1,:] - unique_reached_config_transitions[:,0,:]
    unique_reached_delta_configs = np.unique(all_reached_delta_configs, axis=0)
    reached_delta_magnitudes = np.sum(np.abs(unique_reached_delta_configs), axis=1)
    unique, counts = np.unique(reached_delta_magnitudes, return_counts=True)
    plt.bar(unique, counts, alpha=0.4)
    plt.legend(['All delta', 'reached delta'])

    predicates = ['close_0_1',
                  'close_0_2',
                  'close_1_2',
                  'above_0_1',
                  'above_1_0',
                  'above_0_2',
                  'above_2_0',
                  'above_1_2',
                  'above_2_1']


    predicate_to_id = dict(zip(predicates, range(9)))
    id_to_predicate = dict(zip(range(9), predicates))

    colors = {'0':'green', '1':'blue', '2':'red'}

    return unique_reached_config_transitions, reached_config_transitions, predicates, predicate_to_id, id_to_predicate, colors