from django import forms
from .models import Estudiante


class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ["nombre", "cedula", "edad", "email", "carrera"]
        labels = {
            "nombre": "Nombre completo",
            "cedula": "Cédula",
            "edad": "Edad",
            "email": "Correo electrónico",
            "carrera": "Carrera",
        }
        widgets = {
            "nombre": forms.TextInput(attrs={
                "placeholder": "Ingrese el nombre completo",
                "class": "w-full",
            }),
            "cedula": forms.TextInput(attrs={
                "placeholder": "Ingrese la cédula",
                "maxlength": "10",
                "inputmode": "numeric",
            }),
            "edad": forms.NumberInput(attrs={
                "placeholder": "Ingrese la edad",
                "min": "0",
            }),
            "email": forms.EmailInput(attrs={
                "placeholder": "ejemplo@correo.com",
            }),
            "carrera": forms.Select(),
        }

    def clean_cedula(self):
        cedula = self.cleaned_data.get("cedula")
        if cedula:
            cedula = cedula.strip()
            if not cedula.isdigit() or len(cedula) != 10:
                raise forms.ValidationError(
                    "La cédula debe contener exactamente 10 números."
                )
        return cedula

    def clean_edad(self):
        edad = self.cleaned_data.get("edad")
        if edad is not None and edad < 0:
            raise forms.ValidationError("La edad no puede ser negativa.")
        return edad
