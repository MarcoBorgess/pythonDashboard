import  streamlit as st
import controller.f1Controller as f1

def getStandings():
    drivers, constructors = st.columns(2)

    driverStandings = f1.getDriverStandings()
    constructorStandings = f1.getConstructorStandings()
    

    allDrivers = f""""""

    for driver in driverStandings:
        allDrivers += f"""<tr>
                <th>{driver[2]}</th>
                <td>{driver[0]}</td>
                <td>{driver[1]}</td>
            </tr>
        """
        
    allConstructors = f""""""

    for constructor in constructorStandings:
        allConstructors += f"""<tr>
                <th>{constructor[2]}</th>
                <td>{constructor[0]}</td>
                <td>{constructor[1]}</td>
            </tr>
        """
    
    with drivers:
        st.markdown(f"""
        <style>
            th, tbody, tr, td {{
                border: none!important;
            }}
        </style>            
        <section style="width: 25vw; padding-bottom: 5vh">
            <table>
                <tbody>
                    {allDrivers}
                
        </section>""", unsafe_allow_html=True)
    
    with constructors:
        st.markdown(f"""
        <style>
            th, tbody, tr, td {{
                border: none!important;
            }}
        </style
        </style>            
        <section style="width: 25vw; padding-bottom: 5vh">
            <table>
                <tbody>
                    {allConstructors}
                
        </section>""", unsafe_allow_html=True)