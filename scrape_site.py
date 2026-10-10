import urllib.request
import json
import re
import html
from bs4 import BeautifulSoup

BASE_URL = "https://buket43.ru/"

def fetch_url(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as response:
        return response.read().decode('utf-8')

def parse_float(val):
    if not val:
        return 0.0
    if isinstance(val, (int, float)):
        return float(val)
    val_str = str(val).replace(',', '.').strip()
    try:
        return float(val_str)
    except ValueError:
        return 0.0

def parse_site():
    main_html = fetch_url(BASE_URL)
    soup = BeautifulSoup(main_html, 'html.parser')

    # 1. Site Metadata
    title = soup.title.string.strip() if soup.title else ""
    meta_desc = ""
    meta_keywords = ""
    og_title = ""
    og_desc = ""
    og_image = ""

    for meta in soup.find_all('meta'):
        name = meta.get('name', '').lower()
        prop = meta.get('property', '').lower()
        content = meta.get('content', '')

        if name == 'description':
            meta_desc = content
        elif name == 'keywords':
            meta_keywords = content
        elif prop == 'og:title':
            og_title = content
        elif prop == 'og:description':
            og_desc = content
        elif prop == 'og:image':
            og_image = content

    site_metadata = {
        "title": title,
        "url": BASE_URL,
        "meta_description": meta_desc,
        "meta_keywords": meta_keywords,
        "og": {
            "title": og_title,
            "description": og_desc,
            "image": og_image
        }
    }

    # 2. Contacts & Company Information
    phones = ["+7 (912) 372-22-85"]
    address = "г.Киров, ул.Горького, д.56, Киров"
    working_hours = "ежедневно с 9.00 до 22.00"
    order_intake_hours = "09:00 - 21:00"

    social_links = {
        "vk_group": "https://vk.com/kirov_buket",
        "vk_clips": "https://vk.com/clips/kirov_buket",
        "whatsapp": "https://wa.me/79123722285",
        "telegram": "https://t.me/YanaA2802",
        "dzen": "https://dzen.ru/kirov_buket",
        "yandex_map_reviews": "https://yandex.ru/maps/org/buket/30494414686/reviews/"
    }

    # Extract Requisites
    requisites_text = ""
    footer_text_el = soup.find(string=re.compile(r'ИП Антипина'))
    if footer_text_el:
        requisites_text = footer_text_el.strip()
    else:
        requisites_text = "ИП Антипина Яна Викторовна — действующее предприятие. ИНН 041104993015, ОГРНИП 325430000001829, ОКПО 2038909067, ОКАТО 33401361000, ОКТМО 33701000001, ОКОПФ 50102, ОКОГУ 4210015, ОКФС 16."

    company_info = {
        "name": "Цветочная лавка «Букет»",
        "phones": phones,
        "address": address,
        "working_hours": working_hours,
        "order_intake_hours": order_intake_hours,
        "social_links": social_links,
        "requisites": requisites_text,
        "developer": "Разработка и продвижение сайта — «Полдень» (https://experts.tilda.ru/ivan_15355)"
    }

    # 3. Navigation Links
    nav_links = [
        {"title": "Каталог букетов", "url": "https://buket43.ru/catalog"},
        {"title": "Доставка и оплата", "url": "https://buket43.ru/dostavka"},
        {"title": "О нас", "url": "https://buket43.ru/about"},
        {"title": "Контакты", "url": "https://buket43.ru/contacts"}
    ]

    # 4. Promotions and Benefits
    promotions = [
        {
            "title": "Скидка при самовывозе",
            "description": "Скидка 300₽ при самовывозе при покупке от 3500 рублей."
        },
        {
            "title": "СЕЗОННОЕ МЕНЮ",
            "subtitle": "Собрали лето в букеты",
            "link": "https://buket43.ru/piony"
        },
        {
            "title": "Индивидуальные букеты",
            "subtitle": "Создаем индивидуальные букеты, для свадеб и мероприятий в Кирове",
            "link": "https://buket43.ru/svadebnye-bukety"
        }
    ]

    benefits = [
        {"title": "Бонусная система", "link": "https://buket43.ru/catalog"},
        {"title": "Быстрая доставка", "description": "Мы доставляем букеты в течение 3 часов после заказа (в течении 60 минут в черте города)"},
        {"title": "Всегда свежие цветы", "description": "Наши букеты будут вас радовать как минимум полторы недели"},
        {"title": "Талантливые флористы", "description": "Все наши флористы имеют многолетний опыт работы и хороший вкус"}
    ]

    # 5. FAQ (Frequently Asked Questions)
    faq_items = [
        {
            "question": "Цветы будут свежие?",
            "answer": "Мы работаем только со свежими цветами, закупаем их у проверенных поставщиков. Цветы правильно обработаны и всегда проходят наш контроль качества."
        },
        {
            "question": "Какие гарантии, что цветы не завянут?",
            "answer": "Мы принимаем все меры, чтобы обеспечить свежесть и сохранность цветка:\n- Мы работаем только со свежими цветами, закупаем их у проверенных поставщиков.\n- Мы не пересобираем старые букеты. Все букеты делаются строго под заказ.\n- Букеты всегда упаковываются в одноразовую вазу с водой и в транспортировочных коробках. В холодную погоду букеты дополнительно утепляются.\n- К каждому букету прилагается инструкция по уходу и специальная подкормка, продлевающая жизнь цветов."
        },
        {
            "question": "Как быстро доставят купленные цветы и подарки по адресу?",
            "answer": "В течении 60 минут в черте города. За пределами города обсуждается лично с заказчиком."
        },
        {
            "question": "Все ли букеты на сайте доступны для заказа?",
            "answer": "Мы поддерживаем каталог актуальным и обновляем его согласно сезонности. Тем не менее, возможны ситуации, что цветок ненадлежащего качества или не пришел в поставке. Наши менеджеры подтверждают заказ после оформления."
        },
        {
            "question": "Будет ли букет выглядеть как на картинке?",
            "answer": "Все фотографии на нашем сайте – это букеты, сделанные флористами Цветочная лавка Buket. Но цветы – это живой организм, кроме того многие из них – сезонные. А значит, они не всегда доступны и даже в рамках одного сезона могут отличаться размером, формой и оттенком. Если вы хотите получить букет, максимально приближенный к фотографии, выбирайте букет из 1-2 видов цветов (моно и дуобукеты) и укажите свои пожелания при оформлении заказа. По готовности мы отправим фотографию именно вашего букета."
        },
        {
            "question": "Как ухаживать за букетом дома?",
            "answer": "К каждому букету прилагается инструкция по уходу и специальная подкормка, продлевающая жизнь цветов."
        }
    ]

    # 6. Catalog Categories & Products from Tilda API
    recs = soup.find_all('div', id=re.compile(r'^rec\d+'))

    rec_title_map = {}
    for r in recs:
        r_id = r.get('id')
        title_el = r.find(class_=re.compile(r't050__title|t-title|t-heading|t-name'))
        if title_el:
            rec_title_map[r_id] = title_el.get_text(strip=True)

    storepart_matches = re.finditer(r'recid\s*:\s*[\'\"](\d+)[\'\"]?.*?,.*?storepart\s*:\s*[\'\"](\d+)[\'\"]', main_html, re.DOTALL)

    cat_list = []
    seen_sp = set()

    for m in storepart_matches:
        rec_id = 'rec' + m.group(1)
        sp = m.group(2)

        if sp in seen_sp:
            continue
        seen_sp.add(sp)

        cat_title = rec_title_map.get(rec_id, "")
        if not cat_title:
            pos = main_html.find(rec_id)
            prev_snippet = main_html[max(0, pos-2500):pos]
            t_match = re.findall(r'class=\"[^\"]*(?:t050__title|t-title|t-name)[^\"]*\"[^>]*>(.*?)</div>|</h2>', prev_snippet, re.DOTALL)
            if t_match:
                cat_title = BeautifulSoup(t_match[-1], 'html.parser').get_text(strip=True)

        if sp == "836368059052":
            cat_title = "Цветы поштучно"
        elif sp == "470655217732":
            cat_title = "Букеты невесты"

        if not cat_title:
            cat_title = f"Категория {sp}"

        api_url = f"https://store.tildacdn.com/api/getproductslist/?storepartuid={sp}"
        try:
            sp_res = fetch_url(api_url)
            sp_data = json.loads(sp_res)
            raw_products = sp_data.get('products', [])

            formatted_products = []
            for p in raw_products:
                images = []
                gallery_str = p.get('gallery', '')
                if gallery_str:
                    try:
                        gallery_json = json.loads(gallery_str)
                        for img_obj in gallery_json:
                            if isinstance(img_obj, dict) and 'img' in img_obj:
                                images.append(img_obj['img'])
                    except Exception:
                        pass

                if not images and p.get('img'):
                    images.append(p['img'])

                formatted_products.append({
                    "id": p.get('uid'),
                    "title": html.unescape(p.get('title', '')).strip(),
                    "price": parse_float(p.get('price')),
                    "price_old": parse_float(p.get('priceold')) if p.get('priceold') else None,
                    "description": p.get('descr', '').strip(),
                    "sku": p.get('sku', ''),
                    "badge": p.get('mark', ''),
                    "unit": p.get('unit', ''),
                    "images": images,
                    "characteristics": p.get('characteristics', []),
                    "url": p.get('url', '')
                })

            cat_note = ""
            if sp == "470655217732":
                cat_note = "Заказы на свадебные букеты принимаются минимум за 14 дней до торжества, если срок меньше — мы можем подготовить букет невесты из наличия."

            cat_item = {
                "category_id": sp,
                "category_name": cat_title,
                "products_count": len(formatted_products),
                "products": formatted_products
            }

            if cat_note:
                cat_item["note"] = cat_note

            cat_list.append(cat_item)

        except Exception as e:
            print(f"Error fetching storepart {sp}: {e}")

    result = {
        "site_metadata": site_metadata,
        "company_info": company_info,
        "navigation": nav_links,
        "promotions": promotions,
        "benefits": benefits,
        "faq": faq_items,
        "catalog_categories": cat_list
    }

    return result

if __name__ == '__main__':
    data = parse_site()
    with open('buket43_data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print("Data extraction complete! Saved to buket43_data.json")
