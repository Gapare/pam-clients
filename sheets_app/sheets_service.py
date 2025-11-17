import os
import json
from google.oauth2 import service_account
from googleapiclient.discovery import build
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

def get_sheets_service():
    """Initialize and return Google Sheets service"""
    print("🔧 SHEETS SERVICE: Initializing Google Sheets service...")
    
    try:
        # Read from JSON file instead of environment variable
        with open('service_account.json', 'r') as f:
            service_account_info = json.load(f)
        
        print("✅ JSON FILE: Service account JSON loaded from file")
        
        credentials = service_account.Credentials.from_service_account_info(
            service_account_info,
            scopes=['https://www.googleapis.com/auth/spreadsheets']
        )
        print("✅ CREDENTIALS: Service account credentials created")
        
        service = build('sheets', 'v4', credentials=credentials)
        print("✅ SHEETS API: Google Sheets service built successfully")
        
        return service
        
    except Exception as e:
        print(f"❌ ERROR in get_sheets_service: {e}")
        import traceback
        print(f"🔍 FULL TRACEBACK: {traceback.format_exc()}")
        return None



def append_to_sheet(row_data):
    """Append a row to Google Sheet - Only Name, Email, Timestamp, Device Info"""
    print(f"📝 APPEND TO SHEET: Attempting to append data: {row_data}")
    
    try:
        service = get_sheets_service()
        if not service:
            print("❌ NO SHEETS SERVICE: Cannot proceed without Sheets service")
            return False
            
        sheet_id = settings.GOOGLE_SHEET_ID
        print(f"📄 SHEET ID: Using sheet ID: {sheet_id}")
        
        body = {
            'values': [row_data]
        }
        
        print("🔄 CALLING SHEETS API: Making append request...")
        result = service.spreadsheets().values().append(
            spreadsheetId=sheet_id,
            range='Sheet1!A:D',
            valueInputOption='RAW',
            body=body
        ).execute()
        
        print(f"🎉 SHEETS SUCCESS: Data appended successfully!")
        print(f"   📊 Result: {result}")
        logger.info(f"Successfully appended data to sheet: {row_data}")
        return True
        
    except Exception as e:
        print(f"❌ SHEETS ERROR: Failed to append data - {e}")
        logger.error(f"Error appending to sheet: {str(e)}")
        import traceback
        print(f"🔍 FULL TRACEBACK: {traceback.format_exc()}")
        return False