from django.forms import ModelForm
from mapapp.models import Points

#FIELD_NAME_MAPPING = {
 #   'point_name': 'Mein Punkt'
#}

class PointsForm(ModelForm):
    #def add_prefix(self, field_name):
     #   # look up field name; return original if not found
      #  field_name = FIELD_NAME_MAPPING.get('point_name')
       # return super(PointsForm, self).add_prefix(field_name)

    #submit_button = SubmitButtonField(label="", ini)
    class Meta:
        model = Points
        fields = [
            'point_name', 'longitude', 'latitude'
        ]