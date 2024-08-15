from django.shortcuts import render, redirect
from .models import Product, Coupon
from django.contrib.auth.decorators import login_required

@login_required
def upload_product(request):
    if request.method == 'POST':
        # Handle product upload
        pass
    return render(request, 'marketplace/upload_product.html')

def apply_coupon(request):
    if request.method == 'POST':
        code = request.POST.get('code')
        try:
            coupon = Coupon.objects.get(code=code, active=True)
            # Apply discount logic
        except Coupon.DoesNotExist:
            # Handle invalid coupon
            pass
    return render(request, 'marketplace/apply_coupon.html')
