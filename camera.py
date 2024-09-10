import cv2
import tkinter as tk
from tkinter import Label, Canvas
from PIL import Image, ImageTk
import folium
import io
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from gmplot import gmplot

# Function to show the video feed
def show_video():
    _, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(frame)
    imgtk = ImageTk.PhotoImage(image=img)
    video_label.imgtk = imgtk
    video_label.configure(image=imgtk)
    video_label.after(10, show_video)

# Function to display Google Maps using Folium
def create_map():
    # Define a location (latitude, longitude)
    latitude, longitude = 37.7749, -122.4194
    map_obj = folium.Map(location=[latitude, longitude], zoom_start=14)
    
    # Save the map as an HTML file
    map_obj.save("map.html")
    
    # Load the map into a Tkinter Canvas
    with open("map.html", 'r') as f:
        map_html = f.read()
    
    return map_html

# Initialize Tkinter window
root = tk.Tk()
root.title("Object Detection and Google Maps Interface")

# Capture video from the camera
cap = cv2.VideoCapture(0)

# Create a frame for the video feed
video_frame = tk.Frame(root, width=400, height=400)
video_frame.pack(side="left", padx=10, pady=10)

# Create a frame for the map
map_frame = tk.Frame(root, width=400, height=400)
map_frame.pack(side="right", padx=10, pady=10)

# Video Label to display the camera feed
video_label = Label(video_frame)
video_label.pack()

# Show the video feed
show_video()

# Embed Google Maps into the interface
map_canvas = Canvas(map_frame, width=400, height=400)
map_canvas.pack()

# Here you can add the map as an image or embedded HTML
map_html = create_map()
map_label = tk.Label(map_frame, text="Google Map Display", padx=10, pady=10)
map_label.pack()

# Run the Tkinter main loop
root.mainloop()

# Release the video capture object
cap.release()
cv2.destroyAllWindows()
