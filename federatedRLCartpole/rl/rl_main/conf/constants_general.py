import torch

from conf.names import OptimizerName

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

# [GENERAL]
SEED = 1
MY_PLATFORM = None
PYTHON_PATH = None
EMA_WINDOW = 10
VERBOSE = True
MODEL_SAVE = True

# [MQTT]
MQTT_SERVER = None
MQTT_PORT = 1883
MQTT_TOPIC_EPISODE_DETAIL = "Episode_Detail"
MQTT_TOPIC_SUCCESS_DONE = "Success_Done"
MQTT_TOPIC_FAIL_DONE = "Fail_Done"
MQTT_TOPIC_TRANSFER_ACK = "Transfer_Ack"
MQTT_TOPIC_UPDATE_ACK = "Update_Ack"
MQTT_TOPIC_ACK = "Ack"
MQTT_LOG = False

# MQTT for RIP
MQTT_SERVER_FOR_RIP = "192.168.0.10"
MQTT_PUB_TO_SERVO_POWER = 'motor_power_2'
MQTT_PUB_RESET = 'reset_2'
MQTT_SUB_FROM_SERVO = 'servo_info_2'
MQTT_SUB_MOTOR_LIMIT = 'motor_limit_info_2'
MQTT_SUB_RESET_COMPLETE = 'reset_complete_2'

# [WORKER]
NUM_WORKERS = 1

# [TRANSFER]
SOFT_TRANSFER = False
SOFT_TRANSFER_TAU = 0.3

# [TARGET_UPDATE]
SOFT_TARGET_UPDATE = False
SOFT_TARGET_UPDATE_TAU = 0.3

# [MLP_DEEP_LEARNING_MODEL]
HIDDEN_1_SIZE = 128
HIDDEN_2_SIZE = 128
HIDDEN_3_SIZE = 128
# HIDDEN_SIZE_LIST = [128, 128, 128, 256]

# [CNN_DEEP_LEARNING_MODEL]
CNN_CRITIC_HIDDEN_1_SIZE = 128
CNN_CRITIC_HIDDEN_2_SIZE = 128

# [OPTIMIZATION]
MAX_EPISODES = 2000
GAMMA = 0.98 # discount factor

# [MODE]
MODE_SYNCHRONIZATION = True
MODE_GRADIENTS_UPDATE = True         # Distributed
MODE_PARAMETERS_TRANSFER = True     # Transfer

# [TRAINING]
EPSILON_GREEDY_ACT = False
EPSILON_DECAY = False
EPSILON_START = 0.9
EPSILON_END = 0.05
EPSILON_DECAY_RATE = 200 #Large value means low decaying
OPTIMIZER = OptimizerName.ADAM
GAE_LAMBDA = 0.95
LEARNING_RATE = 0.001

# [TRAJECTORY_SAMPLING]
TRAJECTORY_SAMPLING = True
TRAJECTORY_LIMIT_SIZE = 200
TRAJECTORY_BATCH_SIZE = 64

# [PPO]
PPO_K_EPOCH = 10
PPO_EPSILON_CLIP = 0.2
PPO_VALUE_LOSS_WEIGHT = 0.5
PPO_ENTROPY_WEIGHT = 0.01

# [DQN]
DQN_BATCH_SIZE = 128

# [CUDA]
CUDA_VISIBLE_DEVICES_NUMBER_LIST = '2, 3'