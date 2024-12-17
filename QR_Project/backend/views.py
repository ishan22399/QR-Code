from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Profile, ActionLog
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Profile, ActionLog
from django.contrib.auth.models import User

# Home view (already defined)
def home(request):
    return render(request, 'index.html')


from django.contrib.auth import login as auth_login  # Alias the built-in login function
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)  # Use the aliased login function here
            return redirect('dashboard')  # Redirect to dashboard after login
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')


# Register view
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from new.forms import UserRegisterForm
from .models import Profile
from django.contrib import messages

from django.contrib.auth.models import User
from .models import Profile
from django.shortcuts import render, redirect
from new.forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # Create the user
            user = form.save()
            
            # Create the profile for the new user
            profile = Profile(user=user, first_name=form.cleaned_data.get('first_name'),
                              last_name=form.cleaned_data.get('last_name'),
                              phone_number=form.cleaned_data.get('phone_number'),
                              country_code=form.cleaned_data.get('country_code'),
                              dob=form.cleaned_data.get('dob'))
            profile.save()
            
            # Log the user in or redirect to login page
            # Assuming you use Django's built-in login functionality
            login(request, user)
            return redirect('dashboard')  # Redirect to the dashboard after successful registration

    else:
        form = UserRegisterForm()

    return render(request, 'register.html', {'form': form})




# Dashboard view (only accessible by logged-in users)
@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Profile, ActionLog
from django.contrib import messages

# View Profile - Show current profile information
@login_required
def view_profile(request):
    profile = request.user.profile  # Assuming a OneToOne relation between User and Profile
    return render(request, 'view_profile.html', {'profile': profile})

# Edit Profile - Show edit form and save changes
@login_required
def edit_profile(request):
    profile = request.user.profile  # Get user's profile

    if request.method == 'POST':
        # Update profile with POST data
        profile.name = request.POST.get('name')
        profile.email = request.POST.get('email')
        profile.phone = request.POST.get('phone')
        profile.dob = request.POST.get('dob')

        # Save the updated profile
        profile.save()

        # Log the action
        ActionLog.objects.create(user=request.user, action="Updated profile")

        # Show a success message
        messages.success(request, 'Profile updated successfully!')
        return redirect('view_profile')  # Redirect to the profile view page

    return render(request, 'edit_profile.html', {'profile': profile})

