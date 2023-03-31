from django import forms
from .models import PC, Ram,Firma

   
    
class RamForm(forms.ModelForm):
    firma = forms.ModelChoiceField(queryset=Firma.objects.all(),empty_label="Firma Seç")
    class Meta:
        model = Ram
        fields = (
            "marka",
            "model",
            "capacity",
            "mhz",
            "seri_no",
            "garanti",
            "garanti_bitis_tarihi",
            "firma",
        )

class PcForm(forms.ModelForm):

    class Meta:
        model = PC
        fields = (
            "name",
            "role",
            "kasa",
            "psu",
            "motherboard",
            "cpu",
            "ram",
            "gpu",
            "monitor",
            "headset",
            "klavye",
            "mouse",
            "mouse_pad",
            "koltuk",
             "notes",
        )

