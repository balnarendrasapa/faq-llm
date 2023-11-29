import streamlit as st

if "responses" not in st.session_state:
    st.session_state.responses = []

if "questions" not in st.session_state:
    st.session_state.questions = []


def app():
    st.set_page_config(
        page_title="Chat with Chatbot",
        page_icon="🤖",
        layout="centered"
    )
    st.title("Chat with Chatbot")

    container = st.container()
    st.write("Ask Your Question Here")
    question = st.text_input(
        "Ask your question here",
        label_visibility="collapsed"
    )
    with container:
        with st.chat_message("assistant"):
            st.write("How can I help you?")

        if question != "":
            st.session_state.responses.insert(0, "Sample Response")
            st.session_state.questions.insert(0, question)

            for i in range(len(st.session_state.responses)):
                with st.chat_message("user"):
                    st.write(st.session_state.questions[i - 1])

                with st.chat_message("assistant"):
                    with st.expander(
                        "Response (Click here to collapse)",
                        expanded=True
                    ):
                        result = st.session_state.responses[i]
                        st.write(result)
                    st.divider()


if __name__ == "__main__":
    app()
