import databaseop as op
from flask import Flask, url_for, redirect, render_template, request, abort
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security, SQLAlchemyUserDatastore, \
    UserMixin, RoleMixin, login_required, current_user, roles_accepted
import flask_admin
from flask_admin.contrib import sqla
from flask_admin import helpers as admin_helpers
from flask_admin import expose, AdminIndexView
import dash_bootstrap_components as dbc
import dash
from werkzeug.wsgi import DispatcherMiddleware
from werkzeug.serving import run_simple
from dashapp1.layout import layout2, layout3, layout4
# Create Flask application
app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)

# Define models

roles_users = db.Table(
    'roles_users',
    db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
    db.Column('role_id', db.Integer(), db.ForeignKey('role.id'))
)


class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

    def __str__(self):
        return self.name


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Integer)
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary=roles_users, backref=db.backref('users', lazy='dynamic'))

    def __str__(self):
        return self.email


# Setup Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)


# Create customized model view class
class MyModelView(sqla.ModelView):

    def is_accessible(self):
        if not current_user.is_active or not current_user.is_authenticated:
            return False

        if current_user.has_role('superuser'):
            # edit_modal = False
            return True

        return False

    def _handle_view(self, name, **kwargs):
        """
        Override builtin _handle_view in order to redirect users when a view is not accessible.
        """
        if not self.is_accessible():
            if current_user.is_authenticated:
                # permission denied
                abort(403)
            else:
                # login
                return redirect(url_for('security.login', next=request.url))

    can_edit = True
    edit_modal = False
    create_modal = False
    can_export = True
    can_view_details = True
    details_modal = True


class UserView(MyModelView):
    column_editable_list = ['email', 'first_name', 'last_name']  # ,'webapiurl','mysqlurl','sqlserverurl']
    column_searchable_list = column_editable_list
    column_exclude_list = ['password']
    form_excluded_columns = []
    column_details_exclude_list = ['password']
    column_filters = column_editable_list


# Admin Home view

class CustomView(AdminIndexView):
    @expose('/')
    def index(self):
        try:
            op.getavailableproducts()
            l = []
            if current_user.id:
                l = op.getroles(current_user.id)
                li = l.copy()
                dashapp1.layout = layout3
                dash_app2.layout = layout3
            if 'clinion' in li:
                dashapp1.layout = layout2
            if 'ctms' in li:
                dash_app2.layout = layout4
            else:
                dashapp1.layout = layout3
                dash_app2.layout = layout3
        except:
            pass
        return self.render('admin/custom_index.html', l=l)


# Create admin url
admin = flask_admin.Admin(app, 'Dashboard', index_view=CustomView(
    name='My Workspaces',
    template='my_master.html',
    url='/admin'
), template_mode='bootstrap3',
                          )

# Add model views
admin.add_view(MyModelView(Role, db.session, menu_icon_type='fa', menu_icon_value='fa-server', name="Workspaces"))
admin.add_view(UserView(User, db.session, menu_icon_type='fa', menu_icon_value='fa-users', name="Users"))


# admin.add_view(
# CustomView(name="My Workspaces", endpoint='custom', menu_icon_type='fa', menu_icon_value='fa-connectdevelop', ))

# Flask views
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/admin/dashboard/<product>', methods=["GET"])
@login_required
def dashboard(product=None):
    usr = op.getroles(current_user.id)
    adm = op.getadminrole(current_user.id)
    if product is None:
        return render_template('admin/404.html',adm=adm),404
    if product in usr:
        l = op.urlproducts()
        if product in l:
            num = l.index(product)
        url = op.getsourceurl(current_user.id,num)
        if not url:
            return render_template('admin/dashboard.html', adm=adm, product=product, url='no')
        return render_template('admin/dashboard.html', adm=adm,product=product,url=url[0])
    else:
        return render_template('admin/404.html', adm=adm), 404


@app.route('/admin/datasource/<product>', methods=["GET","POST"])
@login_required
def datasource(product=None):
    if request.method == "GET":
        usr = op.getroles(current_user.id)
        adm = op.getadminrole(current_user.id)
        if product is None:
            return render_template('admin/404.html',adm=adm),404
        if product in usr:
            return render_template('admin/datasource.html', adm=adm,product=product)
        else:
            return render_template('admin/404.html', adm=adm), 404
    else:
        curr = str(current_user.id)
        product = request.url.rsplit('/', 1)[1]
        l = op.urlproducts()
        if product in l:
            num = l.index(product)
        idd = op.checkid(curr, num)
        if not idd:
            op.createidd(curr, num)
        if 'webapi' in request.form:
            op.upwebapi(curr, request.form, num)
        elif 'mysql' in request.form:
            op.upmysql(curr, request.form, num)
        elif 'sqlserver' in request.form:
            op.upsqlserver(curr, request.form, num)
        adm = op.getadminrole(current_user.id)
        return render_template('admin/datasource.html', adm=adm, product=product)


@app.errorhandler(404)
def page_not_found(e):
    try:
        adm = op.getadminrole(current_user.id)
    except:
        adm=[]
        return render_template('404.html', adm=adm), 404
    return render_template('admin/404.html',adm=adm), 404

# define a context processor for merging flask-admin's template context into the
# flask-security views.
@security.context_processor
def security_context_processor():
    return dict(
        admin_base_template=admin.base_template,
        admin_view=admin.index_view,
        h=admin_helpers,
        get_url=url_for
    )



# define protect_views to protect dash apps
def protect_views(app):
    for view_func in app.server.view_functions:
        if view_func.startswith(app.url_base_pathname):
            app.server.view_functions[view_func] = login_required(app.server.view_functions[view_func])

    return app


dashapp1 = dash.Dash(__name__, server=app, url_base_pathname='/admin/clinion/',
                     external_stylesheets=[dbc.themes.BOOTSTRAP])
dashapp1.title = 'Dashapp 1'
dashapp1.layout = layout3

dash_app2 = dash.Dash(__name__, server=app, url_base_pathname='/admin/ctms/',
                      external_stylesheets=[dbc.themes.BOOTSTRAP])
dash_app2.title = 'Study by area'
dash_app2.layout = layout3

# from dashapp2.layout import layout
# from dashapp2.callbacks import register_callbacks

# Meta tags for viewport responsiveness
meta_viewport = {"name": "viewport", "content": "width=device-width, initial-scale=1, shrink-to-fit=no"}

dashapp2 = dash.Dash(__name__,
                     server=app,
                     url_base_pathname='/admin/Dashboard/',

                     meta_tags=[meta_viewport])

dashapp2.title = 'Dashapp 1'
dashapp2.layout = layout3
# register_callbacks(dashapp2)
# protecting
dashapp1 = protect_views(dashapp1)
dash_app2 = protect_views(dash_app2)
dashapp2 = protect_views(dashapp2)




if __name__ == '__main__':
    xyz = DispatcherMiddleware(app, {'/admin/dash1': dashapp1.server, '/admin/dash2': dash_app2.server,
                                     '/admin/dash3': dashapp2.server})
    run_simple('localhost', 5000, xyz, use_reloader=True, use_debugger=True)

