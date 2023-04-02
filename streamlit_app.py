import streamlit as st
import base64
import os


# 设置页面标题
st.title('大语言模型在客服中心的应用前景')
st.write(os.getcwd())

# 加载PDF文件
def show_pdf(file_path):
    with open(file_path, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="1200" height="800" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)

show_pdf("https://drive.google.com/file/d/14vP-PgHZum11hhRbTRbhYGlatz9gjPm_/view?usp=share_link")

# st.markdown("""
# <embed src="/app/whitepaper_llm_cc/llm_for_cc.pdf" width="1000" height="800">
# """, unsafe_allow_html=True)
