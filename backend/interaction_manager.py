from backend.recipe import Recipe
from backend.utils import get_recipes_from_commend
from backend.bot import ask
from backend.constants import RECIPE_COLUMN, RECIPE_OPTIONS_COUNT


class InteractionManager(object):
    def __init__(self, socManager):
        self.socManager = socManager
        self.recipe = None

    def display_single_message(self, message):
        self.socManager.emit_message("voice_command_bot_response", message)

    def display_single_message_user_input(self, message):
        self.socManager.emit_message("voice_command_bot_input", message)

    def display_multiple_messages(self, messages):
        self.socManager.emit_data(
            "voice_command_bot_response_output_multiple", messages)

    def startInteraction(self, command="", returned=False):
        if returned == True:
            while not command:
                question = "What next do you want to do? Else you may exit the conversation."
                self.display_single_message(question)
                command = ask(question)
                if command == 0:
                    return 0
        else:
            if not command:
                question = "What can I do for you?"
                self.display_single_message(question)
                command = ask("What can I do for you?")
            if command == 0:
                self.socManager.emit_message("end_connection", "Goodbye")
                return 0

        self.display_single_message_user_input(command)
        self.recipePrompt(command)

    def value_set_intersects(value, sets):
        return set(value.split()).intersection(sets)

    def recipePrompt(self, command=None):
        while not command:
            command = ask(
                "What are you craving for today? Else say 'Goodbye' to exit.")
            if command == 0:
                self.socManager.emit_message("end_connection", "Goodbye")
                return 0
            self.display_single_message_user_input(command)

        all_recipes, recipe_name = get_recipes_from_commend(command)
        value = 100
        if len(all_recipes) > 1:
            # return json.dumps({"Select": all_recipes})
            message = "Here's what I found, which one do you want to cook? (First/Second/Third...)"
            all_recipe_names = all_recipes[RECIPE_COLUMN].tolist()[:5]
            self.display_multiple_messages(all_recipe_names)
            self.display_single_message(message)

            value = ask(message, all_recipe_names)

            if value == 0:
                self.socManager.emit_message("end_connection", "Goodbye")
                return 0

            value = 1
            for number_value, value_in_string in RECIPE_OPTIONS_COUNT.items():
                if len(self.value_set_intersects(value, set(value_in_string))) > 0:
                    value = number_value
                    break

            self.display_single_message_user_input(value)
            
        selected_recipe = all_recipes[all_recipes.index == list(all_recipes.index)[value-1]]
        recipe = Recipe(self.socManager, selected_recipe, command, recipe_name)
        self.startInteraction(returned=True)
