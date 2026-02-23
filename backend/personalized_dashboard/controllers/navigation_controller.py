# Epic Title: Develop Main Navigation for the E-commerce Platform

from flask import Blueprint, render_template

navigation_bp = Blueprint('navigation', __name__)

@navigation_bp.route('/navigation')
def navigation_bar():
    return render_template('navigation.html')