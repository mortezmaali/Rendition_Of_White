import cv2
import numpy as np
import time

# Set up the window to match the laptop screen size
screen_width = 1920  # Replace with your screen width
screen_height = 1080  # Replace with your screen height

# Create an initial blank screen with white level 0.7
white_level = 0.7
screen = np.ones((screen_height, screen_width, 3), dtype=np.float32) * white_level

# Split the text into two lines
text_line1 = "Which one do you think"
text_line2 = "is the true white?"

font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 3
font_thickness = 7

# Function to overlay the text in the center of the screen, split into two lines
def draw_text(image):
    # Get text sizes for both lines
    text_size1 = cv2.getTextSize(text_line1, font, font_scale, font_thickness)[0]
    text_size2 = cv2.getTextSize(text_line2, font, font_scale, font_thickness)[0]
    
    # Calculate x and y positions for both lines to be centered
    text_x1 = (screen_width - text_size1[0]) // 2
    text_x2 = (screen_width - text_size2[0]) // 2
    text_y1 = (screen_height - text_size1[1]) // 2 - 40  # Adjust the vertical spacing between lines
    text_y2 = (screen_height + text_size2[1]) // 2 + 40
    
    # Draw the first line of text in black
    cv2.putText(image, text_line1, (text_x1, text_y1), font, font_scale, (0, 0, 0), font_thickness, lineType=cv2.LINE_AA)
    
    # Draw the second line of text in black
    cv2.putText(image, text_line2, (text_x2, text_y2), font, font_scale, (0, 0, 0), font_thickness, lineType=cv2.LINE_AA)

# Loop through different white levels and render progressively smaller rectangles
white_levels = [0.75, 0.775, 0.8, 0.825, 0.85, 0.875, 0.9, 0.925, 0.95, 0.975, 1.0]
rect_size_factor = 0.9  # Factor to reduce the rectangle size progressively

cv2.namedWindow('White Levels', cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty('White Levels', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

# Show the initial full white screen
draw_text(screen)
cv2.imshow('White Levels', screen)
cv2.waitKey(5000)  # Show for 5 seconds

for white in white_levels:
    # Reduce rectangle size
    rect_width = int(screen_width * rect_size_factor)
    rect_height = int(screen_height * rect_size_factor)
    top_left_x = (screen_width - rect_width) // 2
    top_left_y = (screen_height - rect_height) // 2

    # Create the smaller rectangle with the new white level
    cv2.rectangle(screen, (top_left_x, top_left_y), (top_left_x + rect_width, top_left_y + rect_height), (white, white, white), -1)
    
    # Redraw text to ensure it's on top
    draw_text(screen)

    # Show the updated screen
    cv2.imshow('White Levels', screen)
    cv2.waitKey(5000)  # Show each white level for 5 seconds

    # Update the size factor for the next rectangle
    rect_size_factor *= 0.9

cv2.destroyAllWindows()
