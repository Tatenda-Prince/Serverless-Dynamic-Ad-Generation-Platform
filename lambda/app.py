import json
import logging
import time
import random

# Configure logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    try:
        logger.info(f"Received event: {json.dumps(event)}")
        
        # Extract query parameters with South African defaults
        params = event.get("queryStringParameters") or {}
        view_mode = params.get("view", "list")  # Default to list view
        
        # Generate timestamp for unique image generation
        timestamp = str(int(time.time()))
        
        # Random Cape Town hotels for refresh
        cape_town_hotels = [
            {"name": "Cape Grace Hotel", "price": "R2,500", "rating": "5"},
            {"name": "The Silo Hotel", "price": "R4,200", "rating": "5"},
            {"name": "Belmond Mount Nelson", "price": "R3,800", "rating": "5"},
            {"name": "One&Only Cape Town", "price": "R5,500", "rating": "5"},
            {"name": "Camps Bay Retreat", "price": "R2,900", "rating": "4"},
            {"name": "Table Bay Hotel", "price": "R3,200", "rating": "4"},
            {"name": "Twelve Apostles Hotel", "price": "R4,800", "rating": "5"}
        ]
        
        # If no hotel specified or refresh requested, pick random hotel
        if not params.get("hotel") or params.get("t"):
            random_hotel = random.choice(cape_town_hotels)
            hotel_name = params.get("hotel", random_hotel["name"])
            price = params.get("price", random_hotel["price"])
            rating = params.get("rating", random_hotel["rating"])
        else:
            hotel_name = params.get("hotel", "Cape Grace Hotel")
            price = params.get("price", "R2,500")
            rating = params.get("rating", "4")
            
        location = params.get("location", "Cape Town, South Africa")
        
        logger.info(f"Processing request - View: {view_mode}, Hotel: {hotel_name if view_mode == 'single' else 'Multiple'}, Location: {location}")
        
        # Check if single view is requested, otherwise show list
        if view_mode == "single":
            # Continue to single ad generation
            pass
        else:
            return generate_hotel_list()
        
        logger.info(f"Processing ad for: {hotel_name}, {location}, {price}, {rating} stars")

        # Beautiful Cape Town luxury hotel images
        hotel_images = {
            "Cape Grace Hotel": "https://images.unsplash.com/photo-1571896349842-33c89424de2d?w=800&h=600&fit=crop&q=90",
            "The Silo Hotel": "https://images.unsplash.com/photo-1566073771259-6a8506099945?w=800&h=600&fit=crop&q=90",
            "Belmond Mount Nelson": "https://images.unsplash.com/photo-1582719478250-c89cae4dc85b?w=800&h=600&fit=crop&q=90",
            "One&Only Cape Town": "https://images.unsplash.com/photo-1580587771525-78b9dba3b914?w=800&h=600&fit=crop&q=90",
            "Camps Bay Retreat": "https://images.unsplash.com/photo-1576485290814-1c72aa4bbb8e?w=800&h=600&fit=crop&q=90",
            "Table Bay Hotel": "https://images.unsplash.com/photo-1564501049412-61c2a3083791?w=800&h=600&fit=crop&q=90",
            "Twelve Apostles Hotel": "https://images.unsplash.com/photo-1551882547-ff40c63fe5fa?w=800&h=600&fit=crop&q=90",
            "default": "https://images.unsplash.com/photo-1571896349842-33c89424de2d?w=800&h=600&fit=crop&q=90"
        }
        
        # Get hotel image with timestamp for freshness
        base_image = hotel_images.get(hotel_name, hotel_images["default"])
        hotel_image = f"{base_image}&t={timestamp}"
        
        # Create beautiful HTML hotel ad with real hotel image
        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Hotel Ad - {hotel_name}</title>
            <meta charset="UTF-8">
            <style>
                @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&family=Open+Sans:wght@400;600&display=swap');
                
                body {{ 
                    margin: 0; 
                    font-family: 'Open Sans', sans-serif; 
                    background: linear-gradient(135deg, #2c3e50 0%, #34495e 100%); 
                    min-height: 100vh;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                }}
                
                .ad-container {{ 
                    position: relative; 
                    width: 800px; 
                    height: 600px; 
                    background: linear-gradient(
                        rgba(0, 0, 0, 0.4), 
                        rgba(0, 0, 0, 0.6)
                    ), url('{hotel_image}');
                    background-size: cover;
                    background-position: center;
                    border-radius: 15px;
                    overflow: hidden;
                    box-shadow: 0 20px 60px rgba(0,0,0,0.4);
                    border: 3px solid #f39c12;
                }}
                
                .logo {{ 
                    position: absolute; 
                    top: 25px; 
                    right: 25px; 
                    width: 120px; 
                    height: 80px; 
                    background: linear-gradient(45deg, #3498db, #2980b9);
                    border-radius: 12px;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    font-weight: bold;
                    color: white;
                    font-size: 14px;
                    box-shadow: 0 8px 20px rgba(0,0,0,0.4);
                    text-align: center;
                    line-height: 1.3;
                    border: 2px solid #f39c12;
                }}
                
                .search-container {{
                    position: absolute;
                    bottom: 30px;
                    right: 30px;
                    display: flex;
                    gap: 10px;
                }}
                
                .search-input {{
                    padding: 10px 15px;
                    border: none;
                    border-radius: 25px;
                    background: rgba(255,255,255,0.9);
                    color: #333;
                    font-size: 14px;
                    width: 200px;
                    outline: none;
                }}
                
                .search-btn {{
                    padding: 10px 20px;
                    background: linear-gradient(45deg, #e74c3c, #c0392b);
                    color: white;
                    border: none;
                    border-radius: 25px;
                    font-weight: bold;
                    cursor: pointer;
                    font-size: 14px;
                    box-shadow: 0 4px 15px rgba(0,0,0,0.3);
                    margin-right: 10px;
                }}
                
                .refresh-btn {{
                    padding: 10px 15px;
                    background: linear-gradient(45deg, #f39c12, #e67e22);
                    color: white;
                    border: none;
                    border-radius: 25px;
                    font-weight: bold;
                    cursor: pointer;
                    font-size: 14px;
                    box-shadow: 0 4px 15px rgba(0,0,0,0.3);
                }}
                
                .content {{ 
                    position: absolute; 
                    top: 80px; 
                    left: 60px; 
                    right: 60px;
                    color: white; 
                }}
                
                .hotel-name {{ 
                    font-family: 'Playfair Display', serif;
                    font-size: 36px; 
                    font-weight: 700; 
                    margin-bottom: 12px; 
                    color: #ffffff; 
                    text-shadow: 3px 3px 6px rgba(0,0,0,0.8);
                    line-height: 1.1;
                }}
                
                .rating {{
                    font-size: 24px;
                    margin-bottom: 15px;
                    color: #f39c12;
                    text-shadow: 2px 2px 4px rgba(0,0,0,0.7);
                }}
                
                .location {{ 
                    font-size: 20px; 
                    margin-bottom: 25px; 
                    color: #f39c12; 
                    font-weight: 600;
                    text-shadow: 2px 2px 4px rgba(0,0,0,0.7);
                }}
                
                .location::before {{
                    content: '📍 ';
                    margin-right: 8px;
                }}
                
                .price {{ 
                    font-size: 24px; 
                    color: #3498db; 
                    font-weight: 700;
                    background: rgba(0,0,0,0.7);
                    padding: 10px 16px;
                    border-radius: 8px;
                    display: inline-block;
                    text-shadow: 2px 2px 4px rgba(0,0,0,0.8);
                    border: 2px solid #3498db;
                }}
                
                .status {{ 
                    position: absolute; 
                    bottom: 30px; 
                    left: 60px; 
                    background: linear-gradient(45deg, #2ecc71, #27ae60);
                    color: white; 
                    padding: 12px 20px; 
                    border-radius: 25px; 
                    font-weight: 600;
                    font-size: 16px;
                    box-shadow: 0 5px 15px rgba(0,0,0,0.3);
                }}
                

            </style>
        </head>
        <body>
            <div class="ad-container">
                <div class="logo">SkyTrip.com</div>
                <div class="content">
                    <div class="hotel-name"><a href="?view=list" style="color: inherit; text-decoration: none;">{hotel_name}</a></div>
                    <div class="rating">{'⭐' * int(rating)} ({rating}/5)</div>
                    <div class="location">{location}</div>
                    <div class="price">{price}</div>
                </div>
                <div class="search-container">
                    <input type="text" class="search-input" placeholder="Search destinations..." id="searchInput">
                    <button class="search-btn" onclick="searchLocation()">Search</button>
                    <button class="refresh-btn" onclick="refreshAd()" title="Generate New Ad">🔄</button>
                </div>
            </div>
            <script>
                function searchLocation() {{
                    const location = document.getElementById('searchInput').value;
                    if (location) {{
                        const currentUrl = new URL(window.location);
                        currentUrl.searchParams.set('location', location);
                        currentUrl.searchParams.set('t', Date.now()); // Force refresh
                        window.location.href = currentUrl.toString();
                    }}
                }}
                
                function refreshAd() {{
                    const currentUrl = new URL(window.location);
                    currentUrl.searchParams.set('t', Date.now());
                    // Remove hotel param to get random hotel
                    currentUrl.searchParams.delete('hotel');
                    currentUrl.searchParams.delete('price');
                    currentUrl.searchParams.delete('rating');
                    window.location.href = currentUrl.toString();
                }}
                
                document.getElementById('searchInput').addEventListener('keypress', function(e) {{
                    if (e.key === 'Enter') {{
                        searchLocation();
                    }}
                }});
                
                // Auto-refresh every 30 seconds for demo
                setTimeout(refreshAd, 30000);
            </script>
        </body>
        </html>
        """
        
        logger.info(f"Successfully generated hotel ad for {hotel_name} in {location} with image: {hotel_image}")
        return {
            "statusCode": 200,
            "headers": { 
                "Content-Type": "text/html",
                "Access-Control-Allow-Origin": "*"
            },
            "body": html_content
        }

    except Exception as e:
        logger.error(f"Error generating ad: {str(e)}")
        return {
            "statusCode": 500,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps({"error": str(e), "status": "failed"})
        }

def generate_hotel_list():
    """Generate HTML page with list of African hotels with images"""
    african_hotels = [
        {"name": "Cape Grace Hotel", "location": "Cape Town, South Africa", "price": "R2,500", "rating": 5, "image": "https://images.unsplash.com/photo-1571896349842-33c89424de2d?w=300&h=200&fit=crop&q=85"},
        {"name": "The Silo Hotel", "location": "Cape Town, South Africa", "price": "R4,200", "rating": 5, "image": "https://images.unsplash.com/photo-1566073771259-6a8506099945?w=300&h=200&fit=crop&q=85"},
        {"name": "Four Seasons Safari Lodge", "location": "Serengeti, Tanzania", "price": "$850", "rating": 5, "image": "https://images.unsplash.com/photo-1516026672322-bc52d61a55d5?w=300&h=200&fit=crop&q=85"},
        {"name": "Singita Grumeti", "location": "Serengeti, Tanzania", "price": "$1,200", "rating": 5, "image": "https://images.unsplash.com/photo-1547036967-23d11aacaee0?w=300&h=200&fit=crop&q=85"},
        {"name": "Giraffe Manor", "location": "Nairobi, Kenya", "price": "$590", "rating": 4, "image": "https://images.unsplash.com/photo-1523805009345-7448845a9e53?w=300&h=200&fit=crop&q=85"},
        {"name": "Hemingways Nairobi", "location": "Nairobi, Kenya", "price": "$320", "rating": 4, "image": "https://images.unsplash.com/photo-1518548419970-58e3b4079ab2?w=300&h=200&fit=crop&q=85"},
        {"name": "Royal Livingstone Hotel", "location": "Victoria Falls, Zambia", "price": "$420", "rating": 5, "image": "https://images.unsplash.com/photo-1547036967-23d11aacaee0?w=300&h=200&fit=crop&q=85"},
        {"name": "Belmond Mount Nelson", "location": "Cape Town, South Africa", "price": "R3,800", "rating": 5, "image": "https://images.unsplash.com/photo-1582719478250-c89cae4dc85b?w=300&h=200&fit=crop&q=85"},
        {"name": "La Mamounia", "location": "Marrakech, Morocco", "price": "€650", "rating": 5, "image": "https://images.unsplash.com/photo-1544735716-392fe2489ffa?w=300&h=200&fit=crop&q=85"},
        {"name": "Four Seasons Marrakech", "location": "Marrakech, Morocco", "price": "€480", "rating": 4, "image": "https://images.unsplash.com/photo-1539650116574-75c0c6d73f6e?w=300&h=200&fit=crop&q=85"},
        {"name": "Sofitel Legend Old Cataract", "location": "Aswan, Egypt", "price": "$280", "rating": 4, "image": "https://images.unsplash.com/photo-1564501049412-61c2a3083791?w=300&h=200&fit=crop&q=85"},
        {"name": "Twelve Apostles Hotel", "location": "Cape Town, South Africa", "price": "R4,800", "rating": 5, "image": "https://images.unsplash.com/photo-1551882547-ff40c63fe5fa?w=300&h=200&fit=crop&q=85"}
    ]
    
    hotel_cards = ""
    for hotel in african_hotels:
        stars = '⭐' * hotel['rating']
        hotel_cards += f"""
        <div class="hotel-card" onclick="selectHotel('{hotel['name']}', '{hotel['price']}', '{hotel['location']}', '{hotel['rating']}')">
            <div class="hotel-image" style="background-image: url('{hotel['image']}')"></div>
            <div class="hotel-info">
                <h3>{hotel['name']}</h3>
                <div class="hotel-rating">{stars} ({hotel['rating']}/5)</div>
                <div class="hotel-location">📍 {hotel['location']}</div>
                <div class="hotel-price">{hotel['price']} per night</div>
            </div>
        </div>
        """
    
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>African Hotels - SkyTrip.com</title>
        <meta charset="UTF-8">
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&family=Open+Sans:wght@400;600&display=swap');
            
            body {{
                margin: 0;
                font-family: 'Open Sans', sans-serif;
                background: linear-gradient(135deg, #2c3e50 0%, #34495e 100%);
                min-height: 100vh;
                padding: 20px;
            }}
            
            .header {{
                text-align: center;
                color: white;
                margin-bottom: 30px;
            }}
            
            .header h1 {{
                font-family: 'Playfair Display', serif;
                font-size: 48px;
                margin-bottom: 10px;
            }}
            
            .logo {{
                display: inline-block;
                background: linear-gradient(45deg, #3498db, #2980b9);
                color: white;
                padding: 10px 20px;
                border-radius: 25px;
                font-weight: bold;
                margin-bottom: 20px;
            }}
            
            .hotels-grid {{
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
                gap: 20px;
                max-width: 1000px;
                margin: 0 auto;
                padding: 0 20px;
            }}
            
            .hotel-card {{
                background: rgba(255,255,255,0.95);
                border-radius: 12px;
                overflow: hidden;
                box-shadow: 0 8px 25px rgba(0,0,0,0.2);
                cursor: pointer;
                transition: transform 0.3s ease;
                height: 320px;
                display: flex;
                flex-direction: column;
            }}
            
            .hotel-card:hover {{
                transform: translateY(-3px);
                box-shadow: 0 12px 35px rgba(0,0,0,0.3);
            }}
            
            .hotel-image {{
                width: 100%;
                height: 160px;
                background-size: cover;
                background-position: center;
                background-repeat: no-repeat;
                background-color: #f8f9fa;
            }}
            
            .hotel-info {{
                padding: 15px;
                flex: 1;
                display: flex;
                flex-direction: column;
                justify-content: space-between;
            }}
            
            .hotel-card h3 {{
                font-family: 'Playfair Display', serif;
                color: #2c3e50;
                margin: 0 0 8px 0;
                font-size: 18px;
                line-height: 1.2;
            }}
            
            .hotel-rating {{
                color: #f39c12;
                margin-bottom: 6px;
                font-size: 14px;
            }}
            
            .hotel-location {{
                color: #7f8c8d;
                margin-bottom: 8px;
                font-size: 13px;
            }}
            
            .hotel-price {{
                color: #3498db;
                font-weight: bold;
                font-size: 16px;
                margin-top: auto;
            }}
            
            .back-btn {{
                position: fixed;
                top: 15px;
                left: 15px;
                background: linear-gradient(45deg, #e74c3c, #c0392b);
                color: white;
                border: none;
                padding: 8px 16px;
                border-radius: 20px;
                cursor: pointer;
                font-weight: 600;
                text-decoration: none;
                font-size: 14px;
                box-shadow: 0 4px 12px rgba(0,0,0,0.2);
                transition: transform 0.2s ease;
            }}
            
            .back-btn:hover {{
                transform: translateY(-1px);
                box-shadow: 0 6px 16px rgba(0,0,0,0.3);
            }}
        </style>
    </head>
    <body>
        <a href="?view=single" class="back-btn">← Single Ad View</a>
        <div class="header">
            <div class="logo">SkyTrip.com</div>
            <h1>Luxury Hotels Across Africa</h1>
            <p>Click any hotel to generate an ad</p>
        </div>
        <div class="hotels-grid">
            {hotel_cards}
        </div>
        
        <script>
            function selectHotel(name, price, location, rating) {{
                // Redirect to single ad view with selected hotel
                const url = new URL(window.location);
                url.searchParams.set('view', 'single'); // Set to single view
                url.searchParams.set('hotel', name);
                url.searchParams.set('price', price);
                url.searchParams.set('location', location);
                url.searchParams.set('rating', rating);
                url.searchParams.set('t', Date.now());
                window.location.href = url.toString();
            }}
        </script>
    </body>
    </html>
    """
    
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "text/html",
            "Access-Control-Allow-Origin": "*"
        },
        "body": html_content
    }


