# **Project Description: New Restaurant Generator**

## **Introduction:**
The New Restaurant Generator is a creative tool designed to assist entrepreneurs and restaurant owners in brainstorming ideas for opening a new restaurant. It leverages the power of AI, specifically OpenAI's language model, to suggest restaurant names and menu items based on the chosen cuisine. This project aims to streamline the initial planning stage of starting a restaurant business by offering creative suggestions tailored to the user's preferences.

## **Project Components:**

1. **OpenAI Integration:**
   - The project utilizes the OpenAI GPT-3.5 language model for generating restaurant names and menu items.
   - It sets the model's temperature to 0.6, which controls the randomness of the generated responses.

2. **Prompt Templates:**
   - The project defines two prompt templates for interaction with the language model.
   - The first template takes the user's chosen cuisine and asks for a restaurant name suggestion.
   - The second template takes the generated restaurant name and asks for menu items.

3. **Chains:**
   - The project uses Langchain's SequentialChain to create a sequence of interactions with the language model.
   - It combines the name_chain and items_chain for a two-step process.

4. **Streamlit Frontend:**
   - The frontend is built using Streamlit, which allows users to interact with the project via a user-friendly interface.
   - Users can select a cuisine type from a list and trigger the AI's suggestions.

5. **Cuisine List:**
   - The project provides a list of cuisine types for users to choose from when seeking restaurant suggestions.
   - This list includes a wide variety of cuisines, from Italian to Ethiopian, and even an "Any" option for more generic suggestions.

## **How It Works:**
1. Users visit the Streamlit interface and select a cuisine type from the dropdown menu.
2. Upon selecting a cuisine, the project triggers the data generation process.
3. The AI, powered by OpenAI's GPT-3.5, suggests a restaurant name and a list of menu items based on the chosen cuisine.
4. The AI's suggestions are displayed in the Streamlit interface.
5. Users can explore the suggested restaurant name and menu items for inspiration.

## **Benefits:**
- Provides creative and personalized suggestions for restaurant names and menu items.
- Saves time and effort in brainstorming ideas for a new restaurant.
- Offers a wide range of cuisine options to cater to different tastes and preferences.
- Streamlines the early planning phase of opening a restaurant.

## **Note:**
This project's success depends on the quality of AI-generated suggestions, which may vary based on the input and the language model. Users are encouraged to use the generated suggestions as a starting point for their restaurant concepts and adapt them to their specific vision and market.
