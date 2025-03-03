from django import forms

class VideoDownloadForm(forms.Form):
    video_url = forms.URLField(label='Instagram Video URL', required=True)