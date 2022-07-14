# COLOR PALETTE = https://coolors.co/0e1117-262730-7cea9c-537a5a-1c7c54

def getF1Card(eventTitle, eventStartTime):

    card = f"""
    <head>
        <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
        <script src="https://cdn.jsdelivr.net/npm/popper.js@1.14.7/dist/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    </head>
    <style>
        

        .card-49 {{
            position: relative;
            display: flex;
            flex-direction: column;
            min-width: 0;
            word-wrap: break-word;
            background-color: #262730;
            background-clip: border-box;
            border: 1px solid #0e1117;
            border-radius: 8px;
        }}

        .widget-49 .widget-49-title-wrapper {{
            display: flex;
            align-items: center;
        }}

        .widget-49 .widget-49-title-wrapper .widget-49-date-success {{
            display: flex;
            align-items: center;
            justify-content: center;
            flex-direction: column;
            background-color: #7cea9c;
            width: 4rem;
            height: 4rem;
            border-radius: 50%;
        }}

        .widget-49 .widget-49-title-wrapper .widget-49-date-success .widget-49-date-day {{
            color: #1c7c54;
            font-weight: 900;
            font-size: 1.5rem;
            line-height: 1;
        }}

        .widget-49 .widget-49-title-wrapper .widget-49-date-success .widget-49-date-month {{
            color: #1c7c54;
            line-height: 1;
            font-size: 1rem;
            font-weight: 500;
            text-transform: uppercase;
        }}

        .widget-49 .widget-49-title-wrapper .widget-49-meeting-info {{
            display: flex;
            flex-direction: column;
            margin-left: 1rem;
        }}

        .widget-49 .widget-49-title-wrapper .widget-49-meeting-info .widget-49-pro-title {{
            color: #fafafa;
            font-size: 14px;
        }}

        .widget-49 .widget-49-title-wrapper .widget-49-meeting-info .widget-49-meeting-time {{
            color: #B1BAC5;
            font-size: 13px;
        }}
    </style>
    <body>
        <div class="container">
            <div class="row">
                <div class="col-lg-3 pl-0">
                    <div class="card-49 card-margin">
                        <div class="card-body">
                            <div class="widget-49">
                                <div class="widget-49-title-wrapper">
                                    <div class="widget-49-date-success">
                                        <span class="widget-49-date-day">22</span>
                                        <span class="widget-49-date-month">apr</span>
                                    </div>
                                    <div class="widget-49-meeting-info">
                                        <span class="widget-49-pro-title">{eventTitle}</span>
                                        <span class="widget-49-meeting-time">{eventStartTime}</span>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="col-lg-3 pl-0">
                    <div class="card-49 card-margin">
                        <div class="card-body">
                            <div class="widget-49">
                                <div class="widget-49-title-wrapper">
                                    <div class="widget-49-date-success">
                                        <span class="widget-49-date-day">22</span>
                                        <span class="widget-49-date-month">apr</span>
                                    </div>
                                    <div class="widget-49-meeting-info">
                                        <span class="widget-49-pro-title">{eventTitle}</span>
                                        <span class="widget-49-meeting-time">{eventStartTime}</span>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="col-lg-3 pl-0">
                    <div class="card-49 card-margin">
                        <div class="card-body">
                            <div class="widget-49">
                                <div class="widget-49-title-wrapper">
                                    <div class="widget-49-date-success">
                                        <span class="widget-49-date-day">22</span>
                                        <span class="widget-49-date-month">apr</span>
                                    </div>
                                    <div class="widget-49-meeting-info">
                                        <span class="widget-49-pro-title">{eventTitle}</span>
                                        <span class="widget-49-meeting-time">{eventStartTime}</span>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </body>
    """
    return card
    
