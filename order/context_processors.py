from .models import TransactionOrder


def get_transaction(request):
    try:
        transactions_filter = TransactionOrder.objects.filter(order__user__user=request.user)
        transactions = TransactionOrder.objects.all()


    except:
        transactions = None
        transactions_filter = None

    return dict(transactions=transactions,
                transactions_filter=transactions_filter)