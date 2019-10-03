# Supervised Deep-learning AI

In this project, I created AI using alexnet model.

to play high-way racer, simple web game.

![highway racer ai](https://media.giphy.com/media/QxpHXm8IgVqGMQnKlR/200w_d.gif)

## First, create the data

Done by recording yourself playing the game

1. enter [game site](https://www.crazygames.com/game/highway-racer)
2. pick the type of game you want to play
3. cd highway-racer-ai
4. run python create_training_data.py
5. when you done playing, press Q to quit the record

## Balance the data

most of the actions are going straight forward.

to prevent the AI to make this as 90% of the choices, I've balanced the data

to make almost equally data spread.

therefore run python balance_data.py

## Training model

once there is *enough data*, train the model by executing the train_model.py script.

*enough data* - The more mass of data you got, the better the training, for excellent results start with 1k for each
the action you got.

## Test model
the D-Day for the model.
1. enter [game site](https://www.crazygames.com/game/highway-racer)
2. pick the type of game you recorded playing
3. run the test_model.py script, and the AI is controlling the output keys.

