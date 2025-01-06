
from django import forms
from .models import Transaction
class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = [
            'coin',
            'transaction_type'
        ]

    def __init__(self, *args, **kwargs):
        self.profile = kwargs.pop('profile')  
        super().__init__(*args, **kwargs)
        self.fields['transaction_type'].disabled = True  
        self.fields['transaction_type'].widget = forms.HiddenInput()  

    def save(self, commit=True):
        self.instance.profile = self.profile
        self.instance.coin_after_transaction = self.profile.coin
        return super().save()


class DepositForm(TransactionForm):
    def clean_coin(self):  
        min_deposit_coin = 100
        coin = self.cleaned_data.get('coin')  
        if coin < min_deposit_coin:
            raise forms.ValidationError(
                f'You need to deposit at least {min_deposit_coin} $'
            )

        return coin

 
 