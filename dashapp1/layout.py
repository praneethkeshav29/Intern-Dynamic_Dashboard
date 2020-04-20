import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import plotly.graph_objs as go
import urllib.request, json
from collections import Counter

############################ BOOT STRAP #############################################################
navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Help", href="#")),
        dbc.DropdownMenu(
            id='drop',
            nav=True,
            in_navbar=True,
            label="Options",
            children=[
                dbc.DropdownMenuItem("Return to Workspace",href='http://localhost:5000/admin/'),
                dbc.DropdownMenuItem("logout",href='http://loclahost:5000/admin/logout'),
                dbc.DropdownMenuItem(divider=True),

            ],
        ),
    ],
    brand="CLINION",
    brand_href="#",
    sticky="top",
)

# STUDIES BY THERAPY - PIE CHART
try:
    areas = []
    with urllib.request.urlopen("http://ctmsapi.quad1test.com:8687/api/admin/studystatuscount?CompanyId=TEST%20PzMJ1Dv6") as url:
        totaldata = json.loads(url.read().decode())


    projectdata = totaldata["ProjectData"]
    for i in range(len(projectdata)):
        x = projectdata[i]
        areas.append(x.get("TherapeuticArea"))

    temp1 = Counter(areas)
    labels = list(temp1.keys())
    values = list(temp1.values())
    data_pie = [go.Pie(labels=labels, values=values, marker=dict(
        line=dict(color='#000000', width=1)))]
    layout_p = go.Layout(title='Studies by Therapy', autosize=False,
                         width=350,
                         height=400,
                         )

    fig_pie = go.Figure(data=data_pie, layout=layout_p)

    # STUDIES BY SPONSOR - BAR CHART
    sponsor = []
    for i in range(len(projectdata)):
        x = projectdata[i]
        sponsor.append(x.get("SponsorName"))

    temp2 = Counter(sponsor)
    labels_sbs = list(temp2.keys())
    values_sbs = list(temp2.values())
    trace_sbs = data = [go.Bar(
        x=labels_sbs,
        y=values_sbs,
        width=[0.3, 0.3, 0.3, 0.3],
        name='Studies by Sponsor'
    )]
    layout_sbs = go.Layout(
        title='Studies by Sponsor', autosize=False,
        width=300,
        height=400,
    )
    fig_sbs = go.Figure(data=trace_sbs, layout=layout_sbs)

    # STATUS GRAPH - BAR CHART

    ongoing = []
    completed = []
    cname = []
    with urllib.request.urlopen("http://ctmsapi.quad1test.com:8687/api/admin/studystatuscount?CompanyId=HETEROSInCc31") as url:
        data1 = json.loads(url.read().decode())

    for i in range(len(data1)):
        x = data1
        ongoing.append(x['OnGoing'])
        completed.append(x['CompletedprojectCount'])
        cname.append(x['ComapanyName'])
    trace_s1 = go.Bar(
        x=cname,
        y=ongoing,
        name='OnGoing',
        text='OnGoing',
        textposition='auto',
        marker=dict(
            color='rgb(15,150,225)',
            line=dict(

                width=1.5),
        ),
        opacity=0.5

    )

    trace_s2 = go.Bar(
        x=cname,
        y=completed,
        name='Completed Projects',
        text='Completed Count',
        textposition='auto',
        marker=dict(
            color='rgb(158,150,225)',
            line=dict(

                width=1.5),
        ),

    )

    status_data = [trace_s1, trace_s2]
    layout_s = go.Layout(
        title='Status Count Of Each Company', autosize=False,
        width=300,
        height=400,
        legend=dict(
            x=-0.8,
            y=1.2,
            traceorder='normal',
            font=dict(
                family='sans-serif',
                size=15,

            ),

        )
    )
    fig_sts = go.Figure(data=status_data, layout=layout_s)

    # FINANCIAL GRAPH
    prof = []
    acprof = []
    pas = []
    acpas = []

    studies = []

    for i in range(len(projectdata)):
        x = projectdata[i]
        prof.append(x['ProfessionalCost'])
        pas.append(x['PassthroughCost'])
        acprof.append(x['ActualProfessionalCost'])
        acpas.append(x['ActualPassThroughCost'])
        studies.append(x['StudyName'])

    y = prof
    y2 = acprof
    y3 = pas
    y4 = acpas
    trace1 = go.Bar(
        x=studies,
        y=prof,

        name='prof cost',
        text='prof cost',
        textposition='auto',
        marker=dict(
            color='rgb(57, 198, 170)',
            line=dict(width=1.5)
        ),

    )

    trace2 = go.Bar(
        x=studies,
        y=acprof,
        name='actual prof cost',
        text='actual prof cost',
        textposition='auto',
        marker=dict(
            color='rgb(179, 198, 194)',
            line=dict(

                width=1.5),
        ),
        opacity=0.6
    )
    trace3 = go.Bar(
        x=studies,
        y=pas,
        name='Passthrough Cost ',
        text='pas cost',
        textposition='auto',

        marker=dict(
            color='rgb(88, 140, 81)',
            line=dict(

                width=1.5),
        ),

    )
    trace4 = go.Bar(
        x=studies,
        y=acpas,
        name='actual Passthrough Cost',
        text='actual pas cost',
        textposition='auto',
        marker=dict(
            color='rgb(205, 232, 139)',
            line=dict(

                width=1.5),
        ),

    )

    trace_f = [trace1, trace2, trace3, trace4]
    layout_f = go.Layout(
        title='Financial Graphs', autosize=False,
        width=400,
        height=500,
        legend=dict(
            x=0.9,
            y=1.0,
            traceorder='normal',
            font=dict(
                family='sans-serif',
                size=15,

            )),
    )
    fig_f = go.Figure(data=trace_f, layout=layout_f)

    # TARGET ENROLLMENT STUDYWISE - GROUPED BAR
    target_enroll = []
    actual_enrol = []
    enrol_stud = []
    for i in range(len(projectdata)):
        x = projectdata[i]
        target_enroll.append(x['TargetEnrollment'])
        actual_enrol.append(x['ActualTargetEnrollment'])
        enrol_stud.append(x['StudyName'])

    ex = enrol_stud
    ey = target_enroll
    ey2 = actual_enrol

    trace_e1 = go.Bar(
        y=ex,
        x=ey,
        name='target ',
        width=[0.4, 0.4,0.4,0.4],
        text='target ',
        textposition='inside',
        orientation='h',
        marker=dict(
            color='rgb(64, 105, 170)',
            line=dict(width=1.0)
        ),

    )

    trace_e2 = go.Bar(
        y=ex,
        x=ey2,
        width=[0.4, 0.4,0.4,0.4],
        name='actual ',
        text='actual ',
        textposition='inside',
        orientation='h',
        marker=dict(
            color='rgb(6, 1, 68)',
            line=dict(

                width=1.0),
        ),

    )

    enroll_data = [trace_e1, trace_e2]
    layout_e = go.Layout(title='Enrollment Status', barmode='stack', autosize=False,
                         width=350,
                         height=500, yaxis=dict(titlefont=dict(family='Arial, sans-serif',size=18,color='lightgrey'
            ),showticklabels=True,
            tickangle=90,
            tickfont=dict(
                family='Old Standard TT, serif',
                size=14,
                color='black'
            )))
    enroll_fig = go.Figure(data=enroll_data, layout=layout_e)

    # SETERM COUNT
    sterm = []
    s_stud = []

    for i in range(len(projectdata)):
        x = projectdata[i]
        s_stud.append(x.get("StudyName"))
        sterm.append(x.get("SaeTermCount"))
    w = [0.5] * len(projectdata)
    trace_sterm = [go.Bar(
        x=s_stud,
        y=sterm,
        width=w,
        name='Studies by Sponsor', marker=dict(
            color='rgb(216, 158, 216)',
            line=dict(width=1.5)
        )
    )]
    layout_sterm = go.Layout(
        title='SeTerm Count', autosize=False,
        width=300,
        height=500,

    )
    fig_stm = go.Figure(data=trace_sterm, layout=layout_sterm, )

    # COMPLETED VISITS
    cvisits = []
    c_stud = []

    for i in range(len(projectdata)):
        x = projectdata[i]
        c_stud.append(x.get("StudyName"))
        cvisits.append(x.get("OnTimeCompletedVisit"))
    w = [0.5] * len(projectdata)
    trace_cvisits = [go.Bar(
        x=c_stud,
        y=cvisits,
        width=w,
        name='Study Name',
        marker=dict(
            color='rgb(239, 160, 168)',
            line=dict(width=1.5)
        )

    )]
    layout_cvisits = go.Layout(
        title='OnTimeCompletedVisit', autosize=False,
        width=300,
        height=500,

    )
    fig_cvs = go.Figure(data=trace_cvisits, layout=layout_cvisits, )

    # PROTOCOL DEVIATION COUNT
    pdc = []
    pd_stud = []

    for i in range(len(projectdata)):
        x = projectdata[i]
        pd_stud.append(x.get("StudyName"))
        pdc.append(x.get("PdCount"))
    w = [0.5] * len(projectdata)
    trace_pdc = [go.Bar(
        x=pd_stud,
        y=pdc,
        width=w,
        name='Study Name',
        marker=dict(
            color='rgb(154, 175, 209)',
            line=dict(width=1.5)
        )
    )]
    layout_pdc = go.Layout(
        title='Protocol Deviation Count', autosize=False,
        width=300,
        height=500,

    )
    fig_pdc = go.Figure(data=trace_pdc, layout=layout_pdc, )
    body = dbc.Container(
        [
            dbc.Row(
                [
                    dbc.Col(
                        [

                            dcc.Graph(id='Pie', figure=fig_pie, config={
                                'modeBarButtonsToRemove': ['pan2d', 'lasso2d'], "displaylogo": False
                            })
                        ],

                    ),
                    dbc.Col(
                        [

                            dcc.Graph(id='study by sponsor', figure=fig_sbs, config={
                                'modeBarButtonsToRemove': ['pan2d', 'lasso2d', 'zoom2d', 'select2d', 'autoScale2d'],
                                "displaylogo": False
                            }),
                        ]
                    ),
                    dbc.Col(
                        [
                            dcc.Graph(id='status', figure=fig_sts, config={
                                'modeBarButtonsToRemove': ['pan2d', 'lasso2d', 'zoom2d', 'select2d', 'autoScale2d'],
                                "displaylogo": False}),
                        ]
                    ),
                ]
            ),
            dbc.Row(
                [
                    dbc.Col(
                        [
                            dcc.Graph(id='Financial Status', figure=fig_f, config={
                                'modeBarButtonsToRemove': ['pan2d', 'lasso2d', 'zoom2d', 'select2d', 'autoScale2d'],
                                "displaylogo": False})

                        ],

                    ),
                    dbc.Col(
                        [
                            dcc.Graph(id='estack', figure=enroll_fig, config={
                                'modeBarButtonsToRemove': ['pan2d', 'lasso2d', 'zoom2d', 'select2d', 'autoScale2d',
                                                           'displaylogo'], 'displaylogo': False})
                        ]
                    ),
                    dbc.Col(
                        [
                            dcc.Graph(id='sterm', figure=fig_stm, config={
                                'modeBarButtonsToRemove': ['pan2d', 'lasso2d', 'zoom2d', 'select2d', 'autoScale2d'],
                                'displaylogo': False})
                        ]
                    ),
                ]
            ),
            dbc.Row(
                [

                    dbc.Col(
                        [
                            dcc.Graph(id='cvisits', figure=fig_cvs, config={
                                'modeBarButtonsToRemove': ['pan2d', 'lasso2d', 'zoom2d', 'select2d', 'autoScale2d'],
                                "displaylogo": False}),
                        ]
                    ),
                    dbc.Col(
                        [
                            dcc.Graph(id='pdcount', figure=fig_pdc, config={
                                'modeBarButtonsToRemove': ['pan2d', 'lasso2d', 'zoom2d', 'select2d', 'autoScale2d'],
                                "displaylogo": False}),
                        ]
                    ),
                ]
            ),
        ],
        className="mt-4",
    )
except:
    layout2 = html.Div("Exception raised in clinion dashboard. Please check if the link is working properly.")
# LAYOUT
layout2 = html.Div([navbar, body])
layout3 = html.Div("ERROR  ! YOU DON'T HAVE THIS PRODUCT")
layout4 = html.Div("welcome ctms")
