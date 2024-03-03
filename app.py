import streamlit as st

def main():
    # Set page configuration
    st.set_page_config(
        page_title="To Mansi",
        page_icon="✨",
        layout="wide",
        initial_sidebar_state="collapsed",
    )

    # Set the background color to light pink
    st.markdown(
        """
        <style>
            .reportview-container  {
                background-color: #FFFF;
            }
            .e1nzilvr5{background-color: #FFFF;color:{#0000};border-radius: 15px; width: auto;}
            .ezrtsby2{background-color: #FFFF;}
            .main {
                background-color: #FFFF;
                font-color:#0000;
            }
            .block-container  {
                background-color: #FFFF;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Title
    st.balloons()
    st.subheader("Welcome To")
    st.title("Code of Apologies ✨ : Debugging Love's Errors")
    st.caption("-----------")
    st.caption("\n\n\n\n\n\n\n\n")
    # Story
    st.markdown(
        """
        Once upon a time in the Green City Gandhinagar, there lived two pips deeply entwined in the tapestry of life. Mansi, a brilliant psychology student, exuded an aura of kindness and warmth. Her world was painted in the gentle hues of light pink, reflecting her love for creativity and the softer aspects of life. Anuj, on the other hand, delved into the complexities of computer science, finding solace in the harmonious blend of saffron and dark black.
Their love story began with the promise of understanding and companionship. Mansi, having endured childhood traumas, found solace in Anuj's understanding of nature. However, as time unfolded, the colors of their relationship started to fade. As time went by, Anuj started paying less attention to Mansi, and the special treatment she used to get, like a princess, began to fade away. His actions didn't match his earlier gestures, showing a noticeable decline in the care and concern that once defined their relationship. Deep within, Anuj cherished Mansi even more, recognizing her immense value in his heart. However, this growing appreciation remained concealed, surfacing only in his words and not in his visible actions.
Mansi, with her pure soul, felt the subtle shifts in Anuj's behavior. The gestures of care dwindled, and the once small, meaningful things were forgotten. Anuj, consumed by his own world, failed to see the distress that had crept into Mansi's eyes.
One day, after a particularly challenging argument, Mansi found herself questioning the foundation of their love. Anuj, sensing the impending storm, decided to take a step back and reflect on the damage he had unintentionally caused. He knew he had to do something significant to mend the cracks in their relationship.
In the quietude of his room, Anuj sat down with a laptop, pouring his heart out in a webpage titled, "Sorry For Everything," addressed to his beloved Mansiidi.



        """
        
    )
    st.divider()
    st.image("love.png",caption="Capturing the Essence of Love in a Symphony of Penguin Poses 🐧💕")
    
    st.markdown("""Dear Mansiidi (my Mansi),\n\n
I hope this letter finds its way to the deepest corners of your heart, for that is where it truly belongs. I pen down these words with a heavy heart, burdened by the realization of my shortcomings and the pain I've caused you.
I am sorry. A simple phrase, yet it carries the weight of a thousand unspoken apologies. I am sorry for the times when I failed to see the sparkle in your eyes, for the moments when I let the intricacies of our love slip through the cracks. I am sorry for the hurt that found its way into your heart, the hurt caused by my negligence and oversight.
In the canvas of our love, I've been the artist who unintentionally smeared the vibrant pink hues with the dark shades of my actions. You, my Mansi, deserve a masterpiece, not a flawed creation marred by my own ignorance.
I want you to know that I understand the fragility of your soul, and I am deeply remorseful for any pain I've caused. It hurts me to know that I've become the source of disappointment and upset in your life.
Yesterday's heated exchange was a culmination of my inadequacies, and I want you to know that it hurt me just as much as it hurt you. I can no longer stand as the cause of your tears, and I refuse to let our love be tainted by my shortcomings.
I apologize for the issues surrounding our recent trip. My poor planning and lack of consideration left you feeling unimportant, and for that, I am truly sorry. I promise you, my love, that from now on, we will plan our adventures meticulously, ensuring every moment is as beautiful as the love we once shared.
I vow to be a better partner, to appreciate the small things that make you smile, and to be there for you in times of joy and sorrow. Your appearance, my dear, is a marvel that leaves me breathless every day. I am sorry if my words ever conveyed otherwise. You are the epitome of beauty, and I am blessed to have you as mine.
The essence of your soul, the fragrance that fills my life, deserves to be cherished and celebrated. No longer will my aura cast shadows upon your brilliance. I promise to make you feel alive, happy, and cherished.
Do you still reminisce about the scent of salsa perfume that enveloped us when we shared those romantic moments? I want you to carry that fragrance with you, even when I am not by your side. My love, my world, I miss you from the woods of Gandhinagar, and I want to assure you that I am here. From now on, I am committed to being the Anuj Patel you fell in love with – a blossomed lover, ready to paint your world with the pinkish hues of happiness.
Mansi, my heart, I choose you. I am sorry for everything, and I am ready to make amends. Let our love story continue, not as a tale of sorrow but as a testament to the strength of our bond.
With all the love in my heart,\n\n\n
Anuj Patel (Your Blossomed Lover).""")
    st.divider()
    st.markdown("""Anuj sealed the digital message with utmost sincerity, deploying a personalized website on Streamlit and sending Mansi a QR code. As he awaited her response, his heart pounded with anticipation, hoping this modern gesture would rekindle the spark that had once illuminated their love, and eager for the chance to prove that their relationship was worth fighting for.
""")
    video_url = "https://www.youtube.com/watch?v=nG-15Ql8a2k"
    st.video(video_url)

    st.divider()
    st.subheader("Mansi, thank you so much for reading this till here")
    st.markdown("Made with  ❤️ by Anuj.")
    

if __name__ == "__main__":
    main()
