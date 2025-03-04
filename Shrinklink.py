import streamlit as st
import requests
import time

# مفتاح API الخاص بك من ShrinkEarn
API_KEY = "f846b26135aca746c4fdfcd3195a295b96e6027b"
BASE_URL = "https://shrinkearn.com/api"

# عنوان التطبيق ووصف جذاب
st.title("اختصر واربح مع التنبيهات!")
st.write("قصّر أي رابط وحقق أرباحًا من كل نقرة - تلقَ تنبيهات ذكية لزيادة تفاعلك!")

# حقل إدخال الرابط
long_url = st.text_input("أدخل رابطك الطويل هنا", "")

# حالة التطبيق لتتبع الروابط
if "links" not in st.session_state:
    st.session_state.links = []

if st.button("قصّر الرابط"):
    if long_url:
        # طلب تقصير الرابط عبر API
        params = {"api": API_KEY, "url": long_url}
        try:
            response = requests.get(BASE_URL, params=params)
            if response.status_code == 200:
                data = response.json()
                if data.get("status") == "success":
                    short_url = data["shortenedUrl"]
                    st.success(f"رابطك المختصر: {short_url}")
                    st.write("📢 شاركه الآن على وسائل التواصل لتبدأ الأرباح!")
                    # إضافة الرابط إلى القائمة
                    st.session_state.links.append({"original": long_url, "short": short_url, "clicks": 0})
                else:
                    st.error(f"خطأ: {data.get('message', 'غير محدد')}")
            else:
                st.error("فشل الاتصال بخدمة ShrinkEarn. حاول لاحقًا.")
        except Exception as e:
            st.error(f"خطأ غير متوقع: {str(e)}")
    else:
        st.error("يرجى إدخال رابط!")

# عرض الروابط المختصرة السابقة مع تنبيهات
if st.session_state.links:
    st.subheader("روابطك المختصرة:")
    for idx, link in enumerate(st.session_state.links):
        st.write(f"الأصلي: {link['original']} | المختصر: {link['short']}")
        # محاكاة عدد النقرات (لأغراض العرض فقط)
        link["clicks"] += 1  # في الواقع، تحتاج API لتتبع النقرات
        if link["clicks"] >= 10:  # تنبيه عند وصول النقرات إلى 10
            st.warning(f"🎉 تنبيه: رابطك '{link['short']}' حصل على {link['clicks']} نقرة! شاركه أكثر لزيادة الأرباح!")

# نصائح للمستخدمين
st.info("💡 نصيحة: انشر روابطك في مجموعات فيسبوك، تويتر، أو واتساب لتحقيق أقصى ربح!")
