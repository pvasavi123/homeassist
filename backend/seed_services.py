import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from services.models import Service, Category

# Map of categories to IDs (simplified for script)
categories_data = {
    '1': 'Cleaning',
    '2': 'Plumbing',
    '3': 'AC Repair',
    '4': 'Electrical',
    '5': 'Painting',
    '8': 'Appliances',
    '11': 'Smart Home',
    '12': 'Security'
}

cat_objects = {}
for cid, cname in categories_data.items():
    cat, _ = Category.objects.get_or_create(id=int(cid), defaults={'name': cname})
    cat_objects[cid] = cat

services = [
  { 'id': 1, 'category_id': '1', 'name': 'Deep Home Cleaning', 'base_price': '150.00', 'description': 'Complete home deep cleaning service by professionals.' },
  { 'id': 4, 'category_id': '1', 'name': 'Sofa & Upholstery Cleaning', 'base_price': '60.00', 'description': 'Stain removal and deep shampooing for sofas.' },
  { 'id': 2, 'category_id': '2', 'name': 'Premium Plumber', 'base_price': '120.00', 'description': 'Fix leaks and pipe issues instantly with our premium plumbers.' },
  { 'id': 5, 'category_id': '2', 'name': 'Water Heater Installation', 'base_price': '200.00', 'description': 'Professional installation of water heating systems.' },
  { 'id': 3, 'category_id': '3', 'name': 'AC Servicing', 'base_price': '90.00', 'description': 'Expert AC repair and maintenance.' },
  { 'id': 6, 'category_id': '3', 'name': 'AC Gas Top-Up', 'base_price': '80.00', 'description': 'Refrigerant gas refill for optimal cooling.' },
  { 'id': 7, 'category_id': '4', 'name': 'Fan & Light Installation', 'base_price': '40.00', 'description': 'Ceiling fan and LED lighting setup.' },
  { 'id': 8, 'category_id': '4', 'name': 'Main Panel Repair', 'base_price': '150.00', 'description': 'Complex electrical wiring and panel troubleshooting.' },
  { 'id': 9, 'category_id': '11', 'name': 'Smart Lock Setup', 'base_price': '110.00', 'description': 'Install and configure Wi-Fi smart locks.' },
  { 'id': 10, 'category_id': '12', 'name': 'CCTV Installation', 'base_price': '250.00', 'description': 'Complete home security camera wiring and setup.' },
  { 'id': 11, 'category_id': '5', 'name': 'Full Room Painting', 'base_price': '300.00', 'description': 'Premium wall painting with textured finish options.' },
  { 'id': 12, 'category_id': '8', 'name': 'Washing Machine Repair', 'base_price': '75.00', 'description': 'Fix drum issues, leaks, and circuit board problems.' }
]

for s in services:
    Service.objects.update_or_create(
        id=s['id'],
        defaults={
            'category': cat_objects[s['category_id']],
            'name': s['name'],
            'base_price': s['base_price'],
            'description': s['description']
        }
    )

print("Expanded Database seeded successfully with 12 premium services!")
