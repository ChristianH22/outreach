<<<<<<< HEAD
# outreach
Startup Outreach
=======
# RevenueMax - Product Market Fit Testing Website

A simple website to test your hypothesis that digital marketing agencies have a pain point around budget allocation decisions. This website tracks clicks and collects email addresses for your waitlist.

## Features

- **Compelling Landing Page**: Targets digital marketing agencies with their specific pain point
- **Click Tracking**: Tracks page views, CTA clicks, and form submissions
- **Email Collection**: Collects agency names and email addresses for waitlist
- **Local Data Storage**: All data is saved to a CSV file on your computer
- **Real-time Statistics**: View engagement metrics in real-time

## Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Start the Server

```bash
python server.py
```

### 3. Access Your Website

- **Main Website**: http://localhost:5000
- **View Statistics**: http://localhost:5000/stats
- **Download Data**: http://localhost:5000/data

## How It Works

### Tracking Events

The website automatically tracks:

1. **Page Views**: Every time someone visits your website
2. **Waitlist Signups**: When someone submits their email and agency name
3. **CTA Clicks**: When someone clicks on call-to-action buttons

### Data Collection

All data is saved to `tracking_data.csv` with the following columns:

- `timestamp`: When the event occurred
- `event_type`: Type of event (page_view, waitlist_signup, cta_click)
- `email`: Email address (for signups)
- `agency`: Agency name (for signups)
- `user_agent`: Browser information
- `referrer`: Where the visitor came from
- `button_text`: Text of clicked button (for CTA clicks)
- `ip_address`: Visitor's IP address

## Testing Your Hypothesis

### 1. Share the Website

Share the website URL (http://localhost:5000) in:
- Digital marketing agency Facebook groups
- LinkedIn agency communities
- Slack channels for marketers
- Reddit marketing subreddits

### 2. Monitor Engagement

Check your statistics at http://localhost:5000/stats to see:
- How many people are visiting
- How many are signing up for the waitlist
- Which CTAs are getting the most clicks

### 3. Analyze the Data

Download the CSV file at http://localhost:5000/data to analyze:
- Conversion rates
- Most effective traffic sources
- Agency types showing interest

## Key Metrics to Track

- **Click-through Rate**: Page views vs. waitlist signups
- **Engagement Rate**: CTA clicks vs. page views
- **Quality of Interest**: Agency names and email domains
- **Traffic Sources**: Referrer data to see where your audience comes from

## Customization

### Modify the Landing Page

Edit `index.html` to:
- Change the value proposition
- Adjust the pain point messaging
- Update the features list
- Modify the design/colors

### Add More Tracking

In `server.py`, you can add new event types by:
1. Adding new tracking calls in the JavaScript
2. Updating the CSV headers
3. Modifying the `save_to_csv` function

## Deployment Options

### Local Testing (Current Setup)
- Perfect for initial hypothesis testing
- Data stays on your computer
- Easy to modify and iterate

### Public Deployment
For wider testing, consider:
- **Heroku**: Easy deployment with free tier
- **Vercel**: Great for static sites
- **Netlify**: Simple deployment with form handling
- **DigitalOcean**: More control over the server

## Next Steps

1. **Run the website locally** and test it yourself
2. **Share with a small group** of agency owners you know
3. **Monitor the data** to see if there's genuine interest
4. **Iterate on the messaging** based on feedback
5. **Scale up** if you see strong engagement

## Troubleshooting

### Common Issues

1. **Port already in use**: Change the port in `server.py` (line 95)
2. **Flask not found**: Run `pip install -r requirements.txt`
3. **CSV file not created**: The server will create it automatically on first use

### Getting Help

If you encounter issues:
1. Check the console output for error messages
2. Ensure all dependencies are installed
3. Verify the port isn't being used by another application

---

**Good luck with your product-market fit testing! 🚀** 
>>>>>>> master
