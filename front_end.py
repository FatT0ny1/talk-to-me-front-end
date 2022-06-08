import aifc
import streamlit as st
from streamlit_chat import message as st_message
import random
from PIL import Image
from st_clickable_images import clickable_images
import requests
from audio import Audio

st.set_page_config(page_title="Talk to me", page_icon='🤖',layout="wide")

url = "https://talktome-wzyr3jo7ga-ew.a.run.app"

# BACK END #
@st.cache
def get_seed():
    return random.randint(0,1000)
user_avatar = get_seed()


def generate_answer():
    # if st.session_state['button_is_clicked']  == True:
    #     ai = Audio(character_id)
    #     ai.speech_to_text()
    #     user_message = ai.text
    # else:
    user_message = st.session_state.input_text

    params = {
        "character_id" : character_id,
        "text" : user_message
    }
    response = requests.get(url, params)
    message_bot=response.json()

    # if st.session_state['button_is_clicked']  == True:
    #     ai.text_to_speech(response)

    st.session_state.history.append({"message": user_message, "is_user": True,'avatar_style': 'avataaars',  'seed': user_avatar})
    st.session_state.history.append({"message": message_bot, "is_user": False, 'seed': '58'})

# FRONT END

if "intro" not in st.session_state:
    st.session_state["intro"] = False

if "history" not in st.session_state:
    st.session_state.history = []

if 'input_text' in st.session_state:
    st.session_state['input_text'] = ''

if 'hide_everything' not in st.session_state:
    st.session_state['hide_everything'] = True

if 'second_page' not in st.session_state:
    st.session_state['second_page'] = True

if 'number_office' not in st.session_state:
    st.session_state['number_office'] = -1

if 'number_s' not in st.session_state:
    st.session_state['number_s'] = -1

    #### First Page #####
# st.write(st.session_state)

col1,col2 = st.columns([1,3])

if st.session_state['hide_everything'] == True:

    with col1:
            image = Image.open('logo.png')
            st.image(image, use_column_width = True)

    with col2:
        st.write('')
        st.markdown('<br><br><h2><strong><b> Talk to your<span style="color:red"> favourite character<br> </span> with an<span style="color:red"> AI brain </span> designed to entertain you</b></strong></h2>', unsafe_allow_html=True)

    st.markdown('<h2 style="background-color:#f3bdba;padding:3px;border:1px black;border-radius:15px;text-align:center"><b><strong><span style="color:red"> Select your character</span></strong></b></h2>',unsafe_allow_html=True)

    col1,col2,col3,col4,col5, = st.columns([1,1,1,1,1])


    # OLD IMAGES

    # "https://www.looper.com/img/gallery/who-voices-bart-on-the-simpsons/l-intro-1650682725.jpg"
    # "https://br.web.img2.acsta.net/r_1280_720/newsv7/20/08/20/22/44/03441350.jpg"


    # Clickable images!

    clicked_office = clickable_images(
        [
            "https://i.pinimg.com/550x/b1/a7/eb/b1a7ebe072fd40364dca1cf2e006e9a1.jpg",
            "https://www.wvisd.net/cms/lib/TX01001412/Centricity/Domain/333/dwight3.jpg",
            "http://cdn.akamai.steamstatic.com/steamcommunity/public/images/avatars/cc/cc43056062c943d77081d6369100d0c0caf5e24a_full.jpg",
            "https://i.pinimg.com/564x/b4/37/0b/b4370be92a23d01d414d94983c2fb925.jpg",
            "https://akns-images.eonline.com/eol_images/Entire_Site/2020023/rs_600x600-200123145928-office1.jpg?fit=around%7C1080:1080&output-quality=90&crop=1080:1080;center,top",
        ],
        titles=['Jim Halpert', 'Dwight Schrute', 'Michael Scott', 'Pam Beesly', 'Andy Bernard (Nard Dog)'],
        div_style={"display": "block", "justify-content": "center", "flex-wrap": "wrap-reverse", "background": 'transparent', 'box-shadow': 'gray'},
        img_style={"margin": "35px", "height": "165px", "width": "165px", 'border-radius': '50%', 'border': '1px solid white', 'box-shadow': 'gray 0 0 5px', 'margin-bottom': '1px'},
        key= 'office'
    )

    col1,col2,col3 = st.columns([1,1,1])


    clicked_simpsons = clickable_images(
        [
             "https://openpsychometrics.org/tests/characters/test-resources/pics/S/2.jpg",
             "https://pbs.twimg.com/profile_images/769201881826533376/IhFgf0dO_400x400.jpg",
             "https://i.pinimg.com/originals/37/df/40/37df409cd5d62efdb36804c6cfdbc85b.png",
             "https://pbs.twimg.com/profile_images/1550268954/margee_400x400.jpg",
        ],
        titles=['Bart Simpson', 'Homer Simpson', 'Lisa Simpson', 'Marge Simpson'],
        div_style={"display": "block","margin-left": "112px", "justify-content": "center", "flex-wrap": "wrap-reverse", "background": 'transparent', 'box-shadow': 'gray'},
        img_style={"margin": "35px", "height": "165px", "width": "165px", 'border-radius': '50%', 'border': '1px solid white', 'box-shadow': 'gray 0 0 5px', 'margin-top': '1px'},
        key= 'simpsons'
    )


    if clicked_office > -1:
        st.session_state['hide_everything'] = False
        st.session_state['intro'] = True
        st.session_state['number_office'] = clicked_office
        st.experimental_rerun()


    if clicked_simpsons > -1:
        st.session_state['hide_everything'] = False
        st.session_state['intro'] = True
        st.session_state['number_s'] = clicked_simpsons
        st.experimental_rerun()

########### SECOND PAGE ############
# A LOT OF SHIT DOWN HERE

if st.session_state['intro']:

    col1,col2,col3 = st.columns([1,2,1])

    with col2:
        st.markdown('<h2><br></h2>', unsafe_allow_html=True)
    with col3:
        st.markdown('<h2><br></h2>', unsafe_allow_html=True)

    with col1:
        image = Image.open('logo.png')
        st.image(image, use_column_width = True)

    if st.session_state['number_office'] == 4:
        character_id = 'andy'
        with col2:
            st.markdown('<h2><strong><b> Start chatting with <span style="color:red">Andy <br> </span>and<span style="color:red">  have fun</span></b></strong></h2>', unsafe_allow_html=True)
        with col3:
            st.markdown("""
                        <div>
                        <img src="https://akns-images.eonline.com/eol_images/Entire_Site/2020023/rs_600x600-200123145928-office1.jpg?fit=around%7C1080:1080&output-quality=90&crop=1080:1080;center,top"
                            style="border-radius : 50%;
                            marin : 35px;
                            height : 165px;
                            width: 165px;
                            border: 1px solid white;
                            box-shadow: gray 0 0 5px;">
                        </div>
                        """,
                        unsafe_allow_html=True)
    if st.session_state['number_office'] == 3:
        character_id = 'pam'
        with col2:
            st.markdown('<h2><strong><b> Start chatting with <span style="color:red">Pam <br> </span> and<span style="color:red">  have fun</span></b></strong></h2>', unsafe_allow_html=True)
        with col3:
            st.markdown("""
                        <div>
                        <img src="https://i.pinimg.com/564x/b4/37/0b/b4370be92a23d01d414d94983c2fb925.jpg"
                            style="border-radius : 50%;
                            marin : 35px;
                            height : 165px;
                            width: 165px;
                            border: 1px solid white;
                            box-shadow: gray 0 0 5px;">
                        </div>
                        """,
                        unsafe_allow_html=True)
    if st.session_state['number_office'] == 2:
        character_id = 'michael'
        with col2:
            st.markdown('<h2><strong><b> Start chatting with <span style="color:red">Michael <br> </span> and<span style="color:red">  have fun</span></b></strong></h2>', unsafe_allow_html=True)
        with col3:
            st.markdown("""
                        <div>
                        <img src="http://cdn.akamai.steamstatic.com/steamcommunity/public/images/avatars/cc/cc43056062c943d77081d6369100d0c0caf5e24a_full.jpg"
                            style="border-radius : 50%;
                            marin : 35px;
                            height : 165px;
                            width: 165px;
                            border: 1px solid white;
                            box-shadow: gray 0 0 5px;">
                        </div>
                        """,
                        unsafe_allow_html=True)
    if st.session_state['number_office'] == 1:
        character_id = 'dwight'
        with col2:
            st.markdown('<h2><strong><b> Start chatting with <span style="color:red">Dwight <br> </span> and<span style="color:red">  have fun</span></b></strong></h2>', unsafe_allow_html=True)
        with col3:
            st.markdown("""
                        <div>
                        <img src="https://www.wvisd.net/cms/lib/TX01001412/Centricity/Domain/333/dwight3.jpg"
                            style="border-radius : 50%;
                            marin : 35px;
                            height : 165px;
                            width: 165px;
                            border: 1px solid white;
                            box-shadow: gray 0 0 5px;">
                        </div>
                        """,
                        unsafe_allow_html=True)
    if st.session_state['number_office'] == 0:
        character_id = 'jim'
        with col2:
            st.markdown('<h2><strong><b> Start chatting with <span style="color:red">Jim <br> </span> and<span style="color:red">  have fun</span></b></strong></h2>', unsafe_allow_html=True)
        with col3:
            st.markdown("""
                        <div>
                        <img src="https://i.pinimg.com/550x/b1/a7/eb/b1a7ebe072fd40364dca1cf2e006e9a1.jpg"
                            style="border-radius : 50%;
                            marin : 35px;
                            height : 165px;
                            width: 165px;
                            border: 1px solid white;
                            box-shadow: gray 0 0 5px;">
                        </div>
                        """,
                        unsafe_allow_html=True)
    if st.session_state['number_s'] == 3:
        with col2:
            st.markdown('<h2><strong><b> Start chatting with <span style="color:red">Marge <br> </span> and<span style="color:red">  have fun</span></b></strong></h2>', unsafe_allow_html=True)
        with col3:
            st.markdown("""
                        <div>
                        <img src="https://pbs.twimg.com/profile_images/1550268954/margee_400x400.jpg"
                            style="border-radius : 50%;
                            marin : 35px;
                            height : 165px;
                            width: 165px;
                            border: 1px solid white;
                            box-shadow: gray 0 0 5px;">
                        </div>
                        """,
                        unsafe_allow_html=True)
    if st.session_state['number_s'] == 2:
        with col2:
            st.markdown('<h2><strong><b> Start chatting with <span style="color:red">Lisa <br> </span> and<span style="color:red">  have fun</span></b></strong></h2>', unsafe_allow_html=True)
        with col3:
            st.markdown("""
                        <div>
                        <img src="https://i.pinimg.com/originals/37/df/40/37df409cd5d62efdb36804c6cfdbc85b.png"
                            style="border-radius : 50%;
                            marin : 35px;
                            height : 165px;
                            width: 165px;
                            border: 1px solid white;
                            box-shadow: gray 0 0 5px;">
                        </div>
                        """,
                        unsafe_allow_html=True)
    if st.session_state['number_s'] == 1:
        with col2:
            st.markdown('<h2><strong><b> Start chatting with <span style="color:red">Homer <br> </span> and <span style="color:red"> have fun</span></b></strong></h2>', unsafe_allow_html=True)
        with col3:
            st.markdown("""
                        <div>
                        <img src="https://pbs.twimg.com/profile_images/769201881826533376/IhFgf0dO_400x400.jpg"
                            style="border-radius : 50%;
                            marin : 35px;
                            height : 165px;
                            width: 165px;
                            border: 1px solid white;
                            box-shadow: gray 0 0 5px;">
                        </div>
                        """,
                        unsafe_allow_html=True)
    if st.session_state['number_s'] == 0:
        with col2:
            st.markdown('<h2><strong><b> Start chatting with <span style="color:red">Bart <br> </span> and<span style="color:red">  have fun</span></b></strong></h2>', unsafe_allow_html=True)
        with col3:
            st.markdown("""
                        <div>
                        <img src="https://openpsychometrics.org/tests/characters/test-resources/pics/S/2.jpg"
                            style="border-radius : 50%;
                            marin : 35px;
                            height : 165px;
                            width: 165px;
                            border: 1px solid white;
                            box-shadow: gray 0 0 5px;">
                        </div>
                        """,
                        unsafe_allow_html=True)

    with col2:
            st.write("---")
            st.markdown('<br>', unsafe_allow_html=True)

    st.session_state['second_page'] = False





    with col2:

        for chat in st.session_state.history:
            st_message(**chat)  # unpacking

        st.text_input(label=" ", key="input_text",placeholder ='Type your message here', on_change=generate_answer)
        # st.write(st.session_state)
    with col2:
        if 'button_is_clicked' not in st.session_state:
            st.session_state['button_is_clicked'] = False

        def chance_button_status():
            st.session_state['button_is_clicked']  = (st.session_state['button_is_clicked']  == False)

        button = st.button('🔊', key=None, help='Click me to send audio message', on_click=(chance_button_status), args=None, kwargs=None, disabled=False)

    with col3:
        change_avatar = st.button('🦸‍♀️', help='Click me to change your avatar')
        if change_avatar:
            st.legacy_caching.caching.clear_cache()
            user_avatar = get_seed()
            for chat in st.session_state.history:
                if chat['is_user']:
                    chat["seed"] = user_avatar
            st.experimental_rerun()

#SIDE_BAR

# #     ### Create sidebar
#     with col3:

#         if st.button("🍳", help='More Information'):

#             st.sidebar.subheader('*Meet the Team*')
#             st.sidebar.write('[Blandine Delval](https://www.linkedin.com/in/blandine-delval-32a693147/)')
#             st.sidebar.write('[Immy Stege](https://www.linkedin.com/in/immy-stege-863093165/)')
#             st.sidebar.write('[Pedro Sousa](https://www.linkedin.com/in/pedro-bongiovanni-9b1579184//)')
