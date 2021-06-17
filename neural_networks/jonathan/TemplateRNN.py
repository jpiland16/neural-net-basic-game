from torch import nn
from GameElements import GameState, Game

class TemplateRNN(nn.Module):
    """
    An empty framework that could potentially include a neural network.
    """
    def __init__(self, N, M, device):
        """
        The initialization function receives three parameters:
         - N: number of policies
         - M: number of bandwidths
         - device: device on which to store tensors (CPU/GPU)

        You can save these parameters using `self` and/or use them
        to create a neural network.
        """
        
        # Must have this line below in order to use neural network capabilities
        # (Otherwise there will be an error in NetworkInteraction.py
        # when we try to move to the specified device.)
        super(TemplateRNN, self).__init__()

    def get_prediction(self, game_state: GameState):
        """
        This function accepts a GameState and should return an integer
        from 0 to (M - 1).
        """
        return 0


    def train(self, completed_games: 'list[Game]', params: dict) -> None:
        """
        This function is called whenever the neural network should be trained.
        It accepts a list of completed games and a set of parameters
        (see ParameterHost.py for examples of parameter sets).
        """
        pass