import reflex as rx


class State(rx.State):
    """The app state."""

    nav_items: list[str] = ["Home Page", "About Me", "Courses", "Speaker", "Blog"]
    about_text: str = "Leader in Emerging Technologies, Self-taught Developer, and Speaker. I actively collaborate with ACIA GDG Bogotá, am a member of Young AI Leaders Bogotá, and am an ambassador for Stellar/Vara Network. I have training from Samsung Innovation Campus (Python) and Platzi Master. Winner of Hackathons in AI/Web3, applying my skills in AI and Web3 to create a positive impact on society."
    courses: list[dict[str, str]] = [
        {"image": "/placeholder.svg", "title": "Full-Stack Apps with Reflex"},
        {"image": "/placeholder.svg", "title": "AI Chatbots in Python"},
    ]
    speaking_engagements: list[dict[str, str]] = [
        {"event": "PyCon US", "topic": "Web Apps in Pure Python", "href": "https://www.youtube.com/watch?v=kVNA1hBPj-E&themeRefresh=1"},
        {"event": "AI Dev Summit", "topic": "The Future of AI"},
    ]
    blog_posts: list[dict[str, str]] = [
        {"image": "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=400&h=300&fit=crop", "title": "Inteligencia Artificial en Colombia", "href": "https://www.linkedin.com/posts/asociaci%C3%B3n-colombiana-de-inteligencia-artificial_inteligenciaartificial-comunidadtech-innovaciaejn-activity-7392616151253639168-O9b7?utm_source=social_share_send&utm_medium=member_desktop_web&rcm=ACoAAC_O7osBySuyG5cm-7rv-qOeayO1p-y2BY0"},
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