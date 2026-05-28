from app import app, db
from models import Route
from seo_generator import generate_seo_content

routes = [
{

        "name": "K2 Base Camp",
        "country": "Pakistan",
        "difficulty": "Extreme",
        "distance_km": 150,
        "description": "A legendary high‑altitude trek through the Karakoram, leading to the base of the world’s second‑highest mountain.",
        "image_url": "https://images.unsplash.com/photo-1521295121783-8a321d551ad2",

        "overview": """The K2 Base Camp Trek is one of the most spectacular and demanding trekking routes on Earth. 
    This expedition takes trekkers deep into Pakistan’s Karakoram Range, across the mighty Baltoro Glacier, 
    past iconic peaks such as Trango Towers, Masherbrum, and Broad Peak, before reaching the legendary Concordia — 
    the “Throne Room of the Mountain Gods.” This trek is ideal for experienced hikers seeking a raw, remote, 
    and unforgettable expedition. With its dramatic landscapes and towering 8,000‑meter giants, the K2 Base Camp 
    Trek offers a once‑in‑a‑lifetime Himalayan experience.""",

        "best_season": "June to September",
        "elevation_gain": "5,150m",
        "duration_days": 14,
        "starting_point": "Skardu",
        "ending_point": "K2 Base Camp",

        "map_embed": "<iframe src='https://www.google.com/maps/embed?...' width='100%' height='300'></iframe>",

        "itinerary": [
            {"day": 1, "title": "Arrival in Skardu", "desc": "Arrive in Skardu, surrounded by towering peaks."},
            {"day": 2, "title": "Skardu to Askole", "desc": "A rugged jeep ride to the last village before the trek."},
            {"day": 3, "title": "Askole to Jhula", "desc": "The trek begins along the Braldu River."},
            {"day": 4, "title": "Jhula to Paiju", "desc": "A scenic day with views of Paiyu Peak."},
            {"day": 5, "title": "Acclimatization at Paiju", "desc": "Rest day before entering the glacier."},
            {"day": 6, "title": "Paiju to Khoburtse", "desc": "Enter the Baltoro Glacier."},
            {"day": 7, "title": "Khoburtse to Urdukas", "desc": "Steep glacier sections with granite towers overhead."},
            {"day": 8, "title": "Urdukas to Goro II", "desc": "Walk entirely on the glacier."},
            {"day": 9, "title": "Goro II to Concordia", "desc": "Reach the legendary Concordia."},
            {"day": 10, "title": "Concordia to K2 Base Camp", "desc": "Final push to the base of K2."},
            {"day": 11, "title": "Return to Concordia", "desc": "Retrace your steps with stunning views."},
            {"day": 12, "title": "Concordia to Goro II", "desc": "Begin descent."},
            {"day": 13, "title": "Goro II to Urdukas", "desc": "Continue descending."},
            {"day": 14, "title": "Urdukas to Paiju", "desc": "Final day before returning to Askole."}
        ],

        "how_to_reach": "Fly to Islamabad → flight/road to Skardu → jeep to Askole.",
        "permits": "Trekking permit + passport registration required.",
        "packing_list": "Down jacket, thermal layers, waterproof boots, trekking poles, glacier sunglasses, -15°C sleeping bag.",
        "safety_tips": "Acclimatize properly, stay hydrated, avoid overexertion, be cautious on glacier sections.",
        "accommodation": "Tented camps throughout the trek; hotels in Skardu.",
        "weather": "Cold nights, strong winds, rapidly changing weather.",
        "faqs": [
            {"q": "Is this trek suitable for beginners?",
             "a": "No. It requires high fitness and prior trekking experience."},
            {"q": "Do I need a guide?", "a": "Yes. Authorized guides are mandatory."}
        ]
    },
    {
        "name": "Nanga Parbat Base Camp",
        "country": "Pakistan",
        "difficulty": "Hard",
        "distance_km": 50,
        "description": "A dramatic trek to the base of the Killer Mountain.",
        "image_url": "https://images.unsplash.com/photo-1500048993959-dcfe1c5f1c5c",

        "overview": """The Nanga Parbat Base Camp Trek via Fairy Meadows is one of Pakistan’s most beautiful 
    high‑altitude adventures. Known for its lush meadows, pine forests, and breathtaking views of the 8,126‑meter 
    Nanga Parbat, this trek blends natural beauty with thrilling mountain scenery. It is ideal for trekkers 
    seeking a challenging yet accessible Himalayan experience.""",

        "best_season": "May to September",
        "elevation_gain": "3,900m",
        "duration_days": 7,
        "starting_point": "Raikot Bridge",
        "ending_point": "Nanga Parbat Base Camp",

        "map_embed": "<iframe src='https://www.google.com/maps/embed?...' width='100%' height='300'></iframe>",

        "itinerary": [
            {"day": 1, "title": "Drive to Raikot Bridge → Jeep to Tattu",
             "desc": "Thrilling jeep ride along cliff roads."},
            {"day": 2, "title": "Tattu to Fairy Meadows", "desc": "Steep hike through pine forests."},
            {"day": 3, "title": "Acclimatization at Fairy Meadows",
             "desc": "Explore the meadows and prepare for base camp."},
            {"day": 4, "title": "Fairy Meadows to Beyal Camp", "desc": "Scenic walk with increasing mountain views."},
            {"day": 5, "title": "Beyal Camp to Base Camp", "desc": "Challenging rocky terrain to reach base camp."},
            {"day": 6, "title": "Return to Fairy Meadows", "desc": "Descend with stunning views."},
            {"day": 7, "title": "Fairy Meadows to Tattu → Raikot Bridge", "desc": "Return to the starting point."}
        ],

        "how_to_reach": "Fly or drive to Gilgit → jeep to Raikot Bridge → jeep to Tattu.",
        "permits": "Foreigners must register at police checkpoints.",
        "packing_list": "Warm layers, trekking boots, rain jacket, snacks, power bank.",
        "safety_tips": "Avoid hiking after dark; stay hydrated.",
        "accommodation": "Huts and camps at Fairy Meadows.",
        "weather": "Warm days, cold nights; sudden rain possible.",
        "faqs": [
            {"q": "Is Fairy Meadows safe?", "a": "Yes, with proper planning."},
            {"q": "Can beginners do this trek?", "a": "Yes, with moderate fitness."}
        ]
    },
    {
        "name": "Adam's Peak",
        "country": "Sri Lanka",
        "difficulty": "Medium",
        "distance_km": 7,
        "description": "A sacred pilgrimage climb known for its sunrise views and spiritual significance.",
        "image_url": "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee",

        "overview": """Adam’s Peak, also known as Sri Pada, is one of Sri Lanka’s most iconic pilgrimage routes. 
    The climb is a deeply spiritual experience, attracting Buddhists, Hindus, Muslims, and Christians alike. 
    Trekkers ascend thousands of stone steps through misty forests and illuminated pathways, aiming to reach 
    the summit before sunrise. The peak is famous for its breathtaking dawn views and the mysterious triangular 
    shadow it casts across the landscape. This trek blends cultural heritage, natural beauty, and spiritual 
    symbolism, making it one of the most unique climbs in Asia.""",

        "best_season": "December to May",
        "elevation_gain": "1,000m",
        "duration_days": 1,
        "starting_point": "Dalhousie",
        "ending_point": "Adam’s Peak Summit",

        "map_embed": "<iframe src='https://www.google.com/maps/embed?...'></iframe>",

        "itinerary": [
            {"day": 1, "title": "Night Ascent to Adam’s Peak",
             "desc": "Begin the climb around midnight to reach the summit by sunrise. Enjoy panoramic views and the famous triangular shadow."}
        ],

        "how_to_reach": "Drive or take a bus from Colombo or Kandy to Dalhousie, the main trailhead.",
        "permits": "No permits required.",
        "packing_list": "Water, snacks, warm jacket, flashlight, comfortable shoes.",
        "safety_tips": "Climb slowly, take breaks, avoid slippery steps, stay warm during the night ascent.",
        "accommodation": "Guesthouses and lodges available in Dalhousie.",
        "weather": "Cool nights, misty mornings, warm afternoons.",
        "faqs": [
            {"q": "Is the climb difficult?", "a": "It is steep but manageable with breaks."},
            {"q": "Why do people climb at night?", "a": "To witness the famous sunrise from the summit."}
        ]
    },
    {
        "name": "Mount Apo",
        "country": "Philippines",
        "difficulty": "Medium",
        "distance_km": 20,
        "description": "A volcanic trek to the highest peak in the Philippines, featuring forests, sulfur vents, and summit views.",
        "image_url": "https://images.unsplash.com/photo-1500534314209-a25ddb2bd429",

        "overview": """Mount Apo, rising to 2,954 meters, is the highest mountain in the Philippines and a crown jewel 
    of Southeast Asian trekking. The trail offers a diverse landscape of mossy forests, volcanic boulder fields, 
    geothermal sulfur vents, and sweeping summit views over Mindanao. Rich in biodiversity, the mountain is home 
    to rare species such as the Philippine eagle. This trek is ideal for hikers seeking a challenging yet 
    rewarding multi‑day adventure through one of the country’s most pristine natural environments.""",

        "best_season": "March to May",
        "elevation_gain": "2,954m",
        "duration_days": 3,
        "starting_point": "Kapatagan",
        "ending_point": "Mount Apo Summit",

        "map_embed": "<iframe src='https://www.google.com/maps/embed?...'></iframe>",

        "itinerary": [
            {"day": 1, "title": "Kapatagan to Tinikaran Camp",
             "desc": "Trek through farmlands and forests to reach the first campsite."},
            {"day": 2, "title": "Tinikaran Camp to Summit",
             "desc": "Climb through volcanic boulders and sulfur vents to reach the summit."},
            {"day": 3, "title": "Descent to Kapatagan",
             "desc": "Return through the same trail with scenic views."}
        ],

        "how_to_reach": "Drive from Davao City to Kapatagan, the main trailhead.",
        "permits": "Climbing permit required from DENR.",
        "packing_list": "Rain gear, warm layers, gloves, trekking poles, headlamp.",
        "safety_tips": "Beware of sulfur vents, slippery rocks, and sudden weather changes.",
        "accommodation": "Tents at designated campsites.",
        "weather": "Cool summit temperatures, humid forests.",
        "faqs": [
            {"q": "Is Mount Apo open year‑round?", "a": "It may close during heavy rains or maintenance."},
            {"q": "Is the trail difficult?", "a": "Moderately challenging with volcanic terrain."}
        ]
    },
    {
        "name": "Mount Fansipan",
        "country": "Vietnam",
        "difficulty": "Hard",
        "distance_km": 14,
        "description": "A steep jungle climb to the Roof of Indochina, offering panoramic summit views.",
        "image_url": "https://images.unsplash.com/photo-1501785888041-af3ef285b470",

        "overview": """Mount Fansipan, standing at 3,147 meters, is the highest peak in Vietnam and the entire 
    Indochina region. The trek takes hikers through dense jungles, bamboo forests, and rocky ridges before 
    reaching the summit, which offers sweeping views over Sapa and the Hoang Lien Son range. Known for its 
    steep ascents and rugged terrain, Fansipan is a challenging but rewarding climb for experienced trekkers 
    seeking a true mountain adventure in northern Vietnam.""",

        "best_season": "September to April",
        "elevation_gain": "1,500m",
        "duration_days": 2,
        "starting_point": "Tram Ton Pass",
        "ending_point": "Fansipan Summit",

        "map_embed": "<iframe src='https://www.google.com/maps/embed?...'></iframe>",

        "itinerary": [
            {"day": 1, "title": "Tram Ton Pass to Base Camp",
             "desc": "Trek through forests and steep sections to reach the campsite."},
            {"day": 2, "title": "Base Camp to Summit → Return",
             "desc": "Climb to the summit for sunrise, then descend back to Tram Ton Pass."}
        ],

        "how_to_reach": "Drive from Sapa to Tram Ton Pass, the main starting point.",
        "permits": "Permit included with guide service.",
        "packing_list": "Warm jacket, gloves, trekking shoes, rain protection.",
        "safety_tips": "Watch for slippery rocks, sudden fog, and steep sections.",
        "accommodation": "Mountain huts or tents.",
        "weather": "Cold summit, mild forests.",
        "faqs": [
            {"q": "Can beginners climb Fansipan?", "a": "It is challenging but possible with a guide."},
            {"q": "Is there a cable car?", "a": "Yes, but the trek is the traditional route."}
        ]
    },
    {
        "name": "Mount Damavand",
        "country": "Iran",
        "difficulty": "Hard",
        "distance_km": 12,
        "description": "A volcanic ascent to the highest peak in the Middle East, known for sulfur vents and sweeping alpine views.",
        "image_url": "https://images.unsplash.com/photo-1506744038136-46273834b3fb",

        "overview": """Mount Damavand, standing at 5,671 meters, is the highest peak in Iran and the tallest volcano 
    in Asia. This iconic mountain is deeply rooted in Persian mythology and offers a challenging yet achievable 
    climb for experienced trekkers. The route features volcanic landscapes, sulfur vents, alpine meadows, and 
    panoramic views over the Alborz Mountains. Damavand is a symbol of strength and endurance, attracting 
    climbers from around the world.""",

        "best_season": "June to September",
        "elevation_gain": "2,500m",
        "duration_days": 3,
        "starting_point": "Polour",
        "ending_point": "Damavand Summit",

        "map_embed": "<iframe src='https://www.google.com/maps/embed?...'></iframe>",

        "itinerary": [
            {"day": 1, "title": "Polour to Goosfand Sara",
             "desc": "Drive from Polour to the base camp at Goosfand Sara. Begin a short acclimatization hike."},
            {"day": 2, "title": "Goosfand Sara to Bargah Sevom",
             "desc": "A steady ascent to the high camp at 4,200m."},
            {"day": 3, "title": "Summit Push → Return",
             "desc": "Climb steep volcanic slopes to reach the summit. Descend back to Goosfand Sara."}
        ],

        "how_to_reach": "Drive from Tehran to Polour (2 hours), then take a 4x4 to Goosfand Sara.",
        "permits": "Climbing permit required from the Iranian Mountaineering Federation.",
        "packing_list": "Crampons (early season), warm layers, trekking poles, sunscreen.",
        "safety_tips": "Beware of sulfur fumes near the summit; acclimatize properly.",
        "accommodation": "Mountain huts and tents at high camp.",
        "weather": "Cold summit temperatures, windy ridges.",
        "faqs": [
            {"q": "Is Damavand technical?", "a": "No, but altitude and weather make it challenging."},
            {"q": "Do I need a guide?", "a": "Recommended for safety and logistics."}
        ]
    },
    {
        "name": "Mount Batur Sunrise Trek",
        "country": "Indonesia",
        "difficulty": "Easy",
        "distance_km": 8,
        "description": "A popular sunrise hike overlooking volcanic landscapes and Lake Batur.",
        "image_url": "https://images.unsplash.com/photo-1500534314209-a25ddb2bd429",

        "overview": """Mount Batur is one of Bali’s most famous sunrise treks, offering breathtaking views of the 
    caldera, Lake Batur, and Mount Agung. The trail is accessible, well‑marked, and suitable for beginners, 
    making it one of the most popular hikes in Indonesia. The sunrise from the summit is a magical experience 
    that draws thousands of trekkers each year.""",

        "best_season": "April to October",
        "elevation_gain": "700m",
        "duration_days": 1,
        "starting_point": "Toyabungkah",
        "ending_point": "Mount Batur Summit",

        "map_embed": "<iframe src='https://www.google.com/maps/embed?...'></iframe>",

        "itinerary": [
            {"day": 1, "title": "Night Ascent to Mount Batur",
             "desc": "Start hiking around 3 AM to reach the summit by sunrise. Enjoy panoramic views over Bali’s volcanic landscape."}
        ],

        "how_to_reach": "Drive from Ubud or Kuta to Toyabungkah village.",
        "permits": "Entrance fee required at the base.",
        "packing_list": "Light jacket, water, snacks, flashlight.",
        "safety_tips": "Watch for loose volcanic gravel; stay on marked paths.",
        "accommodation": "Hotels available in nearby Kintamani.",
        "weather": "Cool mornings, warm afternoons.",
        "faqs": [
            {"q": "Is a guide required?", "a": "Yes, local guides are mandatory."}
        ]
    },

    {
        "name": "Mount Hua Shan",
        "country": "China",
        "difficulty": "Hard",
        "distance_km": 12,
        "description": "A steep and thrilling trek famous for its cliff‑side plank walk and dramatic staircases.",
        "image_url": "https://images.unsplash.com/photo-1501785888041-af3ef285b470",

        "overview": """Mount Hua Shan is one of China’s Five Great Mountains and is known for its steep staircases, 
    narrow ridges, and the world‑famous plank walk. The trek offers breathtaking views, ancient Taoist temples, 
    and adrenaline‑pumping cliff paths. It is a challenging but rewarding climb for adventure seekers.""",

        "best_season": "April to October",
        "elevation_gain": "1,800m",
        "duration_days": 1,
        "starting_point": "Hua Shan Visitor Center",
        "ending_point": "South Peak",

        "map_embed": "<iframe src='https://www.google.com/maps/embed?...'></iframe>",

        "itinerary": [
            {"day": 1, "title": "Ascent of Mount Hua Shan",
             "desc": "Climb steep stone steps, pass through narrow ridges, and explore the famous plank walk before reaching the South Peak."}
        ],

        "how_to_reach": "High‑speed train from Xi’an to Hua Shan North Station.",
        "permits": "Entrance ticket required.",
        "packing_list": "Gloves, sturdy shoes, water, snacks.",
        "safety_tips": "Use handrails, avoid slippery steps, follow safety instructions.",
        "accommodation": "Guesthouses near the base.",
        "weather": "Mild spring and autumn, hot summers.",
        "faqs": [
            {"q": "Is the plank walk safe?", "a": "Yes, with harnesses and supervision."}
        ]
    },
    {
        "name": "Mount Tai",
        "country": "China",
        "difficulty": "Medium",
        "distance_km": 9,
        "description": "A historic pilgrimage route with thousands of stone steps and ancient temples.",
        "image_url": "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee",

        "overview": """Mount Tai, a UNESCO World Heritage Site, is one of China’s most sacred mountains. The trek 
    features ancient stone staircases, historic temples, and panoramic views. For centuries, emperors and 
    pilgrims have climbed Mount Tai to offer prayers and witness its legendary sunrise.""",

        "best_season": "March to November",
        "elevation_gain": "1,400m",
        "duration_days": 1,
        "starting_point": "Hongmen Gate",
        "ending_point": "South Heavenly Gate",

        "map_embed": "<iframe src='https://www.google.com/maps/embed?...'></iframe>",

        "itinerary": [
            {"day": 1, "title": "Climb to the Summit of Mount Tai",
             "desc": "Ascend thousands of stone steps, passing temples, gates, and scenic viewpoints before reaching the summit."}
        ],

        "how_to_reach": "Train or bus to Tai’an City, then taxi to Hongmen Gate.",
        "permits": "Entrance ticket required.",
        "packing_list": "Comfortable shoes, water, sun protection.",
        "safety_tips": "Take breaks, avoid slippery steps after rain.",
        "accommodation": "Hotels in Tai’an City.",
        "weather": "Warm summers, cool spring and autumn.",
        "faqs": [
            {"q": "How long is the climb?", "a": "4–6 hours depending on pace."}
        ]
    },

    {
        "name": "Mount Hallasan",
        "country": "South Korea",
        "difficulty": "Medium",
        "distance_km": 19,
        "description": "A volcanic crater trek on Jeju Island with panoramic views and diverse ecosystems.",
        "image_url": "https://images.unsplash.com/photo-1500534314209-a25ddb2bd429",

        "overview": """Mount Hallasan, the highest peak in South Korea, rises from the center of Jeju Island. The trek 
    features lush forests, volcanic rock formations, and a stunning crater lake at the summit. It is one of Korea’s 
    most popular day hikes and offers a rewarding challenge for nature lovers.""",

        "best_season": "April to October",
        "elevation_gain": "1,200m",
        "duration_days": 1,
        "starting_point": "Seongpanak Trailhead",
        "ending_point": "Hallasan Summit",

        "map_embed": "<iframe src='https://www.google.com/maps/embed?...'></iframe>",

        "itinerary": [
            {"day": 1, "title": "Seongpanak Trail to Hallasan Summit",
             "desc": "A long but steady ascent through forests and volcanic terrain to reach the crater rim."}
        ],

        "how_to_reach": "Bus or taxi from Jeju City to Seongpanak Trailhead.",
        "permits": "No permits required.",
        "packing_list": "Water, snacks, windbreaker, trekking shoes.",
        "safety_tips": "Start early; summit access may close due to weather.",
        "accommodation": "Hotels in Jeju City.",
        "weather": "Cool summit, mild forests.",
        "faqs": [
            {"q": "Is Hallasan suitable for beginners?", "a": "Yes, with good fitness and preparation."}
        ]
    },
    {
        "name": "Tre Cime di Lavaredo Loop",
        "country": "Italy",
        "difficulty": "Easy",
        "distance_km": 10,
        "description": "A world‑famous loop around the iconic Three Peaks of the Dolomites.",
        "image_url": "https://images.unsplash.com/photo-1500534314209-a25ddb2bd429",

        "overview": """The Tre Cime di Lavaredo Loop is one of the most iconic day hikes in the Dolomites, offering 
    breathtaking views of the towering limestone peaks known as the Three Sisters. The trail is accessible, 
    well‑marked, and suitable for most hikers, making it a must‑do route for anyone visiting northern Italy. 
    With dramatic cliffs, alpine meadows, and panoramic vistas, this loop captures the essence of the Dolomites’ 
    unique beauty.""",

        "best_season": "June to October",
        "elevation_gain": "400m",
        "duration_days": 1,
        "starting_point": "Rifugio Auronzo",
        "ending_point": "Rifugio Auronzo",

        "map_embed": "<iframe src='https://www.google.com/maps/embed?...'></iframe>",

        "itinerary": [
            {"day": 1, "title": "Tre Cime Loop",
             "desc": "Walk around the base of the Three Peaks, passing Rifugio Lavaredo and Rifugio Locatelli for stunning views."}
        ],

        "how_to_reach": "Drive or shuttle from Misurina to Rifugio Auronzo.",
        "permits": "Parking fee required at the trailhead.",
        "packing_list": "Water, snacks, sun protection, camera.",
        "safety_tips": "Avoid exposed areas during thunderstorms.",
        "accommodation": "Mountain huts and hotels in Misurina.",
        "weather": "Warm summers, cool evenings.",
        "faqs": [
            {"q": "Is the loop family‑friendly?", "a": "Yes, it is suitable for most ages."}
        ]
    },
    {
        "name": "Mount Triglav Summit",
        "country": "Slovenia",
        "difficulty": "Hard",
        "distance_km": 20,
        "description": "A challenging alpine ascent to Slovenia’s highest and most symbolic peak.",
        "image_url": "https://images.unsplash.com/photo-1501785888041-af3ef285b470",

        "overview": """Mount Triglav, rising to 2,864 meters, is the national symbol of Slovenia and a rite of passage 
    for many Slovenians. The trek features steep alpine trails, exposed ridges, and via ferrata sections near the 
    summit. The climb is demanding but incredibly rewarding, offering panoramic views over the Julian Alps. 
    This route is ideal for experienced hikers seeking a thrilling alpine challenge.""",

        "best_season": "July to September",
        "elevation_gain": "1,800m",
        "duration_days": 2,
        "starting_point": "Krma Valley",
        "ending_point": "Triglav Summit",

        "map_embed": "<iframe src='https://www.google.com/maps/embed?...'></iframe>",

        "itinerary": [
            {"day": 1, "title": "Krma Valley to Kredarica Hut",
             "desc": "A long ascent through forests and alpine terrain to the main mountain hut."},
            {"day": 2, "title": "Kredarica Hut to Triglav Summit → Return",
             "desc": "Climb via ferrata sections to reach the summit, then descend back to the valley."}
        ],

        "how_to_reach": "Drive from Ljubljana to Krma Valley trailhead.",
        "permits": "No permits required.",
        "packing_list": "Helmet, via ferrata kit, gloves, warm layers.",
        "safety_tips": "Use proper gear for exposed sections; avoid storms.",
        "accommodation": "Kredarica Hut (mountain refuge).",
        "weather": "Cool alpine climate with sudden changes.",
        "faqs": [
            {"q": "Is via ferrata experience required?", "a": "Recommended for safety on exposed ridges."}
        ]
    },
    {
        "name": "Tour du Mont Blanc",
        "country": "France / Italy / Switzerland",
        "difficulty": "Hard",
        "distance_km": 170,
        "description": "A legendary multi‑country alpine circuit around the Mont Blanc massif.",
        "image_url": "https://images.unsplash.com/photo-1500534314209-a25ddb2bd429",

        "overview": """The Tour du Mont Blanc (TMB) is one of the world’s most iconic long‑distance treks, circling 
    the entire Mont Blanc massif through France, Italy, and Switzerland. The route features dramatic glaciers, 
    rugged high passes, charming alpine villages, and sweeping views of Western Europe’s highest peak. 
    This trek blends physical challenge with cultural immersion, offering trekkers a chance to experience 
    three distinct mountain cultures in one unforgettable journey.""",

        "best_season": "June to September",
        "elevation_gain": "10,000m",
        "duration_days": 10,
        "starting_point": "Les Houches (France)",
        "ending_point": "Les Houches (France)",

        "map_embed": "<iframe src='https://www.google.com/maps/embed?...'></iframe>",

        "itinerary": [
            {"day": 1, "title": "Les Houches to Les Contamines",
             "desc": "Forests, meadows, and classic French alpine scenery."},
            {"day": 2, "title": "Les Contamines to Croix du Bonhomme",
             "desc": "Climb over the Col du Bonhomme with glacier views."},
            {"day": 3, "title": "Croix du Bonhomme to Courmayeur",
             "desc": "Descend into Italy with stunning views of Mont Blanc."},
            {"day": 4, "title": "Courmayeur to Rifugio Bonatti", "desc": "Walk along the Italian side of the massif."},
            {"day": 5, "title": "Rifugio Bonatti to La Fouly",
             "desc": "Cross into Switzerland via the Grand Col Ferret."},
            {"day": 6, "title": "La Fouly to Champex", "desc": "A gentle day through Swiss forests and lakes."},
            {"day": 7, "title": "Champex to Trient", "desc": "Climb the Fenêtre d’Arpette or the Bovine Route."},
            {"day": 8, "title": "Trient to Argentière", "desc": "Return to France with glacier views."},
            {"day": 9, "title": "Argentière to Chamonix", "desc": "Walk beneath the Aiguilles Rouges."},
            {"day": 10, "title": "Chamonix Loop", "desc": "Optional final day exploring the valley."}
        ],

        "how_to_reach": "Fly to Geneva → bus to Chamonix → start in Les Houches.",
        "permits": "No permits required.",
        "packing_list": "Rain gear, trekking poles, warm layers, hut sleeping liner.",
        "safety_tips": "Weather can change rapidly; avoid high passes during storms.",
        "accommodation": "Mountain refuges, hotels, and guesthouses.",
        "weather": "Warm days, cool nights, occasional storms.",
        "faqs": [
            {"q": "Is TMB crowded?", "a": "Yes during peak season; book huts early."},
            {"q": "Can beginners do it?", "a": "Yes with training and proper pacing."}
        ]
    },
    {
        "name": "Ronda to Grazalema Trek",
        "country": "Spain",
        "difficulty": "Medium",
        "distance_km": 45,
        "description": "A scenic trek through Andalusia’s white villages, limestone cliffs, and rolling hills.",
        "image_url": "https://images.unsplash.com/photo-1501785888041-af3ef285b470",

        "overview": """This classic Andalusian trek connects the historic town of Ronda with the mountain village of 
    Grazalema. The route passes through dramatic limestone formations, cork forests, and picturesque whitewashed 
    villages. Trekkers experience the cultural richness of southern Spain while enjoying mild Mediterranean 
    landscapes and rugged mountain scenery.""",

        "best_season": "March to June, September to November",
        "elevation_gain": "1,800m",
        "duration_days": 3,
        "starting_point": "Ronda",
        "ending_point": "Grazalema",

        "map_embed": "<iframe src='https://www.google.com/maps/embed?...'></iframe>",

        "itinerary": [
            {"day": 1, "title": "Ronda to Benaoján", "desc": "Walk through rolling hills and limestone valleys."},
            {"day": 2, "title": "Benaoján to Montejaque", "desc": "Pass through caves and rugged terrain."},
            {"day": 3, "title": "Montejaque to Grazalema", "desc": "Climb into the Sierra de Grazalema Natural Park."}
        ],

        "how_to_reach": "Train or bus from Málaga or Seville to Ronda.",
        "permits": "No permits required.",
        "packing_list": "Sun protection, water, snacks, breathable clothing.",
        "safety_tips": "Avoid midday heat; carry plenty of water.",
        "accommodation": "Guesthouses and rural inns.",
        "weather": "Warm Mediterranean climate.",
        "faqs": [
            {"q": "Is this trek family‑friendly?", "a": "Yes, with moderate fitness."}
        ]
    },
    {
        "name": "Lysefjord & Preikestolen",
        "country": "Norway",
        "difficulty": "Medium",
        "distance_km": 8,
        "description": "A dramatic cliff‑top hike overlooking Norway’s Lysefjord, ending at the iconic Pulpit Rock.",
        "image_url": "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee",

        "overview": """Preikestolen, or Pulpit Rock, is one of Norway’s most famous natural landmarks. The trek climbs 
    through forests, rocky plateaus, and glacially carved terrain before reaching a massive cliff that towers 
    604 meters above Lysefjord. The panoramic views from the top are among the most breathtaking in Scandinavia, 
    making this a must‑do hike for visitors to Norway.""",

        "best_season": "May to October",
        "elevation_gain": "350m",
        "duration_days": 1,
        "starting_point": "Preikestolen Mountain Lodge",
        "ending_point": "Pulpit Rock",

        "map_embed": "<iframe src='https://www.google.com/maps/embed?...'></iframe>",

        "itinerary": [
            {"day": 1, "title": "Preikestolen Trail",
             "desc": "A scenic climb over rocky terrain leading to the famous cliff overlooking Lysefjord."}
        ],

        "how_to_reach": "Ferry or bus from Stavanger to the trailhead.",
        "permits": "No permits required.",
        "packing_list": "Windproof jacket, sturdy shoes, water, snacks.",
        "safety_tips": "Stay away from cliff edges; avoid hiking in strong winds.",
        "accommodation": "Hotels and lodges in Stavanger.",
        "weather": "Cool, windy, and often wet.",
        "faqs": [
            {"q": "Is the trail dangerous?", "a": "Safe if you stay on marked paths and avoid edges."}
        ]
    },
    {
        "name": "Mount Kilimanjaro (Marangu Route)",
        "country": "Tanzania",
        "difficulty": "Hard",
        "distance_km": 72,
        "description": "A classic ascent of Africa’s highest peak via the Marangu ‘Coca‑Cola’ Route.",
        "image_url": "https://images.unsplash.com/photo-1500534314209-a25ddb2bd429",

        "overview": """Mount Kilimanjaro, rising to 5,895 meters, is the tallest mountain in Africa and one of the 
    world’s most iconic trekking summits. The Marangu Route, known as the ‘Coca‑Cola Route,’ is the only path 
    offering hut accommodations instead of tents. The trail passes through lush rainforests, moorlands, alpine 
    deserts, and finally the icy slopes leading to Uhuru Peak. Despite being considered one of the easier routes, 
    altitude makes this trek a serious challenge requiring proper acclimatization and determination.""",

        "best_season": "January to March, June to October",
        "elevation_gain": "4,000m",
        "duration_days": 6,
        "starting_point": "Marangu Gate",
        "ending_point": "Uhuru Peak",

        "map_embed": "<iframe src='https://www.google.com/maps/embed?...'></iframe>",

        "itinerary": [
            {"day": 1, "title": "Marangu Gate to Mandara Hut",
             "desc": "Walk through dense rainforest with rich wildlife."},
            {"day": 2, "title": "Mandara Hut to Horombo Hut", "desc": "Enter moorland terrain with sweeping views."},
            {"day": 3, "title": "Acclimatization Day at Horombo", "desc": "Optional hike to Zebra Rocks."},
            {"day": 4, "title": "Horombo Hut to Kibo Hut", "desc": "Cross the alpine desert toward the summit base."},
            {"day": 5, "title": "Kibo Hut to Uhuru Peak → Return to Horombo",
             "desc": "Midnight summit push to Africa’s highest point."},
            {"day": 6, "title": "Horombo Hut to Marangu Gate", "desc": "Final descent through rainforest."}
        ],

        "how_to_reach": "Fly to Kilimanjaro Airport → drive to Marangu village.",
        "permits": "Park fees and licensed guide required.",
        "packing_list": "Thermal layers, -15°C sleeping bag, trekking poles, headlamp, hydration system.",
        "safety_tips": "Ascend slowly, hydrate well, monitor altitude sickness symptoms.",
        "accommodation": "Mountain huts along the route.",
        "weather": "Cold summit, mild rainforest, windy alpine desert.",
        "faqs": [
            {"q": "Is Kilimanjaro technical?", "a": "No, but altitude makes it challenging."},
            {"q": "Do I need a guide?", "a": "Yes, guides are mandatory."}
        ]
    },
    {
        "name": "Mount Kenya (Lenana Peak)",
        "country": "Kenya",
        "difficulty": "Hard",
        "distance_km": 48,
        "description": "A stunning trek to the third‑highest peak in Africa, featuring alpine lakes and rugged ridges.",
        "image_url": "https://images.unsplash.com/photo-1501785888041-af3ef285b470",

        "overview": """Mount Kenya, Africa’s second‑highest mountain, offers one of the continent’s most beautiful 
    trekking experiences. While the highest peaks require technical climbing, Point Lenana (4,985m) is accessible 
    to trekkers via scenic trails passing through bamboo forests, moorlands, alpine lakes, and dramatic volcanic 
    ridges. The mountain’s unique ecosystems and rugged beauty make it a world‑class trekking destination.""",

        "best_season": "January to March, July to October",
        "elevation_gain": "3,000m",
        "duration_days": 4,
        "starting_point": "Sirimon Gate",
        "ending_point": "Lenana Peak",

        "map_embed": "<iframe src='https://www.google.com/maps/embed?...'></iframe>",

        "itinerary": [
            {"day": 1, "title": "Sirimon Gate to Old Moses Camp",
             "desc": "Gradual ascent through forest and moorland."},
            {"day": 2, "title": "Old Moses to Shipton Camp", "desc": "Pass dramatic ridges and alpine valleys."},
            {"day": 3, "title": "Shipton Camp to Lenana Summit → Down to Mintos",
             "desc": "Early morning summit push with stunning sunrise."},
            {"day": 4, "title": "Mintos to Chogoria Gate", "desc": "Descend through lush forests and waterfalls."}
        ],

        "how_to_reach": "Drive from Nairobi to Nanyuki → Sirimon Gate.",
        "permits": "Park entry fee required.",
        "packing_list": "Warm layers, gloves, trekking poles, hydration pack.",
        "safety_tips": "Acclimatize properly; weather can change rapidly.",
        "accommodation": "Mountain huts and campsites.",
        "weather": "Cold nights, mild days, unpredictable storms.",
        "faqs": [
            {"q": "Is Lenana technical?", "a": "No, it is a trekking peak."},
            {"q": "Which route is best?", "a": "Sirimon–Chogoria is the most scenic."}
        ]
    },
    {
        "name": "Mount Cameroon",
        "country": "Cameroon",
        "difficulty": "Hard",
        "distance_km": 38,
        "description": "A volcanic trek to West Africa’s highest peak, crossing lava fields and cloud forests.",
        "image_url": "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee",

        "overview": """Mount Cameroon, also known as Mongo ma Ndemi, is West Africa’s highest mountain and one of the 
    continent’s most active volcanoes. The trek features diverse ecosystems, from dense cloud forests to barren 
    volcanic slopes and ancient lava flows. The climb is steep and physically demanding, but the panoramic views 
    over the Atlantic coast and surrounding landscapes make it an unforgettable adventure.""",

        "best_season": "November to March",
        "elevation_gain": "3,000m",
        "duration_days": 2,
        "starting_point": "Buea",
        "ending_point": "Mount Cameroon Summit",

        "map_embed": "<iframe src='https://www.google.com/maps/embed?...'></iframe>",

        "itinerary": [
            {"day": 1, "title": "Buea to Hut 2", "desc": "Steep ascent through rainforest and savanna zones."},
            {"day": 2, "title": "Hut 2 to Summit → Return",
             "desc": "Climb volcanic slopes to the summit, then descend to Buea."}
        ],

        "how_to_reach": "Drive from Douala to Buea (1.5 hours).",
        "permits": "Climbing permit required; guides mandatory.",
        "packing_list": "Sturdy boots, warm layers, gloves, snacks.",
        "safety_tips": "Beware of loose volcanic rocks; pace yourself on steep sections.",
        "accommodation": "Basic huts on the mountain; hotels in Buea.",
        "weather": "Cool summit, humid forests.",
        "faqs": [
            {"q": "Is Mount Cameroon active?", "a": "Yes, but eruptions are monitored closely."}
        ]
    },
    {
        "name": "Mount Cameroon",
        "country": "Cameroon",
        "difficulty": "Hard",
        "distance_km": 38,
        "description": "A volcanic trek to West Africa’s highest peak, crossing lava fields and cloud forests.",
        "image_url": "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee",

        "overview": """Mount Cameroon, also known as Mongo ma Ndemi, is West Africa’s highest mountain and one of the 
    continent’s most active volcanoes. The trek features diverse ecosystems, from dense cloud forests to barren 
    volcanic slopes and ancient lava flows. The climb is steep and physically demanding, but the panoramic views 
    over the Atlantic coast and surrounding landscapes make it an unforgettable adventure.""",

        "best_season": "November to March",
        "elevation_gain": "3,000m",
        "duration_days": 2,
        "starting_point": "Buea",
        "ending_point": "Mount Cameroon Summit",

        "map_embed": "<iframe src='https://www.google.com/maps/embed?...'></iframe>",

        "itinerary": [
            {"day": 1, "title": "Buea to Hut 2", "desc": "Steep ascent through rainforest and savanna zones."},
            {"day": 2, "title": "Hut 2 to Summit → Return",
             "desc": "Climb volcanic slopes to the summit, then descend to Buea."}
        ],

        "how_to_reach": "Drive from Douala to Buea (1.5 hours).",
        "permits": "Climbing permit required; guides mandatory.",
        "packing_list": "Sturdy boots, warm layers, gloves, snacks.",
        "safety_tips": "Beware of loose volcanic rocks; pace yourself on steep sections.",
        "accommodation": "Basic huts on the mountain; hotels in Buea.",
        "weather": "Cool summit, humid forests.",
        "faqs": [
            {"q": "Is Mount Cameroon active?", "a": "Yes, but eruptions are monitored closely."}
        ]
    },
    {
        "name": "Mount Cameroon",
        "country": "Cameroon",
        "difficulty": "Hard",
        "distance_km": 38,
        "description": "A volcanic trek to West Africa’s highest peak, crossing lava fields and cloud forests.",
        "image_url": "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee",

        "overview": """Mount Cameroon, also known as Mongo ma Ndemi, is West Africa’s highest mountain and one of the 
    continent’s most active volcanoes. The trek features diverse ecosystems, from dense cloud forests to barren 
    volcanic slopes and ancient lava flows. The climb is steep and physically demanding, but the panoramic views 
    over the Atlantic coast and surrounding landscapes make it an unforgettable adventure.""",

        "best_season": "November to March",
        "elevation_gain": "3,000m",
        "duration_days": 2,
        "starting_point": "Buea",
        "ending_point": "Mount Cameroon Summit",

        "map_embed": "<iframe src='https://www.google.com/maps/embed?...'></iframe>",

        "itinerary": [
            {"day": 1, "title": "Buea to Hut 2", "desc": "Steep ascent through rainforest and savanna zones."},
            {"day": 2, "title": "Hut 2 to Summit → Return",
             "desc": "Climb volcanic slopes to the summit, then descend to Buea."}
        ],

        "how_to_reach": "Drive from Douala to Buea (1.5 hours).",
        "permits": "Climbing permit required; guides mandatory.",
        "packing_list": "Sturdy boots, warm layers, gloves, snacks.",
        "safety_tips": "Beware of loose volcanic rocks; pace yourself on steep sections.",
        "accommodation": "Basic huts on the mountain; hotels in Buea.",
        "weather": "Cool summit, humid forests.",
        "faqs": [
            {"q": "Is Mount Cameroon active?", "a": "Yes, but eruptions are monitored closely."}
        ]
    },
    {
        "name": "Mount Triglav (Krma Route)",
        "country": "Slovenia",
        "difficulty": "Hard",
        "distance_km": 26,
        "description": "A scenic ascent of Slovenia’s highest peak via the long Krma Valley approach.",
        "image_url": "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee",

        "overview": """The Krma Route is the longest but gentlest approach to Mount Triglav, Slovenia’s national 
    symbol. This trail winds through the peaceful Krma Valley before climbing steadily toward the Kredarica Hut 
    and the exposed summit ridge. The final ascent includes via ferrata sections, offering a thrilling but 
    manageable climb to the top of the Julian Alps.""",

        "best_season": "July to September",
        "elevation_gain": "1,900m",
        "duration_days": 2,
        "starting_point": "Krma Valley Trailhead",
        "ending_point": "Triglav Summit",

        "map_embed": "<iframe src='https://www.google.com/maps/embed?...'></iframe>",

        "itinerary": [
            {"day": 1, "title": "Krma Valley to Kredarica Hut",
             "desc": "A long but steady ascent through forests and alpine meadows."},
            {"day": 2, "title": "Kredarica Hut to Summit → Return",
             "desc": "Climb via ferrata sections to reach the summit, then descend back to the valley."}
        ],

        "how_to_reach": "Drive from Ljubljana to Krma Valley trailhead.",
        "permits": "No permits required.",
        "packing_list": "Helmet, via ferrata kit, gloves, warm layers.",
        "safety_tips": "Weather changes quickly; avoid exposed ridges during storms.",
        "accommodation": "Kredarica Hut (mountain refuge).",
        "weather": "Cool alpine climate with sudden changes.",
        "faqs": [
            {"q": "Is the Krma Route easier?", "a": "It is longer but less steep than other routes."}
        ]
    },
    {
        "name": "Mount Toubkal",
        "country": "Morocco",
        "difficulty": "Hard",
        "distance_km": 25,
        "description": "A high‑altitude ascent to the highest peak in North Africa, rising above the Atlas Mountains.",
        "image_url": "https://images.unsplash.com/photo-1500534314209-a25ddb2bd429",

        "overview": """Mount Toubkal, standing at 4,167 meters, is the highest peak in North Africa and one of the 
    most popular trekking destinations in Morocco. The route begins in the traditional Berber village of Imlil 
    and climbs through rugged valleys, rocky slopes, and high‑altitude terrain. The summit offers sweeping views 
    over the Atlas Mountains and the Sahara Desert. This trek is challenging but achievable for fit hikers, 
    making it a perfect introduction to high‑altitude climbing.""",

        "best_season": "April to October",
        "elevation_gain": "2,400m",
        "duration_days": 2,
        "starting_point": "Imlil",
        "ending_point": "Toubkal Summit",

        "map_embed": "<iframe src='https://www.google.com/maps/embed?...'></iframe>",

        "itinerary": [
            {"day": 1, "title": "Imlil to Toubkal Refuge",
             "desc": "A steady ascent through Berber villages and rocky valleys to the mountain refuge."},
            {"day": 2, "title": "Refuge to Summit → Return to Imlil",
             "desc": "Early morning climb to the summit for sunrise, then descend back to Imlil."}
        ],

        "how_to_reach": "Drive from Marrakech to Imlil (1.5 hours).",
        "permits": "Passport registration required at trail checkpoints.",
        "packing_list": "Warm layers, gloves, trekking poles, headlamp.",
        "safety_tips": "Start early; summit winds can be strong and cold.",
        "accommodation": "Toubkal Refuge (mountain hut).",
        "weather": "Cold summit, mild valleys.",
        "faqs": [
            {"q": "Is a guide required?", "a": "Yes, guides are mandatory in the Toubkal region."}
        ]
    },
    {
        "name": "Mount Sinai",
        "country": "Egypt",
        "difficulty": "Medium",
        "distance_km": 7,
        "description": "A historic pilgrimage trek to the summit where Moses is said to have received the Ten Commandments.",
        "image_url": "https://images.unsplash.com/photo-1501785888041-af3ef285b470",

        "overview": """Mount Sinai, rising from the desert of the Sinai Peninsula, is one of the most spiritually 
    significant mountains in the world. The trek is a pilgrimage for people of many faiths and offers a 
    breathtaking sunrise experience from the summit. The route passes ancient monasteries, rugged desert 
    landscapes, and historic stone steps carved centuries ago. This trek is accessible yet deeply meaningful, 
    blending natural beauty with profound cultural heritage.""",

        "best_season": "October to April",
        "elevation_gain": "700m",
        "duration_days": 1,
        "starting_point": "St. Catherine’s Monastery",
        "ending_point": "Mount Sinai Summit",

        "map_embed": "<iframe src='https://www.google.com/maps/embed?...'></iframe>",

        "itinerary": [
            {"day": 1, "title": "Night Ascent to Mount Sinai",
             "desc": "Climb the Camel Path or the Steps of Repentance to reach the summit for sunrise."}
        ],

        "how_to_reach": "Drive from Sharm El Sheikh or Dahab to St. Catherine’s Monastery.",
        "permits": "Entrance fee required at the monastery.",
        "packing_list": "Warm jacket, flashlight, water, snacks.",
        "safety_tips": "Night temperatures can be freezing; bring warm layers.",
        "accommodation": "Guesthouses near St. Catherine’s Monastery.",
        "weather": "Cold nights, warm days.",
        "faqs": [
            {"q": "Is the climb difficult?", "a": "Moderate, with well‑maintained paths."}
        ]
    },
    {
        "name": "Mount Ararat",
        "country": "Turkey",
        "difficulty": "Hard",
        "distance_km": 34,
        "description": "A high‑altitude volcanic ascent to Turkey’s highest peak, steeped in biblical legend.",
        "image_url": "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee",

        "overview": """Mount Ararat, rising to 5,137 meters, is the highest peak in Turkey and a massive dormant 
    volcano. The mountain is famously associated with the legend of Noah’s Ark and offers a challenging 
    high‑altitude climb across rocky slopes and permanent snowfields. The trek requires proper acclimatization 
    and is typically done with licensed guides. The summit provides sweeping views over Turkey, Armenia, and Iran.""",

        "best_season": "July to September",
        "elevation_gain": "3,200m",
        "duration_days": 4,
        "starting_point": "Dogubayazit",
        "ending_point": "Ararat Summit",

        "map_embed": "<iframe src='https://www.google.com/maps/embed?...'></iframe>",

        "itinerary": [
            {"day": 1, "title": "Dogubayazit to Camp 1", "desc": "Drive to the trailhead and hike to the first camp."},
            {"day": 2, "title": "Camp 1 to Camp 2", "desc": "Steep ascent to high camp at 4,200m."},
            {"day": 3, "title": "Summit Day → Return to Camp 2",
             "desc": "Early morning climb across snowfields to the summit."},
            {"day": 4, "title": "Camp 2 to Dogubayazit", "desc": "Descend to the trailhead and return to town."}
        ],

        "how_to_reach": "Fly to Agri or Van → drive to Dogubayazit.",
        "permits": "Special climbing permit required; must join a licensed expedition.",
        "packing_list": "Crampons, ice axe, warm layers, high‑altitude boots.",
        "safety_tips": "Acclimatize properly; summit winds can be extreme.",
        "accommodation": "Tents at high camps; hotels in Dogubayazit.",
        "weather": "Cold summit, windy ridges, mild lower slopes.",
        "faqs": [
            {"q": "Is Mount Ararat technical?", "a": "Non‑technical but requires glacier gear."}
        ]
    },
    {
        "name": "Mount Kazbek",
        "country": "Georgia",
        "difficulty": "Hard",
        "distance_km": 32,
        "description": "A dramatic glacier ascent to one of the most iconic peaks in the Caucasus.",
        "image_url": "https://images.unsplash.com/photo-1500534314209-a25ddb2bd429",

        "overview": """Mount Kazbek, rising to 5,047 meters, is one of the most striking peaks in the Caucasus and a 
    legendary mountain in Georgian folklore. The trek begins in the village of Stepantsminda and climbs past the 
    famous Gergeti Trinity Church before entering high‑altitude glacier terrain. The ascent requires proper 
    acclimatization and basic mountaineering skills, but the reward is a breathtaking summit overlooking the 
    rugged Caucasus range.""",

        "best_season": "June to September",
        "elevation_gain": "3,000m",
        "duration_days": 4,
        "starting_point": "Stepantsminda",
        "ending_point": "Kazbek Summit",

        "map_embed": "<iframe src='https://www.google.com/maps/embed?...'></iframe>",

        "itinerary": [
            {"day": 1, "title": "Stepantsminda to Altihut",
             "desc": "Hike past Gergeti Church and ascend to the high‑altitude hut."},
            {"day": 2, "title": "Acclimatization Day",
             "desc": "Short hikes around the glacier to prepare for summit day."},
            {"day": 3, "title": "Summit Push → Return to Altihut",
             "desc": "Early morning glacier ascent to the summit of Kazbek."},
            {"day": 4, "title": "Descent to Stepantsminda",
             "desc": "Return to the valley with stunning views of the Caucasus."}
        ],

        "how_to_reach": "Drive from Tbilisi to Stepantsminda via the Georgian Military Highway.",
        "permits": "No permits required, but registration recommended.",
        "packing_list": "Crampons, ice axe, harness, warm layers, glacier goggles.",
        "safety_tips": "Beware of crevasses; climb with experienced guides.",
        "accommodation": "Altihut or Betlemi Hut.",
        "weather": "Cold summit, windy ridges, unpredictable storms.",
        "faqs": [
            {"q": "Is Kazbek technical?", "a": "Moderately technical due to glacier travel."}
        ]
    },
    {
        "name": "Aoraki / Mount Cook Hooker Valley Track",
        "country": "New Zealand",
        "difficulty": "Easy",
        "distance_km": 10,
        "description": "A stunning alpine valley walk with views of glaciers, lakes, and New Zealand’s highest peak.",
        "image_url": "https://images.unsplash.com/photo-1501785888041-af3ef285b470",

        "overview": """The Hooker Valley Track is one of New Zealand’s most iconic day hikes, offering spectacular 
    views of Aoraki / Mount Cook, the highest mountain in the country. The trail crosses swing bridges, passes 
    glacial rivers, and ends at the iceberg‑filled Hooker Lake. This trek is accessible to all fitness levels and 
    showcases the dramatic beauty of the Southern Alps.""",

        "best_season": "October to April",
        "elevation_gain": "150m",
        "duration_days": 1,
        "starting_point": "White Horse Hill Campground",
        "ending_point": "Hooker Lake",

        "map_embed": "<iframe src='https://www.google.com/maps/embed?...'></iframe>",

        "itinerary": [
            {"day": 1, "title": "Hooker Valley Track",
             "desc": "Walk across swing bridges and alpine boardwalks to reach Hooker Lake with views of Aoraki."}
        ],

        "how_to_reach": "Drive from Christchurch or Queenstown to Mount Cook Village.",
        "permits": "No permits required.",
        "packing_list": "Sun protection, water, snacks, windbreaker.",
        "safety_tips": "Weather changes quickly; check conditions before hiking.",
        "accommodation": "Mount Cook Village lodges and campgrounds.",
        "weather": "Cool alpine climate with strong winds.",
        "faqs": [
            {"q": "Is this trail suitable for beginners?", "a": "Yes, it is one of New Zealand’s easiest iconic hikes."}
        ]
    },
    {
        "name": "Mount Fuji (Yoshida Trail)",
        "country": "Japan",
        "difficulty": "Medium",
        "distance_km": 14,
        "description": "A classic pilgrimage climb to Japan’s highest and most sacred mountain.",
        "image_url": "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee",

        "overview": """Mount Fuji, rising to 3,776 meters, is Japan’s tallest and most iconic mountain. The Yoshida 
    Trail is the most popular route, offering mountain huts, rest stations, and panoramic views of the Kanto 
    region. The climb is steep but non‑technical, attracting thousands of pilgrims and hikers each year. 
    Reaching the summit for sunrise — known as *Goraiko* — is considered a deeply spiritual experience.""",

        "best_season": "July to September",
        "elevation_gain": "1,450m",
        "duration_days": 2,
        "starting_point": "Fifth Station",
        "ending_point": "Fuji Summit",

        "map_embed": "<iframe src='https://www.google.com/maps/embed?...'></iframe>",

        "itinerary": [
            {"day": 1, "title": "Fifth Station to Mountain Hut",
             "desc": "Climb volcanic switchbacks to the 7th or 8th Station huts."},
            {"day": 2, "title": "Summit Push → Return",
             "desc": "Early morning ascent to catch sunrise from the crater rim, then descend to Fifth Station."}
        ],

        "how_to_reach": "Bus from Tokyo or Kawaguchiko to the Fifth Station.",
        "permits": "Voluntary climbing fee; mandatory during peak season.",
        "packing_list": "Warm layers, gloves, headlamp, snacks, water.",
        "safety_tips": "Altitude sickness is common; ascend slowly.",
        "accommodation": "Mountain huts along the trail.",
        "weather": "Cold summit, windy ridges, mild lower slopes.",
        "faqs": [
            {"q": "Is Fuji crowded?", "a": "Yes, especially during weekends and holidays."}
        ]
    },
    {
        "name": "Mount Roraima",
        "country": "Venezuela / Brazil / Guyana",
        "difficulty": "Hard",
        "distance_km": 34,
        "description": "A surreal trek to the tabletop summit that inspired Arthur Conan Doyle’s 'The Lost World'.",
        "image_url": "https://images.unsplash.com/photo-1500534314209-a25ddb2bd429",

        "overview": """Mount Roraima is one of the most extraordinary trekking destinations on Earth — a massive 
    tabletop mountain rising vertically from the jungle. Its summit is a prehistoric landscape of quartz fields, 
    strange rock formations, endemic plants, and deep fissures. The trek involves river crossings, jungle trails, 
    and a steep ascent up the natural ramp known as La Rampa. The experience feels like stepping into another 
    world, making it one of South America’s most unforgettable adventures.""",

        "best_season": "December to April",
        "elevation_gain": "1,800m",
        "duration_days": 6,
        "starting_point": "Paraitepui",
        "ending_point": "Roraima Summit",

        "map_embed": "<iframe src='https://www.google.com/maps/embed?...'></iframe>",

        "itinerary": [
            {"day": 1, "title": "Paraitepui to Rio Tek",
             "desc": "Cross savanna landscapes toward the base of the tepui."},
            {"day": 2, "title": "Rio Tek to Base Camp",
             "desc": "River crossings and views of Roraima’s massive cliffs."},
            {"day": 3, "title": "Base Camp to Summit", "desc": "Climb the steep natural ramp to reach the plateau."},
            {"day": 4, "title": "Summit Exploration",
             "desc": "Visit the Valley of Crystals, La Ventana, and unique rock formations."},
            {"day": 5, "title": "Summit to Rio Tek", "desc": "Descend from the plateau and return to the savanna."},
            {"day": 6, "title": "Rio Tek to Paraitepui", "desc": "Final trek back to the village."}
        ],

        "how_to_reach": "Drive from Santa Elena de Uairén to Paraitepui.",
        "permits": "Local permits required; guides mandatory.",
        "packing_list": "Waterproof bags, insect repellent, sturdy boots, rain gear.",
        "safety_tips": "Summit weather is unpredictable; stay with your guide.",
        "accommodation": "Tents at designated campsites.",
        "weather": "Warm lowlands, cool and rainy summit.",
        "faqs": [
            {"q": "Is the summit flat?", "a": "Yes, it is a vast plateau with unique formations."}
        ]
    },
    {
        "name": "Laguna de los Tres (Mount Fitz Roy)",
        "country": "Argentina",
        "difficulty": "Medium",
        "distance_km": 20,
        "description": "A spectacular Patagonian trek to the iconic viewpoint beneath Mount Fitz Roy.",
        "image_url": "https://images.unsplash.com/photo-1501785888041-af3ef285b470",

        "overview": """Laguna de los Tres is one of Patagonia’s most famous day hikes, offering jaw‑dropping views of 
    Mount Fitz Roy — a towering granite spire that dominates the skyline. The trail begins in El Chaltén and 
    winds through forests, rivers, and glacial valleys before a steep final ascent to the turquoise lake. 
    This trek is a must‑do for anyone visiting Argentine Patagonia.""",

        "best_season": "November to March",
        "elevation_gain": "800m",
        "duration_days": 1,
        "starting_point": "El Chaltén",
        "ending_point": "Laguna de los Tres",

        "map_embed": "<iframe src='https://www.google.com/maps/embed?...'></iframe>",

        "itinerary": [
            {"day": 1, "title": "Laguna de los Tres Trail",
             "desc": "A scenic hike through forests and valleys with a steep final climb to the lake."}
        ],

        "how_to_reach": "Bus or drive from El Calafate to El Chaltén.",
        "permits": "No permits required.",
        "packing_list": "Windproof jacket, water, snacks, trekking poles.",
        "safety_tips": "Patagonian winds can be extreme; secure your gear.",
        "accommodation": "Hotels and hostels in El Chaltén.",
        "weather": "Windy, cool, and unpredictable.",
        "faqs": [
            {"q": "Is the final climb difficult?", "a": "Steep but manageable with breaks."}
        ]
    },
    {
        "name": "Torres del Paine W Trek",
        "country": "Chile",
        "difficulty": "Hard",
        "distance_km": 80,
        "description": "A world‑famous Patagonian trek featuring granite towers, glaciers, and turquoise lakes.",
        "image_url": "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee",

        "overview": """The W Trek in Torres del Paine National Park is one of the most iconic multi‑day hikes in the 
    world. The route winds through dramatic valleys, past massive glaciers, and beneath the towering granite 
    spires known as the Torres. Trekkers experience the raw power of Patagonian weather, the beauty of glacial 
    lakes, and some of the most dramatic landscapes on Earth. This trek is challenging but deeply rewarding.""",

        "best_season": "November to March",
        "elevation_gain": "2,500m",
        "duration_days": 5,
        "starting_point": "Refugio Las Torres",
        "ending_point": "Paine Grande",

        "map_embed": "<iframe src='https://www.google.com/maps/embed?...'></iframe>",

        "itinerary": [
            {"day": 1, "title": "Las Torres to Base of the Towers",
             "desc": "Climb to the iconic viewpoint beneath the granite spires."},
            {"day": 2, "title": "Refugio to Los Cuernos", "desc": "Walk along turquoise lakes with mountain views."},
            {"day": 3, "title": "Los Cuernos to French Valley", "desc": "Explore the dramatic glacial valley."},
            {"day": 4, "title": "French Valley to Paine Grande",
             "desc": "Traverse rolling terrain with views of the Paine Massif."},
            {"day": 5, "title": "Grey Glacier Viewpoint",
             "desc": "Hike to the viewpoint overlooking the massive Grey Glacier."}
        ],

        "how_to_reach": "Bus from Puerto Natales to Torres del Paine National Park.",
        "permits": "Park entry fee required; refugio reservations mandatory.",
        "packing_list": "Windproof layers, trekking poles, snacks, hydration system.",
        "safety_tips": "Patagonian winds are extreme; secure tents and gear.",
        "accommodation": "Refugios and campsites along the route.",
        "weather": "Windy, cold, rapidly changing.",
        "faqs": [
            {"q": "Is the W Trek crowded?", "a": "Yes during peak season; book early."}
        ]
    },
    {
        "name": "Mount Whitney",
        "country": "United States",
        "difficulty": "Hard",
        "distance_km": 35,
        "description": "A demanding high‑altitude trek to the highest summit in the contiguous United States.",
        "image_url": "https://images.unsplash.com/photo-1500534314209-a25ddb2bd429",

        "overview": """Mount Whitney, standing at 4,421 meters (14,505 ft), is the tallest peak in the contiguous 
    United States. The classic Whitney Trail begins in Lone Pine and climbs through alpine forests, granite 
    switchbacks, and high‑altitude ridges before reaching the summit. The trek is physically demanding due to 
    elevation and distance, but the panoramic views over the Sierra Nevada make it one of America’s most iconic 
    mountain adventures.""",

        "best_season": "July to October",
        "elevation_gain": "1,900m",
        "duration_days": 2,
        "starting_point": "Whitney Portal",
        "ending_point": "Mount Whitney Summit",

        "map_embed": "<iframe src='https://www.google.com/maps/embed?...'></iframe>",

        "itinerary": [
            {"day": 1, "title": "Whitney Portal to Trail Camp",
             "desc": "A steady climb through forests and granite terrain to the main high camp."},
            {"day": 2, "title": "Trail Camp to Summit → Return",
             "desc": "Early morning ascent up the 99 Switchbacks to reach the summit, then descend to Whitney Portal."}
        ],

        "how_to_reach": "Drive from Los Angeles or Reno to Lone Pine → Whitney Portal.",
        "permits": "Highly regulated; lottery permit required.",
        "packing_list": "Warm layers, trekking poles, headlamp, hydration system.",
        "safety_tips": "Altitude sickness is common; acclimatize properly.",
        "accommodation": "Camping at Trail Camp or Whitney Portal.",
        "weather": "Cold summit, dry alpine climate.",
        "faqs": [
            {"q": "Is the Whitney permit hard to get?", "a": "Yes, the lottery is competitive."}
        ]
    },
    {
        "name": "Mount Rainier (Camp Muir Route)",
        "country": "United States",
        "difficulty": "Hard",
        "distance_km": 14,
        "description": "A challenging high‑altitude trek to Camp Muir on the slopes of Mount Rainier.",
        "image_url": "https://images.unsplash.com/photo-1501785888041-af3ef285b470",

        "overview": """Mount Rainier is one of the most iconic peaks in the Pacific Northwest, rising to 4,392 meters 
    (14,411 ft). The trek to Camp Muir is a demanding but non‑technical climb that takes hikers across volcanic 
    ridges, snowfields, and glacial terrain. Camp Muir sits at 3,063 meters and serves as the base camp for 
    summit expeditions. The route offers spectacular views of the Nisqually Glacier and the surrounding Cascades.""",

        "best_season": "June to September",
        "elevation_gain": "1,400m",
        "duration_days": 1,
        "starting_point": "Paradise",
        "ending_point": "Camp Muir",

        "map_embed": "<iframe src='https://www.google.com/maps/embed?...'></iframe>",

        "itinerary": [
            {"day": 1, "title": "Paradise to Camp Muir",
             "desc": "Climb steadily across snowfields and volcanic slopes to reach the high camp."}
        ],

        "how_to_reach": "Drive from Seattle or Tacoma to Mount Rainier National Park (Paradise).",
        "permits": "Climbing pass required for travel above 10,000 ft.",
        "packing_list": "Crampons (early season), warm layers, sunglasses, trekking poles.",
        "safety_tips": "Snowfields can be icy; weather changes rapidly.",
        "accommodation": "Camp Muir shelters (very basic).",
        "weather": "Cold, windy, and unpredictable.",
        "faqs": [
            {"q": "Is Camp Muir dangerous?", "a": "Safe with proper gear and weather awareness."}
        ]
    },
    {
        "name": "Mount Hood (South Side Route)",
        "country": "United States",
        "difficulty": "Hard",
        "distance_km": 11,
        "description": "A steep alpine ascent to Oregon’s highest peak via the classic south side route.",
        "image_url": "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee",

        "overview": """Mount Hood, rising to 3,429 meters (11,249 ft), is Oregon’s highest peak and one of the most 
    climbed glaciated mountains in the United States. The South Side Route is the standard ascent, beginning at 
    Timberline Lodge and climbing steep snowfields toward Crater Rock and the Hogsback Ridge. The final push 
    involves a steep chute leading to the summit ridge. This climb requires proper gear and early starts to avoid 
    rockfall and soft snow.""",

        "best_season": "May to July",
        "elevation_gain": "1,600m",
        "duration_days": 1,
        "starting_point": "Timberline Lodge",
        "ending_point": "Mount Hood Summit",

        "map_embed": "<iframe src='https://www.google.com/maps/embed?...'></iframe>",

        "itinerary": [
            {"day": 1, "title": "Timberline to Summit → Return",
             "desc": "Early morning ascent across steep snowfields to reach the summit ridge, then descend before conditions soften."}
        ],

        "how_to_reach": "Drive from Portland to Timberline Lodge.",
        "permits": "Climbing permit required above 9,500 ft.",
        "packing_list": "Crampons, ice axe, helmet, warm layers, headlamp.",
        "safety_tips": "Start early; rockfall and avalanches are common later in the day.",
        "accommodation": "Timberline Lodge or nearby campgrounds.",
        "weather": "Cold mornings, rapidly changing alpine conditions.",
        "faqs": [
            {"q": "Is Mount Hood technical?", "a": "Moderately technical with steep snow climbing."}
        ]
    },
    {
        "name": "Everest Base Camp Trek",
        "country": "Nepal",
        "difficulty": "Hard",
        "distance_km": 130,
        "description": "A world‑famous high‑altitude trek through the Khumbu Valley to the base of Mount Everest.",
        "image_url": "https://images.unsplash.com/photo-1500534314209-a25ddb2bd429",

        "overview": """The Everest Base Camp Trek is one of the most iconic trekking routes on the planet. 
    Beginning with a thrilling flight to Lukla, the trail winds through Sherpa villages, Buddhist monasteries, 
    suspension bridges, and dramatic Himalayan landscapes. Trekkers experience the culture of the Khumbu region 
    while gradually ascending toward Everest Base Camp at 5,364 meters. The route offers breathtaking views of 
    Everest, Lhotse, Ama Dablam, and the surrounding giants of the Himalayas.""",

        "best_season": "March to May, September to November",
        "elevation_gain": "2,700m",
        "duration_days": 12,
        "starting_point": "Lukla",
        "ending_point": "Everest Base Camp",

        "map_embed": "<iframe src='https://www.google.com/maps/embed?...'></iframe>",

        "itinerary": [
            {"day": 1, "title": "Lukla to Phakding", "desc": "A gentle warm‑up walk along the Dudh Koshi River."},
            {"day": 2, "title": "Phakding to Namche Bazaar",
             "desc": "Cross suspension bridges and climb to the Sherpa capital."},
            {"day": 3, "title": "Acclimatization in Namche", "desc": "Optional hike to Everest View Hotel."},
            {"day": 4, "title": "Namche to Tengboche", "desc": "Visit the famous Tengboche Monastery."},
            {"day": 5, "title": "Tengboche to Dingboche",
             "desc": "Walk through rhododendron forests and alpine terrain."},
            {"day": 6, "title": "Acclimatization in Dingboche",
             "desc": "Hike to Nagarjun Hill for altitude adjustment."},
            {"day": 7, "title": "Dingboche to Lobuche", "desc": "Pass memorials dedicated to climbers."},
            {"day": 8, "title": "Lobuche to Gorak Shep → Everest Base Camp",
             "desc": "Reach the legendary base of the world’s highest mountain."},
            {"day": 9, "title": "Kala Patthar Sunrise", "desc": "Optional climb for the best Everest viewpoint."},
            {"day": 10, "title": "Descent to Pheriche", "desc": "Begin the return journey."},
            {"day": 11, "title": "Pheriche to Namche", "desc": "Retrace steps through the Khumbu Valley."},
            {"day": 12, "title": "Namche to Lukla", "desc": "Final day of the trek."}
        ],

        "how_to_reach": "Fly from Kathmandu to Lukla.",
        "permits": "TIMS card + Sagarmatha National Park permit.",
        "packing_list": "Down jacket, thermal layers, trekking poles, -10°C sleeping bag.",
        "safety_tips": "Acclimatize properly; avoid rushing; hydrate well.",
        "accommodation": "Tea houses along the route.",
        "weather": "Cold nights, clear mornings, unpredictable storms.",
        "faqs": [
            {"q": "Is this trek dangerous?", "a": "Safe with acclimatization and proper pacing."}
        ]
    },
    {
        "name": "Annapurna Circuit",
        "country": "Nepal",
        "difficulty": "Hard",
        "distance_km": 160,
        "description": "A legendary multi‑day trek circling the Annapurna massif, crossing the 5,416m Thorong La Pass.",
        "image_url": "https://images.unsplash.com/photo-1501785888041-af3ef285b470",

        "overview": """The Annapurna Circuit is one of the most diverse and rewarding long‑distance treks in the world. 
    The route circles the entire Annapurna massif, passing through subtropical forests, deep river gorges, 
    Tibetan‑influenced villages, and high‑altitude deserts. The highlight is crossing Thorong La Pass at 5,416 meters, 
    one of the highest trekking passes on Earth. This trek offers unmatched cultural variety, dramatic landscapes, 
    and a true Himalayan adventure.""",

        "best_season": "March to May, October to November",
        "elevation_gain": "3,300m",
        "duration_days": 14,
        "starting_point": "Besisahar",
        "ending_point": "Jomsom / Pokhara",

        "map_embed": "<iframe src='https://www.google.com/maps/embed?...'></iframe>",

        "itinerary": [
            {"day": 1, "title": "Besisahar to Bhulbhule", "desc": "Walk through terraced fields and riverside trails."},
            {"day": 2, "title": "Bhulbhule to Chamje", "desc": "Enter the Marsyangdi Valley."},
            {"day": 3, "title": "Chamje to Dharapani", "desc": "Pass waterfalls and steep gorges."},
            {"day": 4, "title": "Dharapani to Chame", "desc": "Reach the district headquarters with mountain views."},
            {"day": 5, "title": "Chame to Pisang", "desc": "Walk through pine forests and dramatic cliffs."},
            {"day": 6, "title": "Pisang to Manang", "desc": "Enter the high‑altitude desert region."},
            {"day": 7, "title": "Acclimatization in Manang", "desc": "Optional hikes to Ice Lake or Gangapurna Lake."},
            {"day": 8, "title": "Manang to Yak Kharka", "desc": "Gradual ascent toward the pass."},
            {"day": 9, "title": "Yak Kharka to Thorong Phedi", "desc": "Reach the base of the high pass."},
            {"day": 10, "title": "Thorong La Pass → Muktinath",
             "desc": "Cross the 5,416m pass with breathtaking views."},
            {"day": 11, "title": "Muktinath to Kagbeni", "desc": "Walk through ancient Mustang villages."},
            {"day": 12, "title": "Kagbeni to Jomsom", "desc": "Windy valley walk to the airport town."},
            {"day": 13, "title": "Jomsom to Pokhara (Flight)", "desc": "Optional flight or continue trekking."},
            {"day": 14, "title": "Pokhara Rest Day", "desc": "Relax by the lakeside after the long trek."}
        ],

        "how_to_reach": "Drive from Kathmandu to Besisahar; return via Jomsom or Pokhara.",
        "permits": "ACAP permit + TIMS card.",
        "packing_list": "Down jacket, trekking poles, warm layers, sunscreen.",
        "safety_tips": "Acclimatize properly; Thorong La can be dangerous in bad weather.",
        "accommodation": "Tea houses along the entire route.",
        "weather": "Varied — tropical lowlands to freezing high passes.",
        "faqs": [
            {"q": "Is the Annapurna Circuit still popular?", "a": "Yes, it remains one of the world’s top treks."}
        ]
    }

]
with app.app_context():
    for r in routes:
        print("Generating SEO for:", r["name"])

        seo = generate_seo_content(r)
        print("SEO GENERATED:", seo[:200] if seo else "NONE")

        route = Route(**r)
        route.seo_content = seo

        db.session.add(route)

    db.session.commit()


