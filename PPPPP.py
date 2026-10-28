import streamlit as st

# إعدادات الصفحة
st.set_page_config(
    page_title="Expert System for Chronic Patients",
    page_icon="🩺",
    layout="centered"
)

# القواميس الخاصة باللغات (العربية والإنجليزية)
translations = {
    "English": {
        "title": "🩺 Safe Health & Fitness Expert System",
        "subtitle": "Personalized recommendations for chronic patients",
        "sidebar_lang": "Language / اللغة",
        "step1_title": "Step 1: Basic Information",
        "age": "Age (Years)",
        "weight": "Weight (kg)",
        "height": "Height (cm)",
        "activity": "Activity Level",
        "activities": ["Sedentary (Little or no exercise)", "Moderate (Exercise 1-3 days/week)", "Active (Exercise 3-5 days/week)"],
        "step2_title": "Step 2: Medical History & Goals",
        "chronic": "Select Chronic Conditions (Choose all that apply):",
        "conditions": ["Diabetes", "Hypertension", "Knee Osteoarthritis", "High Cholesterol", "None"],
        "goal": "Select Your Health Goal:",
        "goals": ["Weight Loss", "Maintain Weight", "Improve Fitness"],
        "btn_run": "Run Expert System",
        "report_title": "📊 Expert System Diagnosis & Recommendations Report",
        "bmi_label": "Your Body Mass Index (BMI):",
        "status_label": "Health Status Classification:",
        "diet_title": "🥗 Recommended Diet & Food Guidelines",
        "allowed_food": "Allowed & Recommended Foods:",
        "avoid_food": "Foods to Avoid (Restricted):",
        "fitness_title": "🏋️ Safe Fitness & Exercise Plan",
        "allowed_ex": "Safe Exercises (Allowed):",
        "avoid_ex": "Prohibited Exercises (Avoid to Prevent Injury):",
        "reset_btn": "Start Over"
    },
    "العربية": {
        "title": "🩺 النظام الخبير للصحة والتغذية الآمنة",
        "subtitle": "توصيات مخصصة لأصحاب الأمراض المزمنة",
        "sidebar_lang": "اللغة / Language",
        "step1_title": "الخطوة الأولى: البيانات الأساسية",
        "age": "العمر (بالسنوات)",
        "weight": "الوزن (كجم)",
        "height": "الطول (سم)",
        "activity": "مستوى النشاط اليومي",
        "activities": ["قليل (حركة قليلة أو معدومة)", "متوسط (تمرين من 1 لـ 3 أيام أسبوعياً)", "عالي (تمرين من 3 لـ 5 أيام أسبوعياً)"],
        "step2_title": "الخطوة الثانية: التاريخ الطبي والأهداف",
        "chronic": "اختر الأمراض المزمنة (يمكن اختيار أكثر من واحد):",
        "conditions": ["مرض السكر", "ارتفاع ضغط الدم", "خشونة الركبة والمفاصل", "ارتفاع الكوليسترول", "لا يوجد"],
        "goal": "اختر هدفك الصحي:",
        "goals": ["خسارة الوزن", "الحفاظ على الوزن", "تحسين اللياقة البدنية"],
        "btn_run": "تشغيل النظام الخبير وعرض التقرير",
        "report_title": "📊 تقرير التشخيص والتوصيات من النظام الخبير",
        "bmi_label": "مؤشر كتلة الجسم (BMI):",
        "status_label": "تصنيف الحالة الصحية:",
        "diet_title": "🥗 الجدول الغذائي والتوجيهات",
        "allowed_food": "الأطعمة المسموحة والموصى بها:",
        "avoid_food": "الأطعمة المحظورة (يجب تجنبها):",
        "fitness_title": "🏋️ خطة التمارين الرياضية الآمنة",
        "allowed_ex": "التمارين الآمنة (المسموحة):",
        "avoid_ex": "التمارين المحظورة (تجنباً للإصابة):",
        "reset_btn": "إعادة ضبط النظام"
    }
}

# اختيار اللغة من الشريط الجانبي
st.sidebar.title("Settings / الإعدادات")
selected_lang = st.sidebar.selectbox("Language / اختر اللغة", ["English", "العربية"])
t = translations[selected_lang]

# عنوان التطبيق
st.title(t["title"])
st.markdown(t["subtitle"])
st.divider()

# نموذج إدخال البيانات (الخطوتين مجتمعتين أو كشاشات تتابع)
with st.form("expert_form"):
    st.subheader(t["step1_title"])
    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.number_input(t["age"], min_value=10, max_value=100, value=30)
    with col2:
        weight = st.number_input(t["weight"], min_value=30.0, max_value=200.0, value=70.0)
    with col3:
        height = st.number_input(t["height"], min_value=100.0, max_value=220.0, value=170.0)
        
    activity_level = st.selectbox(t["activity"], t["activities"])

    st.subheader(t["step2_title"])
    selected_conditions = st.multiselect(t["chronic"], t["conditions"])
    health_goal = st.radio(t["goal"], t["goals"])

    submitted = st.form_submit_button(t["btn_run"])

# منطق النظام الخبير (Inference Engine & Rule-Based Logic)
if submitted:
    # 1. حساب مؤشر كتلة الجسم (BMI)
    height_m = height / 100.0
    bmi = weight / (height_m ** 2)
    
    if bmi < 18.5:
        bmi_status = "Underweight / نحيف"
    elif 18.5 <= bmi < 24.9:
        bmi_status = "Normal Weight / وزن مثالي وطبيعي"
    elif 25 <= bmi < 29.9:
        bmi_status = "Overweight / زيادة في الوزن"
    else:
        bmi_status = "Obese / سمنة مفرطة"

    # 2. محرك القواعد (Inference Engine Rules) لتحديد الغذاء والتمارين
    allowed_foods_list = []
    avoid_foods_list = []
    allowed_exercises_list = []
    avoid_exercises_list = []

    # قواعد السكر (Diabetes Rules)
    if "Diabetes" in selected_conditions or "مرض السكر" in selected_conditions:
        avoid_foods_list.append("Sugary drinks, sweets, white bread, and fast carbohydrates / المشروبات السكرية، الحلويات، الخبز الأبيض")
        allowed_foods_list.append("High-fiber foods, vegetables, whole grains, and lean proteins / الأطعمة الغنية بالألياف، الخضروات، الحبوب الكاملة")
    
    # قواعد الضغط (Hypertension Rules)
    if "Hypertension" in selected_conditions or "ارتفاع ضغط الدم" in selected_conditions:
        avoid_foods_list.append("High-sodium foods, canned goods, and excess salt / الأطعمة المالحة، المعلبات، والمخللات")
        allowed_foods_list.append("Potassium-rich foods, fresh fruits, and low-sodium meals / الأطعمة الغنية بالبوتاسيوم، الفواكه الطازجة")

    # قواعد خشونة الركبة (Knee Osteoarthritis Rules)
    if "Knee Osteoarthritis" in selected_conditions or "خشونة الركبة والمفاصل" in selected_conditions:
        avoid_exercises_list.append("Running, jumping, heavy squats, and high-impact sports / الجري، النط، السكوات العنيف، الرياضات عالية التأثير")
        allowed_exercises_list.append("Swimming, stationary cycling, and light walking / السباحة، ركوب الدراجة الثابتة، المشي الخفيف")
    else:
        allowed_exercises_list.append("Moderate cardio and light weight training / كارديو معتدل وتمارين مقاومة خفيفة")

    # قواعد عامة حسب الهدف (Goal Rules)
    if health_goal == "Weight Loss" or health_goal == "خسارة الوزن":
        allowed_foods_list.append("Calorie-deficit balanced meals, water, and green tea / وجبات محسوبة السعرات، الماء، الشاي الأخضر")
    elif health_goal == "Maintain Weight" or health_goal == "الحفاظ على الوزن":
        allowed_foods_list.append("Balanced portions of proteins, carbs, and healthy fats / حصص متوازنة من البروتينات والكربوهيدرات والدهون الصحية")

    # لو مفيش أمراض مختارة
    if not selected_conditions or "None" in selected_conditions or "لا يوجد" in selected_conditions:
        allowed_foods_list.append("All healthy food groups in balanced proportions / جميع المجموعات الغذائية الصحية باعتدال")
        allowed_exercises_list.append("Any safe fitness routine or gym workout / أي روتين لياقة بدنية أو تمارين جمباز طبيعي")
        avoid_exercises_list.append("Overtraining without warm-up / الإفراط في التمرين بدون تسخين")

    # 3. عرض التقرير والنتائج للمستخدم
    st.success(t["report_title"])
    
    st.metric(label=t["bmi_label"], value=f"{bmi:.2f}")
    st.info(f"**{t['status_label']}** {bmi_status}")

    st.markdown(f"### {t['diet_title']}")
    st.markdown(f"✅ **{t['allowed_food']}**")
    for food in allowed_foods_list:
        st.write(f"- {food}")
        
    st.markdown(f"❌ **{t['avoid_food']}**")
    for food in avoid_foods_list:
        st.write(f"- {food}")

    st.markdown(f"### {t['fitness_title']}")
    st.markdown(f"✅ **{t['allowed_ex']}**")
    for ex in allowed_exercises_list:
        st.write(f"- {ex}")
        
    st.markdown(f"⛔ **{t['avoid_ex']}**")
    for ex in avoid_exercises_list:
        st.write(f"- {ex}")