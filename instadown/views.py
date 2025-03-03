from django.shortcuts import render
from .forms import VideoDownloadForm
import instaloader

def download_video(request):
    if request.method == 'POST':
        form = VideoDownloadForm(request.POST)
        if form.is_valid():
            video_url = form.cleaned_data['video_url']
            # Logic to download video using Instaloader
            L = instaloader.Instaloader()
            # Extract the shortcode from the URL
            shortcode = video_url.split('/')[-2]
            L.download_post(instaloader.Post.from_shortcode(L.context, shortcode), target='downloads')
            return render(request, 'instadown/success.html', {'video_url': video_url})
    else:
        form = VideoDownloadForm()
    return render(request, 'instadown/download.html', {'form': form})

def landing_page(request):
    return render(request, 'instadown/landing_page.html')