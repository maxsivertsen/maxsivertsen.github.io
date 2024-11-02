# Hide - Connects voila to current notebook
#!jupyter serverextension enable --sys-prefix voila

# Voila runs jpnb but hides the code cells and only displays the output (including the ipywidgets) as well as the markdown cells.

#import fastbook
#fastbook.setup_book()
from fastbook import *
from fastai.vision.widgets import *

# Load the model
path = Path()
path.ls(file_exts='.pkl')

learn_inf = load_learner(path/'export.pkl')

# Create a button widget
btn_upload = widgets.FileUpload()
btn_upload

# Create a clear_output widget
out_pl = widgets.Output()
out_pl.clear_output()

# Create a label widget
lbl_pred = widgets.Label()

# Create a run button widget
btn_run = widgets.Button(description='Classify')
btn_run

# Function to classify the image
def on_click_classify(change):
    img = PILImage.create(btn_upload.data[-1])
    out_pl.clear_output()
    with out_pl: display(img.to_thumb(128,128))
    pred,pred_idx,probs = learn_inf.predict(img)
    lbl_pred.value = f'Prediction: {pred}; Probability: {probs[pred_idx]:.04f}'

btn_run.on_click(on_click_classify)

# Create a Vertical Box (VBox) to hold the widgets
btn_upload = widgets.FileUpload()
VBox([widgets.Label('Select your forest!'),
      btn_upload, btn_run, out_pl, lbl_pred])

