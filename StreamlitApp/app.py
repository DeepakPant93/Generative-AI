import streamlit as st

DEFAULT_OUTPUT_MSG: str = "There was a problem processing your request. Please try again after some time."
# uploaded_files: list[str] = []

class AskDocsApp:

    def __init__(self):
        pass


    def start(self):

        if 'uploaded_files' not in st.session_state:
            st.session_state.uploaded_files: list[str] = []

        # Add a drop-down list in the sidebar to choose the model
        with st.sidebar:
            st.header("Model Selection")
            model_choice = st.selectbox(
                "Choose a model:",
                ("GPT-3", "GPT-4", "Llama")
            )

        ## streamlit framework
        st.title('AskDocsGPT')
        input_text = st.text_input("Search anything related to docs...")
        output = DEFAULT_OUTPUT_MSG
        source_docs = None

        # Add a file uploader in the sidebar
        with st.sidebar:
            st.header("Upload Data")
            uploaded_file = st.file_uploader("Choose a file")

            # Display the uploaded file in the sidebar if available
            if uploaded_file and uploaded_file.name not in st.session_state.uploaded_files:
                st.session_state.uploaded_files.append(uploaded_file.name)
                print(st.session_state.uploaded_files)
                st.write(f"**Uploaded file:**")

            # for file_name in st.session_state.uploaded_files:
            #     st.write(file_name)

            # Loop through each file and display it with a delete button
            for file_name in st.session_state.uploaded_files:
                col1, col2 = st.columns([0.8, 0.2])
                col1.write(file_name)  # Display the file name
                # Display a delete button with a cross mark
                if col2.button("❌", key=file_name):
                    st.session_state.uploaded_files.remove(file_name)
                    st.rerun()

        if input_text and 3 <= len(input_text) <= 250:
            try:
                output = "I'm processing your request. Please wait."
                source_docs = [
                    {'page_content': 'Processing your request. Please wait.', 'metadata': {'source': 'AskDocsGPT'}}]
            except:
                st.error(output)
                return

            st.write(f"**{output}**")

            # Display the source documents in a more structured way
            if source_docs:
                st.markdown("_Source Documents:_")
                for idx, doc in enumerate(source_docs, start=1):
                    with st.expander(f"Document {idx}:"):
                        st.markdown(f"**Content**: {doc.get('page_content')}")
                        st.markdown(f"**Source**: {doc.get('metadata').get('source')}")

            st.markdown("---")
            st.caption("Powered by AskDocsGPT")
        else:
            st.error("Please enter a question between 3 to 250 characters.")


if __name__ == "__main__":
    ## Start Service
    app = AskDocsApp()

    # Run the async start method using asyncio's event loop
    app.start()
