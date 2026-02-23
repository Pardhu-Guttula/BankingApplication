# Epic Title: Implement Overall Design Framework for the E-commerce Platform

from flask import Blueprint, render_template

layout_bp = Blueprint('layout', __name__)

@layout_bp.route('/')
def home_page():
    return render_template('base.html')

@layout_bp.route('/legal')
def legal_page():
    return render_template('base.html', content="<p>Legal information will be displayed here.</p>")

@layout_bp.route('/contact')
def contact_page():
    return render_template('base.html', content="<p>Contact information will be displayed here.</p>")