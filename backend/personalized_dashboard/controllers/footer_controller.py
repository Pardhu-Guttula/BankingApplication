# Epic Title: Develop Footer for the E-commerce Platform

from flask import Blueprint, render_template

footer_bp = Blueprint('footer', __name__)

@footer_bp.route('/footer')
def footer():
    return render_template('footer.html')