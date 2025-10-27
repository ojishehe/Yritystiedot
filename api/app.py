from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

def parse_company_data(json_data):
    if "companies" in json_data and len(json_data["companies"]) > 0:
        company = json_data["companies"][0]
    elif "results" in json_data and len(json_data["results"]) > 0:
        company = json_data["results"][0]
    else:
        return {
            "company_name": "",
            "website": "",
            "business_id": "",
            "registration_date": "",
            "status": "",
            "address": {
                "street": "",
                "post_code": "",
                "city": ""
            }
        }

    # Hae yrityksen nimi (pääasiallinen nimi, tyyppi 1)
    company_name = ""
    for name_entry in company.get("names", []):
        if name_entry.get("type") == "1":
            company_name = name_entry.get("name", "")
            break

    # Hae verkkosivusto
    website = company.get("website", {}).get("url", "")

    # Hae yrityksen businessId ja rekisteröintipäivä
    business_id = company.get("businessId", {}).get("value", "")
    registration_date = company.get("registrationDate", "")
    status = company.get("status", "")

    # Hae ensimmäinen osoite, jos on
    address_list = company.get("addresses", [])
    if address_list:
        address = address_list[0]
        street = address.get("street", "")
        post_code = address.get("postCode", "")
        city = ""
        if address.get("postOffices"):
            city = address["postOffices"][0].get("city", "")
    else:
        street = post_code = city = ""

    return {
        "company_name": company_name,
        "website": website,
        "business_id": business_id,
        "registration_date": registration_date,
        "status": status,
        "address": {
            "street": street,
            "post_code": post_code,
            "city": city
        }
    }

def hae_yritystiedot(business_id):
    """Hakee yritystiedot YTJ:n API:sta."""
    API_URL = f"https://avoindata.prh.fi/opendata-ytj-api/v3/companies?businessId={business_id}"

    headers = {
        'Accept': 'application/json'
    }

    try:
        response = requests.get(API_URL, headers=headers)
        response.raise_for_status()

        # Tallennetaan vastaus tiedostoon
        with open("api_response.json", "w", encoding="utf-8") as f:
            f.write(response.text)

        print("API vastaus tallennettu tiedostoon api_response.json")  # Debug

        response_text = response.text
        if response_text.startswith('\ufeff'):
            response_text = response_text[1:]

        print("API vastaus (raw):", response_text)  # Debug

        data = json.loads(response_text)
        print("Parsed JSON:", json.dumps(data, indent=4))  # Debug

        # Tarkista löytyvätkö 'companies' tai 'results'
        if 'companies' in data and len(data['companies']) > 0:
            yritys = data['companies'][0]
        elif 'results' in data and len(data['results']) > 0:
            yritys = data['results'][0]
        else:
            return {"status": "NOT_FOUND", "message": f"Y-tunnuksella {business_id} ei löytynyt tietoja."}

        parsed_data = parse_company_data({"companies": [yritys]} if 'companies' in data else {"results": [yritys]})
        return {
            "business_id": business_id,
            "api_data": data,
            "parsed_data": parsed_data,
            "status": "OK"
        }

    except json.JSONDecodeError:
        print("Virhe JSON:sta")  # Debug
        return {"status": "ERROR", "message": "Virhe API-vastauksen käsittelyssä (JSON-muoto)."}
    except requests.exceptions.RequestException as e:
        print("Virhe API-kutsussa:", e)  # Debug
        return {"status": "ERROR", "message": "Virhe yhteydessä YTJ-rajapintaan."}

@app.route('/', methods=['GET', 'POST'])
def index():
    yritys_tiedot = None
    if request.method == 'POST':
        business_id_input = request.form.get('business_id', '').strip()
        print(f"Syötetty Y-tunnus: {business_id_input}")
        # Muotoilu
        business_id_raw = business_id_input.replace('-', '').replace(' ', '')
        if len(business_id_raw) == 8 and business_id_raw.isdigit():
            business_id = f"{business_id_raw[:7]}-{business_id_raw[7:]}"
        else:
            business_id = business_id_input
        print(f"Lähetetään API:lle: {business_id}")
        if business_id:
            yritys_tiedot = hae_yritystiedot(business_id)
            print(f"API vastaus: {yritys_tiedot}")
    else:
        print("Ei POST-pyyntöä.")
    return render_template('index.html', yritys_tiedot=yritys_tiedot)

if __name__ == '__main__':
    app.run(debug=True)