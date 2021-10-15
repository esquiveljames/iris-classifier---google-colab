from ._anvil_designer import iris_classifier_formTemplate
from anvil import *
import anvil.server

class iris_classifier_form(iris_classifier_formTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.

  def categorise_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    if self.sepal_length.text and self.sepal_width.text and self.petal_length.text and self.petal_width.text:
      iris_category = anvil.server.call('predict_iris', self.sepal_length.text,
                                  self.sepal_width.text,
                                  self.petal_length.text,
                                  self.petal_width.text)
      if iris_category:
        self.species_label.visible, self.iris_image.visible = True, True
        self.species_label.text = "The species is " + iris_category.capitalize()
        # Add image to app to correspond with classification
        if iris_category == 'virginica':
          self.iris_image.source = 'https://upload.wikimedia.org/wikipedia/commons/f/f8/Iris_virginica_2.jpg'
          self.iris_image.tooltip = 'Eric Hunt / CC BY-SA (https://creativecommons.org/licenses/by-sa/4.0)'
        elif iris_category == 'versicolor':
          self.iris_image.source = 'https://upload.wikimedia.org/wikipedia/commons/2/27/Blue_Flag%2C_Ottawa.jpg'
          self.iris_image.tooltip = 'D. Gordon E. Robertson / CC BY-SA (https://creativecommons.org/licenses/by-sa/3.0)'
        elif iris_category == 'setosa':
          self.iris_image.source = 'https://upload.wikimedia.org/wikipedia/commons/5/56/Kosaciec_szczecinkowaty_Iris_setosa.jpg'
        else:
          anvil.Notification("Species unknown", timeout=2).show()
    else:
      anvil.Notification("Please enter some data", timeout=2).show()
      
    


