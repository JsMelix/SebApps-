import reflex as rx
from app.states.state import State


def nav_item(text: str) -> rx.Component:
    scroll_target = text.lower().replace(" ", "-")
    return rx.el.a(
        rx.el.p(text, class_name="hover:text-white transition-colors"),
        rx.cond(
            State.active_nav == text,
            rx.el.div(class_name="h-0.5 bg-cyan-400 mt-1"),
            None,
        ),
        on_click=rx.scroll_to(scroll_target),
        class_name="cursor-pointer",
    )


def navbar() -> rx.Component:
    return rx.el.nav(
        rx.el.a(
            rx.el.h2(
                "SEB",
                rx.el.br(),
                "APPS",
                class_name="text-2xl font-bold leading-tight text-cyan-400",
            ),
            href="#",
        ),
        rx.el.div(
            rx.foreach(State.nav_items, nav_item),
            class_name="hidden md:flex items-center space-x-8",
        ),
        class_name="flex justify-between items-center p-6 text-white w-full max-w-7xl mx-auto",
    )


def hero_section() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h1(
                "Turning",
                rx.el.br(),
                "Ideas to",
                rx.el.br(),
                "AppsAI",
                class_name="text-6xl md:text-8xl font-black text-cyan-400 leading-none tracking-tighter",
                style={"textShadow": "3px 3px 0px rgba(255, 255, 255, 0.7)"},
            ),
            class_name="flex-1 flex items-center justify-center text-center md:text-left md:justify-start",
        ),
        rx.el.div(
            rx.el.img(
                src="/modern_3d_rendered.png",
                class_name="max-w-xs md:max-w-sm lg:max-w-md",
            ),
            class_name="hidden md:flex flex-1 items-center justify-center",
        ),
        id="home-page",
        on_mount=lambda: State.set_active_nav("Home Page"),
        class_name="flex flex-col md:flex-row items-center justify-center py-24 w-full max-w-7xl mx-auto px-6 min-h-[calc(100vh-88px)]",
    )


def about_me_section() -> rx.Component:
    return rx.el.div(
        rx.el.h3("ABOUT ME", class_name="text-4xl font-bold text-cyan-400 mb-6"),
        rx.el.p(
            State.about_text, class_name="text-white max-w-2xl text-center text-lg"
        ),
        id="about-me",
        on_mount=lambda: State.set_active_nav("About Me"),
        class_name="py-12 flex flex-col items-center",
    )


def section_header(text: str) -> rx.Component:
    return rx.el.h3(
        text, class_name="text-4xl font-bold text-cyan-400 mb-8 text-center"
    )


def card(image: str, title: str) -> rx.Component:
    return rx.el.div(
        rx.el.img(src=image, class_name="w-full h-40 object-cover rounded-t-lg"),
        rx.el.div(rx.el.p(title, class_name="text-lg font-bold"), class_name="p-4"),
        class_name="bg-gray-800 rounded-lg overflow-hidden border border-gray-700",
    )


def courses_section() -> rx.Component:
    return rx.el.div(
        section_header("COURSES"),
        rx.el.div(
            rx.foreach(State.courses, lambda c: card(c["image"], c["title"])),
            class_name="grid grid-cols-1 md:grid-cols-2 gap-8 max-w-4xl mx-auto",
        ),
        id="courses",
        on_mount=lambda: State.set_active_nav("Courses"),
        class_name="py-12 px-6",
    )


def speaking_section() -> rx.Component:
    return rx.el.div(
        section_header("SPEAKER"),
        rx.el.div(
            rx.foreach(
                State.speaking_engagements,
                lambda s: rx.el.div(
                    rx.el.p(s["event"], class_name="font-bold"),
                    rx.el.p(s["topic"]),
                    class_name="bg-gray-800 p-4 rounded-lg border border-gray-700",
                ),
            ),
            class_name="grid grid-cols-1 md:grid-cols-2 gap-8 max-w-4xl mx-auto",
        ),
        id="speaker",
        on_mount=lambda: State.set_active_nav("Speaker"),
        class_name="py-12 px-6",
    )


def blog_section() -> rx.Component:
    return rx.el.div(
        section_header("BLOG"),
        rx.el.div(
            rx.foreach(State.blog_posts, lambda p: card(p["image"], p["title"])),
            class_name="grid grid-cols-1 md:grid-cols-2 gap-8 max-w-4xl mx-auto",
        ),
        id="blog",
        on_mount=lambda: State.set_active_nav("Blog"),
        class_name="py-12 px-6",
    )


def footer() -> rx.Component:
    return rx.el.footer(
        rx.el.div(
            rx.el.div(
                rx.el.h3(
                    "SEB APPS AI", class_name="text-2xl font-bold text-cyan-400 mb-4"
                ),
                rx.el.p("Turning Ideas to Apps with AI.", class_name="text-white"),
            ),
            rx.el.div(
                rx.el.h4(
                    "QUICK LINKS", class_name="text-lg font-bold text-cyan-400 mb-4"
                ),
                rx.foreach(
                    State.quick_links,
                    lambda link: rx.el.a(
                        link,
                        href="#",
                        class_name="hover:text-cyan-400 transition-colors",
                    ),
                ),
                class_name="flex flex-col space-y-2",
            ),
            rx.el.div(
                rx.el.h4("CONTACT", class_name="text-lg font-bold text-cyan-400 mb-4"),
                rx.el.div(
                    rx.foreach(
                        State.social_links,
                        lambda s: rx.el.a(
                            rx.icon(s["icon"], class_name="h-6 w-6"),
                            href=s["href"],
                            class_name="hover:text-cyan-400 transition-colors",
                            is_external=True,
                        ),
                    ),
                    class_name="flex space-x-4",
                ),
            ),
            class_name="grid grid-cols-1 md:grid-cols-3 gap-8 max-w-7xl mx-auto text-white",
        ),
        class_name="bg-gray-900 py-12 px-6",
    )


def index() -> rx.Component:
    return rx.el.div(
        navbar(),
        rx.el.main(
            hero_section(),
            about_me_section(),
            courses_section(),
            speaking_section(),
            blog_section(),
        ),
        footer(),
        rx.el.div(
            rx.icon("message-square", class_name="text-white"),
            class_name="fixed bottom-8 right-8 bg-purple-600 p-4 rounded-full shadow-lg cursor-pointer hover:bg-purple-700 transition-colors",
        ),
        class_name="font-['VT323'] bg-black min-h-screen grid-background relative scroll-smooth",
    )


app = rx.App(
    theme=rx.theme(appearance="light"),
    head_components=[
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(rel="preconnect", href="https://fonts.gstatic.com", cross_origin=""),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=VT323&display=swap",
            rel="stylesheet",
        ),
    ],
    stylesheets=["/css/styles.css"],
)
app.add_page(index)