# Detection and Classification of Tomato Diseases for Farmers in Nigeria.
Tomatoes hold immense significance not only in Nigerian cuisines but also as a major agricultural commodity in the country. 
Following the 2015 Nigeria tomato crisis triggered by diseases, significant investments were made in tomato production and pest management. 
As of 2024, fear among farmer still soar as to curb the problem; thats where this project comes in hand. This project focuses on applying computer vision techniques to detect early the presence of these unwanted disesases.

### Training
The training involved 4500 images which belonged to 3 classes (Early Blight, Late Blight, Healthy). The reading of the images of the images was done in batches of 32, with 80% assigned to training, 10% assigned to validation and 10% assigned to test.
The model achitecture involved one layer which contained the vgg19 layout, with the top set to false, as well as trainable also set to false and a second layer for the output of the training classes.
With 20 epochs, the output is analysed below
![train_vs_val](https://github.com/fosetorico/tomato_disease_detection/assets/14139087/6c6ffd45-2303-488c-80f2-8699c3529087)

### Testing
For the perpose of testing, a user interface using the React library with an API created using FastAPI was created, the saved was recruited in the API to foster an interaction with react frontend.
Below shows some result from the forntend/backend interaction
![frontend](https://github.com/fosetorico/tomato_disease_detection/assets/14139087/5e2dec56-d869-4c5c-af82-03cab8317528)
![frontend_2](https://github.com/fosetorico/tomato_disease_detection/assets/14139087/4cf199fc-436b-4fed-b98b-1eeacc69f1ee)
