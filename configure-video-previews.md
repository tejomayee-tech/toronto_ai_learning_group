An iframe is a window to another webpage (in this case, the Google Drive previewer). You can't tell the Google Drive player to "hide its video and show this specific image instead" using standard Markdown or HTML attributes.

However, you can achieve a professional "thumbnail" look using a few clever workarounds. Here are the best ways to handle this in MkDocs:

### Option 1: The "Poster Image" Link (Recommended)

Since you want an image instead of the video frame, the most reliable method is to display a static image that, when clicked, opens the video in a new tab. This is much faster for page load times.

```markdown
### Numpy Session 1

[![Numpy Session 1 Thumbnail](path/to/your/custom-image.png)](https://drive.google.com/file/d/1-QsdfqwegasgwwrgedKYOW/view)

*Click the image above to watch the session.*

```

### Option 2: The "Click-to-Play" Overlay (Advanced)

If you want to keep the video on the page but hide it behind an image until the user is ready, you can use a `<details>` tag. This acts as a "spoiler" or dropdown, preventing the video from loading until the user clicks.

```html
### Numpy Session 1

<details>
  <summary style="list-style: none; cursor: pointer;">
    <img src="path/to/your/thumbnail.png" alt="Play Video" width="720">
    <p><em>Click to expand and watch Part 1</em></p>
  </summary>
  
  <iframe 
      src="https://drive.google.com/file/d/1-QsdfqwegasgwwrgedKYOW/preview" 
      width="720" 
      height="360" 
      allow="autoplay" 
      frameborder="0" 
      allowfullscreen>
  </iframe>
</details>

```

---

### Why the Iframe shows what it shows

Google Drive's previewer automatically selects a frame (usually from the beginning or middle) to use as the placeholder. There is no `poster` attribute for Google Drive iframes like there is for the HTML5 `<video>` tag.

If you were hosting the video file locally (e.g., in your `docs/assets/` folder), you could use this native code:

```html
<video width="720" height="360" controls poster="path/to/your/image.png">
  <source src="assets/numpy_session.mp4" type="video/mp4">
</video>

```

### Pro Tip for MkDocs

If you find yourself doing this often, I recommend the **[mkdocs-video](https://www.google.com/search?q=https://github.com/fralau/mkdocs-video)** plugin. It allows for cleaner syntax, though it works best with local files rather than Google Drive links.

**Would you like me to help you format a CSS snippet to make that "Click-to-Play" image look more like a professional video player?**

By the way, to unlock the full functionality of all Apps, enable [Gemini Apps Activity](https://myactivity.google.com/product/gemini).