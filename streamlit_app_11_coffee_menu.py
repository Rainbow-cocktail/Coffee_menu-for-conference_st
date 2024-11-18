"""
提供给老师咖啡菜单，并自己生成老师的咖啡订单
"""
import streamlit as st

st.title('Coffee Menu for Teachers at the Conference')
selected_teacher = st.sidebar.selectbox('Select a teacher:', [' ','teacher A', 'teacher B', 'teacher C'])
if selected_teacher == ' ':
    st.info('Please select a teacher from the left side.')
else:
    with st.form(key='coffee machine'):
        st.subheader('**Order your coffee**')
        # 可在三家咖啡商家中做出选择，每家咖啡菜单都不同
        coffee_shop = st.selectbox('Select a coffee shop:', ['Shop A', 'Shop B', 'Shop C'])
        # 根据选择的咖啡店，显示不同的咖啡菜单
        if coffee_shop == 'Shop A':
            coffee_bean_val = st.selectbox('Coffee bean', ['Arabica', 'Robusta'])
            coffee_roast_val = st.selectbox('Coffee roast', ['Light', 'Medium', 'Dark'])
            brewing_val = st.selectbox('Brewing method', ['Aeropress', 'Drip', 'French press', 'Moka pot', 'Siphon'])
            serving_type_val = st.selectbox('Serving format', ['Hot', 'Iced', 'Frappe'])
            milk_val = st.select_slider('Milk intensity', ['None', 'Low', 'Medium', 'High'])
            owncup_val = st.checkbox('Bring own cup')
        elif coffee_shop == 'Shop B':
            coffee_bean_val = st.selectbox('Coffee bean', ['Arabica', 'Robusta'])
            coffee_roast_val = st.selectbox('Coffee roast', ['Light', 'Medium', 'Dark'])
            brewing_val = st.selectbox('Brewing method', ['Aeropress', 'Drip', 'French press', 'Moka pot', 'Siphon'])
            serving_type_val = st.selectbox('Serving format', ['Hot', 'Iced', 'Frappe'])
            milk_val = st.select_slider('Milk intensity', ['None', 'Low', 'Medium', 'High'])
            owncup_val = st.checkbox('Bring own cup')
        else:
            coffee_bean_val = st.selectbox('Coffee bean', ['Arabica', 'Robusta'])
            coffee_roast_val = st.selectbox('Coffee roast', ['Light', 'Medium', 'Dark'])
            brewing_val = st.selectbox('Brewing method', ['Aeropress', 'Drip', 'French press', 'Moka pot', 'Siphon'])
            serving_type_val = st.selectbox('Serving format', ['Hot', 'Iced', 'Frappe'])
            milk_val = st.select_slider('Milk intensity', ['None', 'Low', 'Medium', 'High'])
            owncup_val = st.checkbox('Bring own cup')
        # Every form must have a submit button
        submitted = st.form_submit_button('Submit')
    # display the order and save it to a file.
    if submitted:
        st.markdown(f'''
                ☕ {selected_teacher} have ordered:
                - Coffee shop: `{coffee_shop}`
                - Coffee bean: `{coffee_bean_val}`
                - Coffee roast: `{coffee_roast_val}`
                - Brewing: `{brewing_val}`
                - Serving type: `{serving_type_val}`
                - Milk: `{milk_val}`
                - Bring own cup: `{owncup_val}`
                ''')
        # save the order to a file
        st.write('Order saved to file.')
        st.download_button(
            label='Download order',
            data=f'{selected_teacher} order:\n'
                 f'Coffee shop: {coffee_shop}\n'
                 f'Coffee bean: {coffee_bean_val}\n'
                 f'Coffee roast: {coffee_roast_val}\n'
                 f'Brewing: {brewing_val}\n'
                 f'Serving type: {serving_type_val}\n'
                 f'Milk: {milk_val}\n'
                 f'Bring own cup: {owncup_val}\n',
            file_name=f'{selected_teacher}_order.txt',
            mime='text/plain'
        )
    else:
        st.write('☝️ Place your order!')






