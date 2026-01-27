import requests
import os

def generate_image():
    # The URL from the original README
    url = "https://pixel-profile.vercel.app/api/github-stats?username=Nahiyus512&theme=crt&pixelate_avatar=true&screen_effect=true"
    
    print(f"Fetching image from {url}...")
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        # Determine file extension based on content type
        content_type = response.headers.get('content-type', '')
        if 'image/png' in content_type:
            filename = "stats.png"
        elif 'image/jpeg' in content_type:
            filename = "stats.jpg"
        else:
            # Default to svg as pixel-profile usually returns svg
            filename = "stats.svg"
            
        with open(filename, "wb") as f:
            f.write(response.content)
            
        print(f"Successfully saved image to {filename}")
        
    except Exception as e:
        print(f"Failed to generate image: {e}")
        exit(1)

if __name__ == "__main__":
    generate_image()
