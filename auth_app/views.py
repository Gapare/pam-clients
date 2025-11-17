from django.shortcuts import render, redirect
from django.views import View

def home(request):
    print("🏠 HOME PAGE: Home page accessed")
    return render(request, 'home.html')

def thank_you(request):
    print("✅ THANK YOU: Thank you page accessed")
    # Clear session data
    request.session.pop('user_agent', None)
    request.session.pop('campaign_source', None)
    print("🧹 SESSION CLEANED: User agent and campaign data cleared")
    return render(request, 'thank_you.html')


class GoogleAuthStart(View):
    def get(self, request):
        # For direct access without phone number, redirect back to home
        return redirect('home')
    
    def post(self, request):
        # Get phone number from form
        phone_number = request.POST.get('phone', '').strip()
        
        if not phone_number:
            print("❌ PHONE MISSING: No phone number provided")
            return redirect('home')
        
        # Get campaign reference from QR code (optional)
        campaign_ref = request.GET.get('ref', 'direct')
        
        # Store in session for tracking
        request.session['user_agent'] = request.META.get('HTTP_USER_AGENT', 'Unknown')
        request.session['campaign_source'] = campaign_ref
        request.session['phone_number'] = phone_number  # Store phone number
        
        print(f"🚀 GOOGLE AUTH START: Starting OAuth flow")
        print(f"   📱 User Agent: {request.session['user_agent']}")
        print(f"   📞 Phone Number: {phone_number}")
        print(f"   🎯 Campaign Source: {campaign_ref}")
        
        # Start Google OAuth flow
        return redirect('social:begin', backend='google-oauth2')



def auth_success(request):
    """Simple redirect to thank you page - data saving handled by pipeline"""
    print("🔄 AUTH SUCCESS: Redirecting to thank you page")
    return redirect('thank-you')

