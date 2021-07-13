import numpy as np
from GameElements import Action, Adversary, GameState, Policy
from ShowInfo import show_game_info
from Util import get_integer
import random

class ExampleAdversary(Adversary):

    def bandwidth_predictor_function(self, game_state: GameState) -> int:
        # Guess a random band (0 to M-1)
        return random.randint(0, game_state.params.M - 1)

    def __init__(self) -> None:
        super(ExampleAdversary, self).__init__(
            self.bandwidth_predictor_function)


class HumanAdversary(Adversary):

    def bandwidth_predictor_function(self, game_state: GameState) -> int:
        # Ask the player to predict the bandwidth based on game info
        show_game_info(game_state)
        return get_integer("Predicted band? (0 - {:d})".format(
            game_state.params.M - 1), min=0, max=game_state.params.M - 1)

    def __init__(self) -> None:
        super(HumanAdversary, self).__init__(
            self.bandwidth_predictor_function)

class GammaAdversary(Adversary):

    def get_policy_value(self, policy: Policy, actions: 'list[Action]'):

        lo_lookback_index = max(0, len(actions) - self.max_lookback)
        lookback_range = range(lo_lookback_index, len(actions))

        state_values = [self.gamma ** (len(actions) - t) 
            for t in lookback_range]

        policy_predictions = [policy.get_bandwidth(t) 
            for t in lookback_range]
        
        value = sum([state_values[t] 
            if policy_predictions[t] == \
                actions[t + lo_lookback_index].transmission_band else 0 
            for t in range(len(lookback_range))])

        return value

    def bandwidth_prediction_function(self, game_state: GameState) -> int:
        policy_values = [self.get_policy_value(policy, game_state.actions) 
            for policy in game_state.policy_list] 

        policy_id = np.argmax(policy_values)

        return game_state.policy_list[policy_id].get_bandwidth(game_state.t)

    def __init__(self) -> None:
        self.gamma = 0.3
        self.max_lookback = 5
        super().__init__(self.bandwidth_prediction_function)