import reflex as rx


class State(rx.State):
    """The app state."""

    nav_items: list[str] = ["Home Page", "About Me", "Courses", "Speaker", "Blog"]
    about_text: str = "Hi, I'm Sebastian. I'm a software engineer and content creator based in Chile. I have a passion for teaching and building things with code."
    courses: list[dict[str, str]] = [
        {"image": "/placeholder.svg", "title": "Full-Stack Apps with Reflex"},
        {"image": "/placeholder.svg", "title": "AI Chatbots in Python"},
    ]
    speaking_engagements: list[dict[str, str]] = [
        {"event": "PyCon US", "topic": "Web Apps in Pure Python"},
        {"event": "AI Dev Summit", "topic": "The Future of AI"},
    ]
    blog_posts: list[dict[str, str]] = [
        {"image": "/placeholder.svg", "title": "Building a Web App in Python"},
        {"image": "/placeholder.svg", "title": "Intro to Machine Learning"},
    ]
    quick_links: list[str] = ["Home", "About", "Courses", "Blog"]
    social_links: list[dict[str, str]] = [
        {"icon": "youtube", "href": "#"},
        {"icon": "twitter", "href": "#"},
        {"icon": "instagram", "href": "#"},
    ]
    active_nav: str = "Home Page"

    @rx.event
    def set_active_nav(self, item: str):
        self.active_nav = item