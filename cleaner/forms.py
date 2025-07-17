from django import forms

class UploadFileForm(forms.Form):
    csv_file = forms.FileField()
    handle_missing = forms.BooleanField(required=False, initial=True, label="Handle Missing Values")
    apply_iqr = forms.BooleanField(required=False, initial=True, label="Remove Outliers (IQR)")
    encode_labels = forms.BooleanField(required=False, initial=True, label="Label Encode Categoricals")
    drop_dupes = forms.BooleanField(required=False, initial=True, label="Drop Duplicates")
    #drop_columns = forms.CharField(required=False, label="Drop Columns (comma-separated)")
