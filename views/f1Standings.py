import  streamlit as st
import controllers.f1Controller as f1

def getStandings(driverStandings, constructorStandings):
    drivers, constructors = st.columns(2)
    
    allDrivers = f""""""

    for driver in driverStandings:
        allDrivers += f"""<tr>
                <th>{driver[2]}</th>
                <td>{getConstructorBadge(driver[3])} <div style="display: inline-block; padding-left: 5px">{driver[0]}</div></td>
                <td>{driver[1]}</td>
            </tr>
        """
        
    allConstructors = f""""""

    for constructor in constructorStandings:
        allConstructors += f"""<tr>
                <th>{constructor[2]}</th>
                <td>{getConstructorBadge(constructor[3])} <div style="display: inline-block; padding-left: 5px">{constructor[0]}</div></td>
                <td>{constructor[1]}</td>
            </tr>
        """
    
    with drivers:
        st.markdown(f"""
        <style>
            th, tbody, tr, td {{
                border: none!important;
            }}
            .team-box {{
                display: flex;
                justify-content: center;
                align-content: center;
                width: 34px;
                height: 24px;
                font-family: "Source Sans Pro", sans-serif;
                font-size: 0.8rem;
                font-weight: 700;
                color: white;
                border-radius: 3px;
                flex-direction: column;
                text-align: center;
                padding: 2px 4px 2px 4px;
                display: inline-block;
            }}
            .RED {{
                background-color: #3b78c6;;
            }}
            .MER {{
                background-color: #6cd3bf;
            }}
            .FER {{
                background-color: #fb1d3c;
            }}
            .MCL {{
                background-color: #f48629;
            }}
            .ALT {{
                background-color: #5d8cac;
            }}
            .ALP {{
                background-color: #2293d1;
            }}
            .AST {{
                background-color: #358c75;
            }}
            .ALF {{
                background-color: #c92d4b;
            }}
            .WIL {{
                background-color: #37bedd;
            }}
            .HAA {{
                background-color: #b6babd;
            }}
        </style>
        <section style="width: 25vw; padding-bottom: 5vh">
            <table>
                <tbody>
                    {allDrivers}
                
        </section>""", unsafe_allow_html=True)
    
    with constructors:
        st.markdown(f"""
        </style>            
        <section style="width: 25vw; padding-bottom: 5vh">
            <table>
                <tbody>
                    {allConstructors}
                
        </section>""", unsafe_allow_html=True)
        
def getConstructorBadge(constructorId):
    if constructorId == "red_bull":
        team = "RED"
    elif constructorId == "ferrari":
        team = "FER"
    elif constructorId == "mclaren":
        team = "MCL"
    elif constructorId == "mercedes":
        team = "MER"
    elif constructorId == "alpine":
        team = "ALP"
    elif constructorId == "alfa":
        team = "ALF"
    elif constructorId == "haas":
        team = "HAA"
    elif constructorId == "alphatauri":
        team = "ALT"
    elif constructorId == "aston_martin":
        team = "AST"
    elif constructorId == "williams":
        team = "WIL"
    
    constructorBadge = f"""<div class="team-box {team}">{team}</div>"""
    return constructorBadge