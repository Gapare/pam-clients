from django.utils import timezone
from sheets_app.sheets_service import append_to_sheet
import logging

logger = logging.getLogger(__name__)

def save_user_to_sheet(backend, user, response, *args, **kwargs):
    """
    Custom pipeline to save user data to Google Sheets after social authentication
    """
    print("🎯 CUSTOM PIPELINE: Saving user data to Google Sheets")
    
    if backend.name == 'google-oauth2':
        try:
            # Get user data from Google response
            name = response.get('name', '')
            email = response.get('email', '')
            timestamp = timezone.now().strftime('%Y-%m-%d %H:%M:%S')
            
            # Get phone number from session (submitted by user)
            phone_number = kwargs['request'].session.get('phone_number', 'Not provided')
            
            print(f"📝 PIPELINE DATA TO SAVE:")
            print(f"   👤 Name: {name}")
            print(f"   📧 Email: {email}")
            print(f"   📞 Phone: {phone_number}")
            print(f"   ⏰ Timestamp: {timestamp}")
            
            # Append to Google Sheet
            print("📤 PIPELINE: Attempting to save to Google Sheets...")
            success = append_to_sheet([
                name,           # Column A: Name
                email,          # Column B: Email  
                phone_number,   # Column C: Phone Number
                timestamp,      # Column D: Timestamp
            ])
            
            if success:
                print(f"🎉 PIPELINE SUCCESS: Added {name} ({email}) to Google Sheet")
                logger.info(f"Successfully added user to sheet via pipeline: {name} ({email})")
            else:
                print(f"❌ PIPELINE FAILED: Could not add {name} ({email}) to Google Sheet")
                logger.error(f"Failed to add user to sheet via pipeline: {name} ({email})")
                
        except Exception as e:
            print(f"💥 PIPELINE ERROR: {e}")
            logger.error(f"Error in pipeline: {str(e)}")
            import traceback
            print(f"🔍 PIPELINE TRACEBACK: {traceback.format_exc()}")
    
    return {'user': user}


