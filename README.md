# LGMVIP-DataScience-Pencil-Sketch-Conversion-

Here I have used 2 methods for working on the task

In the imgtosktch.py, I worked directly without any function by just taking input and doing the below process:
Step 1: Convert to Grey Image. Using cvtColor function of OpenCV. ...
Step 2: Invert Image.
Step 3: Blur image.
Step 4: Invert Blurred Image. 
Step 5: Sketch.
Step 6: Save Sketch. 
Step 7: Display sketch.


In the img_2_pencil.py, I have worked by defining functio and a small use of numpy.copy for copying the image object to process in the function.
In defining the function for convert , i have used the same above mentioned process from step 1 to step 6

Refrence : https://thecleverprogrammer.com/2020/09/30/pencil-sketch-with-python/
