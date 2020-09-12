from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt

import braintree
import os

gateway = braintree.BraintreeGateway(
    braintree.Configuration(
        environment=braintree.Environment.Sandbox,
        merchant_id=os.getenv("MERCHANT_ID"),
        public_key=os.getenv("PUBLIC_KEY"),
        private_key=os.getenv("PRIVATE_KEY"),
    )
)


def validate_user_session(_id, token):
    user_model = get_user_model()
    try:
        user = user_model.objects.get(pk=_id)
        if user.session_token == token:
            return True
        return False
    except user_model.DoesNotExist:
        return False


@csrf_exempt
def generate_token(request, _id, token):
    if not validate_user_session(_id, token):
        return JsonResponse({'error': 'Invalid Session, Please login again'})
    return JsonResponse({'client_token': gateway.client_token.generate(), 'success': True})


@csrf_exempt
def process_payment(request, _id, token):
    if not validate_user_session(_id, token):
        return JsonResponse({'error': 'Invalid Session, Please login again'})

    nonce_from_the_client = request.POST["paymentMethodNonce"]
    amount_from_the_client = request.POST["amount"]

    result = gateway.transaction.sale({
        "amount": amount_from_the_client,
        "payment_method_nonce": nonce_from_the_client,
        "options": {
            "submit_for_settlement": True
        }

    })
    print(result)
    if result.is_success:
        return JsonResponse({
            "success": result.is_success, "error": False, "transaction": {
                'id': result.transaction.id,
                'amount': result.transaction.amount
            }})
    else:
        return JsonResponse({"success": result.is_success, 'error': True})

