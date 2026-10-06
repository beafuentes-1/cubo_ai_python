# Snake in your browser

This version runs in a modern browser on desktop and mobile. It has no Python,
installation, or third-party runtime requirements.

## Play locally

Open `index.html` in a browser. On phones, copy the `web` folder to the device
and open `index.html` with a browser that supports local HTML files.

## Share a link with GitHub Pages

The repository includes a GitHub Actions workflow that publishes this folder
when changes are pushed to `main` or `master`.

1. Push the project changes to the repository on GitHub.
2. In the repository, open **Settings → Pages** and choose **GitHub Actions**
   as the build and deployment source.
3. Wait for the **Publish Snake browser game** workflow to finish successfully.
4. Open the Pages URL shown in the workflow's deployment summary and share it
   with any computer or phone.

The browser game keeps the best score separately in each browser using local
storage.
