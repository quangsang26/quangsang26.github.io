import streamlit as st

# Danh sách sản phẩm – bạn chỉ cần thay ảnh, tên, giá, mô tả ở đây
products = [
    {
        "name": "Laptop Dell XPS 13",
        "price": 25000000,
        "description": "Core i7, 16GB RAM, 512GB SSD",
        "image_url": "https://i.imgur.com/xps13.jpg"
    },
    {
        "name": "MacBook Pro M1",
        "price": 32000000,
        "description": "Apple M1, 8GB RAM, 256GB SSD",
        "image_url": "https://i.imgur.com/macbook.jpg"
    },
    {
        "name": "Asus TUF Gaming",
        "price": 28000000,
        "description": "Ryzen 7, 16GB RAM, 1TB SSD",
        "image_url": "https://i.imgur.com/tuf.jpg"
    }
]

# Cấu hình trang
st.set_page_config(page_title="🛒 Cửa hàng bán hàng", layout="wide")
st.title("🛍️ CỬA HÀNG ONLINE - BÁN LAPTOP")

# Hiển thị danh sách sản phẩm
cols = st.columns(3)  # Hiển thị 3 sản phẩm mỗi hàng

for index, product in enumerate(products):
    with cols[index % 3]:
        st.image(product["image_url"], width=250)
        st.subheader(product["name"])
        st.write(f"💵 **Giá:** {product['price']:,} VND")
        st.write(f"📝 {product['description']}")
        if st.button(f"🛒 Mua ngay: {product['name']}", key=product["name"]):
            st.success(f"✅ Bạn vừa chọn mua: {product['name']}")

