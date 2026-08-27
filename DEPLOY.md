How to deploy Adonai Farm site to GitHub Pages

1. Create a new GitHub repository (or use an existing one) and note the repository URL.

2. Initialize and commit locally (run from the adonai-farm folder):

   git init
   git add .
   git commit -m "Initial site content: add responsive images, SEO, sitemap, and manifest.\n\nCo-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>"
   git branch -M main
   git remote add origin https://github.com/<your-username>/<your-repo>.git
   git push -u origin main

3. Enable GitHub Pages in repository settings:
   - Go to Settings > Pages
   - Set source to 'main' branch and root (/) folder
   - Save and wait a minute for the site to publish at: https://<your-username>.github.io/<your-repo>/

4. After publishing:
   - Update sitemap.xml <loc> to your live domain and update robots.txt accordingly.
   - Test with Google Search Console (submit sitemap) and Rich Results Test.

Notes:
- If you prefer a custom domain, configure DNS (CNAME) and add the domain in Pages settings.
- Clear browser cache or use an incognito window to view updates.
