url_dataset = "https://drive.google.com/uc?id=10FNKOmS8P_d_ex8L4YopqULp6jkaJmYs"

total_time_questions = ["What is the total time to cook",
                        "How much time will it take to get the recipe ready",
                        "What is the recipe total time",
                        "how much total time",
                        "how long does it take to cook",
                        "how long does it take to totally cook this recipe",
                        "how long does it take to total cook the dish",
                        "how long does it take to cook the total meal",
                        "how long does it take to cook this total meal"]

cook_time_questions = ["how much cooking time",
                       "how long cooking time",
                       "how long to cook",
                       "how much time to ",
                       "how long to ",
                       "how much time to ",
                       "how much time to dish",
                       "how long to the meal"]

prep_time_questions = ["how much preparation time",
                       "how long preparation time",
                       "how long to prepare",
                       "how much time to prepare",
                       "how long to prepare the recipe",
                       "how much time to prepare the recipe",
                       "how long to prepare the dish",
                       "how much time to prepare the dish",
                       "how long to prepare the meal",
                       "how much time to prepare the meal",
                       "how long to prepare the food",
                       "how much time to prepare the food",
                       "how long to prepare the meal",
                       "how much time to prepare the meal",
                       "how long to prepare the food",
                       "how much time to prepare the food"]

ingredients_questions = ["what are the ingredients",
                         "what are the ingredients of the recipe",
                         "what are the ingredients of the dish",
                         "what are the ingredients of the meal",
                         "what are the ingredients of the food",
                         "what are the ingredients of the meal",
                         "what are the ingredients of the food"]

serving_questions = ["How many servings",
                     "How many people can be served",
                     "How many people can be served with this recipe",
                     "How many people can be served with this dish",
                     "How many people can be served with this meal",
                     "How many people can be served with this food",
                     "How many people can be served with this meal",
                     "How many people can be served with this food"]

instruction_questions = ["how to make",
                         "how to prepare",
                         "how to cook",
                         "how to make the recipe",
                         "how to make the dish",
                         "how to make the meal",
                         "how to make the food",
                         "how to make the meal",
                         "how to make the food",
                         "how to prepare the recipe",
                         "how to prepare the dish",
                         "how to prepare the meal",
                         "how to prepare the food",
                         "how to prepare the meal",
                         "how to prepare the food",
                         "how to cook the recipe",
                         "how to cook the dish",
                         "how to cook the meal",
                         "how to cook the food",
                         "how to cook the meal",
                         "how to cook the food",
                         "how to cook",
                         "what are instructions",
                         "how to bake",
                         "tell me recipe of",
                         "how many steps"
                         ]

INGREDIENTS_COLUMN = "TranslatedIngredients"
RECIPE_COLUMN = "TranslatedRecipeName"
PREPTIME_COLUMN = "PrepTimeInMins"
COOKTIME_COLUMN = "CookTimeInMins"
TOTALTIME_COLUMN = "TotalTimeInMins"
INSTRUCTIONS_COLUMN = "TranslatedInstructions"
SERVING_COLUMN = "Servings"

RECIPE_OPTIONS_COUNT = {
    1: ["one", "top", "first", "1", "1st"],
    2: ["two", "second", "2nd", "2"],
    3: ["three", "third", "3rd", "3"],
    4: ["four", "fourth", "4th", "4"],
    5: ["five", "fifth", "5th", "5"]
}
