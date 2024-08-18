'''我的主页'''
import streamlit as st
from PIL import Image
page = st.sidebar.radio('我的首页', ['我的兴趣推荐', '我的图片处理工具', '我的智慧词典', '我的留言区'])
def page_1():
    '''我的兴趣推荐'''
    with open('霞光.mp3', 'rb') as f:
        mymp3 = f.read()
    st.audio(mymp3, format='audio/mp3', start_time=0)
    st.image('slogan.png')
    audio_file_path = 'Python创赛营作品提交指南-海龟客户端.mp4'  
    # 打开音频文件并播放  
    with open(audio_file_path, 'rb') as audio_file:  
        audio_bytes = audio_file.read()  
    st.video(audio_bytes, start_time=0)  
    st.write('阿短的电影推荐')
    st.write('-----------------------------')
    st.write('阿短的游戏推荐')
    st.write('-----------------------------')
    st.write('阿短的书籍推荐')
    st.write('-----------------------------')
    st.write('阿短的习题集推荐')
    st.write('-----------------------------')
def page_2():
    '''我的图片处理工具'''
    st.write(":dragon:图片换色小程序:dragon:")
    uploaded_file = st.file_uploader("上传图片", type=['png', 'jpeg', 'jpg'])
    if uploaded_file:
        # 获取图片文件的名称、类型和大小
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size
        img = Image.open(uploaded_file)
        tab1,tab2,tab3,tab4,tab5=st.tabs(["原色","改色1","改色2","改色3","变小"])
        with tab1:
            st.image(img)
        with tab2:
            st.image(img_change(img, 0, 2, 1))
        with tab3:
            st.image(img_change(img, 1, 2, 0))
        with tab4:
            st.image(img_change(img, 1, 0, 2))
        with tab5:
            w=st.text_input("新图片的宽")
            h=st.text_input("新图片的高")
            st.image(img_change1(img,int(w), int(h)))
def page_3():
    '''我的智能词典'''
    st.write('智能词典')
    # 从本地文件中将词典信息读取出来，并存储在列表中
    with open('words_space.txt', 'r', encoding='utf-8') as f:
        words_list = f.read().split('\n')
    # 将列表中的每一项内容再进行分割，分为“编号、单词、解释”
    for i in range(len(words_list)):
        words_list[i] = words_list[i].split('#')
    # 将列表中的内容导入字典，方便查询，格式为“单词：编号、解释”
    words_dict = {}
    for i in words_list:
        words_dict[i[1]] = [int(i[0]), i[2]]
    # 创建输入框
    word = st.text_input('请输入要查询的单词')
    # 显示查询内容
    if word in words_dict:
        st.write(words_dict[word][1])
        # 注意词典中没有python，需要自行添加数据
        if word == 'python':
            st.code('''
                    # 恭喜你触发彩蛋，这是一行python代码
                    print('hello world')''')
        if word == 'snow' or word == 'winter':
            st.snow()
        if word == 'birthday':
            st.balloons()

def page_4():
    '''我的留言区'''
    st.write('我的留言区')
    # 从文件中加载内容，并处理成列表
    with open('leave_messages.txt', 'r', encoding='utf-8') as f:
        messages_list = f.read().split('\n')
    for i in range(len(messages_list)):
        messages_list[i] = messages_list[i].split('#')
    for i in messages_list:
        if i[1] == '阿短':
            with st.chat_message('👦'):
                st.write(i[1],':',i[2])
        elif i[1] == '编程猫':
            with st.chat_message('🙀'):
                st.write(i[1],':',i[2])
        else:
            with st.chat_message('🌞'):
                st.write(i[1],':',i[2])
        
    name = st.selectbox('我是……', ['阿短', '编程猫'])
    new_message = st.text_input('想要说的话……')
    if st.button('留言'):
        messages_list.append([str(int(messages_list[-1][0])+1), name, new_message])
        with open('leave_messages.txt', 'w', encoding='utf-8') as f:
            message = ''
            for i in messages_list:
                message += i[0] + '#' + i[1] + '#' + i[2] + '\n'
            message = message[:-1]
            f.write(message)
def img_change(img,rc,rg,rb):
    '''图片处理'''
    width, height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            # 获取RGB值
            r = img_array[x, y][rc]
            g = img_array[x, y][rb]
            b = img_array[x, y][rb]
            img_array[x, y] = (r, g, b)
    return img
def img_change1(img,w,h):
    '''图片处理'''
    #缩放与拉伸
    newsize=(w,h)
    img_resize=img.resize(newsize)
    return img_resize
if page == '我的兴趣推荐':
    page_1()
elif page == '我的图片处理工具':
    page_2()
elif page == '我的智慧词典':
    page_3()
elif page == '我的留言区':
    page_4()
