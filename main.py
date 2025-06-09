import streamlit as st

# Danh sách sản phẩm mẫu
products = {
    "iPhone 15": 25000000,
    "Samsung Galaxy S24": 20000000,
    "Laptop Dell XPS": 30000000,
    "Tai nghe AirPods Pro": 5000000,
    "Chuột Logitech MX Master": 2000000
}

# Khởi tạo session_state để lưu giỏ hàng
if "cart" not in st.session_state:
    st.session_state.cart = {}

st.title("🛒 Cửa hàng trực tuyến đơn giản")

st.header("📦 Danh sách sản phẩm")

# Hiển thị sản phẩm và cho phép chọn mua
for product, price in products.items():
    col1, col2, col3 = st.columns([3, 1, 2])
    with col1:
        st.markdown(f"**{product}**")
    with col2:
        st.markdown(f"{price:,.0f} VND")
    with col3:
        quantity = st.number_input(f"Số lượng - {product}", min_value=0, max_value=10, step=1, key=product)
        if quantity > 0:
            st.session_state.cart[product] = quantity

# Xử lý giỏ hàng
st.header("🧾 Giỏ hàng của bạn")
if st.session_state.cart:
    total = 0
    for product, quantity in st.session_state.cart.items():
        price = products[product]
        subtotal = price * quantity
        st.write(f"- {product} x {quantity} = {subtotal:,.0f} VND")
        total += subtotal
    st.markdown(f"### 💰 Tổng cộng: {total:,.0f} VND")
    if st.button("🛍️ Thanh toán"):
        st.success("Cảm ơn bạn đã mua hàng!")
        st.session_state.cart.clear()
else:
    st.info("Giỏ hàng đang trống. Hãy chọn sản phẩm!")

