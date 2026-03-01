# Personal Blog - Flask Application Specification

## 1. Project Overview
- **Project Name**: Flask Personal Blog
- **Type**: Web Application (Flask)
- **Core Functionality**: A beautiful, responsive personal blog with posts, categories, about page, and contact functionality
- **Target Users**: Bloggers who want a clean, elegant personal blog

## 2. Technology Stack
- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript
- **Data Storage**: JSON file-based storage for blog posts
- **Font**: Google Fonts (Playfair Display, Source Sans Pro)
- **Icons**: Font Awesome

## 3. UI/UX Specification

### Color Palette
- **Primary**: #2D3436 (Dark charcoal)
- **Secondary**: #636E72 (Gray)
- **Accent**: #E17055 (Coral/Peach)
- **Background**: #FAFAFA (Off-white)
- **Card Background**: #FFFFFF (White)
- **Text Primary**: #2D3436
- **Text Secondary**: #636E72

### Typography
- **Headings**: Playfair Display (serif)
- **Body**: Source Sans Pro (sans-serif)
- **Font Sizes**:
  - H1: 3rem
  - H2: 2rem
  - H3: 1.5rem
  - Body: 1.1rem
  - Small: 0.9rem

### Layout Structure
- **Header**: Fixed navigation with logo, nav links
- **Hero Section**: Featured image with overlay text on home page
- **Main Content**: Two-column layout (content 70%, sidebar 30%)
- **Footer**: Social links, copyright

### Responsive Breakpoints
- Desktop: > 1024px
- Tablet: 768px - 1024px
- Mobile: < 768px

## 4. Page Structure

### 4.1 Home Page
- Hero section with blog title and tagline
- Featured post (latest post highlighted)
- Grid of recent posts (3 columns desktop, 2 tablet, 1 mobile)
- Sidebar with categories, recent posts, about snippet

### 4.2 Blog Posts Page (/posts)
- List of all blog posts with pagination
- Each post card shows: title, excerpt, date, category, read time
- Click to view full post

### 4.3 Single Post Page (/post/<id>)
- Full blog post content
- Author info
- Share buttons
- Related posts section

### 4.4 Categories Page (/category/<name>)
- Filter posts by category
- Same card layout as home page

### 4.5 About Page (/about)
- Personal bio section
- Profile image
- Skills/interests

### 4.6 Contact Page (/contact)
- Contact form (name, email, message)
- Social media links
- Location info

## 5. Functionality Specification

### Core Features
1. **Blog Post Management**
   - Create, read blog posts from JSON data
   - Categories: Technology, Lifestyle, Travel, Food, Tutorial
   - Tags support

2. **Navigation**
   - Home, Blog, About, Contact pages
   - Category filtering

3. **Search Functionality**
   - Search posts by title/content

4. **Responsive Design**
   - Mobile-first approach
   - Smooth animations

5. **Contact Form**
   - Form validation
   - Success message on submit

### Animations
- Page load fade-in animation
- Card hover lift effect
- Smooth scroll behavior
- Button hover transitions

## 6. File Structure
```
Flask project/
├── app.py                 # Main Flask application
├── posts.json            # Blog posts data
├── requirements.txt      # Dependencies
├── static/
│   └── css/
│       └── style.css    # Main stylesheet
└── templates/
    ├── base.html        # Base template
    ├── index.html       # Home page
    ├── posts.html       # All posts page
    ├── post.html        # Single post
    ├── about.html       # About page
    └── contact.html     # Contact page
```

## 7. Acceptance Criteria
- [ ] Flask app runs without errors
- [ ] All pages load correctly
- [ ] Responsive design works on all breakpoints
- [ ] Navigation works between all pages
- [ ] Blog posts display correctly
- [ ] Contact form shows validation
- [ ] Beautiful, modern UI with animations
- [ ] Clean, readable typography
