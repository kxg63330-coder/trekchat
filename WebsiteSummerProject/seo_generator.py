def generate_seo_content(route):
    """
    Generates long-form SEO optimized HTML content for a trekking route.
    """

    name = route.get("name", "")
    country = route.get("country", "")
    difficulty = route.get("difficulty", "")
    distance = route.get("distance_km", "")
    overview = route.get("overview", "")
    best_season = route.get("best_season", "")
    duration = route.get("duration_days", "")
    starting_point = route.get("starting_point", "")
    ending_point = route.get("ending_point", "")

    packing_list = route.get("packing_list", "")
    safety_tips = route.get("safety_tips", "")
    accommodation = route.get("accommodation", "")
    weather = route.get("weather", "")
    how_to_reach = route.get("how_to_reach", "")
    permits = route.get("permits", "")
    faqs = route.get("faqs", [])

    html = f"""
<h2>{name} Trek — Complete Guide ({country})</h2>

<h3>🌍 Overview</h3>
<p>{overview}</p>

<h3>📌 Key Trek Facts</h3>
<ul>
    <li><strong>Country:</strong> {country}</li>
    <li><strong>Difficulty:</strong> {difficulty}</li>
    <li><strong>Distance:</strong> {distance} km</li>
    <li><strong>Duration:</strong> {duration} days</li>
    <li><strong>Start Point:</strong> {starting_point}</li>
    <li><strong>End Point:</strong> {ending_point}</li>
    <li><strong>Best Season:</strong> {best_season}</li>
</ul>

<h3>🧭 How to Reach</h3>
<p>{how_to_reach}</p>

<h3>🪪 Permits Required</h3>
<p>{permits}</p>

<h3>🎒 Packing List</h3>
<p>{packing_list}</p>

<h3>⚠️ Safety Tips</h3>
<p>{safety_tips}</p>

<h3>🏠 Accommodation</h3>
<p>{accommodation}</p>

<h3>🌦️ Weather</h3>
<p>{weather}</p>

<h3>❓ FAQs</h3>
<ul>
"""

    for faq in faqs:
        html += f"<li><strong>{faq['q']}</strong> — {faq['a']}</li>"

    html += "</ul>"

    return html
