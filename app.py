# #http://127.0.0.1:5000/
# from flask import Flask, render_template, request, jsonify
# from werkzeug.utils import secure_filename
# from PIL import Image  # Import for image processing
# import os
# import numpy as np

# app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = 'static/uploads'

# # Ensure upload directory exists
# os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# @app.route('/')
# def index():
#     return render_template('index.html')

# def determine_skin_tone(rgb_avg):
#     r, g, b = rgb_avg
#     if r > 200 and g > 170 and b > 160:
#         return "Very Light"
#     elif r > 190 and g > 150 and b > 130:
#         return "Light"
#     elif r > 180 and g > 140 and b > 120:
#         return "Light-Medium"
#     elif r > 160 and g > 120 and b > 100:
#         return "Medium"
#     elif r > 130 and g > 100 and b > 90:
#         return "Medium-Dark"
#     elif r > 100 and g > 80 and b > 70:
#         return "Dark"
#     else:
#         return "Very Dark"

# def determine_skin_type(img):
#     # Convert image to grayscale for analysis
#     gray_image = img.convert("L")  # Convert to grayscale
#     img_data = np.array(gray_image)

#     # Calculate some basic features
#     average_brightness = np.mean(img_data)
#     standard_deviation = np.std(img_data)

#     # Example classification logic for skin type
#     if average_brightness < 100 and standard_deviation < 20:
#         return "Oily Skin"
#     elif average_brightness < 150 and standard_deviation > 40:
#         return "Dry Skin"
#     elif average_brightness >= 150 and average_brightness <= 180:
#         return "Combination Skin"
#     elif standard_deviation < 30:
#         return "Smooth Skin"
#     elif standard_deviation > 30 and average_brightness > 180:
#         return "Rough Skin"
#     elif average_brightness < 80:
#         return "Dark Circles"
#     elif average_brightness > 180 and standard_deviation < 15:
#         return "Normal Skin"
#     elif average_brightness > 150 and standard_deviation > 30:
#         return "Pigmented Skin"
#     else:
#         return "Unknown Skin Type"

# @app.route('/detect_skin', methods=['POST'])
# def detect_skin():
#     # Get the uploaded file
#     file = request.files.get('image')
    
#     if file:
#         filename = secure_filename(file.filename)
#         filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#         file.save(filepath)

#         # Load the image and calculate average RGB values
#         with Image.open(filepath) as img:
#             img = img.convert("RGB")  # Ensure it's in RGB format
#             img_data = np.array(img)
#             avg_rgb = np.mean(img_data, axis=(0, 1))  # Calculate the average RGB value

#         # Determine the skin tone based on the average RGB values
#         skin_tone_result = determine_skin_tone(avg_rgb)

#         # Determine the skin type based on the image
#         skin_type_result = determine_skin_type(img)

#         # Return results as JSON
#         return jsonify(skin_tone=skin_tone_result, skin_type=skin_type_result)
#     else:
#         return jsonify(result="No file uploaded"), 400

# def get_recommended_products_and_images(skin_type):
#     # Map of skin types to products and images
#     product_recommendations = {
#         "Oily Skin": [
#             ("Oil-free cleanser", "https://example.com/oil_free_cleanser.jpg"),
#             ("Mattifying moisturizer", "https://example.com/mattifying_moisturizer.jpg"),
#             ("Clay mask", "https://example.com/clay_mask.jpg"),
#             ("Salicylic acid serum", "https://example.com/salicylic_acid_serum.jpg")
#         ],
#         "Dry Skin": [
#             ("Hydrating cleanser", "https://example.com/hydrating_cleanser.jpg"),
#             ("Rich moisturizing cream", "https://example.com/rich_moisturizing_cream.jpg"),
#             ("Hyaluronic acid serum", "https://example.com/hyaluronic_acid_serum.jpg"),
#             ("Gentle exfoliator", "https://example.com/gentle_exfoliator.jpg")
#         ],
#         "Combination Skin": [
#             ("Balanced cleanser", "https://example.com/balanced_cleanser.jpg"),
#             ("Gel-based moisturizer", "https://example.com/gel_based_moisturizer.jpg"),
#             ("Exfoliating mask", "https://example.com/exfoliating_mask.jpg"),
#             ("Niacinamide serum", "https://example.com/niacinamide_serum.jpg")
#         ],
#         "Smooth Skin": [
#             ("Gentle cleanser", "https://example.com/gentle_cleanser.jpg"),
#             ("Lightweight moisturizer", "https://example.com/lightweight_moisturizer.jpg"),
#             ("Sunscreen with SPF 30+", "https://example.com/sunscreen_spf30.jpg"),
#             ("Brightening serum", "https://example.com/brightening_serum.jpg")
#         ],
#         "Rough Skin": [
#             ("Deep exfoliating scrub", "https://example.com/exfoliating_scrub.jpg"),
#             ("Repairing moisturizer", "https://example.com/repairing_moisturizer.jpg"),
#             ("Retinol cream", "https://example.com/retinol_cream.jpg"),
#             ("Vitamin C serum", "https://example.com/vitamin_c_serum.jpg")
#         ],
#         "Dark Circles": [
#             ("Eye cream with caffeine", "https://example.com/eye_cream_caffeine.jpg"),
#             ("Brightening under-eye serum", "https://example.com/under_eye_serum.jpg"),
#             ("Concealer", "https://example.com/concealer.jpg"),
#             ("Cooling eye mask", "https://example.com/cooling_eye_mask.jpg")
#         ],
#         "Normal Skin": [
#             ("Mild cleanser", "https://example.com/mild_cleanser.jpg"),
#             ("Daily moisturizer", "https://example.com/daily_moisturizer.jpg"),
#             ("Sunscreen", "https://example.com/sunscreen.jpg"),
#             ("All-purpose serum", "https://example.com/all_purpose_serum.jpg")
#         ],
#         "Pigmented Skin": [
#             ("Brightening serum with Vitamin C", "https://example.com/brightening_vitamin_c.jpg"),
#             ("SPF 50 sunscreen", "https://example.com/spf50_sunscreen.jpg"),
#             ("Niacinamide cream", "https://example.com/niacinamide_cream.jpg"),
#             ("Dark spot corrector", "https://example.com/dark_spot_corrector.jpg")
#         ],
#         "Unknown Skin Type": [
#             ("Consult a dermatologist for personalized recommendations", "https://example.com/consult_dermatologist.jpg")
#         ]
#     }

#     # Return the list of products and images for the given skin type
#     return product_recommendations.get(skin_type, [("No recommendations available", "https://example.com/no_image.jpg")])


# # if __name__ == '__main__':
# #     app.run(debug=True)
# if __name__ == "__main__":
#     # Load an example image (replace "example.jpg" with your image file)
#     image_path = "example.jpg"
#     try:
#         img = Image.open(image_path)

#         # Determine skin type
#         skin_type = determine_skin_type(img)
#         print(f"Detected Skin Type: {skin_type}")

#         # Get recommended products and images
#         products_and_images = get_recommended_products_and_images(skin_type)
#         print("Recommended Products and Images:")
#         for product, image_url in products_and_images:
#             print(f"- {product}: {image_url}")
#     except FileNotFoundError:
#         print("Error: Image file not found. Please provide a valid file path.")



















# #3
# # from flask import Flask, render_template, request, jsonify
# # from werkzeug.utils import secure_filename
# # from PIL import Image  # Import for image processing
# # import os
# # import numpy as np

# # app = Flask(__name__)
# # app.config['UPLOAD_FOLDER'] = 'static/uploads'

# # # Ensure upload directory exists
# # os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# # @app.route('/')
# # def index():
# #     return render_template('index.html')

# # def determine_skin_tone(rgb_avg):
# #     r, g, b = rgb_avg
# #     if r > 200 and g > 170 and b > 160:
# #         return "Very Light"
# #     elif r > 190 and g > 150 and b > 130:
# #         return "Light"
# #     elif r > 180 and g > 140 and b > 120:
# #         return "Light-Medium"
# #     elif r > 160 and g > 120 and b > 100:
# #         return "Medium"
# #     elif r > 130 and g > 100 and b > 90:
# #         return "Medium-Dark"
# #     elif r > 100 and g > 80 and b > 70:
# #         return "Dark"
# #     else:
# #         return "Very Dark"

# # def determine_skin_type(img):
# #     # Convert image to grayscale for analysis
# #     gray_image = img.convert("L")  # Convert to grayscale
# #     img_data = np.array(gray_image)

# #     # Calculate some basic features
# #     average_brightness = np.mean(img_data)
# #     standard_deviation = np.std(img_data)

# #     # Example classification logic for skin type
# #     if average_brightness < 100 and standard_deviation < 20:
# #         return "Oily Skin"
# #     elif average_brightness < 150 and standard_deviation > 40:
# #         return "Dry Skin"
# #     elif average_brightness >= 150 and average_brightness <= 180:
# #         return "Combination Skin"
# #     elif standard_deviation < 30:
# #         return "Smooth Skin"
# #     elif standard_deviation > 30 and average_brightness > 180:
# #         return "Rough Skin"
# #     elif average_brightness < 80:
# #         return "Dark Circles"
# #     elif average_brightness > 180 and standard_deviation < 15:
# #         return "Normal Skin"
# #     elif average_brightness > 150 and standard_deviation > 30:
# #         return "Pigmented Skin"
# #     else:
# #         return "Unknown Skin Type"

# # @app.route('/detect_skin', methods=['POST'])
# # def detect_skin():
# #     # Get the uploaded file
# #     file = request.files.get('image')
    
# #     if file:
# #         filename = secure_filename(file.filename)
# #         filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
# #         file.save(filepath)

# #         # Load the image and calculate average RGB values
# #         with Image.open(filepath) as img:
# #             img = img.convert("RGB")  # Ensure it's in RGB format
# #             img_data = np.array(img)
# #             avg_rgb = np.mean(img_data, axis=(0, 1))  # Calculate the average RGB value

# #         # Determine the skin tone based on the average RGB values
# #         skin_tone_result = determine_skin_tone(avg_rgb)

# #         # Determine the skin type based on the image
# #         skin_type_result = determine_skin_type(img)

# #         # Return results as JSON
# #         return jsonify(skin_tone=skin_tone_result, skin_type=skin_type_result)
# #     else:
# #         return jsonify(result="No file uploaded"), 400

# # if __name__ == '__main__':
# #     app.run(debug=True)








# #2

# # from flask import Flask, render_template, request, jsonify
# # from werkzeug.utils import secure_filename
# # from PIL import Image  # Import for image processing
# # import os
# # import numpy as np

# # app = Flask(__name__)
# # app.config['UPLOAD_FOLDER'] = 'static/uploads'

# # # Ensure upload directory exists
# # os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# # @app.route('/')
# # def index():
# #     return render_template('index.html')

# # def determine_skin_tone(rgb_avg):
# #     r, g, b = rgb_avg
# #     if r > 200 and g > 170 and b > 160:
# #         return "Very Light"
# #     elif r > 190 and g > 150 and b > 130:
# #         return "Light"
# #     elif r > 180 and g > 140 and b > 120:
# #         return "Light-Medium"
# #     elif r > 160 and g > 120 and b > 100:
# #         return "Medium"
# #     elif r > 130 and g > 100 and b > 90:
# #         return "Medium-Dark"
# #     elif r > 100 and g > 80 and b > 70:
# #         return "Dark"
# #     else:
# #         return "Very Dark"

# # def determine_skin_type(img):
# #     # Convert image to grayscale for analysis
# #     gray_image = img.convert("L")  # Convert to grayscale
# #     img_data = np.array(gray_image)

# #     # Calculate some basic features
# #     average_brightness = np.mean(img_data)
# #     standard_deviation = np.std(img_data)

# #     # Example classification logic for skin type
# #     if average_brightness < 100 and standard_deviation < 20:
# #         return "Oily Skin"
# #     elif average_brightness < 150 and standard_deviation > 40:
# #         return "Dry Skin"
# #     elif average_brightness >= 150 and average_brightness <= 180:
# #         return "Combination Skin"
# #     elif standard_deviation < 30:
# #         return "Smooth Skin"
# #     elif standard_deviation > 30 and average_brightness > 180:
# #         return "Rough Skin"
# #     elif average_brightness < 80:
# #         return "Dark Circles"
# #     elif average_brightness > 180 and standard_deviation < 15:
# #         return "Normal Skin"
# #     elif average_brightness > 150 and standard_deviation > 30:
# #         return "Pigmented Skin"
# #     else:
# #         return "Unknown Skin Type"

# # @app.route('/detect_skin', methods=['POST'])
# # def detect_skin():
# #     # Get the uploaded file
# #     file = request.files.get('image')
    
# #     if file:
# #         filename = secure_filename(file.filename)
# #         filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
# #         file.save(filepath)

# #         # Load the image and calculate average RGB values
# #         with Image.open(filepath) as img:
# #             img = img.convert("RGB")  # Ensure it's in RGB format
# #             img_data = np.array(img)
# #             avg_rgb = np.mean(img_data, axis=(0, 1))  # Calculate the average RGB value

# #         # Determine the skin tone based on the average RGB values
# #         skin_tone_result = determine_skin_tone(avg_rgb)

# #         # Determine the skin type based on the image
# #         skin_type_result = determine_skin_type(img)

# #         # Return results as JSON
# #         return jsonify(skin_tone=skin_tone_result, skin_type=skin_type_result)
# #     else:
# #         return jsonify(result="No file uploaded"), 400

# # if __name__ == '__main__':
# #     app.run(debug=True)





# #1

# # from flask import Flask, render_template, request, jsonify
# # from werkzeug.utils import secure_filename
# # from PIL import Image  # Import for image processing
# # import os
# # import numpy as np

# # app = Flask(__name__)
# # app.config['UPLOAD_FOLDER'] = 'static/uploads'

# # # Ensure upload directory exists
# # os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# # @app.route('/')
# # def index():
# #     return render_template('index.html')

# # def determine_skin_tone(rgb_avg):
# #     r, g, b = rgb_avg
# #     if r > 200 and g > 170 and b > 160:
# #         return "Very Light"
# #     elif r > 190 and g > 150 and b > 130:
# #         return "Light"
# #     elif r > 180 and g > 140 and b > 120:
# #         return "Light-Medium"
# #     elif r > 160 and g > 120 and b > 100:
# #         return "Medium"
# #     elif r > 130 and g > 100 and b > 90:
# #         return "Medium-Dark"
# #     elif r > 100 and g > 80 and b > 70:
# #         return "Dark"
# #     else:
# #         return "Very Dark"

# # @app.route('/detect_skin_tone', methods=['POST'])
# # def detect_skin_tone():
# #     # Get the uploaded file
# #     file = request.files.get('image')
    
# #     if file:
# #         filename = secure_filename(file.filename)
# #         filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
# #         file.save(filepath)

# #         # Load the image and calculate average RGB values
# #         with Image.open(filepath) as img:
# #             img = img.convert("RGB")  # Ensure it's in RGB format
# #             img_data = np.array(img)
# #             avg_rgb = np.mean(img_data, axis=(0, 1))  # Calculate the average RGB value

# #         # Determine the skin tone based on the average RGB values
# #         skin_tone_result = determine_skin_tone(avg_rgb)

# #         # Return result as JSON
# #         return jsonify(result=skin_tone_result)
# #     else:
# #         return jsonify(result="No file uploaded"), 400

# # if __name__ == '__main__':
# #     app.run(debug=True)



















# # from flask import Flask, render_template, request, jsonify
# # from werkzeug.utils import secure_filename
# # from PIL import Image  # Import for image processing
# # import os
# # import numpy as np

# # app = Flask(__name__)
# # app.config['UPLOAD_FOLDER'] = 'static/uploads'

# # # Ensure upload directory exists
# # os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# # @app.route('/')
# # def index():
# #     return render_template('index.html')

# # @app.route('/detect_skin_tone', methods=['POST'])
# # def detect_skin_tone():
# #     # Get the uploaded file
# #     file = request.files.get('image')
    
# #     if file:
# #         filename = secure_filename(file.filename)
# #         filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
# #         file.save(filepath)

# #         # Load the image and calculate average RGB values
# #         with Image.open(filepath) as img:
# #             img = img.convert("RGB")  # Ensure it's in RGB format
# #             img_data = np.array(img)
# #             avg_rgb = np.mean(img_data, axis=(0, 1))  # Calculate the average RGB value
            
# #         # Define skin tone ranges and assign labels based on average RGB
# #         if avg_rgb[0] > 200 and avg_rgb[1] > 160 and avg_rgb[2] > 120:
# #             skin_tone_result = "Light Skin Tone"
# #         elif avg_rgb[0] > 150 and avg_rgb[1] > 110 and avg_rgb[2] > 90:
# #             skin_tone_result = "Medium Skin Tone"
# #         else:
# #             skin_tone_result = "Dark Skin Tone"
        
# #         # Return result as JSON
# #         return jsonify(result=skin_tone_result)
# #     else:
# #         return jsonify(result="No file uploaded"), 400

# # if __name__ == '__main__':
# #     app.run(debug=True)









# from flask import Flask, request, jsonify, render_template
# import numpy as np
# import cv2
# from keras.models import load_model

# app = Flask(__name__)

# # Load your pre-trained model
# model = load_model('model/skin_tone_detection_model.h5')
# IMAGE_SIZE = (128, 128)  # Update as necessary

# # Define labels
# labels = ['your skin tone is black', 'your skin tone is brown', 'your skin tone is white']  # Adjust the order accordingly

# @app.route('/')
# def home():
#     return render_template('index.html')  # Render your HTML template

# @app.route('/predict', methods=['POST'])
# def predict_skin_tone():
#     if 'file' not in request.files:
#         return jsonify({'error': 'No file provided'}), 400

#     file = request.files['file']
#     if file.filename == '':
#         return jsonify({'error': 'No file selected'}), 400

#     # Read the image file
#     img = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_COLOR)
#     img = cv2.resize(img, IMAGE_SIZE)
#     img = img.astype('float32') / 255.0
#     img = np.expand_dims(img, axis=0)  # Add batch dimension

#     # Make prediction
#     prediction = model.predict(img)
#     predicted_class_index = np.argmax(prediction)
#     predicted_label = labels[predicted_class_index]

#     return jsonify({'predicted_skin_tone': predicted_label})

# if __name__ == '__main__':
#     app.run(debug=True)



# from flask import Flask, render_template, request, jsonify
# from werkzeug.utils import secure_filename
# from PIL import Image  # Import for image processing
# import os
# import numpy as np

# app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = 'static/uploads'

# # Ensure upload directory exists
# os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# @app.route('/')
# def index():
#     return render_template('index.html')

# def determine_skin_tone(rgb_avg):
#     r, g, b = rgb_avg
#     if r > 200 and g > 170 and b > 160:
#         return "Very Light"
#     elif r > 190 and g > 150 and b > 130:
#         return "Light"
#     elif r > 180 and g > 140 and b > 120:
#         return "Light-Medium"
#     elif r > 160 and g > 120 and b > 100:
#         return "Medium"
#     elif r > 130 and g > 100 and b > 90:
#         return "Medium-Dark"
#     elif r > 100 and g > 80 and b > 70:
#         return "Dark"
#     else:
#         return "Very Dark"

# def determine_skin_type(img):
#     gray_image = img.convert("L")  # Convert to grayscale
#     img_data = np.array(gray_image)

#     # Calculate basic features
#     average_brightness = np.mean(img_data)
#     standard_deviation = np.std(img_data)

#     # Example classification logic for skin type
#     if average_brightness < 100 and standard_deviation < 20:
#         return "Oily Skin"
#     elif average_brightness < 150 and standard_deviation > 40:
#         return "Dry Skin"
#     elif average_brightness >= 150 and average_brightness <= 180:
#         return "Combination Skin"
#     elif standard_deviation < 30:
#         return "Smooth Skin"
#     elif standard_deviation > 30 and average_brightness > 180:
#         return "Rough Skin"
#     elif average_brightness < 80:
#         return "Dark Circles"
#     elif average_brightness > 180 and standard_deviation < 15:
#         return "Normal Skin"
#     elif average_brightness > 150 and standard_deviation > 30:
#         return "Pigmented Skin"
#     else:
#         return "Unknown Skin Type"

# def get_recommended_products_and_images(skin_type):
#     product_recommendations = {
#         "Oily Skin": [
#             ("Oil-free cleanser", "https://example.com/oil_free_cleanser.jpg"),
#             ("Mattifying moisturizer", "https://example.com/mattifying_moisturizer.jpg"),
#             ("Clay mask", "https://example.com/clay_mask.jpg"),
#             ("Salicylic acid serum", "https://example.com/salicylic_acid_serum.jpg")
#         ],
#         "Dry Skin": [
#             ("Hydrating cleanser", "https://example.com/hydrating_cleanser.jpg"),
#             ("Rich moisturizing cream", "https://example.com/rich_moisturizing_cream.jpg"),
#             ("Hyaluronic acid serum", "https://example.com/hyaluronic_acid_serum.jpg"),
#             ("Gentle exfoliator", "https://example.com/gentle_exfoliator.jpg")
#         ],
#         "Combination Skin": [
#             ("Balanced cleanser", "https://example.com/balanced_cleanser.jpg"),
#             ("Gel-based moisturizer", "https://example.com/gel_based_moisturizer.jpg"),
#             ("Exfoliating mask", "https://example.com/exfoliating_mask.jpg"),
#             ("Niacinamide serum", "https://example.com/niacinamide_serum.jpg")
#         ],
#         # Add other skin types similarly...
#         "Unknown Skin Type": [
#             ("Consult a dermatologist for personalized recommendations", "https://example.com/consult_dermatologist.jpg")
#         ]
#     }
#     return product_recommendations.get(skin_type, [("No recommendations available", "https://example.com/no_image.jpg")])

# @app.route('/detect_skin', methods=['POST'])
# def detect_skin():
#     file = request.files.get('image')
    
#     if file:
#         filename = secure_filename(file.filename)
#         filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#         file.save(filepath)

#         with Image.open(filepath) as img:
#             img = img.convert("RGB")  # Ensure it's in RGB format
#             img_data = np.array(img)
#             avg_rgb = np.mean(img_data, axis=(0, 1))  # Calculate average RGB

#         skin_tone_result = determine_skin_tone(avg_rgb)
#         skin_type_result = determine_skin_type(img)
#         products_and_images = get_recommended_products_and_images(skin_type_result)

#         return jsonify(
#             skin_tone=skin_tone_result,
#             skin_type=skin_type_result,
#             products=products_and_images
#         )
#     else:
#         return jsonify(result="No file uploaded"), 400

# if __name__ == "__main__":
#     app.run(debug=True)



#correct
# from flask import Flask, render_template, request, jsonify
# from werkzeug.utils import secure_filename
# from PIL import Image  # Import for image processing
# import os
# import numpy as np

# app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = 'static/uploads'

# # Ensure upload directory exists
# os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# @app.route('/')
# def index():
#     return render_template('index.html')

# # Function to determine skin tone based on RGB values
# def determine_skin_tone(rgb_avg):
#     r, g, b = rgb_avg
#     if r > 200 and g > 170 and b > 160:
#         return "Very Light"
#     elif r > 190 and g > 150 and b > 130:
#         return "Light"
#     elif r > 180 and g > 140 and b > 120:
#         return "Light-Medium"
#     elif r > 160 and g > 120 and b > 100:
#         return "Medium"
#     elif r > 130 and g > 100 and b > 90:
#         return "Medium-Dark"
#     elif r > 100 and g > 80 and b > 70:
#         return "Dark"
#     else:
#         return "Very Dark"

# # Function to determine skin type (oily, dry, etc.) based on image
# def determine_skin_type(img):
#     gray_image = img.convert("L")  # Convert to grayscale
#     img_data = np.array(gray_image)

#     # Calculate basic features
#     average_brightness = np.mean(img_data)
#     standard_deviation = np.std(img_data)

#     # Example classification logic for skin type
#     if average_brightness < 100 and standard_deviation < 20:
#         return "Oily Skin"
#     elif average_brightness < 150 and standard_deviation > 40:
#         return "Dry Skin"
#     elif average_brightness >= 150 and average_brightness <= 180:
#         return "Combination Skin"
#     elif standard_deviation < 30:
#         return "Smooth Skin"
#     elif standard_deviation > 30 and average_brightness > 180:
#         return "Rough Skin"
#     elif average_brightness < 80:
#         return "Dark Circles"
#     elif average_brightness > 180 and standard_deviation < 15:
#         return "Normal Skin"
#     elif average_brightness > 150 and standard_deviation > 30:
#         return "Pigmented Skin"
#     else:
#         return "Unknown Skin Type"

# # Function to map products based on skin type
# def get_recommended_products_and_images(skin_type):
#     product_recommendations = {
#         "Oily Skin": [
#             ("Oil-free cleanser", "https://example.com/oil_free_cleanser.jpg"),
#             ("Mattifying moisturizer", "https://example.com/mattifying_moisturizer.jpg"),
#             ("Clay mask", "https://example.com/clay_mask.jpg"),
#             ("Salicylic acid serum", "https://example.com/salicylic_acid_serum.jpg")
#         ],
#         "Dry Skin": [
#             ("Hydrating cleanser", "https://example.com/hydrating_cleanser.jpg"),
#             ("Rich moisturizing cream", "https://example.com/rich_moisturizing_cream.jpg"),
#             ("Hyaluronic acid serum", "https://example.com/hyaluronic_acid_serum.jpg"),
#             ("Gentle exfoliator", "https://example.com/gentle_exfoliator.jpg")
#         ],
#         "Combination Skin": [
#             ("Balanced cleanser", "https://example.com/balanced_cleanser.jpg"),
#             ("Gel-based moisturizer", "https://example.com/gel_based_moisturizer.jpg"),
#             ("Exfoliating mask", "https://example.com/exfoliating_mask.jpg"),
#             ("Niacinamide serum", "https://example.com/niacinamide_serum.jpg")
#         ],
#         # Add other skin types similarly...
#         "Unknown Skin Type": [
#             ("Consult a dermatologist for personalized recommendations", "https://example.com/consult_dermatologist.jpg")
#         ]
#     }
#     return product_recommendations.get(skin_type, [("No recommendations available", "https://example.com/no_image.jpg")])

# @app.route('/detect_skin', methods=['POST'])
# def detect_skin():
#     file = request.files.get('image')
    
#     if file:
#         filename = secure_filename(file.filename)
#         filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#         file.save(filepath)

#         with Image.open(filepath) as img:
#             img = img.convert("RGB")  # Ensure it's in RGB format
#             img_data = np.array(img)
#             avg_rgb = np.mean(img_data, axis=(0, 1))  # Calculate average RGB

#         skin_tone_result = determine_skin_tone(avg_rgb)
#         skin_type_result = determine_skin_type(img)
#         products_and_images = get_recommended_products_and_images(skin_type_result)

#         return jsonify(
#             skin_tone=skin_tone_result,
#             skin_type=skin_type_result,
#             products=products_and_images
#         )
#     else:
#         return jsonify(result="No file uploaded"), 400

# if __name__ == "__main__":
    # app.run(debug=True)



# from flask import Flask, request, jsonify
# from werkzeug.utils import secure_filename
# import os

# app = Flask(__name__)

# # Configure upload folder
# UPLOAD_FOLDER = 'uploads'
# ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# def allowed_file(filename):
#     return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# @app.route('/detect_skin', methods=['POST'])
# def detect_skin():
#     if 'image' not in request.files:
#         return jsonify({'result': 'No image file provided'}), 400

#     file = request.files['image']
#     if file and allowed_file(file.filename):
#         filename = secure_filename(file.filename)
#         file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#         file.save(file_path)

#         # Process the image here for skin tone detection
#         skin_tone = "fair"  # Example response
#         skin_type = "dry"  # Example response
#         products = [
#             ["Moisturizer", "https://example.com/moisturizer.jpg"],
#             ["Sunscreen", "https://example.com/sunscreen.jpg"]
#         ]
        
#         return jsonify({
#             'skin_tone': skin_tone,
#             'skin_type': skin_type,
#             'products': products
#         })
#     else:
#         return jsonify({'result': 'Invalid file type'}), 400

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
from PIL import Image  # Import for image processing
import os
import numpy as np

app = Flask(__name__)

# Configure upload folder and allowed extensions
UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure upload directory exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Function to determine skin tone based on RGB values
def determine_skin_tone(rgb_avg):
    r, g, b = rgb_avg
    if r > 200 and g > 170 and b > 160:
        return "Very Light"
    elif r > 190 and g > 150 and b > 130:
        return "Light"
    elif r > 180 and g > 140 and b > 120:
        return "Light-Medium"
    elif r > 160 and g > 120 and b > 100:
        return "Medium"
    elif r > 130 and g > 100 and b > 90:
        return "Medium-Dark"
    elif r > 100 and g > 80 and b > 70:
        return "Dark"
    else:
        return "Very Dark"

# Function to determine skin type (oily, dry, etc.) based on image
def determine_skin_type(img):
    gray_image = img.convert("L")  # Convert to grayscale
    img_data = np.array(gray_image)

    # Calculate basic features
    average_brightness = np.mean(img_data)
    standard_deviation = np.std(img_data)

    # Example classification logic for skin type
    if average_brightness < 100 and standard_deviation < 20:
        return "Oily Skin"
    elif average_brightness < 150 and standard_deviation > 40:
        return "Dry Skin"
    elif average_brightness >= 150 and average_brightness <= 180:
        return "Combination Skin"
    elif standard_deviation < 30:
        return "Smooth Skin"
    elif standard_deviation > 30 and average_brightness > 180:
        return "Rough Skin"
    elif average_brightness < 80:
        return "Dark Circles"
    elif average_brightness > 180 and standard_deviation < 15:
        return "Normal Skin"
    elif average_brightness > 150 and standard_deviation > 30:
        return "Pigmented Skin"
    else:
        return "Unknown Skin Type"

# Function to map products based on skin type
def get_recommended_products_and_images(skin_type):
    product_recommendations = {
        "Oily Skin": [
            ("Oil-free cleanser", "static/images/oily1.jpg"),
            ("Mattifying moisturizer", "static/images/oily2.webp"),
            ("Clay mask", "static/images/oily3.jpg"),
            ("Salicylic acid serum", "static/images/oily4.webp")
        ],
        "Dry Skin": [
            ("Hydrating cleanser", "static/images/dry1.jpg"),
            ("Rich moisturizing cream", "static/images/dry2.webp"),
            ("Hyaluronic acid serum", "static/images/dry3.jpg"),
            ("Gentle exfoliator", "static/images/dry4.jpg")
        ],
        "Combination Skin": [
            ("Balanced cleanser", "static/images/comb1.jpg"),
            ("Gel-based moisturizer", "static/images/comb2.jpg"),
            ("Exfoliating mask", "static/images/comb3.webp"),
            ("Niacinamide serum", "static/images/comb4.webp")
        ],
        "Unknown Skin Type": [
            ("Consult a dermatologist for personalized recommendations", "static/images/consult_dermatologist.jpg")
        ]
    }
    return product_recommendations.get(skin_type, [("No recommendations available", "static/images/no_image.jpg")])
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/detect_skin', methods=['POST'])
def detect_skin():
    if 'image' not in request.files:
        return jsonify({'result': 'No image file provided'}), 400

    file = request.files['image']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        # Process the image here for skin tone detection
        with Image.open(file_path) as img:
            img = img.convert("RGB")  # Ensure it's in RGB format
            img_data = np.array(img)
            avg_rgb = np.mean(img_data, axis=(0, 1))  # Calculate average RGB

        skin_tone_result = determine_skin_tone(avg_rgb)
        skin_type_result = determine_skin_type(img)
        products_and_images = get_recommended_products_and_images(skin_type_result)

        return jsonify({
            'skin_tone': skin_tone_result,
            'skin_type': skin_type_result,
            'products': products_and_images
        })
    else:
        return jsonify({'result': 'Invalid file type'}), 400

if __name__ == '__main__':
    app.run(debug=True)




# from flask import Flask, render_template, request, jsonify
# from werkzeug.utils import secure_filename
# from PIL import Image
# import os
# import numpy as np

# app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = 'static/uploads'

# # Ensure upload directory exists
# os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# @app.route('/')
# def index():
#     return render_template('index.html')

# def determine_skin_tone(rgb_avg):
#     r, g, b = rgb_avg
#     if r > 200 and g > 170 and b > 160:
#         return "Very Light"
#     elif r > 190 and g > 150 and b > 130:
#         return "Light"
#     elif r > 180 and g > 140 and b > 120:
#         return "Light-Medium"
#     elif r > 160 and g > 120 and b > 100:
#         return "Medium"
#     elif r > 130 and g > 100 and b > 90:
#         return "Medium-Dark"
#     elif r > 100 and g > 80 and b > 70:
#         return "Dark"
#     else:
#         return "Very Dark"

# def determine_skin_type(img):
#     gray_image = img.convert("L")
#     img_data = np.array(gray_image)
#     avg_brightness = np.mean(img_data)
#     std_deviation = np.std(img_data)
#     if avg_brightness < 100 and std_deviation < 20:
#         return "Oily Skin"
#     elif avg_brightness < 150 and std_deviation < 30:
#         return "Normal Skin"
#     else:
#         return "Dry Skin"

# @app.route('/detect_skin', methods=['POST'])
# def detect_skin():
#     if 'image' not in request.files:
#         return jsonify({'result': 'No file uploaded'}), 400

#     image_file = request.files['image']
#     if image_file.filename == '':
#         return jsonify({'result': 'No selected file'}), 400

#     # Save the uploaded file
#     filename = secure_filename(image_file.filename)
#     filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#     image_file.save(filepath)

#     # Open image
#     img = Image.open(filepath)
#     img = img.resize((300, 300))  # Resize image for consistency

#     # Calculate average RGB values
#     img_data = np.array(img)
#     avg_rgb = np.mean(img_data, axis=(0, 1))

#     # Determine skin tone and skin type
#     skin_tone = determine_skin_tone(avg_rgb)
#     skin_type = determine_skin_type(img)

#     # Here you could return recommended products based on the skin tone and skin type
#     recommended_products = [
#         ("Sunscreen for Medium Skin", "https://example.com/medium_sunscreen.jpg"),
#         ("Moisturizer for Dry Skin", "https://example.com/dry_skin_moisturizer.jpg")
#     ]

#     return jsonify({
#         'skin_tone': skin_tone,
#         'skin_type': skin_type,
#         'products': recommended_products
#     })

# if __name__ == '__main__':
#     app.run(debug=True)

