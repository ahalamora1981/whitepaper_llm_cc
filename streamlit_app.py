import streamlit as st
import base64

# 设置页面标题
st.title('大语言模型在客服中心的应用前景')

# 加载PDF文件
def show_pdf(file_path):
    with open(file_path, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="1200" height="800" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)

show_pdf("llm_for_cc.pdf")
