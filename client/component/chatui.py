import os
import streamlit as st
from utlies.api import ask_question


def render_chat():
    st.subheader("💬 Chat with your assistant")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat history
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # User input
    user_input = st.chat_input("Type your question...")

    if user_input:
        # Display user message
        with st.chat_message("user"):
            st.markdown(user_input)

        st.session_state.messages.append(
            {"role": "user", "content": user_input}
        )

        try:
            with st.spinner("Thinking..."):
                response = ask_question(user_input)

            if response.status_code == 200:
                data = response.json()

                if os.getenv("DEBUG"):
                    print("API Response:", data)
                    st.write("API Response:", data)

                # Safely extract response
                answer = data.get("response")

                if answer is None:
                    error_msg = (
                        "⚠️ Sorry, the assistant didn't return a valid response. "
                        "Please try again."
                    )
                    st.error(
                        f"Backend did not return a 'response' field.\n\nReturned JSON:\n{data}"
                    )
                    with st.chat_message("assistant"):
                        st.markdown(error_msg)
                    st.session_state.messages.append(
                        {"role": "assistant", "content": error_msg}
                    )
                    return

                sources = data.get("sources", [])

                with st.chat_message("assistant"):
                    st.markdown(answer)

                    if sources:
                        st.markdown("**📄 Sources:**")
                        for src in sources:
                            st.markdown(f"- `{src}`")

                # Persist sources alongside the answer so history/downloads
                # keep the full context
                full_content = answer
                if sources:
                    full_content += "\n\n**Sources:**\n" + "\n".join(
                        f"- {src}" for src in sources
                    )

                st.session_state.messages.append(
                    {"role": "assistant", "content": full_content}
                )

            else:
                error_msg = f"⚠️ Server error ({response.status_code}). Please try again."
                st.error(f"Server Error ({response.status_code})")
                st.code(response.text)
                with st.chat_message("assistant"):
                    st.markdown(error_msg)
                st.session_state.messages.append(
                    {"role": "assistant", "content": error_msg}
                )

        except Exception as e:
            error_msg = "⚠️ Something went wrong while contacting the assistant."
            st.error(f"Request failed: {e}")
            with st.chat_message("assistant"):
                st.markdown(error_msg)
            st.session_state.messages.append(
                {"role": "assistant", "content": error_msg}
            )