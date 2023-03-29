from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from api.models import *

# ----------------------------------------------------------------
# ACCOUNT SERIALIZERS
# ----------------------------------------------------------------

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'
        
        
# ----------------------------------------------------------------
# APPEARANCE SERIALIZERS
# ----------------------------------------------------------------

class AppearanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appearance
        fields = '__all__'
        
        
# ----------------------------------------------------------------
# SOCIAL SERIALIZERS
# ----------------------------------------------------------------

class SocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Social
        fields = '__all__'
        
           
# ----------------------------------------------------------------
# CALENDAR SERIALIZERS
# ----------------------------------------------------------------

class CalendarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calendar
        fields = '__all__'
        
        
        
# ----------------------------------------------------------------
# CARD SERIALIZERS
# ----------------------------------------------------------------

class CardSerializer(serializers.ModelSerializer):
    
    id_social = SocialSerializer()
    id_appearance = AppearanceSerializer()
    id_account = AccountSerializer()
    
    class Meta:
        model = Card
        fields = '__all__'
        
        
# ----------------------------------------------------------------
# COMPANYINFO SERIALIZERS
# ----------------------------------------------------------------

class CompanyInfoSerializer(serializers.ModelSerializer):
    id_card = CardSerializer()
    id_social = SocialSerializer()
    
    class Meta:
        model = CompanyInfo
        fields = '__all__'
        
        
# ----------------------------------------------------------------
# PORTFOLIO SERIALIZERS
# ----------------------------------------------------------------

class PortfolioSerializer(serializers.ModelSerializer):
    id_card = CardSerializer()
    class Meta:
        model = Portfolio
        fields = '__all__'