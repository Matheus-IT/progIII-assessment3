from django import forms


class UploadLotteryFile(forms.Form):
    file = forms.FileField(
        label='Arquivo tsv', allow_empty_file=False, required=True
    )
    start_from_scratch = forms.BooleanField(
        label='Iniciar base do zero', required=False
    )
