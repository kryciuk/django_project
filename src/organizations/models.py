from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import reverse


class Company(models.Model):
    name = models.CharField(max_length=50)
    email_domain = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"


class Department(models.Model):

    class DepartmentChoices(models.TextChoices):
        ACCOUNTING = "Accounting"
        ADMINISTRATION = "Administration"
        BOARD_OF_DIRECTORS = "Board of Directors"
        DESIGN = "Design"
        FINANCE = "Finance"
        HUMAN_RESOURCE = "Human Resource"
        INFORMATION_TECHNOLOGY = "Information Technology"
        INSPECTION = "Inspection"
        MARKETING = "Marketing"
        MAINTENANCE = "Maintenance"
        PACKAGING = "Packaging"
        PROCUREMENT = "Procurement"
        PROJECT = "Project"
        PRODUCTION = "Production"
        QUALITY = "Quality"
        RESEARCH_DEVELOPMENT = "Research Development"
        SALES = "Sales"
        SECURITY = "Security"
        STORE = "Store"

    name = models.CharField(choices=DepartmentChoices.choices)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} in {self.company}"


class Position(models.Model):

    class Level(models.TextChoices):
        ENTRY = "Entry"
        JUNIOR = "Junior"
        MID = "Mid"
        SENIOR = "Senior"
        MANAGER = "Manager"
        DIRECTOR = "Director"

    title = models.CharField(max_length=100, help_text="title of the position")
    level = models.TextField(choices=Level.choices)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    class Meta:
        unique_together = ["title", "level", "department", "company"]

    def __str__(self):
        return f"{self.title} ({self.get_level_display()})"

    def get_absolute_url(self):
        return reverse("dashboard-recruiter")


class City(models.Model):
    class Country(models.TextChoices):
        AFGHANISTAN = "Afghanistan"
        ALBANIA = "Albania"
        ALGERIA = "Algeria"
        ANDORRA = "Andorra"
        ANGOLA = "Angola"
        ANTIGUA_AND_BARBUDA = "Antigua and Barbuda"
        ARGENTINA = "Argentina"
        ARMENIA = "Armenia"
        AUSTRALIA = "Australia"
        AUSTRIA = "Austria"
        AZERBAIJAN = "Azerbaijan"
        BAHAMAS = "Bahamas"
        BAHRAIN = "Bahrain"
        BANGLADESH = "Bangladesh"
        BARBADOS = "Barbados"
        BELARUS = "Belarus"
        BELGIUM = "Belgium"
        BELIZE = "Belize"
        BENIN = "Benin"
        BHUTAN = "Bhutan"
        BOLIVIA = "Bolivia"
        BOSNIA_AND_HERZEGOVINA = "Bosnia and Herzegovina"
        BOTSWANA = "Botswana"
        BRAZIL = "Brazil"
        BRUNEI = "Brunei"
        BULGARIA = "Bulgaria"
        BURKINA_FASO = "Burkina Faso"
        BURUNDI = "Burundi"
        CABO_VERDE = "Cabo Verde"
        CAMBODIA = "Cambodia"
        CAMEROON = "Cameroon"
        CANADA = "Canada"
        CENTRAL_AFRICAN_REPUBLIC = "Central African Republic"
        CHAD = "Chad"
        CHILE = "Chile"
        CHINA = "China"
        COLOMBIA = "Colombia"
        COMOROS = "Comoros"
        CONGO = "Congo"
        COSTA_RICA = "Costa Rica"
        COTE_D_IVOIRE = "Côte d'Ivoire"
        CROATIA = "Croatia"
        CUBA = "Cuba"
        CYPRUS = "Cyprus"
        CZECH_REPUBLIC = "Czech Republic"
        DEMOCRATIC_REPUBLIC_OF_THE_CONGO = "Democratic Republic of the Congo"
        DENMARK = "Denmark"
        DJIBOUTI = "Djibouti"
        DOMINICA = "Dominica"
        DOMINICAN_REPUBLIC = "Dominican Republic"
        EAST_TIMOR = "East Timor"
        ECUADOR = "Ecuador"
        EGYPT = "Egypt"
        EL_SALVADOR = "El Salvador"
        EQUATORIAL_GUINEA = "Equatorial Guinea"
        ERITREA = "Eritrea"
        ESTONIA = "Estonia"
        ESWATINI = "Eswatini"
        ETHIOPIA = "Ethiopia"
        FIJI = "Fiji"
        FINLAND = "Finland"
        FRANCE = "France"
        GABON = "Gabon"
        GAMBIA = "Gambia"
        GEORGIA = "Georgia"
        GERMANY = "Germany"
        GHANA = "Ghana"
        GREECE = "Greece"
        GRENADA = "Grenada"
        GUATEMALA = "Guatemala"
        GUINEA = "Guinea"
        GUINEA_BISSAU = "Guinea-Bissau"
        GUYANA = "Guyana"
        HAITI = "Haiti"
        HONDURAS = "Honduras"
        HUNGARY = "Hungary"
        ICELAND = "Iceland"
        INDIA = "India"
        INDONESIA = "Indonesia"
        IRAN = "Iran"
        IRAQ = "Iraq"
        IRELAND = "Ireland"
        ISRAEL = "Israel"
        ITALY = "Italy"
        JAMAICA = "Jamaica"
        JAPAN = "Japan"
        JORDAN = "Jordan"
        KAZAKHSTAN = "Kazakhstan"
        KENYA = "Kenya"
        KIRIBATI = "Kiribati"
        KOSOVO = "Kosovo"
        KUWAIT = "Kuwait"
        KYRGYZSTAN = "Kyrgyzstan"
        LAOS = "Laos"
        LATVIA = "Latvia"
        LEBANON = "Lebanon"
        LESOTHO = "Lesotho"
        LIBERIA = "Liberia"
        LIBYA = "Libya"
        LIECHTENSTEIN = "Liechtenstein"
        LITHUANIA = "Lithuania"
        LUXEMBOURG = "Luxembourg"
        MADAGASCAR = "Madagascar"
        MALAWI = "Malawi"
        MALAYSIA = "Malaysia"
        MALDIVES = "Maldives"
        MALI = "Mali"
        MALTA = "Malta"
        MARSHALL_ISLANDS = "Marshall Islands"
        MAURITANIA = "Mauritania"
        MAURITIUS = "Mauritius"
        MEXICO = "Mexico"
        MICRONESIA = "Micronesia"
        MOLDOVA = "Moldova"
        MONACO = "Monaco"
        MONGOLIA = "Mongolia"
        MONTENEGRO = "Montenegro"
        MOROCCO = "Morocco"
        MOZAMBIQUE = "Mozambique"
        MYANMAR = "Myanmar"
        NAMIBIA = "Namibia"
        NAURU = "Nauru"
        NEPAL = "Nepal"
        NETHERLANDS = "Netherlands"
        NEW_ZEALAND = "New Zealand"
        NICARAGUA = "Nicaragua"
        NIGER = "Niger"
        NIGERIA = "Nigeria"
        NORTH_KOREA = "North Korea"
        NORTH_MACEDONIA = "North Macedonia"
        NORWAY = "Norway"
        OMAN = "Oman"
        PAKISTAN = "Pakistan"
        PALAU = "Palau"
        PALESTINE = "Palestine"
        PANAMA = "Panama"
        PAPUA_NEW_GUINEA = "Papua New Guinea"
        PARAGUAY = "Paraguay"
        PERU = "Peru"
        PHILIPPINES = "Philippines"
        POLAND = "Poland"
        PORTUGAL = "Portugal"
        QATAR = "Qatar"
        ROMANIA = "Romania"
        RUSSIA = "Russia"
        RWANDA = "Rwanda"
        SAINT_KITTS_AND_NEVIS = "Saint Kitts and Nevis"
        SAINT_LUCIA = "Saint Lucia"
        SAINT_VINCENT_AND_THE_GRENADINES = "Saint Vincent and the Grenadines"
        SAMOA = "Samoa"
        SAN_MARINO = "San Marino"
        SAO_TOME_AND_PRINCIPE = "Sao Tome and Principe"
        SAUDI_ARABIA = "Saudi Arabia"
        SENEGAL = "Senegal"
        SERBIA = "Serbia"
        SEYCHELLES = "Seychelles"
        SIERRA_LEONE = "Sierra Leone"
        SINGAPORE = "Singapore"
        SLOVAKIA = "Slovakia"
        SLOVENIA = "Slovenia"
        SOLOMON_ISLANDS = "Solomon Islands"
        SOMALIA = "Somalia"
        SOUTH_AFRICA = "South Africa"
        SOUTH_KOREA = "South Korea"
        SOUTH_SUDAN = "South Sudan"
        SPAIN = "Spain"
        SRI_LANKA = "Sri Lanka"
        SUDAN = "Sudan"
        SURINAME = "Suriname"
        SWEDEN = "Sweden"
        SWITZERLAND = "Switzerland"
        SYRIA = "Syria"
        TAIWAN = "Taiwan"
        TAJIKISTAN = "Tajikistan"
        TANZANIA = "Tanzania"
        THAILAND = "Thailand"
        TOGO = "Togo"
        TONGA = "Tonga"
        TRINIDAD_AND_TOBAGO = "Trinidad and Tobago"
        TUNISIA = "Tunisia"
        TURKEY = "Turkey"
        TURKMENISTAN = "Turkmenistan"
        TUVALU = "Tuvalu"
        UGANDA = "Uganda"
        UKRAINE = "Ukraine"
        UNITED_ARAB_EMIRATES = "United Arab Emirates"
        UNITED_KINGDOM = "United Kingdom"
        UNITED_STATES = "United States"
        URUGUAY = "Uruguay"
        UZBEKISTAN = "Uzbekistan"
        VANUATU = "Vanuatu"
        VATICAN_CITY = "Vatican City"
        VENEZUELA = "Venezuela"
        VIETNAM = "Vietnam"
        YEMEN = "Yemen"
        ZAMBIA = "Zambia"
        ZIMBABWE = "Zimbabwe"

    name = models.CharField(max_length=50)
    country = models.TextField(choices=Country.choices)

    class Meta:
        unique_together = ["name", "country"]

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse("dashboard-recruiter")


class Industry(models.Model):
    class IndustryChoice(models.TextChoices):
        ACCOUNTING = "Accounting"
        AEROSPACE = "Aerospace"
        AGRICULTURE = "Agriculture"
        AUTOMOTIVE = "Automotive"
        BANKING = "Banking"
        BIOTECHNOLOGY = "Biotechnology"
        CHEMICAL = "Chemical"
        COMMUNICATIONS = "Communications"
        CONSTRUCTION = "Construction"
        CONSULTING = "Consulting"
        EDUCATION = "Education"
        ELECTRONICS = "Electronics"
        ENERGY = "Energy"
        ENGINEERING = "Engineering"
        ENTERTAINMENT = "Entertainment"
        ENVIRONMENTAL = "Environmental"
        FINANCE = "Finance"
        FOOD_AND_BEVERAGE = "Food & Beverage"
        GOVERNMENT = "Government"
        HEALTHCARE = "Healthcare"
        HOSPITALITY = "Hospitality"
        HUMAN_RESOURCES = "Human Resources"
        INSURANCE = "Insurance"
        INTERNET = "Internet"
        INVESTMENT_BANKING = "Investment Banking"
        JOURNALISM = "Journalism"
        LAW_ENFORCEMENT = "Law Enforcement"
        LEGAL = "Legal"
        MANUFACTURING = "Manufacturing"
        MARKETING = "Marketing"
        MEDIA = "Media"
        NONPROFIT = "Nonprofit"
        PHARMACEUTICAL = "Pharmaceutical"
        REAL_ESTATE = "Real Estate"
        RETAIL = "Retail"
        SALES = "Sales"
        TECHNOLOGY = "Technology"
        TELECOMMUNICATIONS = "Telecommunications"
        TRANSPORTATION = "Transportation"
        TRAVEL = "Travel"

    industry = models.CharField(choices=IndustryChoice.choices)

    class Meta:
        unique_together = ["industry"]

    def __str__(self):
        return f"{self.industry}"


class CompanyProfile(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    industries = models.ManyToManyField(Industry, blank=True)
    info = models.TextField(help_text="few words about company", null=True, blank=True)

    def __str__(self):
        return f"{self.company} Profile"
