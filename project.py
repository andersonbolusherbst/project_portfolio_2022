import streamlit as st
import pandas as pd
import numpy as np
import requests
import altair as alt

option = st.sidebar.selectbox("HAB LABS Services", ( "Home", "About", 'Analytics', 'Data Infrastructure','Machine Learning','Custom Web Apps'))

st.markdown(
    """
<style>
#root > div:nth-child(1) > div.withScreencast > div > div > div > section.css-163ttbj.e1fqkh3o11 > div.css-6qob1r.e1fqkh3o3{
background: #29abe2;
}
</style>
""",
    unsafe_allow_html=True,
)

if option == "Home":
  st.image("HAB LABS.png", width = 750)
  st.markdown("<h1 style='text-align: center; color: black;'>WE HELP COMPANIES GROW</h1>", unsafe_allow_html=True)
  st.write("")
  st.markdown("<h4 style='text-align: center; color: black;'>Welcome to the HAB LABS Digital Portfolio.</h4>", unsafe_allow_html=True)
  

if option == "About":
  st.image("Team Mugshot.png", width = 750)
  st.markdown("<h4 style='text-align: left; color: black;'>At our core we are a data consultancy that uses data tools and strategies deliver custom data solutions to your business problems.</h4>", unsafe_allow_html=True)
  st.write("")            
  st.markdown("<h4 style='text-align: left; color: black;'>We partner with you as your data team, take the time to understand your business and how data can help you to achieve your goals.</h4>", unsafe_allow_html=True)
  st.write("")
  st.markdown("<h4 style='text-align: left; color: black;'>We use business analysis techniques to determine the best solution to your problem. Examples of our typical solutions are executive dashboards, machine learning models, data infrastructure (databases, API connections, and cloud set up), and web applications.</h4>", unsafe_allow_html=True)
  st.write("")
  st.markdown("<h4 style='text-align: left; color: black;'>We are three friends who identified a worldwide need for data solutions at competitive prices without comprimising on quality. We decided to combine our backgrounds in Programming, Machine Learning, Finance and Economics to help build a team to meet this need.</h4>", unsafe_allow_html=True)

if option == "Analytics":
    st.markdown("<h4 style='text-align: left; color: black;'>Breaking down Customer Acquisition Cost (CAC) to investigate marketing performance</h4>", unsafe_allow_html=True)
    st.write("")     
    st.markdown("<iframe src="https://datastudio.google.com/embed/reporting/f48f602f-2542-4ad6-ad15-f1bc9c6a6ff1/page/p_ex3znh92oc" frameborder="0" style="border:0" allowfullscreen></iframe>", unsafe_allow_html=True)
  
#if option == "Data Infrastructure:
  
if option == "Machine Learning":
  st.image("Doggo.jpg")
  st.markdown("<h2 style='text-align: center; color: black;'>PetTech Company</h2>", unsafe_allow_html=True)
  st.write("")
  st.markdown("<h5 style='text-align: left; color: black;'>For this project we were tasked with using the raw data from a 3-axis accelerometer and a 3-axis gyroscope to classify the postion of a dog.</h5>", unsafe_allow_html=True)
  st.write("")
  st.markdown("<h5 style='text-align: left; color: black;'>For this use case our algorithim was required to be embedded on a device worn around the dogs neck from which various outputs would alert the dogs owner to any abnormal behaiviour (i.e Lying on side for too long).</h5>", unsafe_allow_html=True)
  
  st.write("---------")
  
  st.markdown("<h2 style='text-align: center; color: black;'>Data Gathering and Cleaning</h2>", unsafe_allow_html=True)
  st.write("")
  st.markdown("<h5 style='text-align: left; color: black;'>A crucial part of any Machine Laerning Project is data.</h5>", unsafe_allow_html=True)
  st.write("")
  st.markdown("<h5 style='text-align: left; color: black;'>In this example we were able to obtain a publically available dataset (see link to paper). We went through the appropriate data cleaning methodology and arrived at our dataframe which you can see below.</h5>", unsafe_allow_html=True)
  st.write("")
  st.markdown("<h5 style='text-align: left; color: black;'>We now had data with which to classify a dog into one of six positions (Sitting, Walking, Standing, Running, Lying down and Eating and drinking).</h5>", unsafe_allow_html=True)
  
  
  @st.cache(allow_output_mutation=True)
  def load_data():
   a = pd.read_csv("dog_data (1).csv")
   return a
    
  df = load_data()
  st.checkbox("Click to Expand DataFrame", value=False, key="use_container_width")  
  st.dataframe(df, use_container_width=st.session_state.use_container_width)
 
    
  st.markdown("<h2 style='text-align: center; color: black;'>Model Selection</h2>", unsafe_allow_html=True)
  st.image("machine-learning-cheet-sheet-2.png", width = 700, caption = "Due to the nature of this project (High-level of accuracy in classification required) we chose the XGBoost and Decision Tree Models")
  
  st.write("---------")
  
  
  st.markdown("<h2 style='text-align: center; color: black;'>Model Outcomes</h2>", unsafe_allow_html=True)
  st.markdown("<h3 stayle='text-align: left; color: black;'>A Classification report is used to measure the quality of predictions from a classification algorithm. How many predictions are True and how many are False.</h3>", unsafe_allow_html=True) 
  st.markdown("<h3 stayle='text-align: left; color: black;'>More specifically, True Positives, False Positives, True negatives and False Negatives are used to predict the metrics of a classification report as shown below.</h3>", unsafe_allow_html=True)
  st.markdown("<h4 style='text-align: left; color: black;'>🎯 Precision – What percent of your predictions were correct?</h4>", unsafe_allow_html=True)
  st.markdown("<h4 style='text-align: left; color: black;'>🎯 Recall – What percent of the positive cases did you catch?</h4>", unsafe_allow_html=True)
  st.markdown("<h4 style='text-align: left; color: black;'>🎯 F1 score – What percent of positive predictions were correct?</h4>", unsafe_allow_html=True)
  st.markdown("<h4 style='text-align: left; color: black;'>🎯 Support - How many predictions in each case</h4>", unsafe_allow_html=True)

  st.write("")
  st.markdown("<h2 style='text-align: center; color: black;'>XGBoost Model Results</h2>", unsafe_allow_html=True)
  st.markdown("<h4 style='text-align: left; color: black;'>The results after using the XGBoost Algorithm can be seen below. Overall accuracy 83%.</h4>", unsafe_allow_html=True)
  
   
  
  st.image("XGBoost Classification Report.png", width = 800)
  st.image("XGBoost.png", width = 700)

 
  st.markdown("<h2 style='text-align: center; color: black;'>Decision Tree Model Results</h2>", unsafe_allow_html=True)

  
  st.markdown("<h4 style='text-align: left; color: black;'>The results after using the Decision Tree Algorithm can be seen below. <strong>Overall accuracy 87%<strong>. We selected this model due to its advantages in SPEED and ACCURACY.</h4>", unsafe_allow_html=True)
  
  st.image("Decision Tree Classification Report.png", width = 800)
  st.image("Decision_Tree.png", width = 700)
  
  st.write("---------")
  
  st.markdown("<h2 style='text-align: center; color: black;'>Challenges</h2>", unsafe_allow_html=True) 
    
  st.markdown("<h4 style='text-align: left; color: black;'>❓ Speed – As we used the python ecosystem for our algorithms we needed to convert our decision tree into C so that it could run more effectively on device?</h4>", unsafe_allow_html=True)
  st.markdown("<h4 style='text-align: left; color: black;'>❓ Memory – Another constraint was the memory of the device on which our model needed to run. We needed to simplify our DT model using max_depth to solve this issue</h4>", unsafe_allow_html=True)
  st.markdown("<h4 style='text-align: left; color: black;'>❓ Data Collection – Labelled video data of dogs in different positions proved difficult and time consuming to create. We addressed this by sourcing trained dogs and following a strict data collection methodology</h4>", unsafe_allow_html=True)
  st.markdown("<h4 style='text-align: left; color: black;'>❓ Positions - As we needed to classify the dog in several different positions, we needed to use filters to stop the readings from the device resulting in the over classification of certain positions</h4>", unsafe_allow_html=True)

  
  st.write("---------")
  
  st.markdown("<h2 style='text-align: center; color: black;'>Video Walkthrough</h2>", unsafe_allow_html=True) 

  st.write("Check out our work here [link](https://colab.research.google.com/drive/1sjGgWWfqmBHteGup-PGr0A4XKCkhl8ZR?hl=en#scrollTo=xG55BCrpIwqk)")

  st.write("---------")  
  
if option == "Custom Web Apps":
    st.markdown("<h2 style='text-align: center; color: black;'>INVESTMENT GROWTH CALCULATOR</h2>", unsafe_allow_html=True)
    st.write("")
    st.markdown("<h4 style='text-align: left; color: black;'>For this project we were tasked with creating a simple, affordable investment calculator as a sales tool that could be embedded on a companies website.</h4>", unsafe_allow_html=True)
  #top image
    st.image("thin.png")
    #link back to website
    st.write("Return to the bayswatercapital [website](https://bayswatercapital.co.za/)")
        
    #lists and dictionaries we need
    conv_currency_list = ['USD','EUR','GBP', 'HKD', 'JPY','CAD','CHF','NZD','ZAR']
    escalate_dict ={'No Increase':0.0,'2.5%':0.025, '5%':0.05, '7.5%':0.075, '10%':0.1, '15%':0.15, '20%':0.2}
    frequency ={'Monthly':12,'Quarterly':4,'Annually':1}
    # layout of the actual app, all in one form 
    # with lots of columns on top of each other


    #first row of  two columns
    col1row1, col2row1 = st.columns(2)
    with col1row1: 
        start_age = st.number_input('Enter your starting age: ',value = 0)
    with col2row1: 
        retirement_age = st.number_input('Enter your retirement age: ', value = 0)
        years = retirement_age-start_age
        

    #2nd row of two columns
    col1row2, col2row2 = st.columns(2)
    with col1row2:
        st.markdown('##')
        st.write("Your investment time horizon: ", years)

    with col2row2:
        per_year = st.selectbox("How many times would you like to contribute per year?",['Monthly', 'Quarterly', 'Annually'])
        m= frequency[per_year]

    #3rd row of two columns
    col1row3,col2row3 = st.columns(2)

    with col1row3:
        rate = st.slider('Select annual growth rate',min_value=0.0, max_value=15.0, value=0.0, step=0.1,format="%f %%") 
        rate_converted = rate/100 # is this correct ?? 
    with col2row3: 
        inflation = st.slider('Select expected inflation over the period',min_value=0.0, max_value=15.0, value=0.0, step=0.1,format="%f %%") 
    #writing under row 3
    st.write(f"You expect your investment to grow at a rate of **{round(rate,2)}%** but taking inflation into account the real return will be **{round(rate-inflation,2)}%**")
    inflation_adjusted_rate = (rate - inflation)/100 # use this amount for the extra sentence

    #4th row of two columns
    col1row4,col2row4 =st.columns(2)
    with col1row4:
        deposit = st.number_input('Starting Deposit (R): ',value=0,step=100)
    with col2row4:
        monthly = st.number_input(f'Your {per_year}  Contribution (R): ',value=0,step=100)


    #5th row of two columns
    col1row5,col2row5 =st.columns(2)
    with col1row5:
        escalatep = st.selectbox("Select annual % increase of contribution",['No Increase','2.5%','5%','7.5%','10%','15%','20%'])
    with col2row5:
        conv_currency_selector = st.selectbox('Select target currency to convert to', conv_currency_list)

    #6th row of two columns
    col1row6,col2row6 = st.columns(2)
    with col1row6:
        if m!=1:
            cap_contribution = st.radio("Would you like to cap your contribution?",['No',f'Yes - set a {per_year} cap', 'Yes - set an Annual cap'])
        else: 
            cap_contribution =st.radio("Would you like to cap your contribution?",['No', 'Yes - set an Annual cap'])
        
    with col2row6:
        max_annual_contribution = 0
        if cap_contribution == f"Yes - set a {per_year} cap":
            max_contribution = st.number_input(f'Maximum {per_year} Contribution: ',value =0,step=100)
            max_annual_contribution = max_contribution*m
        elif cap_contribution == "Yes - set an Annual cap":
            max_annual_contribution = st.number_input('Maximum Annual Contribution: ',value=0,step=100)
          
    if max_annual_contribution == 0:
        max_annual_contribution = 1000000000000

        

    pressed = st.button("Calculate")

    growth_rate = rate_converted
    #rate =growth_rate # HEY ? 
    escalate = float(escalate_dict[escalatep]) # fetch the correct format from the dictionary


    # NEWEST FORMULA
    def calculate_attempt_88(years,rate,escalate,deposit,monthly,m):
        accumulated_capital=[]
        accumulated_interest=[]
        amounts=[]
        #contributions=[]
        #base = []
        monthlyesc = monthly
        #escalation=0
        capital = 0
        ann_fv = 0
        escalation = escalate + 1 # change it from 0.1 to 1.1 for example
        extra_deposit = 0

        for x in range(years):
            x+=1
            dep_fv = (deposit + extra_deposit)*((1+(rate/m))**(m)) # calculate the flat interest
            ann_fv = (monthlyesc/(rate/m))*(((1+(rate/m))**(m))-1) # calculate annuity
            
            extra_deposit = ann_fv + dep_fv# add to deposit in year 2 
            
            if x == 1:
                capital = deposit + (monthlyesc*m)    # increase capital after year 1
            else:
                capital = capital + (monthlyesc*m)    # increase capital for the other years
            
            monthlyesc = monthlyesc*escalation #escalate The monthly contribution  
            if max_annual_contribution:
                    if monthlyesc*m >= max_annual_contribution:   # if it's greater than the max then it get's changed back to the max
                        monthlyesc = max_annual_contribution/m

          
            total_fv = dep_fv + ann_fv # get the total future value for our list
            interest = total_fv - capital # get interest portion
            total_fv = round(total_fv,2) 
            amounts.append(total_fv)     # append to all the lists
            accumulated_capital.append(capital)
            accumulated_interest.append(interest)
            
        return amounts,accumulated_capital,accumulated_interest




    if pressed:
        
        if monthly == 0:
            st.error("please input in your contribution amount")
        elif retirement_age == 0 or years < 1:
            st.error("please input correct retirement and starting age")
        elif max_annual_contribution/m < monthly:
            st.error("your maximum contribution is lower than your periodic contribution")
        else:
            amounts,accumulated_capital,accumulated_interest = calculate_attempt_88(years,growth_rate,escalate,deposit,monthly,m)
            amount_after_inf, accumulated_capital_after_inf,accumulated_interest_after_inf = calculate_attempt_88(years,inflation_adjusted_rate,escalate,deposit,monthly,m)
            #st.balloons() 
            # st.write("ann fv",ann_fv, "dep_fv",dep_fv,"total",amounts,"capital",accumulated_capital,"interest",accumulated_interest)

            amounts_rounded = [round(num, 2) for num in amounts]
            acc_cap = [round(num, 2) for num in accumulated_capital]
            acc_int = [round(num, 2) for num in accumulated_interest]

            final_data = pd.DataFrame(list(zip(acc_cap, acc_int,amounts_rounded,range(1,len(amounts_rounded)+1))),columns=['Capital Contribution','Investment Growth','Total','Year'])
            
            base_price_unit = "ZAR"   
            
            def load_data():
                url = f'https://api.apilayer.com/exchangerates_data/convert?to={conv_currency_selector}&from={base_price_unit}&amount={amounts[-1]}'
                
                payload = {}
                headers= {
                    "apikey": "WcqtBq92HnXahaiGoCV22XcgA8oY15pj"
                  }

                response = requests.request("GET", url, headers=headers, data = payload)
              # status_code = response.status_code
                data = response.json()
                return data
            def formatter(raw_number):
                return "{:,}".format(raw_number)
            df = load_data()
            converted = df['result']
            converted= round(converted,2)
            converted = formatter(converted)
            ireturn = (acc_int[-1]/acc_cap[-1])
            ireturn = f"{ireturn:.0%}"
            
            # convert all of them to nice looking numbers e.g 1000000 => 100,000
            monthly = formatter(monthly)
            deposit = formatter(deposit)
            final_amount = formatter(amounts[-1])
            final_interest = formatter(acc_int[-1])
            final_cap = formatter(acc_cap[-1])
            final_inf_adjusted_return = formatter(amount_after_inf[-1])
            
            # make growth rate nicer to read
            display_rate = round(growth_rate*100,1)

            st.header('Your Investment Value')
            st.write(f" If you desposit **R{deposit}** and contribute **R{monthly}**,  **{m}** times a year with an annual escalation of **{escalatep}**,  at a growth rate of **{display_rate}%**, your investment will generate **R{final_amount}**  in **{years}** years.")
            st.write(f"Taking an expected inflation rate of **{inflation}%** into account, your real investment value will be **R{final_inf_adjusted_return}**")
            st.write(f"The converted value of your investment is:  **{conv_currency_selector}** **{converted}** at a rate of **{df['info']['rate']}** ")
            st.write(f" You will earn earn **R{final_interest}**  on your capital contribution of **R{final_cap}**  which is a return of **{ireturn}**")


            stacked_bar = final_data[['Investment Growth','Capital Contribution','Year']]
            new_stacked = stacked_bar.melt('Year', var_name='Key', value_name='Amount')
            
            # write the new bar chart here
            
            Key_dict = {
                    'Capital Contribution': "#DDC385", 
                    'Investment Growth': "#0D1A34", 
        
                                }

            new_stacked['Color'] = new_stacked['Key'].map(Key_dict)

            domain = ['Capital Contribution','Investment Growth']
            range_ = ["#DDC385","#0D1A34"]
            order_bars = ['Investment Growth','Capital Contribution']
            c = alt.Chart(new_stacked).mark_bar().encode(
                x='Year:O',
                y='Amount',
                tooltip= ["Key","Amount"],
                color=alt.Color('Key',scale=alt.Scale(domain=domain,range=range_)),
                order=alt.Order('Key:Q')
                )
            st.altair_chart(c,use_container_width=True)
