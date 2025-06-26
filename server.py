from flask import Flask, request, jsonify, send_from_directory
import csv
import os
from datetime import datetime
import json

app = Flask(__name__)

# CSV file to store tracking data
TRACKING_FILE = 'tracking_data.csv'

def ensure_csv_exists():
    """Create CSV file with headers if it doesn't exist"""
    if not os.path.exists(TRACKING_FILE):
        with open(TRACKING_FILE, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([
                'timestamp',
                'event_type',
                'email',
                'agency',
                'user_agent',
                'referrer',
                'button_text',
                'ip_address'
            ])

def save_to_csv(data):
    """Save tracking data to CSV file"""
    ensure_csv_exists()
    
    with open(TRACKING_FILE, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        
        # Extract data based on event type
        timestamp = data.get('data', {}).get('timestamp', datetime.now().isoformat())
        event_type = data.get('event', 'unknown')
        email = data.get('data', {}).get('email', '')
        agency = data.get('data', {}).get('agency', '')
        user_agent = data.get('data', {}).get('userAgent', '')
        referrer = data.get('data', {}).get('referrer', '')
        button_text = data.get('data', {}).get('buttonText', '')
        ip_address = request.remote_addr
        
        writer.writerow([
            timestamp,
            event_type,
            email,
            agency,
            user_agent,
            referrer,
            button_text,
            ip_address
        ])

@app.route('/')
def index():
    """Serve the main website"""
    return send_from_directory('.', 'index.html')

@app.route('/track', methods=['POST'])
def track():
    """Handle tracking events"""
    try:
        data = request.get_json()
        save_to_csv(data)
        return jsonify({'status': 'success'})
    except Exception as e:
        print(f"Error saving tracking data: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/stats')
def stats():
    """Show basic statistics from the tracking data"""
    if not os.path.exists(TRACKING_FILE):
        return jsonify({
            'total_events': 0,
            'page_views': 0,
            'waitlist_signups': 0,
            'cta_clicks': 0,
            'unique_emails': 0
        })
    
    try:
        with open(TRACKING_FILE, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            rows = list(reader)
        
        total_events = len(rows)
        page_views = len([r for r in rows if r['event_type'] == 'page_view'])
        waitlist_signups = len([r for r in rows if r['event_type'] == 'waitlist_signup'])
        cta_clicks = len([r for r in rows if r['event_type'] == 'cta_click'])
        unique_emails = len(set([r['email'] for r in rows if r['email']]))
        
        return jsonify({
            'total_events': total_events,
            'page_views': page_views,
            'waitlist_signups': waitlist_signups,
            'cta_clicks': cta_clicks,
            'unique_emails': unique_emails
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/data')
def download_data():
    """Download the tracking data as CSV"""
    if os.path.exists(TRACKING_FILE):
        return send_from_directory('.', TRACKING_FILE, as_attachment=True)
    else:
        return "No tracking data available", 404

if __name__ == '__main__':
    print("🚀 Starting RevenueMax tracking server...")
    print(f"📊 Tracking data will be saved to: {TRACKING_FILE}")
    print("🌐 Website will be available at: http://localhost:5000")
    print("📈 View stats at: http://localhost:5000/stats")
    print("📥 Download data at: http://localhost:5000/data")
    print("\nPress Ctrl+C to stop the server")
    
    # Use environment variable for port (for cloud deployment)
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port) 