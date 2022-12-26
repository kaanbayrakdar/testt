# Çalıştırmak için -> streamlit run app.py
# Uygulama kaynağı: https://www.youtube.com/watch?v=VqgUkExPvLY
# streamlit tema kaynağı: https://blog.streamlit.io/introducing-theming/#:~:text=To%20toggle%20between%20various%20themes,is%20Streamlit's%20new%20dark%20theme.

from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie
import pandas as pd

st.set_page_config(page_title="Örnek Web Sitesi", page_icon=":tada:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use Local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# Load Assets
lottie_coding = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_3rwasyjy.json")
img_contract_from = Image.open("images/yt_contract_form.png")
img_lottie_animation = Image.open("images/yt_lottie_animation.png")

# Header
with st.container():
    st.subheader("Selam, Ben Kaan :wave:")
    st.title("Streamlit ile Yapılan Örnek Web Sitesi")
    st.write(
        "21.12.2022 tarihinde bu çalışmayı python alanında yeni şeyler öğrenmek ve bunları gerçek hayat problemlerine uygulamak için yapıyorum.")
    st.write("[Benim CV >](https://www.linkedin.com/in/mehmet-kaan-bayrakdar-11b306190)")

# Ana içerik: Örnek konu olarak vikipedia'dan herhangi bir paragraf alındı.
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Bunları Biliyor Muydunuz")
        st.write("##")
        st.write(
            """
            * [Tetris](https://tr.wikipedia.org/wiki/Tetris), uzayda oynanan ilk video oyunudur.
            * [Deniz seviyesinden](https://tr.wikipedia.org/wiki/Deniz_seviyesi) 5.029 metre yükseklikte yer alan İskelet Gölü, etrafındaki 9. yüzyıldan kalma yüzlerce insan iskeleti ile ünlüdür.
            * Eroin, bir dönem "bağımlılık yapmayan morfin" adı altında ilaç olarak satılmıştır.
            * Türkiye'de bale sanatının geçmişi, 16. yüzyılda İstanbul'da Venedik Balyosu'nun evinde düzenlenen bale gösterisine kadar gider.
            * Linda Hunt, [The Year of Living Dangerously](https://tr.wikipedia.org/wiki/The_Year_of_Living_Dangerously_(film)) filminde canlandırdığı "Billy Kwan" erkek karakteriyle, karşı cinsten bir karakteri canlandırarak Oscar Ödülü kazanmış ilk kişidir.
            * 1917 - Ekim Devrimi'nden sonra Çeka kuruldu.
            * 1924 - Almanya'da tutuklu bulunan Adolf Hitler, şartlı olarak salıverildi.
            * 1957 - Boeing 707 ilk uçuşunu yaptı.
            * 1971 - Pakistan'da Yahya Han istifa etti, yerine Zülfikâr Ali Butto Devlet Başkanı oldu.
            * 1999 - Makao'da Çin egemenliği başladı.
            """)
        st.write("[Vikipedi >](https://tr.wikipedia.org/wiki/Vikipedi:Biliyor_muydunuz%3F)")
    with right_column:
        st_lottie(lottie_coding)

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_lottie_animation)
    with text_column:
        st.subheader("Kaynak Alınan Youtube İçeriği")
        st.write("Build a Website in only 12 minutes using Python & Streamlit")
        st.write("#")
        st.write("lottie ile sayfaya animasyon eklendi.")
        st.markdown("[Youtube >](https://www.youtube.com/watch?v=VqgUkExPvLY)")

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contract_from)
    with text_column:
        st.subheader("iletişim Bilgileri")
        st.write(
            """
            İletişime geçmek için aşağıdaki alanlar kullanılabilir
            """)
        st.markdown("[İletişim >](https://www.linkedin.com/in/mehmet-kaan-bayrakdar-11b306190/)")

# Contact
with st.container():
    st.write("---")
    st.header("Get in Touch With Me!")
    st.write("##")

    # Kaynak: https://formsubmit.co/
    contact_form = """
    <form action="https://formsubmit.co/0d71840f5825ecd281b206331c45b349@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()

# Get Data
df = pd.read_csv("sales_data_example.csv", delimiter=";")  # csv çekildi

with st.container():
    st.write("---")
    st.header("Satış Raporu")
    st.write("##")
    left_graph, right_graph = st.columns(2)
    with left_graph:
        st.subheader("Ürün Bazında Satış Adedi")
        st.line_chart(df.groupby(by=["Product"]).count()["ID"])  # Ürün bazında satış adedi
    with right_graph:
        st.subheader("Ürün Bazında Satış Tutarı")
        st.bar_chart(df.groupby(by=["Product"]).sum()["Price"])  # Ürün bazında satış tutarı
