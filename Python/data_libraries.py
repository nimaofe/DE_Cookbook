
# کتابخانه‌های مهم برای مهندسی داده

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# pandas برای کار با داده‌های جدولی
data = {
    'نام': ['علی', 'مریم', 'نیما'],
    'سن': [25, 30, 22],
    'شهر': ['تهران', 'اصفهان', 'مشهد']
}
df = pd.DataFrame(data)

# نمایش داده‌ها
print(df)

# محاسبه میانگین سن
میانگین_سن = df['سن'].mean()
print(f"میانگین سن: {میانگین_سن}")

# numpy برای محاسبات عددی
آرایه = np.array([1, 2, 3, 4, 5])
جمع = np.sum(آرایه)
میانگین = np.mean(آرایه)

print(f"جمع آرایه: {جمع}")
print(f"میانگین آرایه: {میانگین}")

# رسم نمودار با matplotlib
plt.plot([1, 2, 3, 4], [10, 20, 25, 30])
plt.xlabel('محور X')
plt.ylabel('محور Y')
plt.title('نمودار خطی')
plt.show()

# رسم نمودار با Seaborn
sns.barplot(x=['علی', 'مریم', 'نیما'], y=[25, 30, 22])
plt.xlabel('نام')
plt.ylabel('سن')
plt.title('نمودار ستونی')
plt.show()
