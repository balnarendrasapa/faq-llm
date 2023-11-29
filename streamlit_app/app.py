import streamlit as st
# import torch
# from peft import PeftModel, PeftConfig
# from transformers import AutoModelForCausalLM, AutoTokenizer

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

    # peft_model_id = "bnsapa/faq-llm"
    # config = PeftConfig.from_pretrained(peft_model_id)
    # model = AutoModelForCausalLM.from_pretrained(config.base_model_name_or_path, return_dict=True, load_in_8bit=True, device_map='auto')
    # tokenizer = AutoTokenizer.from_pretrained(config.base_model_name_or_path)
    # model = PeftModel.from_pretrained(model, peft_model_id)

    container = st.container()
    st.write("Ask Your Question Here")
    question = st.text_input(
        "Ask your question here",
        label_visibility="collapsed"
    )

    # batch = tokenizer(f"{question} ->: ", return_tensors='pt')
    # with torch.cuda.amp.autocast():
        # output_tokens = model.generate(**batch, max_new_tokens=50)

    # response = tokenizer.decode(output_tokens[0], skip_special_tokens=True)

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
