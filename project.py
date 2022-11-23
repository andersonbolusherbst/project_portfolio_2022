import streamlit as st
import pandas as pd
import numpy as np
import requests

st.image("Website.png")

option = st.sidebar.selectbox("HAB LABS Services", ('Analytics', 'Data Infrastructure','Machine Learning','Custom Web Apps'))

if option == "Custom Web Apps":
  
if option == "Custom Web Apps":
  
if option == "Custom Web Apps":
  
if option == "Custom Web Apps":
  env = Environment(loader=FileSystemLoader("."), autoescape=select_autoescape())
  template = env.get_template("template.html")

  st.image("thin.png")

  currency_list=currency_list = ['ZAR','USD','EUR','GBP', 'HKD', 'JPY','CAD','CHF','NZD']

  conv_currency_list = ['USD','EUR','GBP', 'HKD', 'JPY','CAD','CHF','NZD','ZAR']
  frequency ={'Monthly':12,'Quarterly':4,'Annual':1}
  max_annual_contribution =0
  max_contribution=0



  rates = {'1%':0.01,'2%':0.02,'3%':0.03,'4%':0.04,'5%':0.05,'6%':0.06,'7%':0.07,'8%':0.08,'9%':0.09,'10%':0.1}
  escalate_dict ={'0%':0.0,'2.5%':0.025, '5%':0.05, '7.5%':0.075, '10%':0.1, '15%':0.15, '20%':0.2}




  col1, col2 = st.columns(2)

  with col1:
      currency_selector = st.selectbox(
       'Which currency will you be investing with?',
       ('ZAR','USD','GBP','EUR','VND'))



  with col2:
      conv_currency_selector = st.selectbox('Select target currency to convert to', conv_currency_list)
  st.write("You're investing with:", currency_selector)  
  rate = st.selectbox('Select annual growth rate', ['1%','2%','3%','4%','5%','6%','7%','8%','9%','10%'])

  col4,col5 = st.columns(2)   
  with col4:
      start_age = st.number_input('Enter your starting age: ',value = 0)
      f = st.selectbox("How many times would you like to contribute per year?",['Monthly', 'Quarterly', 'Annual'])



  with col5:
      retirement_age = st.number_input('Enter your retirement age: ', value = 0)
      years = retirement_age-start_age
      st.markdown('##')
      st.write("Your investment time horizon: ", years)

      m= frequency[f]





  #rate = st.slider('Select annual growth rate',min_value=0.01, max_value=0.15)

  #percentage = f"{rate:.0%}"

  col3, col4 = st.columns(2)
  with col3:
      deposit = st.number_input('Starting Deposit')
      cap_contribution = st.radio("Would you like to cap your contribution?",['Yes - set a monthly cap', 'Yes - set an annual cap','No'])
      if cap_contribution == "Yes - set a monthly cap":
          max_contribution = st.number_input('Maximum Monthly Contribution: ')
      elif cap_contribution == "Yes - set an annual cap":
          max_annual_contribution = st.number_input('Maximum Annual Contribution: ')
      email_choice = st.radio("Would you like to send info to your email address?",["No","Yes"])

  with col4:
      monthly = st.number_input(f'Your {f}  Contribution')
      escalatep = st.selectbox("Select annual % increase of contribution",['0%','2.5%','5%','7.5%','10%','15%','20%'])
      if email_choice == "Yes":
          email_address = st.text_input("Send to: ")

  escalate = float(escalate_dict[escalatep])





  escalation=0

  if max_contribution == 0:
      max_contribution = 1000000000000
  else:
      max_contribution = max_contribution

  if max_annual_contribution == 0:
      max_annual_contribution = 1000000000000000000
  else:
      max_annual_contribution = max_annual_contribution
  pressed = st.button("Calculate")
  amounts=[]
  growth_rate = rate
  rate =rates[rate]
  accumulated_capital=[]
  accumulated_interest=[]
  capital = 0
  monthlyesc = monthly

  def calculate(years,rate,escalation,escalate,deposit,monthly,m, capital,monthlyesc):
      for x in range(years):
          x += 1
          if rate == escalate:
              ann_fv = monthly*(m*x)*(1+(rate/m))**((x*m)-1)
              dep_fv = deposit*(1+(rate/m))**(x*m)
          else:
              ann_fv = monthly *(((1+(rate/m))**(x*m)-(1+(escalate/m))**(x*m))/((rate/m)-(escalate/m)))
              dep_fv = deposit*(1+(rate/m))**(x*m)

          total_fv = dep_fv + ann_fv
          escalation = escalate+1


          if monthlyesc > max_contribution:
              monthlyesc = max_contribution
              continue_calculation(amounts,accumulated_capital,accumulated_interest,x,total_fv,years,rate,escalation,escalate,monthly,m, capital,monthlyesc,max_contribution)
              break
          else:
              monthlyesc = monthlyesc

          if x == 1:
              capital = deposit + (monthly*m)
              monthlyesc = monthlyesc * escalation
          else:
              capital = capital + (monthlyesc*m)
              monthlyesc = monthlyesc * escalation

          interest = total_fv - capital
          total_fv = round(total_fv,2)
          amounts.append(total_fv)
          accumulated_capital.append(capital)
          accumulated_interest.append(interest)
          year_string.append(f" Year {x}")

      return amounts,accumulated_capital,accumulated_interest


          #previous formula
  #             x += 1

  #             if x == 1:
  #                 capital = deposit + (monthly*m)
  #                 dep_fv = deposit*(1+(rate/m))**(x*m)
  #                 ann_fv = monthly*(((1+rate/m)**(x*m)-1)/(rate/m))
  #             else:
  #                 if monthly >= max_contribution:
  #                     monthly = max_contribution
  #                 else:
  #                     monthly = monthly*escalation
  #                 capital = (monthly*m)+capital
  #                 dep_fv = deposit*(1+(rate/m))**(x*m)
  #                 ann_fv = monthly*(((1+rate/m)**(x*m)-1)/(rate/m))

  #             total_fv = dep_fv + ann_fv
  #             interest = total_fv - capital
  #             total_fv = round(total_fv,2)
  #             amounts.append(total_fv)
  #             accumulated_capital.append(capital)
  #             accumulated_interest.append(interest)
  #             escalation = escalate+1

              #monthly = monthly*escalation



  if pressed:
      #@st.cache
      year_string = []
      if monthly == 0:
          st.error("please input in your contribution amount")
      elif retirement_age == 0 or years < 1:
          st.error("please input correct retirement and starting age")
      else:
          calculate(years,rate,escalation,escalate,deposit,monthly,m,capital,monthlyesc)
          st.balloons()

          #st.header("Annuity Table")

          amounts_rounded = [round(num, 2) for num in amounts]
          acc_cap = [round(num, 2) for num in accumulated_capital]
          acc_int = [round(num, 2) for num in accumulated_interest]

          final_data = pd.DataFrame(list(zip(acc_cap, acc_int,amounts_rounded)),columns=['Capital','Interest','Total'])
          #final_data = final_data.T
          #st.dataframe(final_data)
          # Retrieving currency data from ratesapi.io
          # https://api.ratesapi.io/api/latest?base=AUD&symbols=AUD
          base_price_unit = currency_selector   
          #@st.cache
          def load_data():
              url = f'https://api.apilayer.com/exchangerates_data/convert?to={conv_currency_selector}&from={base_price_unit}&amount={amounts[-1]}'
              #url = 'https://api.apilayer.com/exchangerates_data/symbols'
              payload = {}
              headers= {
                  "apikey": "WcqtBq92HnXahaiGoCV22XcgA8oY15pj"
                }

              response = requests.request("GET", url, headers=headers, data = payload)
             # status_code = response.status_code
              data = response.json()
              return data

          df = load_data()
          converted = df['result']
          converted= round(converted,2)
          ireturn = (acc_int[-1]/acc_cap[-1])
          ireturn = f"{ireturn:.0%}"

          st.header('Your Investment Value')
          st.write(f" If you invest **{monthly}** **{currency_selector}**,  **{m}** times a year with an annual escalation of **{escalatep}**, with a desposit of **{deposit}** **{currency_selector}** at a growth rate of **{growth_rate}**, your investment will generate **{amounts[-1]}** **{currency_selector}** in **{years}** years.")
          st.write(f"The converted value of your investment is: **{converted}** **{conv_currency_selector}** at a rate of **{df['info']['rate']}** in **{years}** years.")
          st.write(f" You will earn earn **{acc_int[-1]}** **{currency_selector}** on your capital contribution of **{acc_cap[-1]}** **{currency_selector}** which is a return of **{ireturn}**")


          stacked_bar = final_data[['Capital','Interest',]]
          st.bar_chart(stacked_bar)

          if email_choice =="Yes":
              send_email(st.secrets["email_secret"]["password"][0],monthly,m,escalation,amounts,years,escalatep,deposit,acc_int,acc_cap,ireturn,converted,df,conv_currency_selector,growth_rate,email_address,max_contribution,currency_selector)

  #         html = template.render(
  #             monthly=monthly,
  #             currency_selector=currency_selector,
  #             escalation=escalation,
  #             m=m,
  #             years=years,
  #             escalate=escalate,
  #             rate=rate,
  #             deposit=deposit,
  #             amounts=amounts,
  #             year_string=year_string,
  #             date=date.today().strftime("%B %d, %Y"),
  #             )

  #         pdf = pdfkit.from_string(html, False)
  #         st.balloons()

  #         st.download_button(
  #             "⬇️ Download PDF",
  #             data=pdf,
  #             file_name="calculation.pdf",
  #             mime="application/octet-stream",
  #          )



          #decimal_data = final_data.iloc[:, 0]
          #decimal_data = np.round(decimal_data, decimals = 2)


