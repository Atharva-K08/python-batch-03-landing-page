from django.shortcuts import render
import requests

# Create your views here.


def home(request):
    studentList = [
        {"name": "Raju", "age": 21, "city": "Pune", "rollNo": 20},
        {"name": "Raj", "age": 23, "city": "Pune", "rollNo": 21},
        {"name": "Rajesh", "age": 21, "city": "Pune", "rollNo": 22},
        {"name": "Rajvardhan", "age": 20, "city": "Pune", "rollNo": 23},
    ]
    return render(request, 'website/home.html', {'studentList': studentList})


def about(request):
    return render(request, 'website/about.html')


def contact(request):
    return render(request, 'website/contact.html')


def product_page(request):
    products = [
        {
            "image": "https://akulenterprisesindia.com/wp-content/uploads/2025/08/2-3.png",
            "title": "Bath Towels",
            "material": "100% Cotton and 80/20 Cotton Blend",
            "description": "Soft, absorbent, and durable towels designed for everyday comfort and luxury.",
            "sizes": [
                {"contry": "Indian (cm)", "value": "70 x 140"},
                {"contry": "US / EU (inches)", "value": "27 x 52 / 30 x 56"},
            ],
            "usage": [
                "Hospitality", "Home", "Retail"
            ]
        },
        {
            "image": "https://akulenterprisesindia.com/wp-content/uploads/2025/09/Untitled-design-93.png",
            "title": "Hand Towels",
            "material": "100% Cotton and 80/20 Cotton Blend",
            "description": "Quick-dry, highly absorbent towels perfect for hotels, spas, and homes.",
            "sizes": [
                {"contry": "Indian (cm)", "value": "40 × 60 / 40 × 70"},
                {"contry": "US / EU (inches)", "value": "16 × 28 / 18 × 30"},
            ],
            "usage": [
                "Spas", "Home", "Wellness"
            ]
        },
        {
            "image": "https://akulenterprisesindia.com/wp-content/uploads/2025/08/1-3.png",
            "title": "Face Towels",
            "material": "100% Cotton and 80/20 Cotton Blend",
            "description": "Gentle and skin-friendly towels crafted for personal care and premium guest amenities.",
            "sizes": [
                {"contry": "Indian (cm)", "value": "30 x 30"},
                {"contry": "US / EU (inches)", "value": "12 x 12"},
            ],
            "usage": [
                "Personal Care", "Spa Kits", "Gifting"
            ]
        },
        {
            "image": "https://akulenterprisesindia.com/wp-content/uploads/2025/08/1-3.png",
            "title": "Face Towels",
            "material": "100% Cotton and 80/20 Cotton Blend",
            "description": "Gentle and skin-friendly towels crafted for personal care and premium guest amenities.",
            "sizes": [
                {"contry": "Indian (cm)", "value": "30 x 30"},
                {"contry": "US / EU (inches)", "value": "12 x 12"},
            ],
            "usage": [
                "Personal Care", "Spa Kits", "Gifting"
            ]
        },
        {
            "image": "https://akulenterprisesindia.com/wp-content/uploads/2025/08/1-3.png",
            "title": "Face Towels",
            "material": "100% Cotton and 80/20 Cotton Blend",
            "description": "Gentle and skin-friendly towels crafted for personal care and premium guest amenities.",
            "sizes": [
                {"contry": "Indian (cm)", "value": "30 x 30"},
                {"contry": "US / EU (inches)", "value": "12 x 12"},
            ],
            "usage": [
                "Personal Care", "Spa Kits", "Gifting"
            ]
        },
        {
            "image": "https://akulenterprisesindia.com/wp-content/uploads/2025/08/1-3.png",
            "title": "Face Towels",
            "material": "100% Cotton and 80/20 Cotton Blend",
            "description": "Gentle and skin-friendly towels crafted for personal care and premium guest amenities.",
            "sizes": [
                {"contry": "Indian (cm)", "value": "30 x 30"},
                {"contry": "US / EU (inches)", "value": "12 x 12"},
            ],
            "usage": [
                "Personal Care", "Spa Kits", "Gifting"
            ]
        },
    ]
    return render(request, "website/products.html", {"products": products})


def landing_page(request):
    featured_products = [
        {
            "image": "images/1.png",
            "category": "Earbuds",
            "model": "Model X100",
            "price": "$129.99"
        },
        {
            "image": "images/2.png",
            "category": "Headphones",
            "model": "Model S200",
            "price": "$299.99"
        },
        {
            "image": "images/3.png",
            "category": "Speakers",
            "model": "Model B300",
            "price": "$289.99"
        },
    ]
    response = requests.get("http://localhost:3000/shop")
    shopItems = response.json()
    return render(request, "website/landing_page.html", {"featured_products": featured_products, "shopItems": shopItems})
