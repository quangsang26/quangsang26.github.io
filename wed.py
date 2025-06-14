import streamlit as st

# Dữ liệu laptop mẫu
laptops = [
    {"name": "Dell XPS 13", "price": 25000000, "specs": "Core i7, 16GB RAM, 512GB SSD", "image": "https://i.imgur.com/xps13.jpg"},
    {"name": "MacBook Pro M1", "price": 32000000, "specs": "Apple M1, 8GB RAM, 256GB SSD", "image": "https://i.imgur.com/macbook.jpg"},
    {"name": "HP Pavilion", "price": 18000000, "specs": "Core i5, 8GB RAM, 256GB SSD", "image": "https://i.imgur.com/hppavilion.jpg"},
    {"name": "Asus TUF Gaming", "price": 28000000, "specs": "Ryzen 7, 16GB RAM, 1TB SSD", "image": "https://i.imgur.com/tuf.jpg"},
]

# Giao diện chính
st.set_page_config(page_title="Laptop Store", layout="wide")
st.title("🛒 Cửa hàng Laptop")

# Thanh tìm kiếm và lọc giá
search = st.text_input("🔍 Tìm kiếm laptop theo tên:")
min_price, max_price = st.slider("💸 Khoảng giá", 10000000, 40000000, (10000000, 40000000), step=1000000)

# Lọc laptop theo điều kiện
filtered = [
    laptop for laptop in laptops
    if search.lower() in laptop["name"].lower()
    and min_price <= laptop["price"] <= max_price
]

# Hiển thị sản phẩm
cols = st.columns(2)
for idx, laptop in enumerate(filtered):
    with cols[idx % 2]:
        st.image(laptop["image"], width=300)
        st.subheader(laptop["name"])
        st.write(f"💰 Giá: {laptop['price']:,} VND")
        st.write(f"🧠 Cấu hình: {laptop['specs']}")
        if st.button(f"Mua ngay - {laptop['name']}", key=laptop["name"]):
            st.success(f"✅ Bạn đã chọn mua: {laptop['name']}")

if not filtered:
    st.warning("⚠️ Không tìm thấy laptop phù hợp.")
